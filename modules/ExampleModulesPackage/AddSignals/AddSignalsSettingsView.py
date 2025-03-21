"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the AddSignals plugin
"""

from qtpy import QtWidgets

from ExampleModulesPackage.AddSignals.Ui_AddSignalsSettingsView import Ui_AddSignalsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class AddSignalsSettingsView(BaseSettingsView, Ui_AddSignalsSettingsView, QtWidgets.QWidget):
    """
        AddSignalsView set the AddSignals settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        pass        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        pass
        
    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        pass

   # Called when the user delete an instance of the plugin
    def __del__(self):
        pass
