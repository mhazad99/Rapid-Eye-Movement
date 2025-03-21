#! /usr/bin/env python3
"""
    InputFilesStep
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView
from RapidEyeMovementTools.RapidEyeMovCorrector.InputFilesStep.Ui_InputFilesStep import Ui_InputFilesStep
from widgets.WarningDialog import WarningDialog

import os
from qtpy import QtWidgets
from qtpy import QtCore
from qtpy.QtWidgets import QMessageBox

class InputFilesStep(BaseStepView, Ui_InputFilesStep, QtWidgets.QWidget):
    """
        InputFilesStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform PSGReader of the files to open and propagate the events included in the files.
    """
    context_files_view = "input_files_settings_view"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._psg_reader_identifier = "dd7e6db1-0ee0-4547-b047-cd8e6d7f5600"
        self._node_id_channel_dict = "9e62885f-5b8c-490c-af53-f6546947f518"

        self._EOG_chan_dict = {}

        # To use the SettingsView of a plugin and interract with its fonctions
        module = self.process_manager.get_node_by_id(self._psg_reader_identifier)
        if module is None:
            print(f'ERROR module_id isn\'t found in the process:{self._psg_reader_identifier}')
        else:
            # To extract the SettingsView and add it to our Layout in the preset
            self.my_PsgReaderSettingsView = module.create_settings_view()
            self.verticalLayout.addWidget(self.my_PsgReaderSettingsView)
            self.my_PsgReaderSettingsView.model_updated_signal.connect(self.on_model_modified)
            # To pass the events information to another step
            self._context_manager[self.context_files_view] = self.my_PsgReaderSettingsView

        self._channel_topic = f'{self._node_id_channel_dict}.dictionary'
        self._pub_sub_manager.subscribe(self, self._channel_topic)   


    # Slot created to receive the signal emitted from PSGReaderSettingsView when the files_model is modified
    @QtCore.Slot()
    def on_model_modified(self):
        # Look the extension of the files opened, only edf is supported
        file_list = self.my_PsgReaderSettingsView.get_files_list(self.my_PsgReaderSettingsView.files_model)
        # Look for any extension different than .edf
        files_path = [file for file in file_list if os.path.splitext(file)[1].lower() !='.edf']
        if len(files_path):
            error_message = "Remove any PSG file that are not .edf, only edf file can be corrected"
            for file in files_path:
                error_message = error_message + f'\n\n{file}'
            WarningDialog(error_message)
        # To pass the events information to another step each time the model changes 
        self._context_manager[self.context_files_view] = self.my_PsgReaderSettingsView     


    def load_settings(self):
        #self.my_PsgReaderSettingsView.load_settings()
        self._pub_sub_manager.publish(self, self._channel_topic, 'ping')


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.

        alias = self.my_PsgReaderSettingsView.get_alias()
        for key, val in alias.items():
            if val==['']:
                WarningDialog(f"The alias {key} from the Input File Step is empty. You need to define the {key} channels.")
                return False
                
        # If none of the EEG channels is selected for a subject
        eeg_chan_alias = alias['EEG']
        channels_info_df = self.my_PsgReaderSettingsView.channels_table_model.get_data()
        # For each subject
        file_list = channels_info_df['Filename'].unique()
        for file in file_list:
            chans_used = channels_info_df[(channels_info_df['Filename']==file) & (channels_info_df['Use']==True) & channels_info_df['Channel'].isin(eeg_chan_alias)]
            if len(chans_used)==0:
                WarningDialog(f"At least one recording has no EEG channel (defined in EEG Alias) selected, start looking at {file} in step '1 - Input Files'.")
                return False  

        # If none of the EOG channels is selected for a subject
        eog_chan_alias = alias['EOG']
        for file in file_list:
            chans_used = channels_info_df[(channels_info_df['Filename']==file) & (channels_info_df['Use']==True) & channels_info_df['Channel'].isin(eog_chan_alias)]
            if len(chans_used)==0:
                WarningDialog(f"At least one recording has no EOG channel (defined in EOG Alias) selected, start looking at {file} in step '1 - Input Files'.")
                return False  
            else:
                self._EOG_chan_dict[file] = chans_used['Channel'].values[0]

        # # Fill the EOG channel dictionary to add the REMs_corrected events on the first EOG channel
        # file_list = self.my_PsgReaderSettingsView.get_files_list(self.my_PsgReaderSettingsView.files_model)
        # current_aliases = self.my_PsgReaderSettingsView._alias_line_edit['EOG'].text()

        # self._EOG_chan_dict = {}
        # for file in file_list:
        #     self.my_PsgReaderSettingsView._psg_reader_manager.open_file(file)
        #     # Only edf are available
        #     channels = self.my_PsgReaderSettingsView._psg_reader_manager.get_channels(0)
        #     self.my_PsgReaderSettingsView._psg_reader_manager.close_file()
        #     channel = [chan.name for chan in channels if chan.name in current_aliases] 
        #     if len(channel)>0:
        #         self._EOG_chan_dict[file] = channel[0]

        # Return False if any of the recordings has no valid sleep staging
        for file in file_list:
            if not self.my_PsgReaderSettingsView.is_stages_scored(file, self.my_PsgReaderSettingsView.files_model):
                WarningDialog(f"At least one recording has no valid sleep stage, start looking at {file}.")
                return False
        return True    


    def on_apply_settings(self):
        # Send the dictionnary of EOG channels
        channels_info_df = self.my_PsgReaderSettingsView.channels_table_model.get_data()
        file_list = channels_info_df['Filename'].unique()
        alias = self.my_PsgReaderSettingsView.get_alias()
        eog_chan_alias = alias['EOG']
        for file in file_list:
            chans_used = channels_info_df[(channels_info_df['Filename']==file) & (channels_info_df['Use']==True) & channels_info_df['Channel'].isin(eog_chan_alias)]
            if len(chans_used)>0:
                self._EOG_chan_dict[file] = chans_used['Channel'].values[0]           
        self._pub_sub_manager.publish(self, self._channel_topic, self._EOG_chan_dict)


    def on_topic_response(self, topic, message, sender):
        #self.my_PsgReaderSettingsView.on_topic_response(topic, message, sender)
        if topic == self._channel_topic:
            self._EOG_chan_dict = message


    # Called when the user delete an instance of the plugin
    def __del__(self):
        #self.my_PsgReaderSettingsView.__del__()
        self._pub_sub_manager.unsubscribe(self, self._EOG_chan_dict)