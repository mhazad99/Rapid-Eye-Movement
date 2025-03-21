"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the SignalGenerator plugin
"""

import math
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
from qtpy import QtWidgets

from ExampleModulesPackage.SignalGenerator.Ui_SignalGeneratorSettingsView import Ui_SignalGeneratorSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SignalGeneratorSettingsView(BaseSettingsView, Ui_SignalGeneratorSettingsView, QtWidgets.QWidget):
    """
        SignalGeneratorView set the SignalGenerator settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self.init_figures()

        # Subscribe to the proper topics to send/get data from the node
        self._duration_topic = f'{self._parent_node.identifier}.duration'
        self._pub_sub_manager.subscribe(self, self._duration_topic)
        self._sample_rate_topic = f'{self._parent_node.identifier}.sample_rate'
        self._pub_sub_manager.subscribe(self, self._sample_rate_topic)
        self._frequency_topic = f'{self._parent_node.identifier}.frequency'
        self._pub_sub_manager.subscribe(self, self._frequency_topic)
        self._amplitude_topic = f'{self._parent_node.identifier}.amplitude'
        self._pub_sub_manager.subscribe(self, self._amplitude_topic)
        self._phase_topic = f'{self._parent_node.identifier}.phase'
        self._pub_sub_manager.subscribe(self, self._phase_topic)


    def init_figures(self):
        
        self.freq_resp_figure = Figure()
        self.freq_resp_canvas = FigureCanvas(self.freq_resp_figure)
        #freq_resp_toolbar = NavigationToolbar(self.freq_resp_canvas, self)
        # set the layout
        #self.figure_layout.addWidget(freq_resp_toolbar)
        self.figure_layout.addWidget(self.freq_resp_canvas)
        # create an axis
        self.freq_resp_ax = self.freq_resp_figure.add_subplot(111)
        self.phase_resp_ax = self.freq_resp_ax.twinx()
        self.freq_resp_figure.subplots_adjust(bottom=0.20)


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._duration_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sample_rate_topic, 'ping')
        self._pub_sub_manager.publish(self, self._frequency_topic, 'ping')
        self._pub_sub_manager.publish(self, self._amplitude_topic, 'ping')
        self._pub_sub_manager.publish(self, self._phase_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        # Send the settings to the publisher for inputs to SignalGenerator
        self._pub_sub_manager.publish(self, self._duration_topic, str(self.duration_lineedit.text()))
        self._pub_sub_manager.publish(self, self._sample_rate_topic, str(self.sample_rate_lineedit.text()))
        self._pub_sub_manager.publish(self, self._frequency_topic, str(self.frequency_lineedit.text()))
        self._pub_sub_manager.publish(self, self._amplitude_topic, str(self.amplitude_lineedit.text()))
        self._pub_sub_manager.publish(self, self._phase_topic, str(self.phase_spinBox.value()))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._duration_topic:
            self.duration_lineedit.setText(message)
        if topic == self._sample_rate_topic:
            self.sample_rate_lineedit.setText(message)
        if topic == self._frequency_topic:
            self.frequency_lineedit.setText(message)
        if topic == self._amplitude_topic:
            self.amplitude_lineedit.setText(message)
        if topic == self._phase_topic:
            self.phase_spinBox.setValue(int(message))

        self._update_signal_values()
        self._update_signal_plot()
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._duration_topic)
            self._pub_sub_manager.unsubscribe(self, self._sample_rate_topic)
            self._pub_sub_manager.unsubscribe(self, self._frequency_topic)
            self._pub_sub_manager.unsubscribe(self, self._amplitude_topic)
            self._pub_sub_manager.unsubscribe(self, self._phase_topic)
    
    ## Private functions
    def _update_signal_values(self):
        try:
            self._duration = int(self.duration_lineedit.text())
            self._sample_rate = int(self.sample_rate_lineedit.text())
            self._frequency = float(self.frequency_lineedit.text())
            self._amplitude = float(self.amplitude_lineedit.text())
            phase_degrees = self.phase_spinBox.value()
            self._phase_radians = math.radians(phase_degrees)
        except ValueError:
            self._is_valid = False
        else:
            self._is_valid = True

    def _update_signal_plot(self):
        if not self._is_valid:
            return
        # Generate the signal based on the parameter values
        time = np.linspace(0, self._duration, int(self._duration * self._sample_rate), endpoint=False)
        signal = self._amplitude * np.sin(2 * np.pi * self._frequency * time + self._phase_radians)

        # Clear the previous plot
        self.freq_resp_ax.clear()

        # Plot the signal
        self.freq_resp_ax.plot(time, signal)
        self.freq_resp_ax.set_xlabel('Time')
        self.freq_resp_ax.set_ylabel('Amplitude')
        self.freq_resp_ax.set_title('Generated Signal')

        # Redraw the figure
        self.freq_resp_canvas.draw()

    ## Slots
    def duration_changed(self):
        self._update_signal_values()
        self._update_signal_plot()

    def sample_rate_changed(self):
        self._update_signal_values()
        self._update_signal_plot()

    def frequency_changed(self):
        self._update_signal_values()
        self._update_signal_plot()

    def amplitude_changed(self):
        self._update_signal_values()
        self._update_signal_plot()

    def phase_changed(self):
        self._update_signal_values()
        self._update_signal_plot()
        