#! /usr/bin/env python3
"""
    DetectorStep
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState


from RapidEyeMovementTools.RapidEyeMovCorrector.DetectorStep.Ui_DetectorStep import Ui_DetectorStep

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
        self._node_id_EventSubdivision = "265484c3-34f9-41ea-8a5c-fbf0a7025ed8"
        self._node_id_DerivativeApprox = "270e3293-fc72-4ea6-a98e-7ae6a936501b" 
        self._node_id_RemDetector = "55c67b42-f11c-47cd-bc65-025b603db75c"
        self._node_id_Event_rename = "bc379172-a96c-4d2f-859a-445c87d1cc1d"

        # Modules for deactivation
        self._node_id_SignalsFromEvents = "5228f649-7b8c-4a83-93d5-55f9eece5344" 
        self._node_id_DetrendSignal = "2d3f1181-8738-438b-a92b-d289f9fb107a" 

        self._node_id_expert_events_constant = "58deeb7f-1102-45de-b7c2-c991a6b9ea7a"
        self._node_event_combine_comb = "96475be5-69f8-481d-903a-e5e94bf8084d" # Event combine to combine det and expert
        self._node_event_combine_rename = "bc379172-a96c-4d2f-859a-445c87d1cc1d" # Event combine to rename det events

        # Subscribe to the publisher for each node you want to talk to
        self._window_sec_1_topic = f'{self._node_id_EventSubdivision}.window_sec'
        self._pub_sub_manager.subscribe(self, self._window_sec_1_topic)
        self._order_topic = f'{self._node_id_DerivativeApprox}.order'
        self._pub_sub_manager.subscribe(self, self._order_topic)
        self._border_effect_topic = f'{self._node_id_RemDetector}.border_effect'
        self._pub_sub_manager.subscribe(self, self._border_effect_topic)
        self._percentile_topic = f'{self._node_id_RemDetector}.percentile'
        self._pub_sub_manager.subscribe(self, self._percentile_topic)    
        self._det_name_topic = f'{self._node_id_Event_rename}.new_event_name'
        self._pub_sub_manager.subscribe(self, self._det_name_topic)    
        self._expert_label_topic = f'{self._node_event_combine_comb}.event1_name'
        self._pub_sub_manager.subscribe(self, self._expert_label_topic)   
         

    def load_settings(self):
        # # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._window_sec_1_topic, 'ping')
        self._pub_sub_manager.publish(self, self._order_topic, 'ping')
        self._pub_sub_manager.publish(self, self._border_effect_topic, 'ping')
        self._pub_sub_manager.publish(self, self._percentile_topic, 'ping')
        self._pub_sub_manager.publish(self, self._det_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._expert_label_topic, 'ping')
        
        self._pub_sub_manager.publish(self, self._node_id_EventSubdivision+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_DerivativeApprox+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_RemDetector+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SignalsFromEvents+".get_activation_state", None)
        self._pub_sub_manager.publish(self,  self._node_id_DetrendSignal+".get_activation_state", None)
        self._pub_sub_manager.publish(self,  self._node_id_expert_events_constant+".get_activation_state", None)
        self._pub_sub_manager.publish(self,  self._node_event_combine_comb+".get_activation_state", None)
        self._pub_sub_manager.publish(self,  self._node_event_combine_rename+".get_activation_state", None)
        

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._window_sec_1_topic, \
            round(self.window_sec_doubleSpinBox.value(),2))
        self._pub_sub_manager.publish(self, self._order_topic, \
            self.order_spinBox.value())
        self._pub_sub_manager.publish(self, self._border_effect_topic, \
            round(self.border_effect_doubleSpinBox.value(),2))
        self._pub_sub_manager.publish(self, self._percentile_topic, \
            self.percentile_spinBox.value())
        self._pub_sub_manager.publish(self, self._det_name_topic, \
            self.name_lineEdit.text())       
        self._pub_sub_manager.publish(self, self._expert_label_topic, \
            self.expert_label_lineEdit.text())  
             

        # *** REMs Poulin Detector
        if self.REMs_Det_radioButton.isChecked():
            self._pub_sub_manager.publish(self, \
                self._node_id_EventSubdivision+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, \
                self._node_id_DerivativeApprox+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, \
                self._node_id_RemDetector+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, \
                self._node_id_SignalsFromEvents+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self,  \
                self._node_id_DetrendSignal+".activation_state_change", ActivationState.ACTIVATED)
            # Deactivate the events from the expert
            self._pub_sub_manager.publish(self, \
                self._node_id_expert_events_constant+".activation_state_change", ActivationState.DEACTIVATED)
            # Combine event activated
            self._pub_sub_manager.publish(self,  \
                self._node_event_combine_comb+".activation_state_change", ActivationState.ACTIVATED)           
            self._pub_sub_manager.publish(self,  \
                self._node_event_combine_rename+".activation_state_change", ActivationState.ACTIVATED)         
        # *** Events from the expert
        elif self.expert_annot_radioButton.isChecked():
            self._pub_sub_manager.publish(self, \
                self._node_id_EventSubdivision+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, \
                self._node_id_DerivativeApprox+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, \
                self._node_id_RemDetector+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, \
                self._node_id_SignalsFromEvents+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self,  \
                self._node_id_DetrendSignal+".activation_state_change", ActivationState.DEACTIVATED)
            # Activate the events from the expert
            self._pub_sub_manager.publish(self, \
                self._node_id_expert_events_constant+".activation_state_change", ActivationState.ACTIVATED)
            # Combine event activated
            self._pub_sub_manager.publish(self,  \
                self._node_event_combine_comb+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self,  \
                self._node_event_combine_rename+".activation_state_change", ActivationState.DEACTIVATED)    
        # *** Mutual information exclusively
        elif self.mutual_info_radioButton.isChecked():
            self._pub_sub_manager.publish(self, \
                self._node_id_EventSubdivision+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, \
                self._node_id_DerivativeApprox+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, \
                self._node_id_RemDetector+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, \
                self._node_id_SignalsFromEvents+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self,  \
                self._node_id_DetrendSignal+".activation_state_change", ActivationState.DEACTIVATED)            
            self._pub_sub_manager.publish(self, \
                self._node_id_expert_events_constant+".activation_state_change", ActivationState.DEACTIVATED)    
            # Combine event deactivated
            self._pub_sub_manager.publish(self,  \
                self._node_event_combine_comb+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self,  \
                self._node_event_combine_rename+".activation_state_change", ActivationState.DEACTIVATED)  
      

    
    # To init 
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
        if topic == self._det_name_topic:
            self.name_lineEdit.setText(message)
        if topic == self._expert_label_topic:
            self.expert_label_lineEdit.setText(message)

        if topic == self._node_id_EventSubdivision+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.REMs_Det_radioButton.setChecked(True)
            self.on_active_detector()
        if topic == self._node_id_expert_events_constant+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.expert_annot_radioButton.setChecked(True)
            self.on_active_detector()
        if topic == self._node_event_combine_comb+".get_activation_state":
            if message == ActivationState.DEACTIVATED:
                self.mutual_info_radioButton.setChecked(True)
            self.on_active_detector()
            

    def on_active_detector(self):
        if self.REMs_Det_radioButton.isChecked():
            self.name_lineEdit.setEnabled(True)
            self.percentile_spinBox.setEnabled(True)
            self.expert_checkBox.setEnabled(True)
        else:
            self.name_lineEdit.setEnabled(False)
            self.window_sec_doubleSpinBox.setEnabled(False)
            self.order_spinBox.setEnabled(False)
            self.border_effect_doubleSpinBox.setEnabled(False)
            self.percentile_spinBox.setEnabled(False)
            self.expert_checkBox.setEnabled(False)
        if self.expert_annot_radioButton.isChecked():
            self.expert_label_lineEdit.setEnabled(True)
        else:
            self.expert_label_lineEdit.setEnabled(False)         
        self.expert_mode_slot()


    def expert_mode_slot(self):
        if self.expert_checkBox.isChecked():
            self.window_sec_doubleSpinBox.setEnabled(True)
            self.order_spinBox.setEnabled(True)
            self.border_effect_doubleSpinBox.setEnabled(True)
        else:
            self.window_sec_doubleSpinBox.setEnabled(False)
            self.order_spinBox.setEnabled(False)
            self.border_effect_doubleSpinBox.setEnabled(False)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._window_sec_1_topic)
            self._pub_sub_manager.unsubscribe(self, self._order_topic)
            self._pub_sub_manager.unsubscribe(self, self._border_effect_topic)
            self._pub_sub_manager.unsubscribe(self, self._percentile_topic)
            self._pub_sub_manager.unsubscribe(self, self._det_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._expert_label_topic)
