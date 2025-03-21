"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    EOGBaselineProcess
    TODO CLASS DESCRIPTION
"""
import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture

import config
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import SciNode, InputPlug, OutputPlug

from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.PSGReader import commons


DEBUG = False

class EOGBaselineProcess(SciNode):
    """
    Compute baseline stats and extract signals from R stages.

    Parameters
    ----------
        "filename": String
            Path of the current PSG filename.
        "signals": List of SignalModel divided into epochs
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
        "sleep_stages": Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Sleep stages list.
        "parameters": Dict
                Parameters (empty for now)
        
    Returns
    -------
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
            values are a list of 2 items : mean and std
        
    """
    def __init__(self, **kwargs):
        """ Initialize module EOGBaselineProcess """
        super().__init__(**kwargs)
        if DEBUG: print('EOGBaselineProcess.__init__')

        # Input plugs
        InputPlug('filename',self)
        InputPlug('signals',self)
        InputPlug('sleep_stages',self)
        InputPlug('parameters',self)
        # Output plugs
        OutputPlug('signals',self)
        OutputPlug('baseline_stats',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
        # The number of components from the gaussian mixture
        self._n_gauss_components = 3
    
    def compute(self, filename, signals, sleep_stages, parameters):
        """
        Standardize the EOG signals (based on N3 signals) and apply a smoothing filter.

        Parameters
        ----------
            "signals": List of SignalModel
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
            "sleep_stages": Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                    Sleep stages list.
            "parameters": Dict
                    Parameters (empty for now)
            
        Returns
        -------
            "signals": List of SignalModel
                The signals in the sleep stage R only (raw data)
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
                keys are the EOG channel labels (ex: LOC-A2, ROC-A2)
                values are a list of 3 items : mean, std, std_R

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if DEBUG: print('EOGBaselineProcess.compute')

        if isinstance(signals,str) and signals=='':
            err_message = "ERROR: signals not connected"
            raise NodeInputException(self.identifier, "signals", f"EOGBaselineProcess {err_message}.")
        if not isinstance(sleep_stages,pd.DataFrame):
            err_message = f"expected to be a pandas dataframe and the tytpe is {type(sleep_stages)}"
            raise NodeInputException(self.identifier, "sleep_stages", f"EOGBaselineProcess {err_message}.")
        # Extract the list of channels  
        channels_list = np.unique(SignalModel.get_attribute(signals, 'channel', 'channel'))
        n_chans = len(channels_list)
        if n_chans != 2:
            raise NodeRuntimeException(self.identifier, "signals", \
                f"{filename}: 2 channels are expected and {n_chans} channels are found.")

        # The weights favorize one gaussien if only one component is needed.
        def_weights_gauss = np.ones((self._n_gauss_components,1))
        def_weights_gauss = def_weights_gauss*10**(-10)
        def_weights_gauss[0] = 1-10**(-10)    

        # Extract the baseline
        #   Extract the N3 sleep stages signals
        N3_sleep_stages = sleep_stages[sleep_stages['name']==commons.sleep_stages_name['N3']]
        N3_start_times = N3_sleep_stages['start_sec'].values
        n_N3_epochs = len(N3_start_times)
        # If there is less than 1 minute of N3, the baseline is estimated on REM sleep stages
        if n_N3_epochs<2:
            self._log_manager.log(self.identifier, \
                f"{filename} : baseline computed on REM sleep stages ({n_N3_epochs} epochs of N3).")
            N3_sleep_stages = sleep_stages[sleep_stages['name']==commons.sleep_stages_name['R']]
            N3_start_times = N3_sleep_stages['start_sec'].values            

        # Extact the EOG signals for the baseline
        eog_chans = []
        for channel in channels_list:
            # Extract signals for the current channel as list of SignalModel
            signals_cur_chan = SignalModel.get_attribute(signals, None, 'channel', channel)
            eog_chans.append([signal for signal in signals_cur_chan if signal.start_time in N3_start_times])     

        # Compute stats on the baseline
        baseline_stats = {}
        baseline_samples = {}
        for i_eog_chan, channel in enumerate(channels_list):
            samples_cur_chan = SignalModel.get_attribute(eog_chans[i_eog_chan], 'samples', None)
            if isinstance(samples_cur_chan, list):
                # flat the list
                samples_flat = [item for sublist in samples_cur_chan for item in sublist]
                samples_flat = np.array(samples_flat)
            else:
                samples_flat = samples_cur_chan.flatten()
            # Add the mean and std of the current channel
            baseline_stats[channel] = [samples_flat.mean(), samples_flat.std()]
            baseline_samples[channel] = samples_flat

        # Extract the R sleep stages signals
        R_sleep_stages = sleep_stages[sleep_stages['name']==commons.sleep_stages_name['R']]
        R_start_times = R_sleep_stages['start_sec'].values
        n_R_epochs = len(R_start_times)
        # If there is less than 1 epoch of R
        if n_R_epochs<1:
            self._log_manager.log(self.identifier, f"{filename} : No R sleep stages")        

        # Extact the EOG R (sleep stages) signals
        eog_chans = []

        for channel in channels_list:
            # Extract signals for the current channel as list of SignalModel
            signals_cur_chan = SignalModel.get_attribute(signals, None, 'channel', channel)
            eog_chan_cur_chan = [signal for signal in signals_cur_chan if signal.start_time in R_start_times]
            eog_samples_cur_chan = SignalModel.get_attribute(eog_chan_cur_chan, 'samples', None)
            if isinstance(eog_samples_cur_chan, list):
                # flat the list
                samples_flat = [item for sublist in eog_samples_cur_chan for item in sublist]
                samples_flat = np.array(samples_flat)
            else:
                samples_flat = eog_samples_cur_chan.flatten()
                            
            # init_params="random" is chosen to avoid a dead lock in multi threading (https://github.com/MeteoSwiss/ampycloud/issues/97) 
            gaus_mixt = GaussianMixture(n_components=self._n_gauss_components, covariance_type='spherical', \
                weights_init=def_weights_gauss.reshape(self._n_gauss_components), \
                    init_params="random", random_state=0).fit(samples_flat.reshape(-1,1))
            # The main gaussian distribution has the greatest weight
            main_component = np.argmax(gaus_mixt.weights_)
            # Extract the stats of the main gaussian
            std_main=np.sqrt(gaus_mixt.covariances_[main_component])
            #mean_main=gaus_mixt.means_[main_component,0]
            baseline_stats[channel].append(std_main)
            eog_chans.append(eog_chan_cur_chan)

        # Flat eog_chans list
        eog_chans = [item for sublist in eog_chans for item in sublist]

        # Write the cache
        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            cache['n_N3_epochs'] = n_N3_epochs
            cache['channels_list'] = channels_list
            cache['baseline_stats'] = baseline_stats
            cache['baseline_samples'] = baseline_samples
            self._cache_manager.write_mem_cache(self.identifier, cache)        

        return {
            'signals': eog_chans,
            'baseline_stats': baseline_stats
        }