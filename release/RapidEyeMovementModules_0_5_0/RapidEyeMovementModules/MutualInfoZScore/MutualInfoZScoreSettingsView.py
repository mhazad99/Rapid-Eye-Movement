"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the MutualInfoZScore plugin
"""

import numpy as np
from qtpy import QtWidgets

from RapidEyeMovementModules.MutualInfoZScore.Ui_MutualInfoZScoreSettingsView import Ui_MutualInfoZScoreSettingsView
from commons.BaseSettingsView import BaseSettingsView

class MutualInfoZScoreSettingsView( BaseSettingsView,  Ui_MutualInfoZScoreSettingsView, QtWidgets.QWidget):
    """
        MutualInfoZScoreView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._mean_topic = f'{self._parent_node.identifier}.mean'
        self._pub_sub_manager.subscribe(self, self._mean_topic)

        self._std_topic = f'{self._parent_node.identifier}.std'
        self._pub_sub_manager.subscribe(self, self._std_topic)

        self._criteria_topic = f'{self._parent_node.identifier}.criteria'
        self._pub_sub_manager.subscribe(self, self._criteria_topic)
        
    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
            self._pub_sub_manager.publish(self, self._mean_topic, 'ping')
            self._pub_sub_manager.publish(self, self._std_topic, 'ping')
            self._pub_sub_manager.publish(self, self._criteria_topic, 'ping')


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        if self.mean_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._mean_topic, \
                round(self.mean_doubleSpinBox.value(),5))
        else:
            self._pub_sub_manager.publish(self, self._mean_topic, \
                '')
        if self.std_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._std_topic, \
                round(self.std_doubleSpinBox.value(),5))
        else:
            self._pub_sub_manager.publish(self, self._std_topic, \
                '')

        if self.criteria_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._criteria_topic, \
                round(self.criteria_doubleSpinBox.value(),5))
        else:
            self._pub_sub_manager.publish(self, self._criteria_topic, \
                '')
            
    def on_topic_update(self, topic, message, sender):
        pass

    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._mean_topic and self.mean_checkBox.isChecked():
            self.mean_doubleSpinBox.setValue(float(message))
        
        if topic == self._std_topic and self.std_checkBox.isChecked():
            self.std_doubleSpinBox.setValue(float(message))

        if topic == self._criteria_topic and self.criteria_checkBox.isChecked():
            self.criteria_doubleSpinBox.setValue(float(message))

    def mean_changed(self):
        if self.mean_checkBox.isChecked():
            self.mean_doubleSpinBox.setEnabled(True)
        else:
            self.mean_doubleSpinBox.setEnabled(False)

    def std_changed(self):
        if self.std_checkBox.isChecked():
            self.std_doubleSpinBox.setEnabled(True)
        else:
            self.std_doubleSpinBox.setEnabled(False)

    def criteria_changed(self):
        if self.criteria_checkBox.isChecked():
            self.criteria_doubleSpinBox.setEnabled(True)
        else:
            self.criteria_doubleSpinBox.setEnabled(False)

     
    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._mean_topic)
            self._pub_sub_manager.unsubscribe(self, self._std_topic)
            self._pub_sub_manager.unsubscribe(self, self._criteria_topic)
 