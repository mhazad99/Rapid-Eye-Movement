"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the RemDetector plugin
"""

from qtpy import QtWidgets

from RapidEyeMovementModules.RemDetector.Ui_RemDetectorSettingsView import Ui_RemDetectorSettingsView
from commons.BaseSettingsView import BaseSettingsView

class RemDetectorSettingsView(BaseSettingsView, Ui_RemDetectorSettingsView, QtWidgets.QWidget):
    """
        RemDetectorView set the RemDetector settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._group_topic = f'{self._parent_node.identifier}.event_group'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._name_topic = f'{self._parent_node.identifier}.event_name'
        self._pub_sub_manager.subscribe(self, self._name_topic)   
        self._channel_topic = f'{self._parent_node.identifier}.event_channel'
        self._pub_sub_manager.subscribe(self, self._channel_topic)   

        self._border_effect_topic = f'{self._parent_node.identifier}.border_effect'
        self._pub_sub_manager.subscribe(self, self._border_effect_topic)
        self._percentile_topic = f'{self._parent_node.identifier}.percentile'
        self._pub_sub_manager.subscribe(self, self._percentile_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._channel_topic, 'ping')
        self._pub_sub_manager.publish(self, self._border_effect_topic, 'ping')
        self._pub_sub_manager.publish(self, self._percentile_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to RemDetector
        self._pub_sub_manager.publish(self, self._group_topic, self.group_lineEdit.text())
        self._pub_sub_manager.publish(self, self._name_topic, self.name_lineEdit.text())
        self._pub_sub_manager.publish(self, self._channel_topic, self.channel_lineEdit.text())
        self._pub_sub_manager.publish(self, self._border_effect_topic, self.border_effect_spinBox.value())
        self._pub_sub_manager.publish(self, self._percentile_topic, self.percentile_spinBox.value())
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._group_topic:
            self.group_lineEdit.setText(message)
        if topic == self._name_topic:
            self.name_lineEdit.setText(message)
        if topic == self._channel_topic:
            self.channel_lineEdit.setText(message)
        if topic == self._border_effect_topic:
            self.border_effect_spinBox.setValue(int(message))
        if topic == self._percentile_topic:
            self.percentile_spinBox.setValue(int(message))
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._group_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_topic)
            self._pub_sub_manager.unsubscribe(self, self._channel_topic)
            self._pub_sub_manager.unsubscribe(self, self._border_effect_topic)
            self._pub_sub_manager.unsubscribe(self, self._percentile_topic)
        