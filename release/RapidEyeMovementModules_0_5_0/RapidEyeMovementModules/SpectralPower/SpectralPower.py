"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    Find the SpectralPower for a list of signals.
    Parameters
    -----------
        signals : List
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
        signals2 : List
            Second list of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        mode: String
            Absolute or relative.
        freq_band: Dict
            Dictionnary of the used frequency band.
        filename: String
            Name of the file to output.

"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
import numpy as np
import pandas as pd
from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class SpectralPower(SciNode):
    """
        Find the SpectralPower for a list of signals.
        Parameters
        -----------
            signals : List
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
            signals2 : List
                Second list of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
            mode: String
                Absolute or relative.
            freq_band: Dict
                Dictionnary of the used frequency band.
            filename: String
                Name of the file to output.

    """
    def __init__(self, **kwargs):
        """ Initialize module SpectralPower """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('signals2',self)
        InputPlug('mode',self)
        InputPlug('freq_band',self)
        InputPlug('filename',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, signals,signals2,mode,freq_band,filename):
        """
            Find the SpectralPower for a list of signals.
            Parameters
            -----------
                signals : List
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
                signals2 : List
                    Second list of signal with dictionary of channels with SignalModel with 
                    properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original
                mode: String
                    Absolute or relative.
                freq_band: Dict
                    Dictionnary of the used frequency band.
                filename: String
                    Name of the file to output.

        """

        if DEBUG: print('SpectralPower.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Verify inputs
        if isinstance(signals, str) and signals == '':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            print('SpectralPower' + err_message)

        if SignalModel.is_vectorizable(signals, False):
            L = len(signals[0].samples)              # signal length
            fs = signals[0].sample_rate              # sampling rate
            T = 1/fs                                 # Period
            t = np.linspace(1,L,L)*T                 # time vector

            freq = np.fft.rfftfreq(t.shape[-1], T)   #frequency vector, real frequency up to fs/2
            
            # Get samples
            samples = SignalModel.get_attribute(signals, 'samples', None)

            # Extract fft
            spectral_power = np.abs(np.fft.rfft(samples))**2

            # Extract useful frequency
            f0 = freq[1] - freq[0]

            if 'total' in freq_band:
                freq_tot = np.where((freq >= freq_band['total'][0]) & 
                                    (freq <= freq_band['total'][1]))[0]
            else:
                freq_tot = np.arange(len(freq))

            band_fft = dict()
            band_key = []
            # For each frequency band
            for band in freq_band:  
                if not band == 'total':
                    band_key.append(band)
                    freq_ix = np.where((freq >= freq_band[band][0]) & 
                                    (freq <= freq_band[band][1]))[0]
                    if mode == 'relative':
                        band_fft[band] = np.sum(spectral_power[:,freq_ix],1)/np.sum(spectral_power[:,freq_tot],1)
                    else:
                        band_fft[band] = np.sum(spectral_power[:,freq_ix],1) * f0

            channels = SignalModel.get_attribute(signals, 'channel', None)
            unq_chan = np.unique(channels)

            for i, signal in enumerate(signals):
                signal.meta['spectral_power'] = dict()
                for k, v in band_fft.items():
                    signal.meta['spectral_power'][k] = v[i]

            chan_spec1 = dict()
            for unq in unq_chan:
                idx = np.where(channels == unq)[0]
                chan_spec1[unq] = dict()
                for k, v in band_fft.items(): 
                    chan_spec1[unq][k] = np.mean(v[idx])

            # Check if there is second signal to compare
            if not(isinstance(signals2, str) and signals2 == ''):
                if SignalModel.is_vectorizable(signals2, False):
                    L = len(signals2[0].samples)              # signal length
                    fs = signals2[0].sample_rate              # sampling rate
                    T = 1/fs                                 # Period
                    t = np.linspace(1,L,L)*T                 # time vector

                    freq = np.fft.rfftfreq(t.shape[-1], T)   #frequency vector, real frequency up to fs/2
                    
                    # Get samples
                    samples = SignalModel.get_attribute(signals2, 'samples', None)

                    # Extract fft
                    spectral_power = np.abs(np.fft.rfft(samples))**2

                    # Extract useful frequency
                    f0 = freq[1] - freq[0]

                    if 'total' in freq_band:
                        freq_tot = np.where((freq >= freq_band['total'][0]) & 
                                            (freq <= freq_band['total'][1]))[0]
                    else:
                        freq_tot = np.arange(len(freq))

                    band_fft = dict()
                    # For each frequency band
                    for band in freq_band:  
                        if not band == 'total':
                            band_key.append(band + '2')
                            freq_ix = np.where((freq >= freq_band[band][0]) & 
                                            (freq <= freq_band[band][1]))[0]
                            if mode == 'relative':
                                band_fft[band] = np.sum(spectral_power[:,freq_ix],1)/np.sum(spectral_power[:,freq_tot],1)
                            else:
                                band_fft[band] = np.sum(spectral_power[:,freq_ix],1) * f0

                    channels = SignalModel.get_attribute(signals2, 'channel', None)
                    unq_chan = np.unique(channels)

                    for i, signal in enumerate(signals2):
                        signal.meta['spectral_power'] = dict()
                        for k, v in band_fft.items():
                            signal.meta['spectral_power'][k] = v[i]

                    chan_spec2 = dict()
                    for unq in unq_chan:
                        idx = np.where(channels == unq)[0]
                        chan_spec2[unq] = dict()
                        for k, v in band_fft.items(): 
                            chan_spec2[unq][k + '2'] = np.mean(v[idx])

                    chan_spec = {**chan_spec1, **chan_spec2}
                    for key, value in chan_spec.items():
                        if key in chan_spec1 and key in chan_spec2:
                            chan_spec[key].update(chan_spec1[key])
                else:
                    pass
                    #TODO
            else:
                chan_spec = chan_spec1
            ord_dict = pd.DataFrame.from_dict(chan_spec, columns=band_key , orient='index')

            if not (filename == ''):
                ord_dict.to_csv(filename)

        else:
            for signal in signals:
                L = len(signal.samples) # signal length
                n = len(signal)         # number of channel
                fs = signal.sample_rate # sampling rate
                T = 1/fs                        # sample time
                t = np.linspace(1,L,L)*T        # time vector

                freq = np.fft.rfftfreq(t.shape[-1], T)      #frequency vector, real frequency up to fs/2

                #TODO

        # Write the cache
        cache = {}
        cache['chan_spec'] = ord_dict
        cache['band_key'] = band_key

        self._cache_manager.write_mem_cache(self.identifier, cache)