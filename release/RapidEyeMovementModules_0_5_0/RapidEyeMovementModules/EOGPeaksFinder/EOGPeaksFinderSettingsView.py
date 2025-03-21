"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the EOGPeaksFinder plugin
"""

from qtpy import QtWidgets

from RapidEyeMovementModules.EOGPeaksFinder.Ui_EOGPeaksFinderSettingsView import Ui_EOGPeaksFinderSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EOGPeaksFinderSettingsView(BaseSettingsView, Ui_EOGPeaksFinderSettingsView, QtWidgets.QWidget):
    """
        EOGPeaksFinderView set the EOGPeaksFinder settings
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

        self.parameters = {
            "min_height_z": 1.5,
            "min_interval_s": 0.5
        }
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._parameters_topic, 'ping')
        self.update_ui_from_parameters()
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to EOGPeaksFinder
        self._pub_sub_manager.publish(self, self._parameters_topic, self.parameters)
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._parameters_topic:
            if isinstance(message, str) and not message == '':
                message = eval(message)
            if isinstance(message, dict):
                self.parameters = message
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._parameters_topic)
            

    # Called when the user finish editing a parameter from the UI
    def update_parameters_slot(self):
        self.parameters["min_height_z"] = self.doubleSpinBox_findP_minZ.value()
        self.parameters["min_interval_s"] = self.doubleSpinBox_findP_minInterv.value()


    def update_ui_from_parameters(self):
        self.doubleSpinBox_findP_minZ.setValue(self.parameters["min_height_z"])
        self.doubleSpinBox_findP_minInterv.setValue(self.parameters["min_interval_s"])