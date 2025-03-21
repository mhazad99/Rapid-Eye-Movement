"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the PrintSignal plugin
"""

from qtpy import QtWidgets
import os 

from ExampleModulesPackage.PrintSignal.Ui_PrintSignalSettingsView import Ui_PrintSignalSettingsView
from commons.BaseSettingsView import BaseSettingsView

class PrintSignalSettingsView(BaseSettingsView, Ui_PrintSignalSettingsView, QtWidgets.QWidget):
    """
        PrintSignalView set the PrintSignal settings
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
        
    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        # Send the settings to the publisher for inputs to PrintSignal
        self._pub_sub_manager.publish(self, self._filename_topic, str(self.filename_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._filename_topic:
            self.filename_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            
    def choose_filename(self):
         # Get an existing directory
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', filter='PNG Files (*.png)')[0]

        if filename != "":
            # Add .png extension if there is no extension
            name, ext = os.path.splitext(filename)
            if not ext:
                filename += '.png'

            self.filename_lineedit.setText(filename)