"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    SVDFilter
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import numpy as np
import pandas as pd
import copy
from scipy.signal.windows import tukey

DEBUG = False

class SVDFilter(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        signals: TODO TYPE
            TODO DESCRIPTION
        events: TODO TYPE
            TODO DESCRIPTION
        signals_from_events2: TODO TYPE
            TODO DESCRIPTION
        configuration: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        filtered_signal: TODO TYPE
            TODO DESCRIPTION
        events: TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module SVDFilter """
        super().__init__(**kwargs)
        if DEBUG: print('SVDFilter.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('events',self)
        InputPlug('signals_from_events2',self)
        InputPlug('configuration',self)
        

        # Output plugs
        OutputPlug('filtered_signal',self)
        OutputPlug('events',self)
        
        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, signals,events,signals_from_events2,configuration):
        """
        TODO DESCRIPTION

        Parameters
        ----------
            signals: TODO TYPE
                TODO DESCRIPTION
            events: TODO TYPE
                TODO DESCRIPTION
            signals_from_events2: TODO TYPE
                TODO DESCRIPTION
            configuration: TODO TYPE
                TODO DESCRIPTION
            

        Returns
        -------
            filtered_signal: TODO TYPE
                TODO DESCRIPTION
            events: TODO TYPE
                TODO DESCRIPTION
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if DEBUG: print('SVDFilter.compute')
        # Validate inputs
        if not isinstance(signals, list):
            raise NodeInputException('signals must be a list')
        '''if not isinstance(events, list):
            raise NodeInputException('events must be a list')
        if not isinstance(signals_from_events2, str):
            raise NodeInputException('signals_from_events2 must be a list')
        if not isinstance(configuration, dict):
            raise NodeInputException('configuration must be a dict')'''
        Seg_len = [len(signal.samples) for signal in signals]
        EEG_signals = []
        number_of_channels = len(signals) // len(events)
        for i in range(len(events)):
            start_idx = i * number_of_channels
            end_idx = (i + 1) * number_of_channels
            
            segment_dfs = []
            for seg in signals[start_idx:end_idx]:
                # If seg is already a DataFrame, just append it
                if isinstance(seg, pd.DataFrame):
                    segment_dfs.append(seg.T)
                # If seg is an object with samples as numpy array
                elif hasattr(seg, "samples"):
                    segment_dfs.append(pd.DataFrame(seg.samples).T)
                # If seg is a numpy array
                elif hasattr(seg, "__array__"):
                    segment_dfs.append(pd.DataFrame(seg).T)
                else:
                    raise TypeError(f"Unsupported segment type: {type(seg)}")

            # Concatenate along columns
            merged_channels = pd.concat(segment_dfs, axis=0)
            EEG_signals.append(merged_channels)
        
        EEG_signals_concatenated = pd.concat(EEG_signals, axis=1)
        EEG_signals = EEG_signals_concatenated.to_numpy()
    
        # Remove DC offset
        EEG_signals_centered = EEG_signals - np.mean(EEG_signals, axis=1, keepdims=True)
        
        # Perform SVD
        P = EEG_signals_centered @ EEG_signals_centered.T
        n_components = configuration['number_of_components']  # Default to 1 component if not specified
        U, _, _ = np.linalg.svd(P)
        artifact_spatial = U[:, :n_components]  # strongest components

        # Build projection filter
        projection = artifact_spatial @ artifact_spatial.T
        filter_matrix = np.eye(EEG_signals.shape[0]) - projection
         
        EEG_signals_filtered = filter_matrix @ EEG_signals_centered
        
        # Reconstruct the filtered signal
        filtered_signal = EEG_signals_filtered + np.mean(EEG_signals, axis=1, keepdims=True)

        # Apply the Tukey window to the filtered signal
        '''n_times = filtered_signal.shape[1]
        tukey_window = tukey(n_times, alpha=0.5)[np.newaxis, :]  # Create a 2D array for broadcasting
        Tukey_filtered_signal = tukey_window * filtered_signal + (1 - tukey_window) * EEG_signals'''

        # Convert filtered signal back to the original format
        new_signals = copy.deepcopy(signals)
        Seg_len = [Seg_len[i] for i in range(0, len(Seg_len), number_of_channels)]
        for i, seg_len in enumerate(Seg_len):
            extracted_segment = filtered_signal[:, sum(Seg_len[:i]):sum(Seg_len[:i+1])]
            # Apply the Tukey window to each segment
            n_times = extracted_segment.shape[1]
            tukey_window = tukey(n_times, alpha = configuration['tukey_alpha'])[np.newaxis, :]  # Create a 2D array for broadcasting
            Tukey_filtered_segment = tukey_window * extracted_segment + (1 - tukey_window) * EEG_signals[:, sum(Seg_len[:i]):sum(Seg_len[:i+1])]
            for j in range(number_of_channels):
                idx = i * number_of_channels + j
                if hasattr(signals[idx], "samples"):
                    new_signals[idx].samples = Tukey_filtered_segment[j, :]
                else:
                    raise TypeError(f"Unsupported segment type for assignment: {type(signals[idx])}")
        
        if signals_from_events2 is None or signals_from_events2 == '':
            signals_from_events2 = new_signals         
        # Replace the REMs events with the original events (without extension)
        else:
            for i in range(len(signals_from_events2)):
                len_extended = len(new_signals[i].samples)
                len_original = len(signals_from_events2[i].samples)

                if len_extended < len_original:
                    raise ValueError(f"Extended signal length {len_extended} is less than original length {len_original} for signal {i}.")
                
                start_idx = (len_extended - len_original) // 2
                end_idx = start_idx + len_original
                signals_from_events2[i].samples = new_signals[i].samples[start_idx:end_idx]

        return {
            'filtered_signal': signals_from_events2,
            'events': events
        }