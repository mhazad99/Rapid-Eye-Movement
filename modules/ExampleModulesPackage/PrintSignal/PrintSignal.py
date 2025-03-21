"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    PrintSignal
    Plot the given signal and save it as a PNG file with the specified filename.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class PrintSignal(SciNode):
    def __init__(self, **kwargs):
        """ Initialize module PrintSignal """
        super().__init__(**kwargs)
        if DEBUG: print('PrintSignal.__init__')

        # Input plugs
        InputPlug('signal',self)
        InputPlug('filename',self)
        
        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, signal, filename):
        """
        Plot the given signal and save it as a PNG file with the specified filename.

        Parameters
        ----------
            signal (dict): A dictionary containing the signal data.
            filename (str): The name of the PNG file to save the plot.

        Returns
        -------
            dict: An empty dictionary.

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if not isinstance(signal, dict):
            raise NodeInputException(self.identifier, "signal", "signal must be a dictionary")
        if 'samples' not in signal:
            raise NodeInputException(self.identifier, "samples", "signal must contain 'samples' key")
        if not signal['samples'].any():
            raise NodeInputException(self.identifier, "samples", "signal['samples'] cannot be empty")
        if not isinstance(filename, str):
            raise NodeInputException(self.identifier, "filename", "filename must be a string")
        if filename == "":
            raise NodeInputException(self.identifier, "filename", "filename can't be an empty string.")

        # Plot the signal
        plt.plot(signal["samples"])
        plt.xlabel('Sample')
        plt.ylabel('Amplitude')

        # Save the plot as a PNG file
        plt.savefig(filename, dpi=60)

        # Close the plot
        plt.close()
        
        return {
        }