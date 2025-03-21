"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the SpectralPower plugin
"""
from commons.BaseSettingsView import BaseSettingsView
from RapidEyeMovementModules.SpectralPower.Ui_SpectralPowerSettingsView import Ui_SpectralPowerSettingsView

import numpy as np
from qtpy import QtWidgets

class SpectralPowerSettingsView(BaseSettingsView, Ui_SpectralPowerSettingsView, QtWidgets.QWidget):
    """
        SpectralPowerView set the SpectralPower settings
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
        self._freq_band_topic = f'{self._parent_node.identifier}.freq_band'
        self._pub_sub_manager.subscribe(self, self._freq_band_topic)
        self._filename_topic = f'{self._parent_node.identifier}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_topic)
        

    def on_choose(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None,
            'Save as CSV file',
            None,
            'CSV (*.csv)')
        if filename != '':
            self.filename_lineEdit.setText(filename)

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._mode_topic, 'ping')
        self._pub_sub_manager.publish(self, self._freq_band_topic, 'ping')
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        self.update_freq_band()

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        self.update_freq_band()
        if self.abs_radioButton.isChecked():
            self.mode = 'absolute'
        elif self.rel_radioButton.isChecked():
            self.mode = 'relative'
        self._pub_sub_manager.publish(self, self._mode_topic, \
            self.mode)
        self._pub_sub_manager.publish(self, self._freq_band_topic, \
            self.freq_band)
        self._pub_sub_manager.publish(self, self._filename_topic, \
            str(self.filename_lineEdit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass
    
    def on_change_mode(self):
        if self.abs_radioButton.isChecked():
            self.total_checkBox.setEnabled(bool(True))
        else:
            self.total_checkBox.setChecked(bool(True))
            self.total_checkBox.setEnabled(bool(False))

    def update_freq_band(self):
        self.freq_band = {}
        if self.delta_checkBox.isChecked():
            self.freq_band['delta'] = list(map(float, ''.join(self.delta_lineEdit.text().replace("-", ",")).split(',')))
        if self.theta_checkBox.isChecked():
            self.freq_band['theta'] = list(map(float, ''.join(self.theta_lineEdit.text().replace("-", ",")).split(',')))
        if self.alpha_checkBox.isChecked():
            self.freq_band['alpha'] = list(map(float, ''.join(self.alpha_lineEdit.text().replace("-", ",")).split(',')))
        if self.beta_checkBox.isChecked():
            self.freq_band['beta'] = list(map(float, ''.join(self.beta_lineEdit.text().replace("-", ",")).split(',')))
        if self.gamma_checkBox.isChecked():
            self.freq_band['gamma'] = list(map(float, ''.join(self.gamma_lineEdit.text().replace("-", ",")).split(',')))
        if self.others_checkBox.isChecked():
            x = self.others_lineEdit.text().split(';')
            n = 1
            for band in x:
                self.freq_band[str(n)] = list(map(float, ''.join(band.replace("-", ",")).split(',')))
                n += 1
        if self.total_checkBox.isChecked():
            self.freq_band['total'] = list(map(float, ''.join(self.total_lineEdit.text().replace("-", ",")).split(',')))

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._mode_topic:
            if message == '':
                self.abs_radioButton.setChecked(bool(False))
            else:
                if message == 'absolute':
                    self.abs_radioButton.setChecked(bool(True))
                    self.total_checkBox.setEnabled(bool(True))
                if message == 'relative':
                    self.rel_radioButton.setChecked(bool(True))
                    self.total_checkBox.setChecked(bool(True))
                    self.total_checkBox.setEnabled(bool(False))

        if topic == self._freq_band_topic:
            if message == '' or message == {}:
                self.delta_checkBox.setChecked(bool(False))
                self.theta_checkBox.setChecked(bool(False))
                self.alpha_checkBox.setChecked(bool(False))
                self.beta_checkBox.setChecked(bool(False))
                self.gamma_checkBox.setChecked(bool(False))
                self.others_checkBox.setChecked(bool(False))
                self.total_checkBox.setChecked(bool(False))
                self.delta_lineEdit.setText(str('0.3-4'))
                self.theta_lineEdit.setText(str('4-8'))
                self.alpha_lineEdit.setText(str('8-12'))
                self.beta_lineEdit.setText(str('12-30'))
                self.gamma_lineEdit.setText(str('30-100'))
                self.others_lineEdit.setText(str(''))
                self.total_lineEdit.setText(str('0.3-40'))
            else:
                if "delta" in message:
                    self.delta_checkBox.setChecked(bool(True))
                    new_string = ''.join(str(message['delta']).replace(",", "-"))
                    new_string = new_string.replace("[", "")
                    new_string = new_string.replace("]", "")
                    new_string = new_string.replace(" ", "")
                    self.delta_lineEdit.setText(str(new_string))
                if "theta" in message:
                    self.theta_checkBox.setChecked(bool(True))
                    new_string = ''.join(str(message['theta']).replace(",", "-"))
                    new_string = new_string.replace("[", "")
                    new_string = new_string.replace("]", "")
                    new_string = new_string.replace(" ", "")
                    self.theta_lineEdit.setText(str(new_string))
                if "alpha" in message:
                    self.alpha_checkBox.setChecked(bool(True))
                    new_string = ''.join(str(message['alpha']).replace(",", "-"))
                    new_string = new_string.replace("[", "")
                    new_string = new_string.replace("]", "")
                    new_string = new_string.replace(" ", "")
                    self.alpha_lineEdit.setText(str(new_string))
                if "beta" in message:
                    self.beta_checkBox.setChecked(bool(True))
                    new_string = ''.join(str(message['beta']).replace(",", "-"))
                    new_string = new_string.replace("[", "")
                    new_string = new_string.replace("]", "")
                    new_string = new_string.replace(" ", "")
                    self.beta_lineEdit.setText(str(new_string))
                if "gamma" in message:
                    self.gamma_checkBox.setChecked(bool(True))
                    new_string = ''.join(str(message['gamma']).replace(",", "-"))
                    new_string = new_string.replace("[", "")
                    new_string = new_string.replace("]", "")
                    new_string = new_string.replace(" ", "")
                    self.gamma_lineEdit.setText(str(new_string))
                if "1" in message:
                    self.others_checkBox.setChecked(bool(True))
                    n = 1
                    while str(n) in message:
                        new_string = ''.join(str(message[str(n)]).replace(",", "-"))
                        new_string = new_string.replace("[", "")
                        new_string = new_string.replace("]", "")
                        new_string = new_string.replace(" ", "")
                        if n == 1:
                            new_strings = new_string
                        else:
                            new_strings = new_strings + ';' + new_string
                        n += 1
                    self.others_lineEdit.setText(str(new_strings))
                if "total" in message:
                    self.total_checkBox.setChecked(bool(True))
                    new_string = ''.join(str(message['total']).replace(",", "-"))
                    new_string = new_string.replace("[", "")
                    new_string = new_string.replace("]", "")
                    new_string = new_string.replace(" ", "")
                    self.total_lineEdit.setText(str(new_string))
        if topic == self._filename_topic:
            self.filename_lineEdit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._mode_topic)
            self._pub_sub_manager.unsubscribe(self, self._freq_band_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            
            return
        