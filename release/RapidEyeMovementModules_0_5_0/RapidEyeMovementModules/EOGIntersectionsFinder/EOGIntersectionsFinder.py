"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    EOGIntersectionsFinder
    Detect intersections between both EOG signals (LOC and ROC).
    Intersections are saved in a pandas dataframe.
"""
import numpy as np
import pandas as pd
import time

import config
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import SciNode, InputPlug, OutputPlug

from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class EOGIntersectionsFinder(SciNode):
    """
    Detect intersections between both EOG signals (LOC and ROC).

    Parameters
    ----------
        "EOG_signals": List of SignalModel
            EOG ROC and LOC signals. 
            Each item of the list is a signal object of an epoch from a specific channel.
            Properties:
                samples:np.array
                    List of samples
                start_time:float 
                    Start time in seconds of the signal in relation to the beginning 
                    of the recording.
                end_time:float
                    End time in seconds of the signal in relation to the beginning 
                    of the recording.
                duration:float
                    Duration in seconds of the signal.
                sample_rate:float
                    Sampling rate of the signal
                channel:str
                    Name of the channel
        "parameters": dict
            parameters to detect intersections.
            time_window_s : Time window (sec) to average closely occurring intersection points, preserving the main ones.
        

    Returns
    -------
        "intersections_df": pandas data frame
            Intersections between both EOG signals (LOC and ROC).
            Columns : name, start_sec, amplitude, channels
        
    """
    def __init__(self, **kwargs):
        """ Initialize module EOGIntersectionsFinder """
        super().__init__(**kwargs)
        if DEBUG: print('EOGIntersectionsFinder.__init__')

        # Input plugs
        InputPlug('EOG_signals',self)
        InputPlug('parameters',self)
        # Output plugs
        OutputPlug('intersections_df',self)
        
        self._is_master = False 

    
    def compute(self, EOG_signals,parameters):
        """
        Detect intersections between both EOG signals (LOC and ROC).

        Parameters
        ----------
            "EOG_signals": List of SignalModel
                EOG ROC and LOC signals. 
                Each item of the list is a signal object of an epoch from a specific channel.
                Properties:
                    samples:np.array
                        List of samples
                    start_time:float 
                        Start time in seconds of the signal in relation to the beginning 
                        of the recording.
                    end_time:float
                        End time in seconds of the signal in relation to the beginning 
                        of the recording.
                    duration:float
                        Duration in seconds of the signal.
                    sample_rate:float
                        Sampling rate of the signal
                    channel:str
                        Name of the channel
            "parameters": dict
                parameters to detect intersections.
                time_window_s : Time window (sec) to average closely occurring intersection points, preserving the main ones.

        Returns
        -------
            "intersections_df": pandas data frame
                Intersections between both EOG signals (LOC and ROC).
                Columns : name, start_sec, amplitude, channels

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(EOG_signals,str) and EOG_signals=='':
            raise NodeInputException(self.identifier, "EOG_signals", f"EOGIntersectionsFinder this input is not connected.")
        elif not isinstance(EOG_signals,list):
            raise NodeInputException(self.identifier, "EOG_signals", \
                f"EOGIntersectionsFinder input of wrong type. Expected: <class 'list'> received: {type(EOG_signals)}")     
        elif len(EOG_signals)< 2:
            raise NodeInputException(self.identifier, "EOG_signals", \
                f"EOGIntersectionsFinder at least 2 signals is expected for the operation")   
        if not isinstance(parameters,dict):
            raise NodeInputException(self.identifier, "parameters", \
                f"EOGIntersectionsFinder input of wrong type. Expected: <class 'dict'> received: {type(parameters)}")   

        # Organize signal per start time (so the channels are groupes per start time)
        signals_events = SignalModel.get_attribute(EOG_signals, None, 'start_time')

        # Compute intersections between ROC and LOC for each epochs
        # start timer to measure the execution time
        if DEBUG: start_time = time.time()
        intersections = []
        for signals in signals_events:
            if len(signals) != 2:
                raise NodeInputException(self.identifier, "EOG_signals", \
                    f"EOGIntersectionsFinder at least 2 signals is expected for the operation")
            diff_samples = signals[0].samples - signals[1].samples
            # Find the change of sign in the diff_samples
            change_sign = np.diff(np.sign(diff_samples))
            # Find where the change of sign is not 0
            change_sign_idx = np.where(change_sign != 0)[0]
            for idx in change_sign_idx:
                intersections.append(['EOG_inter',signals[0].start_time + idx / signals[0].sample_rate, signals[0].samples[idx], 'EOG'])

        # Convert the list on intersections to a pandas data frame
        intersections_df = pd.DataFrame(intersections, columns=['name', 'start_sec', 'amplitude', 'channels'])
        # Stop timer
        if DEBUG: end_time = time.time()
        if DEBUG: print(f'Create intersections_df: Elapsed time: {end_time - start_time}')

        # Start timer to measure the execution time
        if DEBUG: start_time_timer = time.time()
        # Average closely occurring intersection points, preserving the main ones
        # Iterate through the intersections_df dataframe
        sel_intersections_list = []
        intersection_starts = intersections_df['start_sec'].values
        analyze_tab = np.zeros(len(intersections_df))
        for i_intersection, start_time in enumerate(intersection_starts):
            # Extract the index of all the other intersections that overlap with the current intersection within the time window
            temp_intersections_i = np.where((intersection_starts >= (start_time - parameters['time_window_s'])) & \
                (intersection_starts <= (start_time + parameters['time_window_s'])))[0]
            # Verify if the intersections extracted are not alraedy analyzed
            not_analysed_i = []
            for i in temp_intersections_i:
                if not analyze_tab[i]:
                    not_analysed_i.append(i)
            # Extract all the other intersections that overlap with the current intersection within the time window
            temp_intersections = intersections_df.iloc[not_analysed_i, :].copy()
            # Create a new one intersection with the average start time
            if len(temp_intersections) > 1:
                new_intersection = intersections_df.iloc[i_intersection].values
                new_intersection[1] = temp_intersections['start_sec'].mean()
                sel_intersections_list.append(new_intersection.tolist())
            elif len(temp_intersections) == 1:
                new_intersection = temp_intersections.values[0]
                sel_intersections_list.append(new_intersection.tolist())
            # Mark the original ones selected as analyzed
            analyze_tab[not_analysed_i] = 1
        # Convert the list on intersections to a pandas data frame
        sel_intersections_df = pd.DataFrame(sel_intersections_list, columns=['name', 'start_sec', 'amplitude', 'channels'])
        # Stop timer
        if DEBUG: end_time = time.time()
        if DEBUG: print(f'Average closely occurring intersections: Elapsed time: {end_time - start_time_timer}')

        # Write to the cache to use the data in the resultTab
        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            cache['signals'] = EOG_signals
            cache['intersections_df'] = sel_intersections_df
            self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'intersections_df': intersections_df
        }