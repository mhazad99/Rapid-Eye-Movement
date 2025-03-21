"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the FilterComponents plugin
"""

import numpy as np
from qtpy import QtWidgets

from RapidEyeMovementModules.FilterComponents.Ui_FilterComponentsSettingsView import Ui_FilterComponentsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class FilterComponentsSettingsView( BaseSettingsView,  Ui_FilterComponentsSettingsView, QtWidgets.QWidget):
    """
        FilterComponentsView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._threshold_topic = f'{self._parent_node.identifier}.threshold'
        self._pub_sub_manager.subscribe(self, self._threshold_topic)
        self._event_group_topic = f'{self._parent_node.identifier}.event_group'
        self._pub_sub_manager.subscribe(self, self._event_group_topic)
        self._event_name_topic = f'{self._parent_node.identifier}.event_name'
        self._pub_sub_manager.subscribe(self, self._event_name_topic)
        self._event_chan_topic = f'{self._parent_node.identifier}.event_channel'
        self._pub_sub_manager.subscribe(self, self._event_chan_topic)        

    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._threshold_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_chan_topic, 'ping')


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        if self.threshold_checkBox.isChecked():
            self._pub_sub_manager.publish(self, self._threshold_topic, \
                round(self.threshold_doubleSpinBox.value(),5))
        else:
            self._pub_sub_manager.publish(self, self._threshold_topic, \
                '')
        self._pub_sub_manager.publish(self, self._event_group_topic, \
            str(self.group_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._event_name_topic, \
            str(self.events_name_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._event_chan_topic, \
            str(self.channel_lineEdit.text()))


    def on_topic_update(self, topic, message, sender):
        pass


    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._threshold_topic and self.threshold_checkBox.isChecked():
            self.threshold_doubleSpinBox.setValue(float(message))
        if topic == self._event_group_topic:
            self.group_lineEdit.setText(str(message))
        if topic == self._event_name_topic:
            self.events_name_lineEdit.setText(str(message))
        if topic == self._event_chan_topic:
            self.channel_lineEdit.setText(str(message))


    def threshold_changed(self):
        if self.threshold_checkBox.isChecked():
            self.threshold_doubleSpinBox.setEnabled(True)
        else:
            self.threshold_doubleSpinBox.setEnabled(False)

     
    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._threshold_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_chan_topic)
 