"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the DetrendSignal plugin
"""

from qtpy import QtWidgets

from RapidEyeMovementModules.DetrendSignal.Ui_DetrendSignalSettingsView import Ui_DetrendSignalSettingsView
from commons.BaseSettingsView import BaseSettingsView

class DetrendSignalSettingsView(BaseSettingsView, Ui_DetrendSignalSettingsView, QtWidgets.QWidget):
    """
        DetrendSignalView set the DetrendSignal settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._mode_topic = f'{self._parent_node.identifier}.mode'
        self._pub_sub_manager.subscribe(self, self._mode_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._mode_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        # Send the settings to the publisher for inputs to DetrendSignal
        self._pub_sub_manager.publish(self, self._mode_topic, str(self.mode_comboBox.currentText()))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._mode_topic:
            self.mode_comboBox.setCurrentText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._mode_topic)
            return
        