#! /usr/bin/env python3
"""
    DetectorStep
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState


from RapidEyeMovementTools.RapidEyeMovDetectorPolynomial.DetectorStep.Ui_DetectorStep import Ui_DetectorStep

from qtpy import QtWidgets

class DetectorStep(BaseStepView, Ui_DetectorStep, QtWidgets.QWidget):
    """
        DetectorStep
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._node_id_EventSubdivision = "d891a937-596e-447d-9e2e-7e472d2c7056"
        self._node_id_DerivativeApprox = "06238342-baf9-4661-b2ab-cd8243141ef9"
        self._node_id_RemDetector = "8682c545-2782-42b8-84e5-cf11a6b049bc" 
        self._node_id_event_name = "28f0cf86-2349-4505-a05e-12cb8fdf4c07"

        # Modules for validation
        self._node_id_EventCompare = "4f53a6ed-b126-4347-9395-3d8b1bd8cb40"
        self._node_id_EventCombine = "dc93a865-b79c-4f3a-ab12-8b05085f57a4"

        # Subscribe to the publisher for each node you want to talk to
        self._window_sec_1_topic = f'{self._node_id_EventSubdivision}.window_sec'
        self._pub_sub_manager.subscribe(self, self._window_sec_1_topic)
        self._order_topic = f'{self._node_id_DerivativeApprox}.order'
        self._pub_sub_manager.subscribe(self, self._order_topic)
        self._border_effect_topic = f'{self._node_id_RemDetector}.border_effect'
        self._pub_sub_manager.subscribe(self, self._border_effect_topic)
        self._percentile_topic = f'{self._node_id_RemDetector}.percentile'
        self._pub_sub_manager.subscribe(self, self._percentile_topic)
        self._REMs_name_topic = f'{self._node_id_event_name}.constant'
        self._pub_sub_manager.subscribe(self, self._REMs_name_topic)

        # The event name to compare with is added to the event combine plugin 
        # to change the event channel.  To evaluate the performance we need 
        # to have the events on the same channel.
        self._event1_name_topic = f'{self._node_id_EventCombine}.event1_name'
        self._pub_sub_manager.subscribe(self, self._event1_name_topic)

        self._filename_topic = f'{self._node_id_EventCompare}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_topic)        
        
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._window_sec_1_topic, 'ping')
        self._pub_sub_manager.publish(self, self._order_topic, 'ping')
        self._pub_sub_manager.publish(self, self._border_effect_topic, 'ping')
        self._pub_sub_manager.publish(self, self._percentile_topic, 'ping')
        self._pub_sub_manager.publish(self, self._REMs_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event1_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')

        self._pub_sub_manager.publish(self, self._node_id_EventCompare+".get_activation_state", None)

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._window_sec_1_topic, \
            round(self.window_sec_doubleSpinBox.value(),2))
        self._pub_sub_manager.publish(self, self._order_topic, \
            self.order_spinBox.value())
        self._pub_sub_manager.publish(self, self._border_effect_topic, \
            round(self.border_effect_doubleSpinBox.value(),2))
        self._pub_sub_manager.publish(self, self._percentile_topic, \
            self.percentile_spinBox.value())
        self._pub_sub_manager.publish(self, self._REMs_name_topic, self.events_name_lineEdit.text())
        self._pub_sub_manager.publish(self, self._event1_name_topic, self.event_name_lineEdit.text())
        self._pub_sub_manager.publish(self, self._filename_topic, self.filename_lineEdit.text())

        if self.validation_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_EventCompare+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_EventCombine+".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_EventCompare+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_EventCombine+".activation_state_change", ActivationState.DEACTIVATED)
    
 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._window_sec_1_topic:
            self.window_sec_doubleSpinBox.setValue(float(message))
        if topic == self._order_topic:
            self.order_spinBox.setValue(int(message))
        if topic == self._border_effect_topic:
            self.border_effect_doubleSpinBox.setValue(float(message))
        if topic == self._percentile_topic:
            self.percentile_spinBox.setValue(int(message))
        if topic == self._REMs_name_topic:
            self.events_name_lineEdit.setText(message)
        if topic == self._event1_name_topic:
            self.event_name_lineEdit.setText(message)
        if topic == self._filename_topic:
            self.filename_lineEdit.setText(message)
        
    # Slot called when the user wants to write the filename
    def on_choose(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save TSV file', 
            None, 
            'TSV (*.tsv)')
        if filename != '':
            self.filename_lineEdit.setText(filename)

    def on_active_validation(self):
        if self.validation_checkBox.isChecked():
            self.event_name_label.setEnabled(True)
            self.event_name_lineEdit.setEnabled(True)
            self.filename_label.setEnabled(True)
            self.filename_lineEdit.setEnabled(True)
            self.filename_pushButton.setEnabled(True)
            
        else:
            self.event_name_label.setEnabled(False)
            self.event_name_lineEdit.setEnabled(False)
            self.filename_label.setEnabled(False)
            self.filename_lineEdit.setEnabled(False)
            self.filename_pushButton.setEnabled(False)

    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._window_sec_1_topic)
            self._pub_sub_manager.unsubscribe(self, self._order_topic)
            self._pub_sub_manager.unsubscribe(self, self._border_effect_topic)
            self._pub_sub_manager.unsubscribe(self, self._percentile_topic)
            self._pub_sub_manager.unsubscribe(self, self._REMs_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._event1_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)