"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Filter a component with the max z value above the threshold to remove the 
    occular artefact.
    Parameters
    -----------
        z_values: List of SignalModel
            List of Z values for each window in each index of the list
        components: List of SignalModel 
            List of initial componants obtain before rescale
        epochs_to_process: pandas DataFrame
            df of epochs with field:
                group: Group of events this event is part of
                name: Name of the event
                start_sec: Starting time of the event in sec
                duration_sec: Duration of the event in sec
                channels : Channel where the event occures
        threshold: array
            Component above this value will be considered to be filtered out.
            There is a threshold value per start time (to supportsleep cycle)
        n_max_to_rem : int
            The maximum number of components to remove.
        event_group: string
            The group of the new event created
        event_name: string
            The name of the new event created
        event_channel : string
            The channel where the new event is added

    Returns
    -----------    
        filter_components : List of SignalModel
            List of componants obtain after filtering (only the signals that a component have been deleted)
        deleted_components : List of SignalModel
            List of deleted componants filtered
        events : pandas DataFrame
            df of epochs with field:
                group: Group of events this event is part of
                name: Name of the event
                start_sec: Starting time of the event in sec
                duration_sec: Duration of the event in sec
                channels : Channel where the event occures
"""
import numpy as np
import pandas as pd
from scipy import signal as sci
from tqdm import tqdm

from flowpipe import SciNode, InputPlug, OutputPlug
import config
from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.EventReader.manage_events import create_event_dataframe
from commons.NodeInputException import NodeInputException

DEBUG = False

class FilterComponents(SciNode):
    """
        Filter a component with the max z value above the threshold to remove the 
        occular artefact. A hamming mask is used during the MOR_C event only. 

        Parameters
        -----------
            z_values: List of SignalModel
                List of Z values for each window in each index of the list
            components: List of SignalModel 
                List of initial componants obtain before rescale
            epochs_to_process: pandas DataFrame
                df of epochs with field:
                    group: Group of events this event is part of
                    name: Name of the event
                    start_sec: Starting time of the event in sec
                    duration_sec: Duration of the event in sec
                    channels : Channel where the event occures
            threshold: array
                Component above this value will be considered to be filtered out.
                There is a threshold value per start time (to supportsleep cycle)
            n_max_to_rem : int
                The maximum number of components to remove.
            event_group: string
                The group of the new event created
            event_name: string
                The name of the new event created
            event_channel : string
                The channel where the new event is added

        Returns
        -----------    
            filter_components : List of SignalModel
                List of componants obtain after filtering (only the signals that a component have been deleted)
            deleted_components : List of SignalModel
                List of deleted componants filtered
            events : pandas DataFrame
                df of epochs with field:
                    group: Group of events this event is part of
                    name: Name of the event
                    start_sec: Starting time of the event in sec
                    duration_sec: Duration of the event in sec
                    channels : Channel where the event occures
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('FilterComponents.__init__')
        self._filename = None
        InputPlug('z_values', self)
        InputPlug('components', self)
        InputPlug('epochs_to_process', self)
        InputPlug('threshold', self)
        InputPlug('n_max_to_rem', self)
        InputPlug('event_group', self)
        InputPlug('event_name', self)
        InputPlug('event_channel', self)
        OutputPlug('filter_components', self)
        OutputPlug('deleted_components', self)
        OutputPlug('events', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, z_values, components, epochs_to_process, threshold, n_max_to_rem, event_group, event_name, event_channel):
        """
            Filter a component with the max z value above the threshold to remove the 
            occular artefact.
            Parameters
            -----------
                z_values: List of SignalModel
                    List of Z values for each window in each index of the list
                    (based on 3 sec MOR_C event, but can be splitted if it crosses a 10 sec REM components)
                components: List of SignalModel 
                    List of initial componants obtain before rescale
                    (list of 10 sec REM components)
                epochs_to_process: pandas DataFrame
                    df of epochs with field:
                        group: Group of events this event is part of
                        name: Name of the event
                        start_sec: Starting time of the event in sec
                        duration_sec: Duration of the event in sec
                        channels : Channel where the event occures
                        (based on 3 sec MOR_C event, but can be splitted if it crosses a 10 sec REM components)
                threshold: array
                    Component above this value will be considered to be filtered out.
                    There is a threshold value per start time (to supportsleep cycle)
                n_max_to_rem : int
                    The maximum number of components to remove.
                event_group: string
                    The group of the new event created
                event_name: string
                    The name of the new event created
                event_channel : string
                    The channel where the new event is added

            Returns
            -----------    
                filter_components : List of SignalModel
                    List of componants obtain after filtering
                deleted_components : List of SignalModel
                    List of deleted componants filtered
                events : pandas DataFrame
                    df of epochs with field:
                        group: Group of events this event is part of
                        name: Name of the event
                        start_sec: Starting time of the event in sec
                        duration_sec: Duration of the event in sec
                        channels : Channel where the event occures
        """

        if DEBUG: print('FilterComponents.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Verify inputs
        if isinstance(z_values,str) and z_values=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "z_values", \
                f"FilterComponents this input is not connected.")
        if not isinstance(z_values,list):
            err_message = "ERROR: signals unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "z_values", \
                f"FilterComponents input of wrong type. Expected: <class 'list'> received: {type(z_values)}")
        elif isinstance(z_values, list) and len(z_values)==0:
            return {'filter_components': [],
                    'deleted_components': [],
                    'events': create_event_dataframe(None)}
        if isinstance(components,str) and components=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "components", \
                f"FilterComponents this input is not connected.")
        if not isinstance(components,list):
            err_message = "ERROR: signals unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "components", \
                f"FilterComponents input of wrong type. Expected: <class 'list'> received: {type(components)}")
        elif isinstance(components, list) and len(components)==0:
            return {'filter_components': [],
                    'deleted_components': [],
                    'events': create_event_dataframe(None)}


        if isinstance(threshold, str) and threshold == '':
            err_message = "ERROR: No threshold input."
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "threshold", \
                f"FilterComponents this input is not connected.")
         
        # Clone components to create new signals (components is a list of [n_channels x 10 s epoch of R])
        copy_components = [signal.clone(clone_samples=True) for signal in components]
        filter_components = []
        deleted_components = []

        # Init new dataframe for EOG_Rejection's events
        event = []
        filter_components_event = SignalModel.get_attribute(copy_components, None, 'start_time')
        z_values_event = SignalModel.get_attribute(z_values, None, 'start_time')

        # For each 10-sec R epoch
        for filt_cmp_event, thresh_val in zip(filter_components_event, threshold):
            # epochs_to_process is the events of the MOR_C
            # We look if there are at least one MOR_C in the current 10 s epoch (filt_cmp_event)
            cond1 = np.array( (epochs_to_process['start_sec']+epochs_to_process['duration_sec']) > filt_cmp_event[0].start_time )
            cond2 = np.array(epochs_to_process['start_sec'] < (filt_cmp_event[0].start_time + filt_cmp_event[0].duration)) 
            one_above_threshold = False
            if (cond1 * cond2).any():
                # z_values_event is a list of SignalModel ordered per start_time
                #   each item of z_values_event is a MOR_C
                # Select the MOR_C in the filt_cmp_event
                zval_cur_epoch = z_values_event[cond1 * cond2]
                # For each MOR_C in the current epoch filt_cmp_event
                for zval in zval_cur_epoch:
                    # zval is a list of SignalModel, length is n_components
                    z_val = np.array([signal.meta['z_value'] for signal in zval])
                    z_start = zval[0].start_time
                    z_duration = zval[0].duration
                    # z_val is an array of n_comp
                    above_threshold = (z_val > thresh_val).any()
                    if above_threshold:
                        one_above_threshold = True
                        # Sort the z_val and choose the max nb components to remove
                        index_sort = np.argsort(z_val)[-(int(n_max_to_rem)):]
                        index_pos = np.where((z_val[index_sort] > thresh_val) == True)
                        index_del = index_sort[index_pos]  
                        # Find in the current component where is the MOR_C (z-vals)
                        diff_start_sec = (z_start-filt_cmp_event[0].start_time)
                        diff_stop_sec = (filt_cmp_event[0].start_time+filt_cmp_event[0].duration)-(z_start+z_duration)
                        deleted_components.append(filt_cmp_event[index_del])
                        # Generate 2 points to compute the linear regression between threshold and maximum MI
                        x_MI = [thresh_val, z_val[index_del[-1]]]
                        y_MI = [0, 1]
                        for index in index_del:
                            # MI near to the threshold has a reduction_thres close to zero (small reduction, we keep the component)
                            # MI near to the max MI has a reduction_thres close to one (big reduction, we remove the component)
                            reduction_thres = np.interp(z_val[index], x_MI, y_MI)
                            # Force to zeros only the section during MOR_C (hamming slope)
                            sampling_rate = filt_cmp_event[index].sample_rate
                            index_start = int(round(diff_start_sec*sampling_rate,0))
                            index_stop = int(round(diff_stop_sec*sampling_rate,0))
                            # MOR starts after the start of the epoch
                            if index_start>=0:
                                # MOR ends with the end of the epoch or after the end of the epoch
                                if index_stop<=0:
                                    comp_2_rem = filt_cmp_event[index].samples[index_start:]
                                    nsample_win = len(comp_2_rem)
                                    scaling_win = 1-(sci.windows.tukey(nsample_win, alpha=0.1)*reduction_thres)
                                    # *** The component is modified ***
                                    filt_cmp_event[index].samples[index_start:] = scaling_win*comp_2_rem
                                # MOR ends before the end of the epoch
                                elif index_stop>0:
                                    comp_2_rem = filt_cmp_event[index].samples[index_start:-index_stop]
                                    nsample_win = len(comp_2_rem)
                                    scaling_win = 1-(sci.windows.tukey(nsample_win, alpha=0.1)*reduction_thres)
                                    # *** The component is modified ***
                                    filt_cmp_event[index].samples[index_start:-index_stop] = scaling_win*comp_2_rem
                            # MOR starts before the start of the epoch
                            elif index_start<0:
                                # MOR ends with the end of the epoch or after the end of the epoch
                                if index_stop<=0:
                                    comp_2_rem = filt_cmp_event[index].samples[0:]
                                    nsample_win = len(comp_2_rem)
                                    scaling_win = 1-(sci.windows.tukey(nsample_win, alpha=0.1)*reduction_thres)
                                    # *** The component is modified ***
                                    filt_cmp_event[index].samples[0:] = scaling_win*comp_2_rem
                                # MOR ends before the end of the epoch
                                elif index_stop>0:
                                    comp_2_rem = filt_cmp_event[index].samples[0:-index_stop]
                                    nsample_win = len(comp_2_rem)
                                    scaling_win = 1-(sci.windows.tukey(nsample_win, alpha=0.1)*reduction_thres)
                                    # *** The component is modified ***
                                    filt_cmp_event[index].samples[0:-index_stop] = scaling_win*comp_2_rem     

                        # Create an Event
                        if isinstance(event_channel,str) and len(event_channel)>0:
                            channels = event_channel
                        else:
                            channels = filt_cmp_event[index_del[0]].channel
                # If at least one MOR_C in the current 10-sec epoch has a correlation higher than the threshold
                if one_above_threshold:
                    event.append([event_group,
                                    event_name,
                                    filt_cmp_event[index_del[0]].start_time,
                                    filt_cmp_event[index_del[0]].duration,
                                    channels]) 
            # The component numbers are not reduced (has to match the signals for the ICA restore)
            # Only components above the threshold is reset (and during a MOR_C if available)
            filter_components.append(filt_cmp_event) 
        events = create_event_dataframe(event)
        # Drop duplicated events from events dataframe
        events = events.drop_duplicates(subset=['start_sec'], keep='first')
        filter_components = list(np.hstack(filter_components))

        # Write the cache
        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            channel_events = len(SignalModel.get_attribute(filter_components, 'channel', 'start_time')[0])
            cache['n_chan'] = channel_events
            cache['signals'] = filter_components

            self._cache_manager.write_mem_cache(self.identifier, cache)

        return {'filter_components': filter_components,
                'deleted_components': deleted_components,
                'events': events}
    
    
