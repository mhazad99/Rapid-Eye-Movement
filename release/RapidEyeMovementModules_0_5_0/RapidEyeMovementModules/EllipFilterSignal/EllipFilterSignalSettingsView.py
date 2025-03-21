"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the EllipFilterSignal plugin
"""

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.ticker as mticker
import numpy as np
import random
from scipy import signal
import traceback

from qtpy import QtWidgets
from qtpy import QtGui
from qtpy import QtCore
from qtpy.QtGui import QRegExpValidator # To validate what the user enters in the interface
from qtpy.QtCore import QRegExp # To validate what the user enters in the interface
from qtpy.QtWidgets import QMessageBox

from RapidEyeMovementModules.EllipFilterSignal.Ui_EllipFilterSignalSettingsView import Ui_EllipFilterSignalSettingsView
from Managers.PubSubManager import PubSubManager
from commons.BaseSettingsView import BaseSettingsView

class EllipFilterSignalSettingsView( BaseSettingsView,  Ui_EllipFilterSignalSettingsView, QtWidgets.QWidget):
    """
        EllipFilterSignalView
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self.freq_resp_figure = None

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node
        self._cutoff_topic = f'{self._parent_node.identifier}.cutoff'
        self._pub_sub_manager.subscribe(self, self._cutoff_topic)
        self._type_topic = f'{self._parent_node.identifier}.type'
        self._pub_sub_manager.subscribe(self, self._type_topic)
        self._IIR_topic = f'{self._parent_node.identifier}.IR_family'
        self._pub_sub_manager.subscribe(self, self._IIR_topic)        
        self._order_topic = f'{self._parent_node.identifier}.order'
        self._pub_sub_manager.subscribe(self, self._order_topic)
        self._window_topic = f'{self._parent_node.identifier}.window'
        self._pub_sub_manager.subscribe(self, self._window_topic)
        self._ellip_param_topic = f'{self._parent_node.identifier}.ellip_params'
        self._pub_sub_manager.subscribe(self, self._ellip_param_topic)

        # Update figures
        self.init_figures()
        self.update_std_order()
        self.update_frequency_response()

        self.ellip_param = {}
        self.ellip_param['filter_family']='butter'
        self.ellip_param['pb_ripple_dB']= 1.0
        self.ellip_param['stopband_dB']= 6.0
        self.ellip_param['stopband_Hz']= [0.1, 120]


    def init_figures(self):
        self.freq_resp_figure = Figure()
        self.freq_resp_canvas = FigureCanvas(self.freq_resp_figure)
        freq_resp_toolbar = NavigationToolbar(self.freq_resp_canvas, self)
        # set the layout
        self.freq_resp_layout.addWidget(freq_resp_toolbar)
        self.freq_resp_layout.addWidget(self.freq_resp_canvas)
        # create an axis
        self.freq_resp_ax = self.freq_resp_figure.add_subplot(111)
        self.phase_resp_ax = self.freq_resp_ax.twinx()
        self.freq_resp_figure.subplots_adjust(bottom=0.20)


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._cutoff_topic, 'ping')
        self._pub_sub_manager.publish(self, self._type_topic, 'ping')
        self._pub_sub_manager.publish(self, self._IIR_topic, 'ping')
        self._pub_sub_manager.publish(self, self._order_topic, 'ping')
        self._pub_sub_manager.publish(self, self._window_topic, 'ping')
        self._pub_sub_manager.publish(self, self._ellip_param_topic, 'ping')
        self.update_frequency_response()


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        # Send the settings to the publisher for inputs to CsvReaderMaster
        self._pub_sub_manager.publish(self, self._cutoff_topic, \
            str(self.cutoff_lineedit.text()))
        self._pub_sub_manager.publish(self, self._type_topic, \
            str(self.type_combobox.currentText()))
        self._pub_sub_manager.publish(self, self._IIR_topic, \
            str(self.IR_comboBox.currentText()))
        if self.IR_comboBox.currentText()=="IIR":
            self._pub_sub_manager.publish(self, self._order_topic, \
                str(self.iir_order_lineEdit.text()))
        else:
            self._pub_sub_manager.publish(self, self._order_topic, \
                str(self.custom_order_lineedit.text()))       
        self._pub_sub_manager.publish(self, self._window_topic, \
            str(self.window_combobox.currentText()))
        if self.ellip_param is not None:
            self._pub_sub_manager.publish(self, self._ellip_param_topic, \
               self.ellip_param)


    def on_order_type_changed(self):
        print("on_order_type_changed")
        if self.custom_radiobutton.isChecked():
            self.custom_order_lineedit.setEnabled(True)
            self.std_order_lineedit.setEnabled(False)
        else:
            self.custom_order_lineedit.setEnabled(False)
            self.std_order_lineedit.setEnabled(True)
            self.update_std_order()
        self._pub_sub_manager.publish(self, 
            f"{self._parent_node.identifier}.use_std_order", 
            str(self.sleep_std_radiobutton.isChecked()))
        self.update_frequency_response()


    # Called by the publisher to init settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        # All lineEdit
        if topic == self._cutoff_topic:
            self.cutoff_lineedit.setText(message)
        if topic == self._type_topic:
            self.type_combobox.setCurrentText(message)
        if topic == self._IIR_topic:
            self.IR_comboBox.setCurrentText(message)
        if topic == self._order_topic:
            if self.IR_comboBox.currentText()=="IIR":
                self.iir_order_lineEdit.setText(message)
            else:
                if self.custom_radiobutton.isChecked():
                    self.custom_order_lineedit.setText(message)
                else:
                    self.custom_order_lineedit.setText(message)
        if topic == self._window_topic:
            self.window_combobox.setCurrentText(message)
        if topic == self._ellip_param_topic:
            if isinstance(message, str) and message != "":
                message = eval(message)
            if isinstance(message, dict):
                self.ellip_param = message
                # Update the UI
                self.update_UI_ellip_params()


    def on_settings_changed(self):

        if self.IR_comboBox.currentText()=="IIR":

            if self.radioButton_butter.isChecked():
                # Turn off FIR settings
                self.window_combobox.setEnabled(False)
                self.sleep_std_radiobutton.setEnabled(False)
                self.custom_radiobutton.setEnabled(False)
                self.std_order_lineedit.setEnabled(False)
                self.custom_order_lineedit.setEnabled(False)
                # Turn on IIR settings for butter
                self.iir_order_lineEdit.setEnabled(True)
                self.textEdit.setEnabled(True)
                # Turn off IIR settings for ellip
                self.lineEdit_stopHz.setEnabled(False)
                self.doubleSpinBox_stopdB.setEnabled(False)
                self.doubleSpinBox_maxripple.setEnabled(False)
                self.ellip_param['filter_family']='butter'

            if self.radioButton_ellip.isChecked():
                # Turn off FIR settings
                self.window_combobox.setEnabled(False)
                self.sleep_std_radiobutton.setEnabled(False)
                self.custom_radiobutton.setEnabled(False)
                self.std_order_lineedit.setEnabled(False)
                self.custom_order_lineedit.setEnabled(False)
                # Turn off IIR settings for butter
                self.iir_order_lineEdit.setEnabled(False)
                self.textEdit.setEnabled(False)
                # Turn on IIR settings for ellip
                self.ellip_param['filter_family']='ellip'
                self.lineEdit_stopHz.setEnabled(True)
                self.doubleSpinBox_stopdB.setEnabled(True)
                self.doubleSpinBox_maxripple.setEnabled(True)
                self.ellip_param['stopband_dB']=self.doubleSpinBox_stopdB.value()
                map_object = map(float, self.lineEdit_stopHz.text().split())
                stop_freqs = list(map_object)
                self.ellip_param['stopband_Hz']=stop_freqs
                self.ellip_param['pb_ripple_dB']=self.doubleSpinBox_maxripple.value()
        else:
            # Turn on FIR settings
            self.window_combobox.setEnabled(True)
            self.sleep_std_radiobutton.setEnabled(True)
            self.custom_radiobutton.setEnabled(True)
            self.std_order_lineedit.setEnabled(True)
            self.custom_order_lineedit.setEnabled(True)
            # Turn off IIR settings
            self.iir_order_lineEdit.setEnabled(False)
            self.textEdit.setEnabled(False)
            self.doubleSpinBox_stopdHz.setEnabled(False)
            self.doubleSpinBox_stopdB.setEnabled(False)
            self.doubleSpinBox_maxripple.setEnabled(False)
            self.ellip_param['filter_family']='FIR'

        self.update_std_order()
        self.update_frequency_response()


    def update_UI_ellip_params(self):
        if self.ellip_param['filter_family']=='butter':
            self.radioButton_butter.setChecked(True)
            # Turn off FIR settings
            self.window_combobox.setEnabled(False)
            self.sleep_std_radiobutton.setEnabled(False)
            self.custom_radiobutton.setEnabled(False)
            self.std_order_lineedit.setEnabled(False)
            self.custom_order_lineedit.setEnabled(False)
            # Turn on IIR settings for butter
            self.iir_order_lineEdit.setEnabled(True)
            self.textEdit.setEnabled(True)
            # Turn off IIR settings for ellip
            self.lineEdit_stopHz.setEnabled(False)
            self.doubleSpinBox_stopdB.setEnabled(False)
            self.doubleSpinBox_maxripple.setEnabled(False)

        elif self.ellip_param['filter_family']=='ellip':
            self.radioButton_ellip.setChecked(True)
            # Turn off FIR settings
            self.window_combobox.setEnabled(False)
            self.sleep_std_radiobutton.setEnabled(False)
            self.custom_radiobutton.setEnabled(False)
            self.std_order_lineedit.setEnabled(False)
            self.custom_order_lineedit.setEnabled(False)
            # Turn off IIR settings for butter
            self.iir_order_lineEdit.setEnabled(False)
            self.textEdit.setEnabled(False)
            # Turn on IIR settings for ellip
            self.lineEdit_stopHz.setEnabled(True)
            self.doubleSpinBox_stopdB.setEnabled(True)
            self.doubleSpinBox_maxripple.setEnabled(True)
            self.doubleSpinBox_stopdB.setValue(self.ellip_param['stopband_dB'])
            # convert the list to a string with items separated by spaces
            if isinstance(self.ellip_param['stopband_Hz'],list):
                stop_freqs_str = ' '.join(map(str, self.ellip_param['stopband_Hz']))
            elif isinstance(self.ellip_param['stopband_Hz'],float):
                stop_freqs_str = str(self.ellip_param['stopband_Hz'])
            else:
                stop_freqs_str = self.ellip_param['stopband_Hz']
            self.lineEdit_stopHz.setText(stop_freqs_str)
            self.doubleSpinBox_maxripple.setValue(self.ellip_param['pb_ripple_dB'])

        else:
            # Turn on FIR settings
            self.window_combobox.setEnabled(True)
            self.sleep_std_radiobutton.setEnabled(True)
            self.custom_radiobutton.setEnabled(True)
            self.std_order_lineedit.setEnabled(True)
            self.custom_order_lineedit.setEnabled(True)
            # Turn off IIR settings
            self.iir_order_lineEdit.setEnabled(False)
            self.textEdit.setEnabled(False)
            self.doubleSpinBox_stopdHz.setEnabled(False)
            self.doubleSpinBox_stopdB.setEnabled(False)
            self.doubleSpinBox_maxripple.setEnabled(False)
        

    def on_topic_update(self, topic, message, sender):
        pass


    # Call to compute and edit the standard slepe order filter.
    def update_std_order(self):
        sample_rate = int(self.sample_rate_lineedit.text())
        map_object = map(float, self.cutoff_lineedit.text().split())
        freqs = list(map_object)
        self.std_order_lineedit.setText(str(int(5*sample_rate/freqs[0])))


    def update_frequency_response(self):
        try:
            # Create the filter in order to get its frequency response
            map_object = map(float, self.cutoff_lineedit.text().split())
            freqs = list(map_object)

            window = self.window_combobox.currentText()
            filter_type = self.type_combobox.currentText()
            IR_family = self.IR_comboBox.currentText()
            sample_rate = int(self.sample_rate_lineedit.text())

            if self.IR_comboBox.currentText()=="IIR":
                order = int(self.iir_order_lineEdit.text())
            else:
                if self.custom_radiobutton.isChecked():
                    order = int(self.custom_order_lineedit.text())
                else:
                    order = int(self.std_order_lineedit.text())

            # Compute frequency axis
            worN = np.linspace(0, sample_rate/2, 512)

            if IR_family=="IIR":
                
                if self.radioButton_butter.isChecked():
                    # Second-order sections representation of the IIR filter
                    sos = signal.butter(int(order), freqs,\
                        btype=filter_type, output='sos', fs=sample_rate)
                    # Get the frequency response
                    w, h = signal.sosfreqz(sos, worN=worN, fs=sample_rate)
                if self.radioButton_ellip.isChecked():
                    # Compute the min oder
                    # pass band frequency
                    nyquist = sample_rate/2
                    wp = np.array(freqs)/nyquist
                    if len(wp) == 1:
                        wp = wp[0]
                    # stop band frequency
                    map_object = map(float, self.lineEdit_stopHz.text().split())
                    ws = list(map_object)
                    ws = np.array(ws)/(sample_rate/2)
                    if len(ws) == 1:
                        ws = ws[0]
                    # bandpass ripple
                    rp = self.doubleSpinBox_maxripple.value()
                    # stop band attenuation
                    rs = self.doubleSpinBox_stopdB.value()
                    [order_min, wn] = signal.ellipord(wp, ws, rp, rs)
                    b, a = signal.ellip(int(order_min), rp=rp, rs=rs, Wn=wn, \
                        btype=filter_type, output='ba')
                    # Get the frequency response
                    w, h = signal.freqz(b, a, worN=worN, fs=sample_rate)
                    #sos = signal.ellip(int(order_min), rp=rp, rs=rs, Wn=wn, \
                    #     btype=filter_type, output='sos')
                    # Get the frequency response
                    #w, h = signal.sosfreqz(sos, worN=worN, fs=sample_rate)

            else:
                # cutoff : between 0 and fs/2
                taps = signal.firwin(int(order), 
                        freqs, 
                        window=window, 
                        pass_zero=filter_type,
                        fs=sample_rate)
                # Get the frequency response
                w, h = signal.freqz(taps,worN=worN,fs=sample_rate)

            # ----------------------------
            # Plot the frequency response
            # ----------------------------
            # discards the old graph
            self.freq_resp_ax.clear()
            self.phase_resp_ax.clear()
            self.freq_resp_ax.set_title('Filter frequency response')
            #self.phase_resp_ax = self.freq_resp_ax.twinx()

            if "dB" in self.freq_resp_unit_comboBox.currentText():
                # Plot Attenuation
                # The maximum value is taken to avoid error on log(0)
                self.freq_resp_ax.plot(w, 20 * np.log10(np.maximum(abs(h),1e-5)), 'b')
                self.freq_resp_ax.set_ylabel('Attenuation (dB)', color='b')
            elif "%" in self.freq_resp_unit_comboBox.currentText():
                # Plot Amplitude
                self.freq_resp_ax.plot(w, abs(h)*100, 'b')
                self.freq_resp_ax.set_ylabel('Amplitude (%)', color='b')

            self.freq_resp_ax.set_xlabel('Frequency (Hz)')
            self.freq_resp_ax.grid()

            # Plot phase delay
            #self.phase_resp_ax.clear()
            angles = np.unwrap(np.angle(h))
            self.phase_resp_ax.plot(w, angles, 'g')
            # set y label on the right side of the graph
            #self.phase_resp_ax.set_ylabel('Angle (radians)', color='g', labelpad=20, rotation=270, position=(1,1))
            self.phase_resp_ax.set_ylabel('Angle (radians)', color='g')

            # refresh canvas
            self.freq_resp_canvas.draw()

        except ValueError as value_error:
            log_msg = QMessageBox()
            log_msg.setWindowTitle("Log Message")
            if "Digital filter critical frequencies" in str(value_error.args[0]):
                log_msg.setText(\
                    "The Sample Rate has to be at least 2 times the highest Cutoff frequency of the filter.\n\n"\
                    "The Sample Rate in the Settings View must be the same as the one used in your PSG files "\
                        "to define a valid filter for your analysis.")
            elif "Must specify a single critical frequency" in str(value_error.args[0]):
                log_msg.setText(\
                    "You must specify a single Cutoff value for a lowpass or highpass filter.\n\n"\
                    "Ex) 0.3 for an highpass or 100 for a lowpass.")
            elif "specify start and stop frequencies" in str(value_error.args[0]):
                log_msg.setText(\
                    "You must specify start and stop frequencies for the Cutoff values of the bandpass or bandstop filter.\n\n"\
                    "Ex) 0.3 100 for a bandpass or 59 61 for a bandstop.")
            else:
                log_msg.setText(value_error.args[0])
            log_msg.setIcon(QMessageBox.Critical)
            log_msg.exec_()
            print(value_error)
        except Exception as err:
            log_msg = QMessageBox()
            log_msg.setWindowTitle("Log Message")
            log_msg.setText(str(type(err))+':'+ err.args[0])
            log_msg.setIcon(QMessageBox.Critical)
            log_msg.exec_()
            print(type(err))
            print(err)
            traceback.print_exc()
    

    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._cutoff_topic)
            self._pub_sub_manager.unsubscribe(self, self._type_topic)
            self._pub_sub_manager.unsubscribe(self, self._IIR_topic)
            self._pub_sub_manager.unsubscribe(self, self._order_topic)
            self._pub_sub_manager.unsubscribe(self, self._window_topic)