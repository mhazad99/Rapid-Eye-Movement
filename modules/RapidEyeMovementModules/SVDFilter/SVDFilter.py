"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    SVDFilter
    A two-stage SVD-based artifact removal filter for EEG signals that uses 
    mutual information to identify and remove artifact components.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import numpy as np
import pandas as pd
import copy
from scipy.signal.windows import tukey
from sklearn.feature_selection import mutual_info_regression
from CEAMSModules.PSGReader.SignalModel import SignalModel
import sys
from tqdm import tqdm

DEBUG = False

class SVDFilter(SciNode):
    """
    A two-stage SVD-based artifact removal filter for EEG signals.
    
    This module operates in two modes:
    1. Component Extraction: Performs SVD decomposition and returns temporal components
       for external mutual information calculation with EOG/artifact reference signals.
    2. Filtering: Uses components with pre-calculated MI artifact indices to remove
       artifacts via spatial projection filtering.

    Parameters
    ----------
        signals: List[SignalModel]
            List of EEG signal segments (one per event) with samples as numpy arrays
        events: DataFrame
            DataFrame of events corresponding to signal segments
        original_signals: List[SignalModel] or None
            Original signal segments for length matching after filtering
        configuration: Dict
            Configuration parameters including 'number_of_components' and 'tukey_alpha'
        components: List[SignalModel] or None
            SVD temporal components with mutual_info metadata for artifact removal
        

    Returns
    -------
        filtered_signal: List[SignalModel] or None
            Artifact-filtered signal segments (filtering mode) or None (extraction mode)
        events: DataFrame
            Pass-through of input events
        components: Array of list[SignalModel] or None
            SVD temporal components with metadata (extraction mode) or None (filtering mode)
        
    """
    def __init__(self, **kwargs):
        """ Initialize module SVDFilter """
        super().__init__(**kwargs)
        if DEBUG: print('SVDFilter.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('events',self)
        InputPlug('original_signals',self)
        InputPlug('configuration',self)
        InputPlug('components',self)

        # Output plugs
        OutputPlug('filtered_signal',self)
        OutputPlug('events',self)
        OutputPlug('components',self)
        
        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, signals,events,original_signals,configuration, components):
        """
        Perform SVD-based artifact removal on EEG signals.
        
        Mode 1 (Component Extraction): When components=None, performs SVD decomposition 
        on each signal segment and returns temporal components for external mutual 
        information calculation.
        
        Mode 2 (Filtering): When components are provided with MI metadata, uses spatial 
        projection to remove artifact components and returns filtered signals.

        Parameters
        ----------
            signals: List[SignalModel]
                EEG signal segments to process, one segment per event
            events: DataFrame
                Event markers corresponding to signal segments
            original_signals: List[SignalModel] or None
                Original signals for length matching after filtering
            configuration: Dict
                Configuration with 'number_of_components' and 'tukey_alpha' parameters
            components: Array of list[SignalModel] or None
                SVD components with mutual_info metadata for artifact identification
            

        Returns
        -------
            filtered_signal: List[SignalModel] or None
                Filtered signals (mode 2) or None (mode 1)
            events: DataFrame
                Pass-through of input events
            components: Array of list[SignalModel] or None
                SVD temporal components (mode 1) or None (mode 2)
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if DEBUG: print('SVDFilter.compute')
        # Clear the cache (useful for the second run)
        self.clear_cache() # It makes the cache=None
        
        # Validate inputs
        if isinstance(signals, str) and signals == '':
            raise NodeInputException(self.identifier, "signals", f"SVDFilter this input is not connected.")
        elif not isinstance(signals, list):
            raise NodeInputException(self.identifier, "signals", \
                f"SVDFilter input of wrong type. Expected: <class 'list'> received: {type(signals)}")
        elif len(signals) == 0:
            raise NodeInputException(self.identifier, "signals", \
                f"SVDFilter at least 1 signal is expected for the operation")
        
        if isinstance(events, str) and events == '':
            raise NodeInputException(self.identifier, "events", f"SVDFilter this input is not connected.")
        elif not isinstance(events, (list, pd.DataFrame)) and events is not None:
            raise NodeInputException(self.identifier, "events", \
                f"SVDFilter input of wrong type. Expected: <class 'list'> or <class 'pandas.DataFrame'> received: {type(events)}")
        
        if isinstance(configuration, str) and configuration == '':
            raise NodeInputException(self.identifier, "configuration", f"SVDFilter this input is not connected.")
        elif not isinstance(configuration, dict):
            raise NodeInputException(self.identifier, "configuration", \
                f"SVDFilter input of wrong type. Expected: <class 'dict'> received: {type(configuration)}")
        
        # Validate configuration dictionary has required keys
        required_config_keys = ['number_of_components', 'tukey_alpha']
        for key in required_config_keys:
            if key not in configuration:
                raise NodeInputException(self.identifier, "configuration", \
                    f"SVDFilter configuration missing required key: '{key}'")
        
        # Validate components input when provided
        if isinstance(components, str) and components == '':
            # Components is an empty string (not connected), this is valid
            pass
        elif components is not None:
            if not isinstance(components, (list, np.ndarray)):
                raise NodeInputException(self.identifier, "components", \
                    f"SVDFilter input of wrong type. Expected: <class 'list'> or <class 'numpy.ndarray'> received: {type(components)}")
            elif len(components) == 0:
                raise NodeInputException(self.identifier, "components", \
                    f"SVDFilter components array is empty when provided")
        
        # Validate original_signals when provided
        if isinstance(original_signals, str) and original_signals == '':
            # original_signals is an empty string (not connected), this is valid
            pass
        elif original_signals is not None:
            if not isinstance(original_signals, list):
                raise NodeInputException(self.identifier, "original_signals", \
                    f"SVDFilter input of wrong type. Expected: <class 'list'> or None received: {type(original_signals)}")
            elif len(original_signals) == 0:
                raise NodeInputException(self.identifier, "original_signals", \
                    f"SVDFilter original_signals list is empty when provided")
            
        signals_events = SignalModel.get_attribute(signals, None, 'start_time')
        samples_events = SignalModel.get_attribute(signals, 'samples', 'start_time')
        channel_events = SignalModel.get_attribute(signals, 'channel', 'start_time')
        if original_signals is None or original_signals == '':
            original_signals_events = SignalModel.get_attribute(signals, None, 'start_time')
        else:
            original_signals_events = SignalModel.get_attribute(original_signals, None, 'start_time')

        total_event = len(signals_events)
        if components is not None and len(components) > 0:
            # Set progress bar
            desc = 'Applying second SVD'
            use_progress_bar = sys.stdout is not None and sys.stdout.isatty()
            pbar1 = tqdm(total=total_event, desc=desc, disable=not use_progress_bar)

            svd_components = None
            meta_events = SignalModel.get_attribute(components, 'meta', 'start_time') 
            n_components = configuration['number_of_components']  # Default to 1 component if not specified
            for signal, sample, chans, meta, original_signal in zip(signals_events, samples_events, channel_events, meta_events, original_signals_events):
                # Extract the index of the maximum mutual information
                MI_vals = [meta[i]['mutual_info'] for i in range(len(meta))]
                Max_indices = list(np.argsort(MI_vals)[-n_components:][::-1])
                # Remove DC offset
                EEG_segments_centered = sample - np.mean(sample, axis=1, keepdims=True)
                # This gives spatial and temporal components explicitly
                U, S, Vt = np.linalg.svd(EEG_segments_centered, full_matrices=False)
                
                # Method 1: Spatial projection
                # Artifact subspace - select columns of U corresponding to artifact Vt rows
                U_art = U[:, Max_indices]
                P_art = U_art @ U_art.T
                Filter = np.eye(U.shape[0]) - P_art
                # Apply the filter to the centered EEG segments
                EEG_segments_filtered = Filter @ EEG_segments_centered
                
                # Alternative Method 2: Direct SVD reconstruction
                # Zero out singular values for artifact components
                # S_filtered = S.copy()
                # S_filtered[Max_indices[item]] = 0
                # EEG_segments_filtered = (U @ np.diag(S_filtered) @ Vt)
                # Reconstruct the filtered signal
                EEG_segments_filtered_mean = EEG_segments_filtered + np.mean(sample, axis=1, keepdims=True)
                # Convert filtered signal back to the original format
                # Apply the Tukey window to each segment
                n_times = EEG_segments_filtered_mean.shape[1]
                tukey_window = tukey(n_times, alpha = configuration['tukey_alpha'])[np.newaxis, :]  # Create a 2D array for broadcasting
                Tukey_filtered_segment = tukey_window * EEG_segments_filtered_mean + (1 - tukey_window) * sample
   
                # Replace the REMs events with the original events (without extension)
                len_extended = len(sample[0])
                len_original = len(original_signal[0].samples)

                if len_extended < len_original:
                    raise ValueError(f"Extended signal length {len_extended} is less than original length {len_original} for signal {i}.")
                
                start_idx = (len_extended - len_original) // 2
                end_idx = start_idx + len_original

                for i, chan in enumerate(original_signal):
                    chan.samples = Tukey_filtered_segment[i,start_idx:end_idx]
                    chan.is_modified = True

                pbar1.update(1)

        elif components is None or len(components) == 0:
            # Set progress bar
            desc = 'Applying first SVD'
            use_progress_bar = sys.stdout is not None and sys.stdout.isatty()
            pbar0 = tqdm(total=total_event, desc=desc, disable=not use_progress_bar)

            original_signals = None
            svd_components = []
            # Loop over events
            for signal, sample, chans in zip(signals_events, samples_events, channel_events):
                # sample is (n_channels, n_samples)
                EEG_segments_centered = sample - np.mean(sample, axis=1, keepdims=True)
                # This gives spatial and temporal components explicitly
                U, S, Vt = np.linalg.svd(EEG_segments_centered, full_matrices=False)
                # component is (n_components, n_samples)
                for i, chan in enumerate(signal):
                    # Create new signal
                    new_signals_chan = chan.clone(clone_samples=False)
                    new_signals_chan.meta = {}
                    new_signals_chan.samples = Vt[i] #(n_samples,)
                    new_signals_chan.is_modified = True
                    new_signals_chan.alias = 'SVD_CMP'
                    new_signals_chan.channel = 'SVD_CMP_' + str(i)
                    new_signals_chan.meta['chan_order'] = chans
                    svd_components.append(new_signals_chan)
            
                pbar0.update(1)

        return {
            'filtered_signal': original_signals,
            'events': events, 
            'components': svd_components
        }