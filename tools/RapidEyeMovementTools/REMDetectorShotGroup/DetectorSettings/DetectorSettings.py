#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite 2024
See the file LICENCE for full license details.

    DetectorSettings
    Class to manage the settings of the EOG preprocessing, normalization and detection.
"""

from qtpy import QtWidgets

from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState

from RapidEyeMovementTools.REMDetectorShotGroup.DetectorSettings.Ui_DetectorSettings import Ui_DetectorSettings

class DetectorSettings(BaseStepView, Ui_DetectorSettings, QtWidgets.QWidget):
    """
        DetectorSettings
        Class to manage the settings of the EOG preprocessing, normalization and detection.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # You need to look into your process.json file to know the ID of the node
        # you are interest in, this is just an example value:
        self._node_id_filter_before = "080165f3-9851-4f90-b764-055513e0657b"
        self._node_id_EOGNormalization = "cfd95a26-7531-47c0-a0fa-a0877e2e9e10"

        # Subscribe to the publisher for each node you want to talk to
        self._parameters_norm_topic = f'{self._node_id_EOGNormalization}.parameters'
        self._pub_sub_manager.subscribe(self, self._parameters_norm_topic)

        # Dict parameters for the EOG normalization plugin
        self.parameters_normalization = {}
        self.parameters_normalization["bsl_normalization"] = False
        self.parameters_normalization["rem_normalization"] = True
        self.parameters_normalization["rem_weight"] = False


    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.

        # Activation state
        self._pub_sub_manager.publish(self, self._node_id_filter_before+".get_activation_state", None)
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._parameters_norm_topic, 'ping')


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        #if topic == self._context_manager.topic:

            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            #if message == "context_some_other_step":
                #updated_value = self._context_manager["context_some_other_step"]
        pass


    def on_topic_response(self, topic, message, sender):
        
        # This will be called as a response to ping request.
        if topic == self._parameters_norm_topic:
            if isinstance(message, str) and not message == "":
                message = eval(message)
            if isinstance(message, dict):
                self.parameters_normalization = message

                # Set the checkbox and radio button depending of the parameters
                if self.parameters_normalization['bsl_normalization'] or self.parameters_normalization['rem_normalization']:
                    self.checkBox_zscore.setChecked(True)
                    #self.radioButton_zn3.setEnabled(True)
                    self.radioButton_zr.setEnabled(True)
                    if self.parameters_normalization['bsl_normalization']:
                        self.radioButton_zn3.setChecked(True)
                    if self.parameters_normalization['rem_normalization']:
                        self.radioButton_zr.setChecked(True)
                else:
                    self.checkBox_zscore.setChecked(False)
                    #self.radioButton_zn3.setEnabled(False)
                    self.radioButton_zr.setEnabled(False)

                if self.parameters_normalization['rem_weight']:
                    self.checkBox_wr.setChecked(True)
                else:
                    self.checkBox_wr.setChecked(False)


    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._parameters_norm_topic, \
            self.parameters_normalization)        


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        return True


    # Called when the user changes the settings
    def update_normalization_slot(self):

        # To activate the selection of the z-score method
        if self.checkBox_zscore.isChecked():
            #self.radioButton_zn3.setEnabled(True)
            self.radioButton_zr.setEnabled(True)
        else:
            #self.radioButton_zn3.setEnabled(False)
            self.radioButton_zr.setEnabled(False)

        # To define the z-score method
        if self.checkBox_zscore.isChecked():
            if self.radioButton_zn3.isChecked():
                self.parameters_normalization['bsl_normalization'] = True
                self.parameters_normalization['rem_normalization'] = False
            if self.radioButton_zr.isChecked():
                self.parameters_normalization['bsl_normalization'] = False
                self.parameters_normalization['rem_normalization'] = True
        else:
            self.parameters_normalization['rem_normalization'] = False
            self.parameters_normalization['bsl_normalization'] = False
        
        # To define the application of the rem weight coefficient
        if self.checkBox_wr.isChecked():
            self.parameters_normalization['rem_weight'] = True
        else:
            self.parameters_normalization['rem_weight'] = False