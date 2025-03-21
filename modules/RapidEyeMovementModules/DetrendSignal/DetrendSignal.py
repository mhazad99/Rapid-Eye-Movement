"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    DetrendSignal
    Detrend a signal
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException

from CEAMSModules.PSGReader.SignalModel import SignalModel
from scipy import signal
import numpy as np

DEBUG = False

class DetrendSignal(SciNode):
    """
    Detrend a signal

    Inputs:
        "signals": List
            Each item of the list is a SignalModel object as described below:
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the sampling rate of the signal
                signal.channel : current channel label
                signal.start_time : The start time of the signal in sec
                signal.end_time : The end time of the signal in sec
                (for more info : look into common/SignalModel)
        "mode": String
            If mode == 'linear' (default), the result of a linear least-squares 
            fit to data is subtracted from data. If mode == 'constant', only the 
            mean of data is subtracted.
        

    Outputs:
        "signals": List
            Each item of the list is a SignalModel object as described below:
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the sampling rate of the signal
                signal.channel : current channel label
                signal.start_time : The start time of the signal in sec
                signal.end_time : The end time of the signal in sec
                (for more info : look into common/SignalModel)
        
    """
    def __init__(self, **kwargs):
        """ Initialize module DetrendSignal """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('mode',self)
        

        # Output plugs
        OutputPlug('signals',self)
        
        self._is_master = False 
    
    def compute(self, signals, mode):
        """
        Detrend a signal

        Inputs:
            "signals": List
                Each item of the list is a SignalModel object as described below:
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the sampling rate of the signal
                    signal.channel : current channel label
                    signal.start_time : The start time of the signal in sec
                    signal.end_time : The end time of the signal in sec
                    (for more info : look into common/SignalModel)
            "mode": String
                If mode == 'linear' (default), the result of a linear least-squares 
                fit to data is subtracted from data. If mode == 'constant', only the 
                mean of data is subtracted.
            

        Outputs:
            "signals": List
                Each item of the list is a SignalModel object as described below:
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the sampling rate of the signal
                    signal.channel : current channel label
                    signal.start_time : The start time of the signal in sec
                    signal.end_time : The end time of the signal in sec
                    (for more info : look into common/SignalModel)
            
        """

        # Verify inputs
        if isinstance(signals,str) and signals=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals", \
                f"SignalsFromEvents this input is not connected.")

        detrend_sig = [sig.clone(clone_samples=True) for sig in signals]

        # Optimized method
        if SignalModel.is_vectorizable(signals, False):
            # Compute as matrix
            samples = np.vstack(SignalModel.get_attribute(signals, 'samples', None))
            if mode == 'p_inv':
                x1 = np.ones([len(signals[0].samples)])
                x2 = np.array(range(len(signals[0].samples)))
                x = np.vstack([x1 , x2])
                p_inv = np.dot(x.T,np.linalg.inv(np.dot(x,x.T)))
                detrend_samples = samples - np.dot(np.dot(samples,p_inv),x)
            else:
                detrend_samples = signal.detrend(samples,axis=-1,type=mode, overwrite_data=True)
            
            # Change samples values
            for i, det_samp in enumerate(detrend_samples):
                detrend_sig[i].samples = det_samp
                detrend_sig[i].is_modified = True
        
        # Slower method
        else:
            # Compute before assigning in loop
            for sig in detrend_sig:
                if mode == 'p_inv':
                    x1 = np.ones([len(sig.samples)])
                    x2 = np.array(range(len(sig.samples)))
                    x = np.vstack([x1 , x2])
                    p_inv = np.dot(x.T,np.linalg.inv(np.dot(x,x.T)))
                    sig.samples = sig.samples - np.dot(np.dot(sig.samples,p_inv),x)
                    sig.is_modified = True
                else:
                    sig.samples = signal.detrend(sig.samples,axis=-1,type=mode,overwrite_data=True)
                    sig.is_modified = True
        
        # Extract the number of channels
        channel_lst = [signal.channel for signal in signals]
        n_chan = len(np.unique(np.array(channel_lst)))

        # Write the cache
        cache = {}
        cache['n_chan'] = n_chan
        cache['signals'] = detrend_sig
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'signals': detrend_sig
        }