"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    SignalGenerator class generates a sinusoidal signal based on the input parameters.
"""
import numpy as np 

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class SignalGenerator(SciNode):
    """
    SignalGenerator class generates a sinusoidal signal based on the input parameters.
    """
    def __init__(self, **kwargs):
        """
        Initializes a new instance of the SignalGenerator class.
        """
        super().__init__(**kwargs)
        if DEBUG: print('SignalGenerator.__init__')

        # Input plugs
        InputPlug('duration',self)
        InputPlug('sample_rate',self)
        InputPlug('frequency',self)
        InputPlug('amplitude',self)
        InputPlug('phase',self)
        

        # Output plugs
        OutputPlug('signal',self)
        
        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, duration,sample_rate,frequency,amplitude,phase):
        """
        Generates a sinusoidal signal based on the input parameters.

        Parameters
        ----------
            duration (float): The duration of the signal in seconds.
            sample_rate (int): The sample rate of the signal in Hz.
            frequency (float): The frequency of the sinusoidal signal in Hz.
            amplitude (float): The amplitude of the sinusoidal signal.
            phase (float): The phase of the sinusoidal signal in radians.

        Returns
        -------
            dict: A dictionary containing the generated sinusoidal signal as a NumPy array with the key 'signal'.
              The 'signal' dictionary contains the following keys:
              - 'samples' (numpy.ndarray): The samples of the sinusoidal signal.
              - 'sample_rate' (int): The sample rate of the signal in Hz.

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        # Check the type of each parameter or convert string inputs
        try:
            if isinstance(duration, str):
                duration = float(duration)
            elif not isinstance(duration, float):
                raise NodeInputException(self.identifier, "duration", "Invalid type for 'duration'. Expected float.")
            
            if isinstance(sample_rate, str):
                sample_rate = int(sample_rate)
            elif not isinstance(sample_rate, int):
                raise NodeInputException(self.identifier, "sample_rate", "Invalid type for 'sample_rate'. Expected int.")
            
            if isinstance(frequency, str):
                frequency = float(frequency)
            elif not isinstance(frequency, float):
                raise NodeInputException(self.identifier, "frequency", "Invalid type for 'frequency'. Expected float.")
            
            if isinstance(amplitude, str):
                amplitude = float(amplitude)
            elif not isinstance(amplitude, float):
                raise NodeInputException(self.identifier, "amplitude", "Invalid type for 'amplitude'. Expected float.")
            
            if isinstance(phase, str):
                phase = float(phase)
            elif not isinstance(phase, float):
                raise NodeInputException(self.identifier, "phase", "Invalid type for 'phase'. Expected float.")
            
        except ValueError as e:
            raise NodeInputException(self.identifier, "parameters", str(e)) from e

        # Create the signal
        num_samples = int(duration * sample_rate)
        t = np.linspace(0, duration, num_samples)
        samples = amplitude * np.sin(2 * np.pi * frequency * t + phase)
        
        # Create the output signal object
        signal = {
            "samples":samples,
            "sample_rate":sample_rate,
        }

        # Cache the signal
        self.cache_signal(signal)

        return {
            "signal": signal
        }

    def cache_signal(self, signal):
        duration = len(signal["samples"]) / signal["sample_rate"]
        duration = min(duration, 10) # Max of 10 seconds of signals
        n_samples = int(duration * signal["sample_rate"])
        cache = {}
        cache['samples'] = signal["samples"][0:n_samples]
        cache['sample_rate'] = signal["sample_rate"]
        self._cache_manager.write_mem_cache(self.identifier, cache)