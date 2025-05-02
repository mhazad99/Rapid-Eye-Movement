"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    Combine two dictionnary of signals.

    Parameters
    -----------     
        signals1 : Dict
            Dictionary of channels. These channels are SignalModel with properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original

        signals2 : Dict
            Dictionary of channels. These channels are SignalModel with properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
 
    Returns
    ----------- 
        signals: Dict
            Dictionary of channels. These channels are SignalModel with properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original


"""

from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.PSGReader.SignalModel import SignalModel

from math import *

DEBUG = False

class SignalsCombine(SciNode):
    """
        Combine two dictionnary of signals.

        Parameters
        -----------     
            signals1 : Dict
                Dictionary of channels. These channels are SignalModel with properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original

            signals2 : Dict
                Dictionary of channels. These channels are SignalModel with properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
    
        Returns
        ----------- 
            signals: Dict
                Dictionary of channels. These channels are SignalModel with properties :
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
        super().__init__(**kwargs)
        if DEBUG: print('SignalsCombine.__init__')
        self._filename = None
        InputPlug('signals1', self)
        InputPlug('signals2', self)
        OutputPlug('signals', self)

    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass

    def compute(self, signals1, signals2):
        """
            Combine two dictionnary of signals.

            Parameters
            -----------     
                signals1 : Dict
                    Dictionary of channels. These channels are SignalModel with properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original

                signals2 : Dict
                    Dictionary of channels. These channels are SignalModel with properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original
        
            Returns
            ----------- 
                signals: Dict
                    Dictionary of channels. These channels are SignalModel with properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original


        """

        if DEBUG: print('SignalsCombine.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None  

        # Verify inputs
        if isinstance(signals1, str) and signals1 == '':
            err_message = "ERROR: signals1 not connected"
            self._log_manager.log(self.identifier, err_message)
            print('SignalsCombine' + err_message)      
            return {'signals': ''}

        if isinstance(signals2, str) and signals2 == '':
            err_message = "ERROR: signals2 not connected"
            self._log_manager.log(self.identifier, err_message)
            print('SignalsCombine' + err_message)      
            return {'signals': ''}

        try :
            signals = {}
            for channel in signals1:
                signals[channel] = signals1[channel].clone(clone_samples=True)
            for channel in signals2:
                signals[channel] = signals2[channel].clone(clone_samples=True)
            
            # Write the cache
            cache = {}
            self._cache_manager.write_mem_cache(self.identifier, cache)

            return {'signals': signals}

        except Exception as e:
                err_message = "ERROR: {}".format(e)
                self._log_manager.log(self.identifier, err_message)
                print('SignalsCombine' + err_message)
                return {'signals': ''}