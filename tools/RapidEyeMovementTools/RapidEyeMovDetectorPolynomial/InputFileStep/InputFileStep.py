#! /usr/bin/env python3
"""
    InputFileStep
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView
from RapidEyeMovementTools.RapidEyeMovDetectorPolynomial.InputFileStep.Ui_InputFileStep import Ui_InputFileStep

from qtpy.QtWidgets import QMessageBox
from qtpy import QtWidgets
from qtpy import QtCore

class InputFileStep(BaseStepView, Ui_InputFileStep, QtWidgets.QWidget):
    """
        InputFileStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform PSGReader of the files to open and propagate the events included in the files.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._psg_reader_identifier = "2f6c7a19-5f99-4665-bc8a-6a8638d3420c"
        self._node_id_channel_dict = "a0cddde6-501c-4e77-982d-0c6123f5a567"

        self._EOG_chan_dict = {}

        # To use the SettingsView of a plugin and interract with its fonctions
        module = self.process_manager.get_node_by_id(self._psg_reader_identifier)
        if module is None:
            print(f'ERROR module_id isn\'t found in the process:{self._psg_reader_identifier}')
        else:
            # To extract the SettingsView and add it to our Layout in the preset
            self.my_PsgReaderSettingsView = module.create_settings_view()
            self.verticalLayout.addWidget(self.my_PsgReaderSettingsView)

        self._channel_topic = f'{self._node_id_channel_dict}.dictionary'
        self._pub_sub_manager.subscribe(self, self._channel_topic)  


    def load_settings(self):
        self.my_PsgReaderSettingsView.load_settings()


    def on_apply_settings(self):
        self.my_PsgReaderSettingsView.on_apply_settings()
        # Fill the EOG channel dictionary to add the REMs_corrected events on the first EOG channel
        file_list = self.my_PsgReaderSettingsView.get_files_list(self.my_PsgReaderSettingsView.files_model)
        for file in file_list:
            channels_info_df = self.my_PsgReaderSettingsView.channels_table_model.get_data()
            chan_file = channels_info_df[channels_info_df['Filename']==file]
            chan_sel = chan_file[chan_file['Use']==True]
            self._EOG_chan_dict[file] = chan_sel['Channel'].values[0]            
        self._pub_sub_manager.publish(self, self._channel_topic, self._EOG_chan_dict)


    def on_response(self, topic, message, sender):
        self.my_PsgReaderSettingsView.on_response(topic, message, sender)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        self.my_PsgReaderSettingsView.__del__()
