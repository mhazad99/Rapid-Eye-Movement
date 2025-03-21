"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    RemDetector
    Detect Rapid eye movements during REM sleep
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
import numpy as np
import pandas as pd
from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class RemDetector(SciNode):
    """
    Detect Rapid eye movements during REM sleep

    Inputs:
        "signals": List
            Each item of the list is a SignalModel object as described below:
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the sampling rate of the signal
                signal.channel : current channel label
                signal.start_time : The start time of the signal in sec
                signal.end_time : The end time of the signal in sec
                (for more info : look into common/SignalModel)
        "event_group" : string
            Group in which the detected events are added.
        "event_name" : string
            Name of the event detected.
        "event_channel" : string
            (optional) : if '' the channel name of the signal is used.
            Channel label to add the detected event.
            Useful when a created channel is used to detect event and 
            you want to see the detected event on a real channel.
        "border_effect": float
            Percentage to remove of each side of the window
        "percentile": int
            Value between 0-100 to threshold the highest slopes
        

    Outputs:
        "detections": pandas DataFrame
            df of events with field
                group: Group of events this event is part of (String)
                name: Name of the event (String)
                start_sec: Starting time of the event in sec (Float)
                duration_sec: Duration of the event in sec (Float)
                channels: Channel where the event occures (String)
        
    """
    def __init__(self, **kwargs):
        """ Initialize module RemDetector """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')
        # Input plugs
        InputPlug('signals',self)
        InputPlug('event_group',self)
        InputPlug('event_name',self)
        InputPlug('event_channel', self)
        InputPlug('border_effect',self)
        InputPlug('percentile',self)
        # Output plugs
        OutputPlug('detections',self)
        self._is_master = False 
    

    def compute(self, signals, event_group, event_name, event_channel, border_effect, percentile):
        """
        Detect Rapid eye movements during REM sleep

        Inputs:
            "signals": List
                Each item of the list is a SignalModel object as described below:
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the sampling rate of the signal
                    signal.channel : current channel label
                    signal.start_time : The start time of the signal in sec
                    signal.end_time : The end time of the signal in sec
                    (for more info : look into common/SignalModel)
            "event_group" : string
                Group in which the detected events are added.
            "event_name" : string
                Name of the event detected.
            "event_channel" : string
                (optional) : if '' the channel name of the signal is used.
                Channel label to add the detected event.
                Useful when a created channel is used to detect event and 
                you want to see the detected event on a real channel.
            "border_effect": float
                Percentage to remove of each side of the window
            "percentile": int
                Value between 0-100 to threshold the highest slopes
            
        Outputs:
            "detections": pandas DataFrame
                df of events with field
                    group: Group of events this event is part of (String)
                    name: Name of the event (String)
                    start_sec: Starting time of the event in sec (Float)
                    duration_sec: Duration of the event in sec (Float)
                    channels: Channel where the event occures (String)
            
        """
        # Clear the cache (usefull for the second run)
        self.clear_cache()

        # Check if all epoch can be compute simultaneously
        is_vectorizable = all([len(signal.meta['derivative']) == len(signals[0].meta['derivative']) for signal in signals])
        if is_vectorizable:
            # Get properties of signal
            n = len(signals[0].meta['derivative'])

            # Set borders to remove
            t_in = int(border_effect/100 * n)

            # Get max slopes from desired derivative
            samples = np.vstack([signal.meta['derivative'] for signal in signals])
            max_slope = np.max(np.abs(samples[:,t_in:-t_in]),axis=1)

        else:
            max_slopes = []
            for signal in signals:
                # Get properties of signal
                n = len(signal.meta['derivative'])

                # Set borders to remove
                t_in = int(border_effect/100 * n)

                # Get max slopes from desired derivative
                samples = signal.meta['derivative'][:,t_in:-t_in]
                max_slope = np.max(np.abs(samples),axis=1)
                max_slopes.append(max_slope)
            max_slopes = np.hstack(max_slopes)

        # Get index with highest amplitude
        index_above_thresh = np.sort(np.argsort(max_slope)[np.ceil(len(signals)*(percentile/100)).astype(int):])
        signals_above_thresh = np.array(signals)[index_above_thresh]

        # Initialize format for detection events
        event = []
        for sig in signals_above_thresh:
            if isinstance(event_channel, str) and len(event_channel)>0:
                event.append([event_group, event_name, sig.start_time, sig.duration, [event_channel]])
            else:
                event.append([event_group, event_name, sig.start_time, sig.duration, sig.channels])

        # Create dataframe of detections
        events = pd.DataFrame(event,
                              index=None,
                              columns=['group','name','start_sec','duration_sec','channels'],
                              dtype=None,
                              copy=False)

        # Write the cache
        cache = {}
        cache['signals'] = signals
        cache['events'] =  events
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'detections': events
        }