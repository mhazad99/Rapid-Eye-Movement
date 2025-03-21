"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the EOGNormalization plugin
"""

from qtpy import QtWidgets

from RapidEyeMovementModules.EOGNormalization.Ui_EOGNormalizationSettingsView import Ui_EOGNormalizationSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EOGNormalizationSettingsView(BaseSettingsView, Ui_EOGNormalizationSettingsView, QtWidgets.QWidget):
    """
        EOGNormalizationView set the EOGNormalization settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._filename_topic = f'{self._parent_node.identifier}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_topic)
        self._signals_topic = f'{self._parent_node.identifier}.signals'
        self._pub_sub_manager.subscribe(self, self._signals_topic)
        self._baseline_stats_topic = f'{self._parent_node.identifier}.baseline_stats'
        self._pub_sub_manager.subscribe(self, self._baseline_stats_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._signals_topic, 'ping')
        self._pub_sub_manager.publish(self, self._baseline_stats_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        # Send the settings to the publisher for inputs to EOGNormalization
        self._pub_sub_manager.publish(self, self._filename_topic, str(self.filename_lineedit.text()))
        self._pub_sub_manager.publish(self, self._signals_topic, str(self.signals_lineedit.text()))
        self._pub_sub_manager.publish(self, self._baseline_stats_topic, str(self.baseline_stats_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._filename_topic:
            self.filename_lineedit.setText(message)
        if topic == self._signals_topic:
            self.signals_lineedit.setText(message)
        if topic == self._baseline_stats_topic:
            self.baseline_stats_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            self._pub_sub_manager.unsubscribe(self, self._signals_topic)
            self._pub_sub_manager.unsubscribe(self, self._baseline_stats_topic)
            