#! /usr/bin/env python3
"""
    ExportResults
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState


from qtpy import QtWidgets

from RapidEyeMovementTools.REMsEOGArtifactCorrector.ExportResults.Ui_ExportResults import Ui_ExportResults

class ExportResults(BaseStepView, Ui_ExportResults, QtWidgets.QWidget):
    """
        ExportResults
        TODO CLASS DESCRIPTION
    """
    # Key for the context shared with other step of the preset
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        self._node_id_StringManip = "c747c3fc-19d4-4e59-af67-618f7a887f1a"
        self._StringManip_topic = f'{self._node_id_StringManip}.suffix'
        self._pub_sub_manager.subscribe(self, self._StringManip_topic)

    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._StringManip_topic, 'ping')

    def on_apply_settings(self):
        # Send the settings to the publisher
        self._pub_sub_manager.publish(self, self._StringManip_topic, self.Suffix_lineEdit.text())

    def on_topic_response(self, topic, message, sender):   
        # This will be called as a response to ping request.
        if topic == self._StringManip_topic:
            self.Suffix_lineEdit.setText(message)

    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._StringManip_topic)