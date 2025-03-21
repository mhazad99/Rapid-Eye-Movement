"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the EOGPeaksMatches plugin
"""

from qtpy import QtWidgets

from RapidEyeMovementModules.EOGPeaksMatches.Ui_EOGPeaksMatchesSettingsView import Ui_EOGPeaksMatchesSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EOGPeaksMatchesSettingsView(BaseSettingsView, Ui_EOGPeaksMatchesSettingsView, QtWidgets.QWidget):
    """
        EOGPeaksMatchesView set the EOGPeaksMatches settings
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

        self.parameters = {}
        self.parameters['time_window_s'] = 0.3
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._parameters_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to EOGPeaksMatches
        self.parameters['time_window_s'] = self.doubleSpinBox_matchP_timeWin.value()
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
            self.doubleSpinBox_matchP_timeWin.setValue(float(self.parameters['time_window_s']))
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._parameters_topic)
            