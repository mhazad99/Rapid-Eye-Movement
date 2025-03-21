"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    PolynomialApprox
    Extract the polynomial approximation of a signal
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException

from CEAMSModules.PSGReader.SignalModel import SignalModel
import numpy as np

DEBUG = False

class PolynomialApprox(SciNode):
    """
    Extract the polynomial approximation of a signal

    Inputs:
        "signals": List
            Each item of the list is a SignalModel object as described below:
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the sampling rate of the signal
                signal.channel : current channel label
                signal.start_time : The start time of the signal in sec
                signal.end_time : The end time of the signal in sec
                (for more info : look into common/SignalModel)
        "order": Int
            Order of the polynomial
        

    Outputs:
        "signals": List
            Same list of SignalModel with associated polynomial in signal.meta[poly]
        "polynomials": List
            List of polynomial of each signal
        
    """
    def __init__(self, **kwargs):
        """ Initialize module PolynomialApprox """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('order',self)
        

        # Output plugs
        OutputPlug('signals',self)
        OutputPlug('polynomials',self)
        
        self._is_master = False 
    
    def compute(self, signals, order):
        """
        Extract the polynomial approximation of a signal

        Inputs:
            "signals": List
                Each item of the list is a SignalModel object as described below:
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the sampling rate of the signal
                    signal.channel : current channel label
                    signal.start_time : The start time of the signal in sec
                    signal.end_time : The end time of the signal in sec
                    (for more info : look into common/SignalModel)
            "order": Int
                Order of the polynomial
            

        Outputs:
            "signals": List
                Same list of SignalModel with associated polynomial in signal.meta[poly]
            "polynomials": List
                List of polynomial of each signal
            
        """
        # Verify inputs
        if isinstance(signals,str) and signals=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals", \
                f"SignalsFromEvents this input is not connected.")

        # Optimized method
        if SignalModel.is_vectorizable(signals, False):
            # Initialize new list
            p_sigs = []

            # Get properties of signal
            k = order + 1
            n_sample = len(signals[0].samples)
            fs = signals[0].sample_rate

            # Get time vector
            t = np.array(range(0,n_sample)/fs)

            # Get coefficient a and b
            a_f = lambda n: (np.sum(np.power(t,n)))
            b_f = lambda y,n: (np.sum(y * np.power(t,n)))

            a = [a_f(2*k-i-j) for i in range(1,k + 1) for j in range(1,k + 1)]
            a = np.reshape(a,(k,k))

            for signal in signals:
                b = np.array([b_f(signal.samples,k-i) for i in range(1,k + 1)])
                
                # Find a\b'
                c = np.linalg.solve(a, b.T)

                # Polynomial fit
                p = (c[-1] * np.ones([1,n_sample]))[0]
                for i in range(1, k):
                    p = p + c[i-1]*np.power(t,k-i)
                
                # Add or create new signal
                signal.meta['poly'] = p

                p_sig = signal.clone(clone_samples=False)
                p_sig.samples = p
                p_sig.is_modified = True

                p_sigs.append(p_sig)

        # Slower method
        else:
            # Initialize new list
            p_sigs = []
            k = order + 1

            for signal in signals:
                # Get properties of signal
                n_sample = len(signal.samples)
                fs = signal.sample_rate

                # Get time vector
                t = np.array(range(0,n_sample)/fs)

                # Get coefficient a and b
                a_f = lambda n: (np.sum(np.power(t,n)))
                b_f = lambda y,n: (np.sum(y * np.power(t,n)))

                a = [a_f(2*k-i-j) for i in range(1,k + 1) for j in range(1,k + 1)]
                a = np.reshape(a,(k,k))

                b = np.array([b_f(signal.samples,k-i) for i in range(1,k + 1)])
                
                # Find a\b'
                c = np.linalg.solve(a, b.T)

                # Polynomial fit
                p = (c[-1] * np.ones([1,n_sample]))[0]
                for i in range(1, k):
                    p = p + c[i-1]*np.power(t,k-i)
                

                # Add or create new signal
                signal.meta['poly'] = p

                p_sig = signal.clone(clone_samples=False)
                p_sig.samples = p
                p_sig.is_modified = True

                p_sigs.append(p_sig)

        # Extract the number of channels
        channel_lst = [signal.channel for signal in signals]
        n_chan = len(np.unique(np.array(channel_lst)))

        # Write the cache
        cache = {}
        cache['n_chan'] = n_chan
        cache['signals'] = signals
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'signals': signals,
            'polynomials': p_sigs
        }