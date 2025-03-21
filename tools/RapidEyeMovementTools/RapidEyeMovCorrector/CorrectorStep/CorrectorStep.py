#! /usr/bin/env python3
"""
    CorrectorStep
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState


from RapidEyeMovementTools.RapidEyeMovCorrector.CorrectorStep.Ui_CorrectorStep import Ui_CorrectorStep

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

        # Define modules and nodes to talk to
        self._node_id_EventSubdivision = "2dea7327-ffdb-422a-b810-af0ec4d03cd3" 
        self._node_id_RescaleSignal_EEG = "cb4b0eba-a6fe-45c7-bba2-96847ab06009"
        self._node_id_RescaleSignal_EOG = "0bf1d03c-49c8-4c1a-902b-b12180a61912"
        self._node_id_AMI = "fff1d910-4c0e-4d0a-aa07-7e6c55372c44"
        self._node_id_group_const = "0a4be148-83e3-4d43-9d7b-0fe08ea6c10f"
        self._node_id_name_const = "09a8251a-7765-4bb0-b645-17ba0a4eb25c"
        self._node_id_sleep_stage_events = "2a08fd81-1170-4c45-ad15-7e447be1ff2d"
        self._node_id_FilterComp = "30e76a17-fbfa-450e-8b57-6cd2661262ac"
        self._node_id_event_cor_filter = "1b9d1341-7469-4b93-b3a5-07e9c2d414d1" # To select MOR_C

        # Subscribe to the publisher for each node you want to talk to
        self._group_topic = f'{self._node_id_group_const}.constant'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._name_topic = f'{self._node_id_name_const}.constant'
        self._pub_sub_manager.subscribe(self, self._name_topic)   

        self._window_sec_topic = f'{self._node_id_EventSubdivision}.window_sec'
        self._pub_sub_manager.subscribe(self, self._window_sec_topic)
        self._parameters_bin_EEG_topic = f'{self._node_id_RescaleSignal_EEG}.parameters'
        self._pub_sub_manager.subscribe(self, self._parameters_bin_EEG_topic)
        self._parameters_bin_EOG_topic = f'{self._node_id_RescaleSignal_EOG}.parameters'
        self._pub_sub_manager.subscribe(self, self._parameters_bin_EOG_topic)
        self._parameters_AMI_topic = f'{self._node_id_AMI}.parameters'
        self._pub_sub_manager.subscribe(self, self._parameters_AMI_topic)   
        self._parameters_in_cycle_topic = f'{self._node_id_sleep_stage_events}.in_cycle'
        self._pub_sub_manager.subscribe(self, self._parameters_in_cycle_topic)   
        self._n_max_comp_rm_topic = f'{self._node_id_FilterComp}.n_max_to_rem'
        self._pub_sub_manager.subscribe(self, self._n_max_comp_rm_topic)       
        self._group_cor_topic = f'{self._node_id_event_cor_filter}.group_selection'
        self._pub_sub_manager.subscribe(self, self._group_cor_topic)     
        self._name_cor_topic = f'{self._node_id_event_cor_filter}.name_selection'
        self._pub_sub_manager.subscribe(self, self._name_cor_topic)     


    def load_settings(self):
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_topic, 'ping')    
        self._pub_sub_manager.publish(self, self._window_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._parameters_bin_EEG_topic, 'ping')
        self._pub_sub_manager.publish(self, self._parameters_bin_EOG_topic, 'ping')
        self._pub_sub_manager.publish(self, self._parameters_AMI_topic, 'ping')
        self._pub_sub_manager.publish(self, self._parameters_in_cycle_topic, 'ping')
        self._pub_sub_manager.publish(self, self._n_max_comp_rm_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_cor_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_cor_topic, 'ping')


    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._group_topic, self.group_lineEdit.text())
        self._pub_sub_manager.publish(self, self._name_topic, self.name_lineEdit.text())

        self._pub_sub_manager.publish(self, self._window_sec_topic, \
            round(self.window_sec_doubleSpinBox.value(),2))
        self.update_parameters()
        self._pub_sub_manager.publish(self, self._parameters_bin_EEG_topic, \
            self.parameters_bin_EEG)
        self._pub_sub_manager.publish(self, self._parameters_bin_EOG_topic, \
            self.parameters_bin_EOG)
        self._pub_sub_manager.publish(self, self._parameters_AMI_topic, \
            self.parameters_AMI)
        self._pub_sub_manager.publish(self, self._parameters_in_cycle_topic, \
            int(self.cycle_radioButton.isChecked()))
        self._pub_sub_manager.publish(self, self._n_max_comp_rm_topic, \
            str(self.n_max_comp_rm_spinBox.value()))

        self._pub_sub_manager.publish(self, self._group_cor_topic, \
            self.lineEdit_group_to_cor.text())  
        self._pub_sub_manager.publish(self, self._name_cor_topic, \
            self.lineEdit_name_to_cor.text())  
    

    def update_parameters(self):
        self.parameters_bin_EEG = {'n_bins' : self.eeg_bin_spinBox.value(),
                                   'encode' : "ordinal",
                                   'strategy' : "uniform",
                                   'dtype' : None
                                   }
        self.parameters_bin_EOG = {'n_bins' : self.eog_bin_spinBox.value(),
                                   'encode' : "ordinal",
                                   'strategy' : "uniform",
                                   'dtype' : None
                                   }
        self.parameters_AMI = {'max_iter': self.n_iter_spinBox.value(),
                               'confidence_level': self.p_val_doubleSpinBox.value(),
                               'criteria_scope' : 0 if self.cycle_radioButton.isChecked() else 1}


    # To init 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._group_topic:
            self.group_lineEdit.setText(message)
        if topic == self._name_topic:
            self.name_lineEdit.setText(message)
        if topic == self._window_sec_topic:
            self.window_sec_doubleSpinBox.setValue(float(message))
        if topic == self._parameters_bin_EEG_topic:
                if message=='':
                    self.eeg_bin_spinBox.setValue(90)
                else:
                    self.eeg_bin_spinBox.setValue(int(message['n_bins']))

        if topic == self._parameters_bin_EOG_topic:
                if message=='':
                    self.eog_bin_spinBox.setValue(30)
                else:
                    self.eog_bin_spinBox.setValue(int(message['n_bins']))

        if topic == self._parameters_AMI_topic:
            if message == '':
                # Default values
                self.n_iter_spinBox.setValue(int(1000))
                self.p_val_doubleSpinBox.setValue(float(0.90))
                self.cycle_radioButton.setChecked(True)                
            else:
                self.n_iter_spinBox.setValue(int(message['max_iter']))
                self.p_val_doubleSpinBox.setValue(float(message['confidence_level']))
                if int(message['criteria_scope'])==0:
                    self.cycle_radioButton.setChecked(True)
                elif int(message['criteria_scope'])==1:
                    self.recording_radioButton.setChecked(True)
        if topic == self._n_max_comp_rm_topic:
            self.n_max_comp_rm_spinBox.setValue(int(message))
        if topic == self._group_cor_topic:
            self.lineEdit_group_to_cor.setText(message)
        if topic == self._name_cor_topic:
            self.lineEdit_name_to_cor.setText(message)

            
    def expert_mode_slot(self):
        if self.expert_mode_checkBox.isChecked():
            self.window_sec_doubleSpinBox.setEnabled(True)
            self.p_val_doubleSpinBox.setEnabled(True)
            self.n_iter_spinBox.setEnabled(True)
            self.eeg_bin_spinBox.setEnabled(True)
            self.eog_bin_spinBox.setEnabled(True)
        else:
            self.window_sec_doubleSpinBox.setEnabled(False)
            self.p_val_doubleSpinBox.setEnabled(False)
            self.n_iter_spinBox.setEnabled(False)
            self.eeg_bin_spinBox.setEnabled(False)
            self.eog_bin_spinBox.setEnabled(False)            


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._group_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_topic)
            self._pub_sub_manager.unsubscribe(self, self._window_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._parameters_bin_EEG_topic)
            self._pub_sub_manager.unsubscribe(self, self._parameters_bin_EOG_topic)
            self._pub_sub_manager.unsubscribe(self, self._parameters_AMI_topic)
            self._pub_sub_manager.unsubscribe(self, self._parameters_in_cycle_topic)
            self._pub_sub_manager.unsubscribe(self, self._n_max_comp_rm_topic)
            self._pub_sub_manager.unsubscribe(self, self._group_cor_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_cor_topic)
