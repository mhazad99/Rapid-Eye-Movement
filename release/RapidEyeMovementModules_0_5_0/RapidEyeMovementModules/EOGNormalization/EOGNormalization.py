"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    EOGNormalization
    Normalize EOG signals based on the baseline stats.
"""

import numpy as np

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

import config
from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class EOGNormalization(SciNode):
    """
    Normalize EOG signals based on the baseline stats.

    Parameters
    ----------        
    
        "filename": String
            Path of the current PSG filename.

        "signals": List of SignalModel
            Signals in R sleep stages only
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        "baseline_stats": Dict
            Statistics of the baseline.
            keys are EOG0 and EOG1 (for left and right)
            values are a list of 3 items : mean N3, stdN3, stdR

        "parameters" : Dict
            Parameters of the normalization.
            'bsl_normalization' : bool
                Flag to normalize the signal with the std got from N3 sleep stages.
                Data is z-scoed transformed.
            'rem_weight' : bool
                Flag to normalize the signal with the std ratio got from the R sleep stage.
                The ratio is used to scale the smaller channel to the larger one.  
            'rem_normalization' : bool
                Flag to normalize the signal with the std got from the R sleep stage.
                Data is z-scoed transformed.    

    Returns
    -------
        "signals": List of SignalModel
            Signals (normalized) from R sleep stages only
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        
    """
    def __init__(self, **kwargs):
        """ Initialize module EOGNormalization """
        super().__init__(**kwargs)
        if DEBUG: print('EOGNormalization.__init__')

        # Input plugs
        InputPlug('filename',self)
        InputPlug('signals',self)
        InputPlug('baseline_stats',self)
        InputPlug('parameters',self)
        # Output plugs
        OutputPlug('signals',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, filename, signals, baseline_stats, parameters):
        """
    Normalize EOG signals based on the baseline stats.

    Parameters
    ----------        
    
        "filename": String
            Path of the current PSG filename.

        "signals": List of SignalModel
            Signals in R sleep stages only
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        "baseline_stats": Dict
            Statistics of the baseline.
            keys are EOG0 and EOG1 (for left and right)
            values are a list of 3 items : mean N3, stdN3, stdR

        "parameters" : Dict
            Parameters of the normalization.
            'bsl_normalization' : bool
                Flag to normalize the signal with the std got from N3 sleep stages.
                Data is z-scoed transformed.
            'rem_weight' : bool
                Flag to normalize the signal with the std ratio got from the R sleep stage.
                The ratio is used to scale the smaller channel to the larger one.  
            'rem_normalization' : bool
                Flag to normalize the signal with the std got from the R sleep stage.
                Data is z-scoed transformed.      

    Returns
    -------
        "signals": List of SignalModel
            Signals (normalized) from R sleep stages only
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        """

        if DEBUG: print('EOGBaselineProcess.compute')

        if isinstance(signals,str) and signals=='':
            err_message = "ERROR: signals not connected"
            raise NodeInputException(self.identifier, "signals", f"EOGBaselineProcess {err_message}.")
        # Extract the list of channels  
        channels_list = np.unique(SignalModel.get_attribute(signals, 'channel', 'channel'))
        n_chans = len(channels_list)
        if n_chans != 2:
            raise NodeRuntimeException(self.identifier, "signals", \
                f"{filename}: 2 channels are expected and {n_chans} channels are found.")
        if isinstance(baseline_stats,str) and signals=='':
            baseline_stats = eval(baseline_stats)
        if not isinstance(baseline_stats,dict):
            err_message = "ERROR: baseline stats are not generated"
            raise NodeInputException(self.identifier, "baseline_stats", f"EOGBaselineProcess {err_message}.")

        # Compute the rem_coeff = (STD_r_stages channel2) / (std_r_stages channel1)
        rem_coeff_list = []
        for channel in channels_list:
            rem_coeff_list.append(baseline_stats[channel][2])
        rem_coeff = {}
        for i_chan, channel in enumerate(channels_list):
            if i_chan==0:
                temp_coeff = rem_coeff_list[1]/rem_coeff_list[0]
                if temp_coeff<1:
                    rem_coeff[channel]=1
                    self._log_manager.log(self.identifier, f"{filename}:{channel} rem coefficient is forced to 1.")
                else:
                    rem_coeff[channel]=temp_coeff
            else:
                temp_coeff = rem_coeff_list[0]/rem_coeff_list[1]
                if temp_coeff<1:
                    rem_coeff[channel]=1
                else:
                    rem_coeff[channel]=temp_coeff

        # Normalize the signals
        signals_norm = []
        for signal in signals:
            signal_norm = SignalModel.clone(signal)
            signal_norm.samples = (signal.samples - np.mean(signal.samples))
            if parameters['bsl_normalization']:
                signal_norm.samples = signal_norm.samples / baseline_stats[signal.channel][1] 
            if parameters['rem_weight']: 
                signal_norm.samples = signal_norm.samples * rem_coeff[signal.channel]
            if parameters['rem_normalization']:
                signal_norm.samples = signal_norm.samples / baseline_stats[signal.channel][2] 
            signals_norm.append(signal_norm)

        # Write to the cache to use the data in the resultTab
        if config.is_dev: # Avoid save of the recording when not developping
            cache = {}
            
            # Extract all the samples of the EOG signals
            channels_norm = []
            for i_chan, channel in enumerate(channels_list):
                signals_cur_chan = SignalModel.get_attribute(signals_norm, None, 'channel', channel)
                eog_samples_cur_chan = SignalModel.get_attribute(signals_cur_chan, 'samples', None)
                if isinstance(eog_samples_cur_chan, list):
                    # flat the list
                    samples_flat = [item for sublist in eog_samples_cur_chan for item in sublist]
                    samples_flat = np.array(samples_flat)
                else:
                    samples_flat = eog_samples_cur_chan.flatten()
                channels_norm.append(samples_flat)
            
            cache['signals'] = channels_norm
            cache['channels_list'] = channels_list
            self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'signals': signals_norm
        }