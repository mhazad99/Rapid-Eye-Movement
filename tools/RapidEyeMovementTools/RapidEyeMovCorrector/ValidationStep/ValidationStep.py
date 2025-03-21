#! /usr/bin/env python3
"""
    ValidationStep
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState


from qtpy import QtWidgets

from RapidEyeMovementTools.RapidEyeMovCorrector.ValidationStep.Ui_ValidationStep import Ui_ValidationStep

class ValidationStep(BaseStepView, Ui_ValidationStep, QtWidgets.QWidget):
    """
        ValidationStep
        TODO CLASS DESCRIPTION
    """
    # Key for the context shared with other step of the preset
    context_files_model = "input_files_model"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._spectral_power_identifier = "80e510c7-4058-4f1f-9bf1-81e1c7869e6e"

        # To use the SettingsView of a plugin and interract with its fonctions
        module = self.process_manager.get_node_by_id(self._spectral_power_identifier)
        if module is None:
            print(f'ERROR module_id isn\'t found in the process:{self._spectral_power_identifier}')
        else:
            # To extract the SettingsView and add it to our Layout in the preset
            self.my_SpectralPowerSettingsView = module.create_settings_view()
            self.verticalLayout.addWidget(self.my_SpectralPowerSettingsView)


    def load_settings(self):
        self.my_SpectralPowerSettingsView.load_settings()
        self.my_SpectralPowerSettingsView.label.setVisible(False)
        self.my_SpectralPowerSettingsView.filename_lineEdit.setVisible(False)
        self.my_SpectralPowerSettingsView.choose_pushButton.setVisible(False)
        self._pub_sub_manager.publish(self, self._spectral_power_identifier+".get_activation_state", None)


    def on_apply_settings(self):
        self.my_SpectralPowerSettingsView.on_apply_settings()

        if self.validation_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._spectral_power_identifier+".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._spectral_power_identifier+".activation_state_change", ActivationState.DEACTIVATED)


    def on_topic_response(self, topic, message, sender):
        if topic == self._spectral_power_identifier+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.validation_checkBox.setChecked(True)
                self.on_active_validation()
            elif message == ActivationState.DEACTIVATED:
                self.validation_checkBox.setChecked(False)
                self.on_active_validation()


    def on_response(self, topic, message, sender):
        self.my_SpectralPowerSettingsView.on_response(topic, message, sender)


    def on_active_validation(self):
        if self.validation_checkBox.isChecked():
            self.my_SpectralPowerSettingsView.setEnabled(True)           
        else:
            self.my_SpectralPowerSettingsView.setEnabled(False)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        self.my_SpectralPowerSettingsView.__del__()
