"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    REMsDetectionYasa
    TODO CLASS DESCRIPTION 
"""
import matplotlib.pyplot as plt
import mne
import numpy as np
import os
import pandas as pd
import yasa


from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class REMsDetectionYasa(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        signal: TODO TYPE
            TODO DESCRIPTION
        events: TODO TYPE
            TODO DESCRIPTION
        sleepstages: TODO TYPE
            TODO DESCRIPTION
        thresholds: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        detectiondataframe: TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module REMsDetectionYasa """
        super().__init__(**kwargs)
        if DEBUG: print('REMsDetectionYasa.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('events',self)
        InputPlug('sleepstages',self)
        InputPlug('filename', self)
        InputPlug('amplitude',self)
        InputPlug('duration',self)
        InputPlug('freq_rem',self)
        InputPlug('relative_prominence',self)
        InputPlug('remove_outliers',self)
        InputPlug('rems_event_name', self)
        InputPlug('rems_event_group', self)
        InputPlug('include', self)
        

        # Output plugs
        OutputPlug('detectiondataframe',self)


        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, filename,signals,events,sleepstages,amplitude, duration, freq_rem, relative_prominence, remove_outliers, rems_event_name, rems_event_group, include):     
        """
        TODO DESCRIPTION

        Parameters
        ----------
            signal: TODO TYPE
                TODO DESCRIPTION
            events: TODO TYPE
                TODO DESCRIPTION
            sleepstages: TODO TYPE
                TODO DESCRIPTION
            thresholds: TODO TYPE
                TODO DESCRIPTION
            

        Returns
        -------
            detectiondataframe: TODO TYPE
                TODO DESCRIPTION
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        # Extract subject label from a list of .edf file
        filename = filename[:-4]
        error_flag = False
        #for i_subject in subject_label:
        hypno = sleepstages # Modified this line: removed _hypno
        raw = self.prepare_raw_data(signals)
        hypno = np.squeeze(hypno["name"].values)
        hypno = list(hypno)
        hypno_up = yasa.hypno_upsample_to_data(hypno, sf_hypno=1/30, data=raw._data[0,:], sf_data=raw.info['sfreq'])

        loc = raw._data[0,:] * 1e6
        roc = raw._data[1,:] * 1e6
        # check the include input
        Include_list = self.extract_ints(include)
        if len(Include_list) == 1:
            include = Include_list[0]
        else:
            include = Include_list

        rem = yasa.rem_detect(loc, roc, raw.info['sfreq'], 
                                hypno=hypno_up, include=include, amplitude=amplitude, 
                                duration=duration, freq_rem=freq_rem, 
                                relative_prominence=relative_prominence, remove_outliers=remove_outliers, verbose='info')

        # Save the REMs dataFrame in a tsv file
        rems_detection_df = rem.summary().round(3)
        rems_detection_df.to_csv(f"{filename}_YASA_REMs_summary.tsv", sep='\t')
        # Modify the DataFrame to be compatible with Snooz
        #   Snooz dataframe : [group, name, start_sec, duration_sec, channels]
        #   Define 
        #       group as "YASA",
        #       name as "YASA_REM", 
        #       start_time as rems_detection_df['start'],
        #       duration as rems_detection_df['duration'],
        #       channel as channels_label
        snooz_rem = pd.DataFrame({
            'group': rems_event_group,
            'name': rems_event_name,
            'start_sec': rems_detection_df['Start'],
            'duration_sec': rems_detection_df['Duration'],
            'channels': [f"{raw.ch_names[0]}, {raw.ch_names[1]}" for _ in range(len(rems_detection_df))]
        })
        # Save the REMs dataFrame in a tsv file
        snooz_rem.to_csv(f"{filename}_YASA_REMs_snooz.tsv", sep='\t', index=False)

        if error_flag:
            raise ValueError

        # Write to the cache to use the data in the resultTab
        # cache = {}
        # cache['this_is_a_key'] = 42
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module detects Rapid Eye movements.")

        return {
            'detectiondataframe': snooz_rem
        }
    
    def prepare_raw_data(self, raw):
        """
        Prepare raw data for sleep staging.

        Parameters
        ----------
        raw: list
            List of raw signal objects.

        Returns
        -------
        RawArray
            Prepared raw data.
        """
        # Check the number of channels as input
        ch_names = [raw[0].channel, raw[1].channel]
        ch_type = ['eog', 'eog']
        # Create MNE RawArray object
        sfreq = raw[0].sample_rate
        data = np.array([r.samples*1e-6 for r in raw]) #Recheck the uv to v conversion
        
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)
        return mne.io.RawArray(data, info)
    
    def extract_ints(self, s):
        nums = []
        for word in s.replace(' ', '').split(','):
            if word.lstrip('-').isdigit():
                nums.append(int(word))
        return nums