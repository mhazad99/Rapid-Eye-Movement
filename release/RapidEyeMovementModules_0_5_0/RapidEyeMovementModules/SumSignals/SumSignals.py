"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Sum a signal to the other.

    Parameters
    -----------
        signals: List
            List of SignalModel and their informations
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
                alias:str
                    Channel alias.
                meta:dict
                    Optional information about this signal
                is_modified:bool
                    Has the signal been modified or not.
        channel: String
            A string with the name of the initial channels.
        channel_to_sum: String
            A string with the name of the channel to sum
        new_channel_name : String
            To rename the new summation channel.
            The default name is "channel + channel to sum".
            
    Returns
    -----------    
        new_signal: List
            List of SignalModel and their informations
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
                alias:str
                    Channel alias.
                meta:dict
                    Optional information about this signal
                is_modified:bool
                    Has the signal been modified or not.
"""
import numpy as np
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException

from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class SumSignals(SciNode):
    """"
    Sum a signal to the other.

    Parameters
    -----------
        signals: List
            List of SignalModel and their informations
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
                alias:str
                    Channel alias.
                meta:dict
                    Optional information about this signal
                is_modified:bool
                    Has the signal been modified or not.
        channel: String
            A string with the name of the initial channels.
        channel_to_sum: String
            A string with the name of the channel to sum
        new_channel_name : String
            To rename the new summation channel.
            The default name is "channel + channel to sum".
            
    Returns
    -----------    
        new_signal: List
            List of SignalModel and their informations
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
                alias:str
                    Channel alias.
                meta:dict
                    Optional information about this signal
                is_modified:bool
                    Has the signal been modified or not.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('SumSignals.__init__')
        self._filename = None
        InputPlug('signals', self)
        InputPlug('channel', self)
        InputPlug('channel_to_sum', self)       
        InputPlug('new_channel_name', self)       
        OutputPlug('new_signals', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, signals, channel, channel_to_sum, new_channel_name):
        """"
            Sum a signal to the other.

            Parameters
            -----------
                signals: List
                    List of SignalModel and their informations
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
                        alias:str
                            Channel alias.
                        meta:dict
                            Optional information about this signal
                        is_modified:bool
                            Has the signal been modified or not.
                channel: String
                    A string with the name of the initial channels.
                channel_to_sum: String
                    A string with the name of the channel to sum
                new_channel_name : String
                    To rename the new summation channel.
                    Valid only when a single channel is summed.
                    The default name is "channel + channel to sum".
                    
            Returns
            -----------    
                new_signal: List
                    List of SignalModel and their informations
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
                        alias:str
                            Channel alias.
                        meta:dict
                            Optional information about this signal
                        is_modified:bool
                            Has the signal been modified or not.
            """

        if DEBUG: print('SumSignals.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(signals,str) and signals=='':
            raise NodeInputException(self.identifier, "signals", f"SumSignals this input is not connected.")
        elif not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"SumSignals input of wrong type. Expected: <class 'list'> received: {type(signals)}")     
        elif len(signals)< 2:
            raise NodeInputException(self.identifier, "signals", \
                f"SumSignals at least 2 signals is expected for the operation")      

        # Get list of channels in signals
        channel_lst = np.unique(SignalModel.get_attribute(signals, 'channel', None))

        #---------------------------------------------------------------------------
        # Extract the signals from each channel
        #---------------------------------------------------------------------------

        # When channels are not specified
        if channel=='' and channel_to_sum=='':   
            if len(channel_lst) != 2:
                err_message = " Warning: signals contain more than 2 channels, the operation is {channel_lst[0]} + {channel_lst[1]}"
                self._log_managfer.log(self.identifier, err_message)
            signal_chan_1 = SignalModel.get_attribute(signals, None, 'channel', value_to_test=channel_lst[0])
            signal_chan_2 = SignalModel.get_attribute(signals, None, 'channel', value_to_test=channel_lst[1])

        # When channels are specified
        elif ((len(channel)>0) and (channel in channel_lst)) and (len(channel_to_sum)>0) and (channel_to_sum in channel_lst):
            signal_chan_1 = SignalModel.get_attribute(signals, None, 'channel', value_to_test=channel)
            signal_chan_2 = SignalModel.get_attribute(signals, None, 'channel', value_to_test=channel_to_sum)

        else:
            err_message = " ERROR: channel or channel_to_sum not in signals"
            self._log_manager.log(self.identifier, err_message)
            return {'new_signals': ''}
        

        new_signals = []
        for signal1, signal2 in zip(signal_chan_1, signal_chan_2):
            # Test for sampling rate and duration with the shape
            if signal1.samples.shape != signal2.samples.shape:
                err_message = " ERROR: The signals have different shapes"
                self._log_manager.log(self.identifier, err_message)
                return {'new_signals': ''}
            # Test for the same start time
            elif signal1.start_time != signal2.start_time:
                err_message = " ERROR: The signals have different start times"
                self._log_manager.log(self.identifier, err_message)
                return {'new_signals': ''}
            else:
                # Clone the signal from signal1 to have a valid strat_time, duration and so on...
                new_signal = signal1.clone(clone_samples=True)
                # sum
                new_signal.samples = new_signal.samples + signal2.samples
                new_signal.is_modified = True # Set the flag as modified otherwise it wont be written in the edf
                # Rename the channel if possible
                if len(new_channel_name) > 0:
                    new_signal.channel = new_channel_name
                else:
                    new_signal.channel = new_signal.channel + ' + ' + signal2.channel
                
                new_signals.append(new_signal)

        # Write the cache
        cache = {}
        cache['n_chan'] = 1
        cache['signals'] = new_signals
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'new_signals': new_signals
        }

