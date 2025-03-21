"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    MovingAverage
    Compute the average value of the samples of signals on a moving window.

"""
import numpy as np

import config
from commons.NodeInputException import NodeInputException
from flowpipe.ActivationState import ActivationState
from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.Stft import ts2windows as ts2w

DEBUG = False

class MovingAverage(SciNode):
    """
    Compute the average value of the samples of signals on a moving window.

    Parameters
    -----------
        signals : a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : the original  sampling rate of the signal
            signal.channel : current channel label
        win_len_sec     : float
            window length in sec (how much data is taken for each RMS computation)
        win_step_sec    : float 
            window step in sec (each time the RMS computation is applied)
        
    Returns
    -----------  
        signals: list of SignalModel object
            The signals averaged through a moving window.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module MovingAverage """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('win_len_sec',self)
        InputPlug('win_step_sec',self)
        # Output plugs
        OutputPlug('signals',self)

        self._is_master = False 

    
    def compute(self, signals, win_len_sec, win_step_sec):
        """
        Compute the average value of the samples of signals on a moving window.

        Parameters
        -----------
            signals : a list of SignalModel
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the original  sampling rate of the signal
                signal.channel : current channel label 
            win_len_sec     : float
                window length in sec (how much data is taken for each RMS computation)
            win_step_sec    : float 
                window step in sec (each time the RMS computation is applied)
            
        Returns
        -----------  
            signals: list of SignalModel object
                The signals averaged through a moving window.
                
        """

        self.clear_cache()

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(signals,str) and signals=='':
            raise NodeInputException(self.identifier, "signals", f"MovingAverage this input is not connected.")
        elif not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"MovingAverage input of wrong type. Expected: <class 'list'> received: {type(signals)}")     
        elif len(signals)==0:
            return {
                'signals': []
            }            
        
        # It is possible to bypass the "MovingAverage" by passing the input signals directly
        # to the output moving_RMS_values without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'signals': signals
            }        

        # Convert input parameter
        try: 
            win_len_sec = float(win_len_sec)
        except:
            raise NodeInputException(self.identifier, "win_len_sec",\
                 f"MovingAverage the type of this input is unexpected.")
        if win_step_sec is not None:
            try : 
                win_step_sec = float(win_step_sec)
            except:
                raise NodeInputException(self.identifier, "win_step_sec",\
                    f"MovingAverage the type of this input is unexpected.")

        # Create an empty list
        signals_avg = []

        # Loop through all channels
        for i, signal_model in enumerate(signals):
            nsamples_data = len(signal_model.samples)
            if nsamples_data == 0:
                err_message = f' WARNING: Signal has no samples for channel:{signal_model.channel}'
                self._log_manager.log(self.identifier, err_message)
                print(err_message)
                continue

            # Convert the signal into windows
            fs = signal_model.sample_rate
            nsample_win = win_len_sec*fs
            if not nsample_win.is_integer():
                # Compute the real win_len used
                err_message = f' Warning : win_len_sec {win_len_sec} is changed for {int(round(nsample_win))/fs}'
                self._log_manager.log(self.identifier, err_message)               
                win_len_sec = int(round(nsample_win))/fs

            if win_step_sec is None:
                nsample_step = 1
            else:
                nsample_step = win_step_sec*fs
                if not nsample_step.is_integer():
                    # Compute the real win_step used
                    err_message = f' Warning : win_step_sec {win_step_sec} is changed for {int(round(nsample_step))/fs}'
                    self._log_manager.log(self.identifier, err_message)        
                    win_step_sec = int(round(nsample_step))/fs

            nsample_win = int(round(win_len_sec*fs))

            # Clone signals without the samples to create a list of SignalModel
            signal_avg = signal_model.clone(clone_samples=False)

            # Compute the moving average via a convolution filter with all weights equal
            weights = np.ones(nsample_win) / nsample_win
            ts_in_win_avg = np.convolve(signal_model.samples.copy(), weights, mode='same')

            signal_avg.samples = ts_in_win_avg
            signals_avg.append(signal_avg)

            # Extract the number of channels
            channel_lst = [signal.channel for signal in signals_avg]
            n_chan = len(np.unique(np.array(channel_lst)))

            # Write the cache
            cache = {}
            if config.is_dev: # Avoid save of the recording when not developping
                cache['n_chan'] = n_chan
                cache['signals'] = signals_avg
                self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'signals': signals_avg
            }