"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    AddSignals class represents a module that adds two signals together.
"""
import numpy as np

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class AddSignals(SciNode):
    """
    This class represents a module that adds two signals together.

    Parameters
    ----------
    signal_1 : dict
        Dictionary representing the first signal.
        It should contain the following keys:
        - 'samples': numpy.ndarray
            Array of signal samples.
        - 'sample_rate': int
            Sample rate of the signal.

    signal_2 : dict
        Dictionary representing the second signal.
        It should contain the same keys as `signal_1`.

    Returns
    -------
    signal : dict
        Dictionary representing the resulting signal.
        It contains the same keys as `signal_1` and `signal_2`.

    Raises
    ------
    NodeInputException
        If any of the input parameters have invalid types or missing keys.
    """

    def __init__(self, **kwargs):
        """ Initialize module AddSignals """
        super().__init__(**kwargs)
        if DEBUG: print('AddSignals.__init__')

        # Input plugs
        InputPlug('signal_1',self)
        InputPlug('signal_2',self)
        

        # Output plugs
        OutputPlug('signal',self)
        

        # Init module variables
        self.this_is_an_example_you_can_delete_it = 0

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, signal_1,signal_2):
        """
        Add two signals together.

        Parameters
        ----------
        signal_1 : dict
            Dictionary representing the first signal.
            It should contain the following keys:
            - 'samples': numpy.ndarray
                Array of signal samples.
            - 'sample_rate': int
                Sample rate of the signal.

        signal_2 : dict
            Dictionary representing the second signal.
            It should contain the same keys as `signal_1`.

        Returns
        -------
        signal : dict
            Dictionary representing the resulting signal.
            It contains the same keys as `signal_1` and `signal_2`.

        Raises
        ------
        NodeInputException
            If any of the input parameters have invalid types or missing keys.
        NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        # Make appropriate checks to input values
        if not isinstance(signal_1, dict):
            raise NodeInputException(self.identifier, "signal_1", "signal_1 must be a dictionary")
        if not isinstance(signal_2, dict):
            raise NodeInputException(self.identifier, "signal_2", "signal_2 must be a dictionary")
        
        if 'samples' not in signal_1 or 'samples' not in signal_2:
            raise NodeInputException(self.identifier, "samples", "signal_1 and signal_2 must contain 'samples' key")

        if 'sample_rate' not in signal_1 or 'sample_rate' not in signal_2:
            raise NodeInputException(self.identifier, "sample_rate", "signal_1 and signal_2 must contain 'sample_rate' key")
        
        if signal_1['sample_rate'] != signal_2['sample_rate']:
            raise NodeInputException(self.identifier, "sample_rate", "Sample rates of both signals must be the same.")

        # Determine the lengths of the signal samples
        len_signal_1 = len(signal_1['samples'])
        len_signal_2 = len(signal_2['samples'])
        
        # Extend the shorter signal with zeros
        if len_signal_1 < len_signal_2:
            signal_1['samples'] = np.pad(signal_1['samples'], (0, len_signal_2 - len_signal_1), 'constant')
        elif len_signal_2 < len_signal_1:
            signal_2['samples'] = np.pad(signal_2['samples'], (0, len_signal_1 - len_signal_2), 'constant')
        
        # Perform the addition of the signals
        result_samples = signal_1['samples'] + signal_2['samples']
        
        # Create the output signal dictionary
        output_signal = {
            'samples': result_samples,
            "sample_rate":signal_1['sample_rate']
        }
        
        # Caching the result will allow us to display it in the results tab.
        self.cache_signal(signal_1, signal_2, output_signal)
        return {'signal': output_signal}
    
    def cache_signal(self, signal1, signal2, output_signal):
        duration = len(output_signal["samples"]) / output_signal["sample_rate"]
        duration = min(duration, 10) # Max of 10 seconds of signals
        n_samples = int(duration * output_signal["sample_rate"])
        cache = {}
        cache['samples1'] = signal1["samples"][0:n_samples]
        cache['samples2'] = signal2["samples"][0:n_samples]
        cache['output_samples'] = output_signal["samples"][0:n_samples]
        cache['sample_rate'] = output_signal["sample_rate"]
        self._cache_manager.write_mem_cache(self.identifier, cache)