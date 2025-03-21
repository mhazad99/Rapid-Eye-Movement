"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the AccidentalMutualInfo plugin
"""

import numpy as np
from qtpy import QtWidgets

from RapidEyeMovementModules.AccidentalMutualInfo.Ui_AccidentalMutualInfoSettingsView import Ui_AccidentalMutualInfoSettingsView
from commons.BaseSettingsView import BaseSettingsView

class AccidentalMutualInfoSettingsView( BaseSettingsView,  Ui_AccidentalMutualInfoSettingsView, QtWidgets.QWidget):
    """
        AccidentalMutualInfoView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._parameters_topic = f'{self._parent_node.identifier}.parameters'
        self._pub_sub_manager.subscribe(self, self._parameters_topic)
        

    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._parameters_topic, 'ping')
        #self.update_parameters()


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        self.update_parameters()
        self._pub_sub_manager.publish(self, self._parameters_topic, \
            self.parameters)


    def on_topic_update(self, topic, message, sender):
        pass
    

    def update_parameters(self):
        self.parameters = {'max_iter': self.max_iter_spinBox.value(),
                           'confidence_level': self.p_val_doubleSpinBox.value(),
                           'criteria_scope' : 0 if self.cycle_radioButton.isChecked() else 1}


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._parameters_topic:
            if message == '':
                # Default values
                self.max_iter_spinBox.setValue(int(1000))
                self.p_val_doubleSpinBox.setValue(float(0.90))
                self.cycle_radioButton.setChecked(True)
            else:
                self.max_iter_spinBox.setValue(int(message['max_iter']))
                self.p_val_doubleSpinBox.setValue(float(message['confidence_level']))
                if int(message['criteria_scope'])==0:
                    self.cycle_radioButton.setChecked(True)
                elif int(message['criteria_scope'])==1:
                    self.recording_radioButton.setChecked(True)
                    
     
    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._parameters_topic)
 