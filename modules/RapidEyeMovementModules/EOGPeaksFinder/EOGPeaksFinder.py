"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    EOGPeaksFinder
    Detect peacks of EOG signals (LOC and ROC), sEOG (LOC+ROC) and dEOG (LOC-ROC).
    Peaks are saved in a pandas dataframe.
"""
import pandas as pd
import scipy.signal as spsignal

import config
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import SciNode, InputPlug, OutputPlug

DEBUG = False

class EOGPeaksFinder(SciNode):
    """
    Detect peacks of EOG signals (LOC and ROC), sEOG (LOC+ROC) and dEOG (LOC-ROC).
    Peaks are saved in a pandas dataframe.

    Parameters
    ----------
        "EOG_signals": List of SignalModel
            EOG ROC and LOC signals. 
            Each item of the list is a signal object of an epoch from a specific channel.
            Properties:
                samples:np.array
                    List of samples
                start_time:float 
                    Start time in seconds of the signal in relation to the beginning 
                    of the recording.
                end_time:float
                    End time in seconds of the signal in relation to the beginning 
                    of the recording.
                duration:float
                    Duration in seconds of the signal.
                sample_rate:float
                    Sampling rate of the signal
                channel:str
                    Name of the channel
        "sEOG_signals": List of SignalModel
            LOC+ROC signals. 
        "dEOG_signals": List of SignalModel
            LOC-ROC signals. 
        "parameters": dict
            The parameters to detect peaks.
            "min_height_z": 1.5,
            "min_interval_s": 0.5,
    
    Returns
    -------
        "peaks_df": pandas data frame
            The list of peaks.
            Columns : 
                group : Group of events this event is part of (String)
                name : Name of the event (String)
                start_sec : Starting time of the event in sec (Float)
                duration_sec : Duration of the event in sec (Float)
                amplitude : Amplitude of the event (Float)
                channels : Channel where the event occures (String)
        "peaks_parameters" : dict
            The parameters used to detect peaks
                "min_height_z": 1.5,
                "min_interval_s": 0.5

        
    """
    def __init__(self, **kwargs):
        """ Initialize module EOGPeaksFinder """
        super().__init__(**kwargs)
        if DEBUG: print('EOGPeaksFinder.__init__')

        # Input plugs
        InputPlug('EOG_signals',self)
        InputPlug('sEOG_signals',self)
        InputPlug('dEOG_signals',self)
        InputPlug('parameters',self)  
        # Output plugs
        OutputPlug('peaks_df',self)
        OutputPlug('peaks_parameters',self)
        
        self._is_master = False 
    

    def compute(self, EOG_signals,sEOG_signals,dEOG_signals,parameters):
        """
        Parameters
        ----------
            "EOG_signals": List of SignalModel
                EOG ROC and LOC signals. 
                Each item of the list is a signal object of an epoch from a specific channel.
                Properties:
                    samples:np.array
                        List of samples
                    start_time:float 
                        Start time in seconds of the signal in relation to the beginning 
                        of the recording.
                    end_time:float
                        End time in seconds of the signal in relation to the beginning 
                        of the recording.
                    duration:float
                        Duration in seconds of the signal.
                    sample_rate:float
                        Sampling rate of the signal
                    channel:str
                        Name of the channel
            "sEOG_signals": List of SignalModel
                LOC+ROC signals. 
            "dEOG_signals": List of SignalModel
                LOC-ROC signals. 
            "parameters": dict
                The parameters to detect peaks.
                "min_height_z": 1.5,
                "min_interval_s": 0.5,
        
        Returns
        -------
            "peaks_df": pandas data frame
                The list of peaks.
                Columns : 
                    group : Group of events this event is part of (String)
                    start_sec : Starting time of the event in sec (Float)
                    amplitude : Amplitude of the event (Float)
                    channels : Channel where the event occures (String)

            "peaks_parameters" : dict
                The parameters used to detect peaks
                    "min_height_z": 1.5,
                    "min_interval_s": 0.5

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        if DEBUG: print('EOGPeaksFinder.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(EOG_signals,str) and EOG_signals=='':
            raise NodeInputException(self.identifier, "EOG_signals", f"EOGPeaksFinder this input is not connected.")
        elif not isinstance(EOG_signals,list):
            raise NodeInputException(self.identifier, "EOG_signals", \
                f"EOGPeaksFinder input of wrong type. Expected: <class 'list'> received: {type(EOG_signals)}")     
        elif len(EOG_signals)< 2:
            raise NodeInputException(self.identifier, "EOG_signals", \
                f"EOGPeaksFinder at least 2 signals is expected for the operation")      

        if isinstance(sEOG_signals,str) and sEOG_signals=='':
            raise NodeInputException(self.identifier, "sEOG_signals", f"EOGPeaksFinder this input is not connected.")
        elif not isinstance(sEOG_signals,list):
            raise NodeInputException(self.identifier, "sEOG_signals", \
                f"EOGPeaksFinder input of wrong type. Expected: <class 'list'> received: {type(sEOG_signals)}")  

        if isinstance(dEOG_signals,str) and dEOG_signals=='':
            raise NodeInputException(self.identifier, "dEOG_signals", f"EOGPeaksFinder this input is not connected.")
        elif not isinstance(dEOG_signals,list):
            raise NodeInputException(self.identifier, "dEOG_signals", \
                f"EOGPeaksFinder input of wrong type. Expected: <class 'list'> received: {type(dEOG_signals)}")  

        if isinstance(parameters,str) and not parameters=='':
            parameters = eval(parameters)
        if not isinstance(parameters,dict):
            raise NodeInputException(self.identifier, "parameters", \
                f"EOGPeaksFinder input of wrong type. Expected: <class 'dict'> received: {type(parameters)}")

        # Raise NodeRuntimeException if there is a critical error during runtime. 
        # This will usually be a user error, a file that can't be read due to security reason,
        # a parameter that is out of bound, etc. This exception will stop and skip the current
        # process but will not stop the followin iterations if a master node is not done.
        # Once the master node is completed, a dialog will appear to show all NodeRuntimeException
        # to the user.
        # Raise the runtime exception
        # raise NodeRuntimeException(self.identifier, "files", \
        #        f"Some file could not be open.")

        self.EOG_peaks_info = []
        # Detect peaks on EOG signals
            # self.EOG_peaks_info is updated with the information of the peaks
        self._detect_peaks(EOG_signals, parameters["min_height_z"], parameters["min_interval_s"], "EOG_peaks")
        # Detect peaks on sEOG signals
        self._detect_peaks(sEOG_signals, parameters["min_height_z"], parameters["min_interval_s"], "sEOG_peaks")
        # Detect peaks on dEOG signals
        self._detect_peaks(dEOG_signals, parameters["min_height_z"], parameters["min_interval_s"], "dEOG_peaks")

        # Convert the list of peaks into a pandas data frame
        peaks_df = pd.DataFrame(self.EOG_peaks_info, columns=["group", "start_sec", "amplitude", "channels"])

        # Write to the cache to use the data in the resultTab

        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            signals = []
            signals.extend(EOG_signals)
            signals.extend(sEOG_signals)
            signals.extend(dEOG_signals)
            cache['signals'] = signals
            cache['peaks_df'] = peaks_df
            cache['min_height_z'] = parameters["min_height_z"]
            self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module does nothing.")

        return {
            'peaks_df': peaks_df,
            'peaks_parameters': parameters
        }


    def _detect_peaks(self, signals, min_height_z, min_interval_s, signal_label):
        for signal in signals:
            x = signal.samples
            height = min_height_z
            distance = min_interval_s*signal.sample_rate
            # Positive peaks
            peaks, properties = spsignal.find_peaks(x, height=height, distance=distance)
            amplitudes = properties['peak_heights']
            for peak_smp, amplitude in (zip(peaks, amplitudes)):
                # start_time
                start_time_sec = peak_smp/signal.sample_rate+signal.start_time
                self.EOG_peaks_info.append([signal_label, start_time_sec, amplitude, signal.channel])
            # Negative peaks
            x = -x
            peaks, properties = spsignal.find_peaks(x, height=height, distance=distance)
            amplitudes = properties['peak_heights']
            for peak_smp, amplitude in (zip(peaks, amplitudes)):
                # start_time
                start_time_sec = peak_smp/signal.sample_rate+signal.start_time
                self.EOG_peaks_info.append([signal_label, start_time_sec, -amplitude, signal.channel])