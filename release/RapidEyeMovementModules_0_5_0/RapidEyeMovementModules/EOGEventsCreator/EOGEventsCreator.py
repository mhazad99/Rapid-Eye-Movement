"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    EOGEventsCreator
    Creates events based on the intersections between both EOG signals (LOC and ROC) 
    and the peaks derived from the EOG signals.
"""

import pandas as pd
import numpy as np
import time

import config
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import SciNode, InputPlug, OutputPlug

from CEAMSModules.PSGReader.SignalModel import SignalModel


DEBUG = False

class EOGEventsCreator(SciNode):
    """
    Creates events based on the intersections between both EOG signals (LOC and ROC) 
    and the peaks derived from the EOG signals.

    Parameters
    ----------
        "EOG_signals": List of SignalModel
            List of EOG signals
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        "intersections_df": pandas data frame
            Intersections between both EOG signals (LOC and ROC).
            Columns : name, start_sec, duration_sec, channels

        "peaks_df": pandas data frame
            The list of peaks.
            Columns : 
                group : Group of events this event is part of (String)
                start_sec : Starting time of the event in sec (Float)
                amplitude : Amplitude of the event (Float)
                duration_sec : Duration of the event in sec (Float)
                channels : Channel where the event occures (String)

        "parameters": dict
            dictionary of parameters
            "time_window_s": 0.655       # Max time window in seconds to match with an intersection
            'min_deflection_angle' = 45  # Min deflection angle in degrees, None to disable
            'max_angle_diff_EOG' = 15    # Max deflection angle difference between EOG channels in degrees, None to disable
            'max_deflection_std' = 1.5   # Max deflection slope standard deviation, None to disable
            'min_amplitude_z_2nd_EOG' = 0.25   # Min amplitude (z-score) of the second EOG channel, None to disable

        "peaks_parameters" : dict
            The parameters used to detect peaks
                "min_height_z": 1.5,
                "min_interval_s": 0.5
        
    Returns
    -------
        "MORs_df": pandas data frame
            The list of possible MORs and Artefacts.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module EOGEventsCreator """
        super().__init__(**kwargs)
        if DEBUG: print('EOGEventsCreator.__init__')

        # Input plugs
        InputPlug('EOG_signals',self)
        InputPlug('intersections_df',self)
        InputPlug('peaks_df',self)
        InputPlug('parameters',self)
        InputPlug('peaks_parameters',self)
        
        # Output plugs
        OutputPlug('MORs_df',self)
        
        self._is_master = False 
    

    def compute(self, EOG_signals, intersections_df, peaks_df, parameters, peaks_parameters):
        """
        Creates events based on the intersections between both EOG signals (LOC and ROC) 
        and the peaks derived from the EOG signals.

        Parameters
        ----------
            "EOG_signals": List of SignalModel
                List of EOG signals
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
            "intersections_df": pandas data frame
                Intersections between both EOG signals (LOC and ROC).
                Columns : name, start_sec, duration_sec, channels

            "peaks_df": pandas data frame
                The list of peaks.
                Columns : 
                    group : Group of events this event is part of (String)
                    start_sec : Starting time of the event in sec (Float)
                    amplitude : Amplitude of the event (Float)
                    channels : Channel where the event occures (String)

            "parameters": dict
                dictionary of parameters
                "time_window_s": 0.655       # Max time window in seconds to match with an intersection
                'min_deflection_angle' = 45  # Min deflection angle in degrees, None to disable
                'max_angle_diff_EOG' = 15    # Max deflection angle difference between EOG channels in degrees, None to disable
                'max_deflection_std' = 1.5   # Max deflection slope standard deviation, None to disable
                'min_amplitude_z_2nd_EOG' = 0.25   # Min amplitude (z-score) of the second EOG channel, None to disable

            "peaks_parameters" : dict
                The parameters used to detect peaks
                    "min_height_z": 1.5,
                    "min_interval_s": 0.5        

        Returns
        -------
            "MORs_df": pandas data frame
                The list of possible MORs and Artefacts.
                Columns : 
                    group : Group of events this event is part of (String)
                    start_sec : Starting time of the event in sec (Float)
                    peak_sec : Time of the peak in sec (Float)
                    peak_amplitude : Amplitude of the event in µV (Float)
                    duration_sec : Duration of the event in sec (Float)
                    channels : Channel where the event occures (String)
        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        if DEBUG: print('EOGEventsCreator.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(EOG_signals,str) and EOG_signals=='':
            raise NodeInputException(self.identifier, "EOG_signals", f"EOGEventsCreator this input is not connected.")
        elif not isinstance(EOG_signals,list):
            raise NodeInputException(self.identifier, "EOG_signals", \
                f"EOGEventsCreator input of wrong type. Expected: <class 'list'> received: {type(EOG_signals)}")     
        elif len(EOG_signals)< 2:
            raise NodeInputException(self.identifier, "EOG_signals", \
                f"EOGEventsCreator at least 2 signals is expected for the operation")      

        if not isinstance(peaks_df, pd.DataFrame):
            raise NodeInputException(self.identifier, "peaks_df", \
                f"EOGEventsCreator input of wrong type. Expected: <class 'DataFrame'> received: {type(peaks_df)}")

        if not isinstance(intersections_df, pd.DataFrame):
            raise NodeInputException(self.identifier, "intersections_df", \
                f"EOGEventsCreator input of wrong type. Expected: <class 'DataFrame'> received: {type(intersections_df)}")

        if isinstance(parameters,str) and not parameters=='':
            parameters = eval(parameters)
        if not isinstance(parameters,dict):
            raise NodeInputException(self.identifier, "parameters", \
                f"EOGEventsCreator input of wrong type. Expected: <class 'dict'> received: {type(parameters)}")

        if isinstance(peaks_parameters,str) and not peaks_parameters=='':
            peaks_parameters = eval(peaks_parameters)
        if not isinstance(peaks_parameters,dict):
            raise NodeInputException(self.identifier, "peaks_parameters", \
                f"EOGEventsCreator input of wrong type. Expected: <class 'dict'> received: {type(peaks_parameters)}")

        # Sort the peaks by start time and reset the index
        peaks_df = peaks_df.sort_values(by=['start_sec'])
        peaks_df = peaks_df.reset_index(drop=True)
        # Sort the intersections per start time and reset the index
        intersections_df = intersections_df.sort_values(by=['start_sec'])
        intersections_df = intersections_df.reset_index(drop=True)

        # Because of the scoring we have to look for edges in the same epoch
        # Extract the start_time of the EOG_signals
        start_time_epoch = np.unique(SignalModel.get_attribute(EOG_signals, 'start_time','start_time').flatten())
        duration_epoch = np.unique(SignalModel.get_attribute(EOG_signals, 'duration', 'start_time').flatten())
        if len(duration_epoch) > 1:
            duration_epoch = np.mean(duration_epoch)
        else:
            duration_epoch = duration_epoch[0]
        end_time_epoch = start_time_epoch + duration_epoch

        # Create the pandas dataframe of events 
        #   with ['group', 'start_sec', 'start_amplitude', 'peak_sec', 'peak_amplitude', 'duration_sec', 'end_amplitude','channels']
        #   based on the peaks and the intersections
        events_df = self.create_events_df(EOG_signals, peaks_df, intersections_df, start_time_epoch, end_time_epoch, parameters)
        self._log_manager.log(self.identifier, f"{len(events_df)} events were created.")

        # Extract the suspected MORs, sort by start time and reset the index
        suspect_MORs_df = events_df[events_df['group'] == 'dEOG']
        suspect_MORs_df = suspect_MORs_df.sort_values(by='start_sec').reset_index(drop=True)
        self._log_manager.log(self.identifier, f"{len(suspect_MORs_df)} were suspected MORs.")

        # Drop the suspected MORs with bad morphology
        suspect_MORs_df, statistics = self.drop_event_with_bad_morphology(\
            suspect_MORs_df, EOG_signals, start_time_epoch, parameters, peaks_parameters)
        self._log_manager.log(self.identifier, f"{len(suspect_MORs_df)} MORs with a valid morphology.")
        # Loop into the dict items of statistics
        for key, value in statistics.items():
            self._log_manager.log(self.identifier, f"{key}: {value}")

        # Create MORs_det as dataframe with ['group', 'name', 'start_sec', 'duration_sec', 'channels']
        MORs_det_df = pd.DataFrame(columns=['group', 'name', 'start_sec', 'duration_sec', 'channels'])
        # copy the values from columns 'group', 'name', 'start_sec', 'duration_sec', 'channels' from suspect_MORs_df to MORs_det_df
        MORs_det_df['group'] = suspect_MORs_df['group']
        MORs_det_df['name'] = suspect_MORs_df['group']
        MORs_det_df['start_sec'] = suspect_MORs_df['start_sec']
        MORs_det_df['duration_sec'] = suspect_MORs_df['duration_sec']
        MORs_det_df['channels'] = suspect_MORs_df['channels']

        # Drop duplicated events based on the start time
        # duplicated events can happen when there are 2 unmatched peaks between 2 intersections
        #  (intersection define the MORs onset and the end)
        MORs_det_df = MORs_det_df.drop_duplicates(subset=['start_sec'], keep='first')

        # Write to the cache to use the data in the resultTab
        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            cache['signals'] = EOG_signals
            cache['MORs_df'] = MORs_det_df
            # cache['intersections_df'] = intersections_df
            self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, f"{len(MORs_det_df)} unique MORs events were found.")

        return {
            'MORs_df': MORs_det_df
        }


    def create_events_df(self, EOG_signals, peaks_df, intersections_df, start_time_epoch, end_time_epoch, parameters):
        """ Create the pandas dataframe of events 
            with ['group', 'start_sec', 'start_amplitude', 'peak_sec', 'peak_amplitude', 'duration_sec', 'end_amplitude','channels']
            based on the peaks and the intersections

        Parameters
        ----------
            "EOG_signals": List of SignalModel
                List of EOG signals
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
            "intersections_df": pandas data frame
                Intersections between both EOG signals (LOC and ROC).
                Columns : name, start_sec, duration_sec, channels

            "peaks_df": pandas data frame
                The list of peaks.
                Columns : 
                    group : Group of events this event is part of (String)
                    start_sec : Starting time of the event in sec (Float)
                    amplitude : Amplitude of the event (Float)
                    duration_sec : Duration of the event in sec (Float)
                    channels : Channel where the event occures (String)

            "parameters": dict
                dictionary of parameters
                "time_window_s": 0.655       # Max time window in seconds to match with an intersection
                'min_deflection_angle' = 45  # Min deflection angle in degrees, None to disable
                'max_angle_diff_EOG' = 15    # Max deflection angle difference between EOG channels in degrees, None to disable
                'max_deflection_std' = 1.5   # Max deflection slope standard deviation, None to disable
                'min_amplitude_z_2nd_EOG' = 0.25   # Min amplitude (z-score) of the second EOG channel, None to disable

        Returns
        ----------
            suspect_MORs_df (pd.DataFrame): list of suspected MORs
        """
        # Create a dictionary to store the events
        MORs_list = []
        # Extract the group, start_sec, amplitude, channels
        group_all = peaks_df['group'].values
        start_sec_all = peaks_df['start_sec'].values
        amplitude_all = peaks_df['amplitude'].values
        channels_all = peaks_df['channels'].values

        # Loop through the peaks and find the nearest intersection
        MORs_df = pd.DataFrame(columns=['group', 'start_sec', 'start_amplitude', 'peak_sec', 'peak_amplitude', 'duration_sec', 'end_amplitude','channels'])

        for group, start_sec, amplitude, channels in zip(group_all, start_sec_all, amplitude_all, channels_all):
            # Find the nearest intersection in the same epoch otherwise
            #   we set the end or the start of the epoch as an intersection
            start_time_peak = start_sec
            # Find the last intersection before the peak
            all_intersections_before = intersections_df.loc[intersections_df['start_sec']<start_time_peak]
            # Find the first intersection after the peak
            all_intersections_after = intersections_df.loc[intersections_df['start_sec']>start_time_peak]
            # If not empty
            if not all_intersections_before.empty and not all_intersections_after.empty:
                last_intersection_before = all_intersections_before.iloc[-1]
                first_intersection_after = all_intersections_after.iloc[0]

                if (last_intersection_before is not None) and (first_intersection_after is not None):
                    # Make sure the intersection is in the same epoch as the peak
                    # Find the last index in the start_time_epoch < than last_intersection_before["start_time"]
                    start_index_epoch = np.where(start_time_epoch <= last_intersection_before['start_sec'])[0][-1]
                    # Find the first index in the end_time_epoch > than first_intersection_after["start_time"]
                    stop_index_epoch = np.where( end_time_epoch >= first_intersection_after['start_sec'])[0][0]
                    # Find the index of the peak in the start_time_epoch
                    # Find the index where the start_time_epoch >= start_time_peak and end_time_epoch <= start_time_peak
                    peak_index_epoch = np.where((start_time_epoch <= start_time_peak))[0][-1]

                    # Extract the samples in the epoch
                    EOG_samples_epoch = SignalModel.get_attribute(EOG_signals, 'samples','start_time', start_time_epoch[peak_index_epoch])[0]

                    # if the distance from the peak to the nearest intersection is less than the time window
                    if ((np.abs(last_intersection_before['start_sec'] - start_time_peak)) < parameters['time_window_s']) and \
                        ((np.abs(first_intersection_after['start_sec'] - start_time_peak)) < parameters['time_window_s']):
                        if start_index_epoch == stop_index_epoch:
                            current_MOR = {
                                'group': group,
                                'start_sec': last_intersection_before['start_sec'],
                                'start_amplitude': last_intersection_before['amplitude'],
                                'peak_sec': start_sec,
                                'peak_amplitude': amplitude,
                                'duration_sec': first_intersection_after['start_sec'] - last_intersection_before['start_sec'],
                                'end_amplitude': first_intersection_after['amplitude'],
                                'channels': channels
                            }
                        else:
                            # If the intersection is before the start of the epoch
                            if start_index_epoch < peak_index_epoch:
                                current_MOR = {
                                    'group': group,
                                    'start_sec': start_time_epoch[peak_index_epoch],
                                    'start_amplitude': EOG_samples_epoch[0][0],
                                    'peak_sec': start_sec,
                                    'peak_amplitude': amplitude,
                                    'duration_sec': first_intersection_after['start_sec'] - start_time_epoch[peak_index_epoch],
                                    'end_amplitude': first_intersection_after['amplitude'],
                                    'channels': channels
                                }
                            # If the intersection is after the end of the epoch
                            else:
                                current_MOR = {
                                    'group': group,
                                    'start_sec': last_intersection_before['start_sec'],
                                    'start_amplitude': last_intersection_before['amplitude'],
                                    'peak_sec': start_sec,
                                    'peak_amplitude': amplitude,
                                    'duration_sec': end_time_epoch[peak_index_epoch] - last_intersection_before['start_sec'],
                                    'end_amplitude': EOG_samples_epoch[-1],
                                    'channels': channels
                                }
                        
                        # Add the MOR
                        MORs_list.append(current_MOR)
    
        # Convert the dictionary to a dataframe
        MORs_df = pd.concat([MORs_df, pd.DataFrame(MORs_list)], ignore_index=True)
        return MORs_df



    def drop_event_with_bad_morphology(self, suspect_MORs_df, EOG_signals, start_time_epoch, parameters, peaks_parameters):
        """ Drop the MORs with a bad morphology

        Parameters
        ----------
            suspect_MORs_df (pd.DataFrame): list of suspected MORs

            "EOG_signals": List of SignalModel
                List of EOG signals
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original

            "start_time_epoch": numpy array
                The list of start time of the epochs

            "parameters": dict
                dictionary of parameters
                "time_window_s": 0.655       # Max time window in seconds to match with an intersection
                'min_deflection_angle' = 45  # Min deflection angle in degrees, None to disable
                'max_angle_diff_EOG' = 15    # Max deflection angle difference between EOG channels in degrees, None to disable
                'max_deflection_std' = 1.5   # Max deflection slope standard deviation, None to disable
                'min_amplitude_z_2nd_EOG' = 0.25   # Min amplitude (z-score) of the second EOG channel, None to disable

        Returns
        ----------
            suspect_MORs_df (pd.DataFrame): list of suspected MORs
            statistics (dict): dictionary of statistics

        """
        SLOPE_DIVISIONS = 4
        fs = EOG_signals[0].sample_rate

        # Extract the start time of the MORs
        start_time_MORs = suspect_MORs_df['start_sec'].values
        # Extract the peak second of the MORs
        peak_time_MORs = suspect_MORs_df['peak_sec'].values
        # Extract the duration of the MORs
        duration_MORs = suspect_MORs_df['duration_sec'].values

        # Statistics to understand the drops
        statistics = {}
        statistics['deflection_angle_too_small'] = 0
        statistics['channel_diff_angle_too_big'] = 0
        statistics['std_2nd_chan_too_small'] = 0
        statistics['slope_std_too_big'] = 0
        statistics['channel_not_inversed'] = 0


        # Iterate through the suspected MORs dataframe
        i_index = 0
        i_index_to_drop = []
        for start_sec, peak_sec, duration_sec in zip(start_time_MORs, peak_time_MORs, duration_MORs):
            # Extract the start of the epoch where the current MOR starts 
            start_index_epoch = np.where(start_time_epoch <= start_sec)[0][-1]
            # Extract the samples in the epoch where the current MOR starts
            EOG_samples_epoch = SignalModel.get_attribute(EOG_signals, 'samples','start_time', start_time_epoch[start_index_epoch])[0]
            # Extract the start, peak and end samples value of the current MOR
            x1_sample = int((start_sec-start_time_epoch[start_index_epoch])*fs)
            if x1_sample < 0: x1_sample=0
            x2_sample = int((peak_sec-start_time_epoch[start_index_epoch])*fs)
            x3_sample = int(x1_sample+duration_sec*fs)

            # To compute the angle
            x_diff = x2_sample - x1_sample
            x_ratio = (x_diff/fs)/parameters['time_window_s']

            # Loop through EOG channels
            EOG_avg_slopes = []
            deflection_angles = []
            for i_EOG in range(len(EOG_samples_epoch)):

                # ----------------------------------------
                # MOR Initiation
                # ----------------------------------------
                # Extract the value at the start and peak
                EOG_y1 = EOG_samples_epoch[i_EOG][x1_sample]
                EOG_y2 = EOG_samples_epoch[i_EOG][x2_sample]
                EOG_avg_slope = (EOG_y2-EOG_y1)/(x2_sample-x1_sample)
                EOG_avg_slopes.append(EOG_avg_slope)

                # Compute the deflection angle
                y_ratio = EOG_y2/peaks_parameters['min_height_z']
                abs_angle_deg = abs(np.arctan(y_ratio/x_ratio)*180/np.pi)
                deflection_angles.append(abs_angle_deg)
                if parameters['min_deflection_angle'] is not None:
                    if abs_angle_deg < parameters['min_deflection_angle']:
                        i_index_to_drop.append(i_index)
                        statistics['deflection_angle_too_small'] += 1
                        # # Transform sec into hh:mm:ss
                        # start_time_str = time.strftime('%H:%M:%S', time.gmtime(start_sec))
                        # print(f"A rejected MOR where the angle is {abs_angle_deg}, start time={start_time_str}")
                        break # the other channel does not have to be analysed

                if parameters['max_deflection_std'] is not None:
                    # Divide the slopes in 4 sections
                    quart_dist = int((x2_sample-x1_sample)/4)
                    EOG_slopes = []
                    if quart_dist>0:
                        x = x1_sample
                        for i_quart in range(SLOPE_DIVISIONS):
                            EOG_y_x = EOG_samples_epoch[i_EOG][x]
                            EOG_y_quart = EOG_samples_epoch[i_EOG][x+quart_dist]
                            EOG_slopes.append((EOG_y_quart-EOG_y_x)/quart_dist)
                            x = x+quart_dist      
                        # Compute the standard deviation of the slopes
                        slope_std = np.std(EOG_slopes)
                        z_score_slope = (EOG_slopes-EOG_avg_slope)/slope_std
                        if any(z_score_slope > parameters['max_deflection_std']):
                            i_index_to_drop.append(i_index)
                            statistics['slope_std_too_big'] += 1
                            #print(f"A rejected MOR where the std slope is higher than {parameters['max_deflection_std']}, start_sec={start_sec}")
                            break # the other channel does not have to be analysed
                
                # If the peak is less than parameters['min_amplitude_z_2nd_EOG'] STD from the mean, drop the MOR
                if parameters['min_amplitude_z_2nd_EOG'] is not None:
                    if (abs(EOG_y2)<parameters['min_amplitude_z_2nd_EOG']):
                        i_index_to_drop.append(i_index)
                        statistics['std_2nd_chan_too_small'] += 1
                        #print(f"A rejected MOR where the peak is less than {parameters['min_amplitude_z_2nd_EOG']} STD from the mean, start_sec={start_sec}")
                        break # the other channel does not have to be analysed
                
                # ----------------------------------------
                # MOR termination
                # ----------------------------------------
                # Extract the value at the end
                if x3_sample>=len(EOG_samples_epoch[i_EOG]):
                    x3_sample = len(EOG_samples_epoch[i_EOG])-1
                EOG_y3 = EOG_samples_epoch[i_EOG][x3_sample]
                EOG_avg_slope = (EOG_y3-EOG_y2)/(x3_sample-x2_sample)
                EOG_avg_slopes.append(EOG_avg_slope)      

                # if parameters['max_deflection_std'] is not None:
                #     # Divide the slopes in 4 sections
                #     quart_dist = int((x3_sample-x2_sample)/4)
                #     EOG_slopes = []
                #     if quart_dist>0:
                #         x = x2_sample
                #         for i_quart in range(SLOPE_DIVISIONS):
                #             EOG_y_x = EOG_samples_epoch[i_EOG][x]
                #             EOG_y_quart = EOG_samples_epoch[i_EOG][x+quart_dist]
                #             EOG_slopes.append((EOG_y_quart-EOG_y_x)/quart_dist)
                #             x = x+quart_dist      

                #         # Compute the standard deviation of the slopes
                #         slope_std = np.std(EOG_slopes)
                #         z_score_slope = (EOG_slopes-EOG_avg_slope)/slope_std
                #         if any(z_score_slope > parameters['max_deflection_std']):
                #             i_index_to_drop.append(i_index)
                #             statistics['slope_std_too_big'] += 1 
                #             #print(f"A rejected MOR where the std slope is higher than {parameters['max_deflection_std']}, start_sec={start_sec}")
                #             break # the other channel does not have to be analysed

            # If the deflection angle is different than more than 15 degrees, drop the MOR
            if len(deflection_angles)==2:
                deflection_angles = np.array(deflection_angles)
                if parameters['max_angle_diff_EOG'] is not None:
                    if np.diff(deflection_angles)>parameters['max_angle_diff_EOG']:
                        i_index_to_drop.append(i_index)
                        i_index += 1
                        statistics['channel_diff_angle_too_big'] += 1 
                        #start_time_str = time.strftime('%H:%M:%S', time.gmtime(start_sec))
                        #print(f"A rejected MOR where the angle differ by {np.diff(deflection_angles)}, start time={start_time_str}")
                        continue # Skip to the next MOR since this one is rejected                    

            # If one of the deflections is not inversed between channels, drop the MOR
            EOG_avg_slopes = np.array(EOG_avg_slopes)
            if len(EOG_avg_slopes)==4:
                if ((EOG_avg_slopes[0]*EOG_avg_slopes[2])>0) or ((EOG_avg_slopes[1]*EOG_avg_slopes[3])>0):
                    i_index_to_drop.append(i_index)
                    i_index += 1
                    statistics['channel_not_inversed'] += 1
                    continue # Skip to the next MOR since this one is rejected

            i_index += 1

        # Make unique the list of MORs to drop
        i_index_to_drop = list(set(i_index_to_drop))
        # Drop the MORS
        suspect_MORs_df = suspect_MORs_df.drop(i_index_to_drop)
        # Reset the index
        suspect_MORs_df = suspect_MORs_df.reset_index(drop=True)
        return suspect_MORs_df, statistics

