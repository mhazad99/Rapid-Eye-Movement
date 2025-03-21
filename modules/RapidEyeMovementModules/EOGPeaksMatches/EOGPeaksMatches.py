"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    EOGPeaksMatches
    Select peaks present in at least 2 signals (ROC, LOC, sEOG, dEOG) within a time window.
    Keep only the selected peaks in the peaks_df dataframe.
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

class EOGPeaksMatches(SciNode):
    """
    Select peaks present in at least 2 signals (ROC, LOC, sEOG, dEOG) within a time window.
    Keep only the selected peaks in the peaks_df dataframe.

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
        "sEOG_signals": List of SignalModel
            LOC+ROC signals. 
        "dEOG_signals": List of SignalModel
            LOC-ROC signals. 
        "peaks_df": pandas data frame
            The list of peaks.
            Columns : 
                group : Group of events this event is part of (String)
                name : Name of the event (String)
                start_sec : Starting time of the event in sec (Float)
                duration_sec : Duration of the event in sec (Float)
                amplitude : Amplitude of the event (Float)
                channels : Channel where the event occures (String)
        "parameters": dict
            dict of parameters.
            "time_window_s": 0.3

    Returns
    -------
        "peaks_df": pandas data frame
            The list of peaks present in at least 2 signals.
            Columns : 
                group : Group of events this event is part of (String)
                name : Name of the event (String)
                start_sec : Starting time of the event in sec (Float)
                duration_sec : Duration of the event in sec (Float)
                amplitude : Amplitude of the event (Float)
                channels : Channel where the event occures (String)

        "peaks_unmatched_df": pandas data frame
            The list of EOG peaks not present in at least 2 signals.
            Columns : 
                group : Group of events this event is part of (String)
                name : Name of the event (String)
                start_sec : Starting time of the event in sec (Float)
                duration_sec : Duration of the event in sec (Float)
                amplitude : Amplitude of the event (Float)
                channels : Channel where the event occures (String)
        
    """
    def __init__(self, **kwargs):
        """ Initialize module EOGPeaksMatches """
        super().__init__(**kwargs)
        if DEBUG: print('EOGPeaksMatches.__init__')

        # Input plugs
        InputPlug('EOG_signals',self)
        InputPlug('sEOG_signals',self)
        InputPlug('dEOG_signals',self)
        InputPlug('peaks_df',self)
        InputPlug('parameters',self)

        # Output plugs
        OutputPlug('peaks_df',self)
        OutputPlug('peaks_unmatched_df',self)
    
        self._is_master = False 
        self.peaks_matched_group = 'dEOG'
        self.peaks_matched_name = 'dEOG'
        self.peaks_sEOG_group = 'sEOG'
        self.peaks_sEOG_name = 'sEOG'

    

    def compute(self, EOG_signals, sEOG_signals, dEOG_signals, peaks_df, parameters):
        """
        Select peaks present in at least 2 signals (ROC, LOC, sEOG, dEOG) within a time window.
        Keep only the selected peaks in the peaks_df dataframe.

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
            "sEOG_signals": List of SignalModel
                LOC+ROC signals. 
            "dEOG_signals": List of SignalModel
                LOC-ROC signals. 
            "peaks_df": pandas data frame
                The list of peaks.
                Columns : 
                    group : Group of events this event is part of (String)
                    name : Name of the event (String)
                    start_sec : Starting time of the event in sec (Float)
                    duration_sec : Duration of the event in sec (Float)
                    amplitude : Amplitude of the event (Float)
                    channels : Channel where the event occures (String)
            "parameters": dict
                dict of parameters.
                "time_window_s": 0.3

        Returns
        -------
            "peaks_df": pandas data frame
                The list of peaks present in at least 2 signals.
                Columns : 
                    group : Group of events this event is part of (String)
                    name : Name of the event (String)
                    start_sec : Starting time of the event in sec (Float)
                    duration_sec : Duration of the event in sec (Float)
                    amplitude : Amplitude of the event (Float)
                    channels : Channel where the event occures (String)

            "peaks_unmatched_df": pandas data frame
                The list of EOG peaks not present in at least 2 signals.
                Columns : 
                    group : Group of events this event is part of (String)
                    name : Name of the event (String)
                    start_sec : Starting time of the event in sec (Float)
                    duration_sec : Duration of the event in sec (Float)
                    amplitude : Amplitude of the event (Float)
                    channels : Channel where the event occures (String)
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
            raise NodeInputException(self.identifier, "EOG_signals", f"EOGPeaksMatches this input is not connected.")
        elif not isinstance(EOG_signals,list):
            raise NodeInputException(self.identifier, "EOG_signals", \
                f"EOGPeaksMatches input of wrong type. Expected: <class 'list'> received: {type(EOG_signals)}")     
        elif len(EOG_signals)< 2:
            raise NodeInputException(self.identifier, "EOG_signals", \
                f"EOGPeaksMatches at least 2 signals is expected for the operation")      

        if isinstance(sEOG_signals,str) and sEOG_signals=='':
            raise NodeInputException(self.identifier, "sEOG_signals", f"EOGPeaksMatches this input is not connected.")
        elif not isinstance(sEOG_signals,list):
            raise NodeInputException(self.identifier, "sEOG_signals", \
                f"EOGPeaksMatches input of wrong type. Expected: <class 'list'> received: {type(sEOG_signals)}")  

        if isinstance(dEOG_signals,str) and dEOG_signals=='':
            raise NodeInputException(self.identifier, "dEOG_signals", f"EOGPeaksMatches this input is not connected.")
        elif not isinstance(dEOG_signals,list):
            raise NodeInputException(self.identifier, "dEOG_signals", \
                f"EOGPeaksMatches input of wrong type. Expected: <class 'list'> received: {type(dEOG_signals)}")  

        if isinstance(parameters,str) and not parameters=='':
            parameters = eval(parameters)
        if not isinstance(parameters,dict):
            raise NodeInputException(self.identifier, "parameters", \
                f"EOGPeaksMatches input of wrong type. Expected: <class 'dict'> received: {type(parameters)}")

        if not isinstance(peaks_df, pd.DataFrame):
            raise NodeInputException(self.identifier, "peaks_df", \
                f"EOGPeaksMatches input of wrong type. Expected: <class 'DataFrame'> received: {type(peaks_df)}")

        # Because of the scoring we have to look for the peaks in the same epoch
        # Extract the start_time of the dEOG_signals
        start_time_epoch = SignalModel.get_attribute(dEOG_signals, 'start_time','start_time').flatten()
        duration_epoch = np.unique(SignalModel.get_attribute(dEOG_signals, 'duration', 'start_time').flatten())
        if len(duration_epoch) > 1:
            duration_epoch = np.mean(duration_epoch)
        else:
            duration_epoch = duration_epoch[0]

        # Iterate through the peaks_df dataframe
        # Sort peaks_df by start_time and reset the index
        peaks_df = peaks_df.sort_values(by='start_sec')
        peaks_df = peaks_df.reset_index(drop=True)
        analyze_tab = np.zeros(len(peaks_df))
        peaks_start_times = peaks_df['start_sec'].values
        # Start timer for the whole function
        if DEBUG: start = time.time()
        # Create a new list of peak events (data reduction applied)
        sel_peaks_df = pd.DataFrame(columns=peaks_df.columns)
        for i_peak, start_time in enumerate(peaks_start_times):
            # Find the first start_time_epoch that is greater than start_time
            epoch_start_peak = start_time_epoch[start_time_epoch<start_time][-1]
            epoch_end_peak = epoch_start_peak + duration_epoch
            # Extract the index of all the other peaks that overlap 
            #   with the current peak within the time window (in the same epoch!!!)
            temp_peaks_i = np.where((peaks_start_times >= (start_time - parameters['time_window_s'])) & \
                (peaks_start_times <= (start_time + parameters['time_window_s'])))[0]
            # Verify if the peaks extracted are not already analyzed
            #    and in the same epoch
            # not_analysed_i = []
            # for i in temp_peaks_i:
            #     if not analyze_tab[i]:
            #         # If the original_peaks.loc[i, 'start_sec'] is included in the epoch
            #         if (epoch_start_peak <= peaks_start_times[i]) and (peaks_start_times[i] <= epoch_end_peak):
            #             not_analysed_i.append(i)
            # Extract all the other peaks that overlap with the current peak within the time window
            temp_peaks = peaks_df.iloc[temp_peaks_i, :].copy()
            # If there are at least 2 peaks in the time window, keep the current peak
            if len(temp_peaks) >= 2:

                # Extract the peak with the biggest amplitude of EOG channels
                EOG_temp_peaks = temp_peaks[temp_peaks['group']=='EOG_peaks']
                EOG_peak = EOG_temp_peaks[EOG_temp_peaks['amplitude'] == EOG_temp_peaks['amplitude'].max()]
                dEOG_peak = temp_peaks[temp_peaks['group']=='dEOG_peaks']
                sEOG_peak = temp_peaks[temp_peaks['group']=='sEOG_peaks']

                if 'dEOG_peaks' in temp_peaks['group'].values:
                    if 'sEOG_peaks' in temp_peaks['group'].values:
                        # Look at the biggest amplitude between sEOG and dEOG
                        # Extract the event amplitude from the peaks_df with the group dEOG
                        dEOG_amplitude = dEOG_peak['amplitude'].values[0]
                        sEOG_amplitude = sEOG_peak['amplitude'].values[0]
                        if abs(dEOG_amplitude) > abs(sEOG_amplitude):
                            matched_peak = EOG_peak.copy()
                            matched_peak['group'] = self.peaks_matched_group
                            matched_peak['name'] = self.peaks_matched_name
                        else:
                            matched_peak = sEOG_peak.copy()
                            matched_peak['group'] = self.peaks_sEOG_group
                            matched_peak['name'] = self.peaks_sEOG_group
                    else:
                        matched_peak = EOG_peak.copy()
                        matched_peak['group'] = self.peaks_matched_group
                        matched_peak['name'] = self.peaks_matched_name
                elif 'sEOG_peaks' in temp_peaks['group'].values:
                    matched_peak = sEOG_peak.copy()
                    matched_peak['group'] = self.peaks_sEOG_group
                    matched_peak['name'] = self.peaks_sEOG_group
                else:
                    matched_peak = EOG_peak.copy()
                    matched_peak['group'] = self.peaks_matched_group
                    matched_peak['name'] = self.peaks_matched_name               
                    # look at the direction of the deflection (in the EOGEventsCreator module)
                
                # Add the matched peak to the sel_peaks_df
                sel_peaks_df = pd.concat([sel_peaks_df, matched_peak], axis=0, ignore_index=True)
                # Mark all the peaks with a match with others
                analyze_tab[temp_peaks_i] = 1

        # stop timer
        if DEBUG: end = time.time()
        if DEBUG: print(f"Match peaks : Elapsed time: {end - start:.2f} seconds")

        # Log the number of peaks alone
        n_peaks_alone = len(analyze_tab[analyze_tab == 0])
        n_peaks_dEOG = len(sel_peaks_df[sel_peaks_df['group'] == self.peaks_matched_group])
        n_peaks_sEOG = len(sel_peaks_df[sel_peaks_df['group'] == self.peaks_sEOG_group])
        self._log_manager.log(self.identifier, \
            f"The number of peaks alone is: {n_peaks_alone} out of {len(peaks_df)} including sEOG and dEOG" )
        self._log_manager.log(self.identifier, \
            f"The number of peaks merged and labbeled to possible REMs: {n_peaks_dEOG} out of {len(sel_peaks_df)}" )
        self._log_manager.log(self.identifier, \
            f"The number of peaks merged and labbeled to possible artifacts: {n_peaks_sEOG} out of {len(sel_peaks_df)}" )

        # Extract the peaks that are alone
        # analyze_tab[not_analysed_i] == 0
        alone_peaks_df = peaks_df.iloc[analyze_tab == 0, :] 
        # Extract only the EOG peaks
        #alone_peaks_df = alone_peaks_df[(alone_peaks_df['group'] == 'EOG_peaks') | (alone_peaks_df['group'] == 'dEOG_peaks')]
        alone_peaks_df = alone_peaks_df[(alone_peaks_df['group'] == 'EOG_peaks')]

        self._log_manager.log(self.identifier, \
            f"The number of EOG peaks alone is: {len(alone_peaks_df)}" )        
        # Rename the group as self.peaks_matched_group
        alone_peaks_df['group'] = self.peaks_matched_group
        # Add the name as self.peaks_matched_name
        alone_peaks_df['name'] = self.peaks_matched_name

        # Write to the cache to use the data in the resultTab
        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            signals = []
            signals.extend(EOG_signals)
            signals.extend(sEOG_signals)
            signals.extend(dEOG_signals)
            cache['signals'] = signals
            cache['peaks_df'] = sel_peaks_df
            cache['min_height_z'] = None
            self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'peaks_df': sel_peaks_df,
            'peaks_unmatched_df': alone_peaks_df
        }