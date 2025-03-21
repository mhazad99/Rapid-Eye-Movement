"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the EOGEventsCreator plugin
"""

from qtpy import QtWidgets

from RapidEyeMovementModules.EOGEventsCreator.Ui_EOGEventsCreatorSettingsView import Ui_EOGEventsCreatorSettingsView
from commons.BaseSettingsView import BaseSettingsView

class EOGEventsCreatorSettingsView(BaseSettingsView, Ui_EOGEventsCreatorSettingsView, QtWidgets.QWidget):
    """
        EOGEventsCreatorView set the EOGEventsCreator settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._paramters_topic = f'{self._parent_node.identifier}.parameters'
        self._pub_sub_manager.subscribe(self, self._paramters_topic)

        self.parameters = {}
        self.parameters['time_window_s'] = 0.665
        self.parameters['min_deflection_angle'] = None
        self.parameters['max_deflection_std'] = None
        self.parameters['max_angle_diff_EOG'] = None
        self.parameters['min_amplitude_z_2nd_EOG'] = None
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._paramters_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to EOGEventsCreator

        self.parameters['time_window_s'] = self.doubleSpinBox_timeWin.value()

        if self.checkBox_angle.isChecked():
            self.parameters['min_deflection_angle'] = self.doubleSpinBox_deflection_angle.value()
        else:
            self.parameters['min_deflection_angle'] = None
        if self.checkBox_max_diff_angle.isChecked():
            self.parameters['max_angle_diff_EOG'] = self.doubleSpinBox_diff_angle.value()
        else:
            self.parameters['max_angle_diff_EOG'] = None
        self._pub_sub_manager.publish(self, self._paramters_topic, self.parameters)
        
        if self.checkBox_slope.isChecked():
            self.parameters['max_deflection_std'] = self.doubleSpinBox_deflection_slope.value()
        else:
            self.parameters['max_deflection_std'] = None

        if self.checkBox_min_z_2nd_chan.isChecked():
            self.parameters['min_amplitude_z_2nd_EOG'] = self.doubleSpinBox_min_z_2nd_chan.value()
        else:
            self.parameters['min_amplitude_z_2nd_EOG'] = None

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._paramters_topic:
            if isinstance(message, str) and not message == '':
                message = eval(message)
            if isinstance(message, dict):
                self.parameters = message
                # Update the UI
                self.doubleSpinBox_timeWin.setValue(float(self.parameters['time_window_s']))

                if self.parameters['min_deflection_angle'] is not None:
                    self.checkBox_angle.setChecked(True)
                    self.doubleSpinBox_deflection_angle.setEnabled(True)
                    self.doubleSpinBox_deflection_angle.setValue(float(self.parameters['min_deflection_angle']))
                else:
                    self.checkBox_angle.setChecked(False)
                    self.doubleSpinBox_deflection_angle.setEnabled(False)

                if self.parameters['max_angle_diff_EOG'] is not None:
                    self.checkBox_max_diff_angle.setChecked(True)
                    self.doubleSpinBox_diff_angle.setEnabled(True)
                    self.doubleSpinBox_diff_angle.setValue(float(self.parameters['max_angle_diff_EOG']))
                else:
                    self.checkBox_max_diff_angle.setChecked(False)
                    self.doubleSpinBox_diff_angle.setEnabled(False)

                if self.parameters['max_deflection_std'] is not None:
                    self.checkBox_slope.setChecked(True)
                    self.doubleSpinBox_deflection_slope.setEnabled(True)
                    self.doubleSpinBox_deflection_slope.setValue(float(self.parameters['max_deflection_std']))
                else:
                    self.checkBox_slope.setChecked(False)
                    self.doubleSpinBox_deflection_slope.setEnabled(False)

                if self.parameters['min_amplitude_z_2nd_EOG'] is not None:
                    self.checkBox_min_z_2nd_chan.setChecked(True)
                    self.doubleSpinBox_min_z_2nd_chan.setEnabled(True)
                    self.doubleSpinBox_min_z_2nd_chan.setValue(float(self.parameters['min_amplitude_z_2nd_EOG']))
                else:
                    self.checkBox_min_z_2nd_chan.setChecked(False)
                    self.doubleSpinBox_min_z_2nd_chan.setEnabled(False)


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._paramters_topic)
            

    # Called when the user change the settings for the deflection
    def change_parameters_slot(self):
        self.doubleSpinBox_diff_angle.setEnabled(self.checkBox_max_diff_angle.isChecked())
        self.doubleSpinBox_deflection_angle.setEnabled(self.checkBox_angle.isChecked())
        self.doubleSpinBox_deflection_slope.setEnabled(self.checkBox_slope.isChecked())
        self.doubleSpinBox_min_z_2nd_chan.setEnabled(self.checkBox_min_z_2nd_chan.isChecked())

