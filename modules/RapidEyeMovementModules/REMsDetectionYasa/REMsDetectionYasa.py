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
        InputPlug('thresholds',self)
        InputPlug('filename', self)
        

        # Output plugs
        OutputPlug('detectiondataframe',self)


        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, filename,signals,events,sleepstages,thresholds):
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
        # Load data
        #data_path = "D:/CEAMS/snooz_workspace/REM Detector/RBD_Project/"
        LOC_label = 'LOC'
        ROC_label = 'ROC'
        channel_2_rem = ['ECG DII', 'ECG D1']

        REM_amplitude_det = 50

        # Extract subject label from a list of .edf file
        # List files with the .edf extension
        #edf_files = [file for file in os.listdir(data_path) if file.endswith('.edf')]
        # Create a list of subject labels without the .edf extension
        #subject_label = [file[:-4] for file in edf_files]  # Removes the last 4 characters (.edf)
        filename = filename[:-4]
        error_flag = False
        #for i_subject in subject_label:
        hypno = sleepstages # Modified this line: removed _hypno
        raw = self.prepare_raw_data(signals)

        # Select a subset of EEG channels
        # Look for the occurrence of LOC in the channels list "raw.ch_names" and pick only those
        '''LOC_chan = [load_chan for load_chan in raw.ch_names if LOC_label in load_chan]
        if not len(LOC_chan)==1:
            error_flag = True
            print('Error : LOC channel not found or found twice')
            if len(LOC_chan)>1:
                LOC_chan = [LOC_chan[0]]
                print(f'LOC channel is forced to {LOC_chan}') 
            #raise ValueError('LOC channel not found or found twice')
        ROC_chan = [load_chan for load_chan in raw.ch_names if ROC_label in load_chan]
        if not len(ROC_chan)==1:
            error_flag = True
            if len(ROC_chan)>1:
                ROC_chan = [ROC_chan[0]]
                print(f'ROC channel is forced to {ROC_chan}') 
            #raise ValueError('ROC channel not found or found twice')
        channels_label = LOC_chan+ROC_chan
        raw.pick(channels_label)
        hypno = np.squeeze(hypno["name"].values)
        hypno = [int(x) for x in hypno if x.isdigit()]''' # remove the non-numeric values'''
        hypno = np.squeeze(hypno["name"].values)
        hypno_up = yasa.hypno_upsample_to_data(hypno, sf_hypno=1/30, data=raw._data[0,:], sf_data=raw.info['sfreq'])

        loc = raw._data[0,:] * 1e6
        roc = raw._data[1,:] * 1e6
        rem = yasa.rem_detect(loc, roc, raw.info['sfreq'], 
                                hypno=hypno_up, include=5, amplitude=(REM_amplitude_det, 325), 
                                duration=(0.3, 1.5), freq_rem=(0.5, 5), 
                                relative_prominence=0.8, remove_outliers=True, verbose='info')
        # rem = yasa.rem_detect(loc, roc, raw.info['sfreq'], hypno=hypno_up, include=5, amplitude=(REM_amplitude_det, 325), duration=(0.3, 1.5), \
        #     freq_rem=(0.5, 5), relative_prominence=0.8, remove_outliers=False, verbose='info')

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
            'group': 'YASA',
            'name': 'YASA_REM',
            'start_sec': rems_detection_df['Start'],
            'duration_sec': rems_detection_df['Duration'],
            'channels': [raw[0].channel, raw[1].channel] * len(rems_detection_df)
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
            'detectiondataframe': None
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
        data = np.array([r.samples*10e-6 for r in raw]) #Recheck the uv to v conversion
        
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)
        return mne.io.RawArray(data, info)