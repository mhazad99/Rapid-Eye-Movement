#! /usr/bin/env python3
"""
    CorrectorStep
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState


from RapidEyeMovementTools.REMsEOGArtifactCorrector.CorrectorStep.Ui_CorrectorStep import Ui_CorrectorStep

import numpy as np
from qtpy import QtWidgets

class CorrectorStep(BaseStepView, Ui_CorrectorStep, QtWidgets.QWidget):
    """
        CorrectorStep
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init UI
        self.setupUi(self)

        self._node_id_SVDFilter = "726508cf-b7c5-4e6e-9a94-67b032cb3c24"  # provide the SVD filter parameters
        self._SVDConfig_topic = f'{self._node_id_SVDFilter}.configuration'
        self._pub_sub_manager.subscribe(self, self._SVDConfig_topic)

        self._SVDConfig = {
            'number_of_components': 1,
            'tukey_alpha': 0.5
        }

    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._SVDConfig_topic, 'ping')

    def on_apply_settings(self):
        # Send the settings to the publisher
        self._SVDConfig['number_of_components'] = self.Number_of_Components_spinBox.value()
        self._SVDConfig['tukey_alpha'] = self.Sharpness_doubleSpinBox.value()
        self._pub_sub_manager.publish(self, self._SVDConfig_topic, self._SVDConfig)

    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._SVDConfig_topic:
            if isinstance(message, str) and not message == '':  
                message = eval(message)
            elif isinstance(message, dict):
                self.Number_of_Components_spinBox.setValue(message.get("number_of_components"))
                self.Sharpness_doubleSpinBox.setValue(message.get("tukey_alpha"))

    def on_topic_update(self, topic, message, sender):
        pass
                
    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._SVDConfig_topic)

    
