"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Results viewer of the EOGIntersectionsFinder plugin
"""


import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from qtpy import QtWidgets
from qtpy import QtGui

from widgets.WarningDialog import WarningDialog
from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.SignalsFromEvents.Ui_SignalsFromEventsResultsView import Ui_SignalsFromEventsResultsView

class EOGIntersectionsFinderResultsView(Ui_SignalsFromEventsResultsView, QtWidgets.QWidget):
    """
        EOGIntersectionsFinderResultsView.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(EOGIntersectionsFinderResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

        # Create the figure : https://matplotlib.org/2.1.2/api/axes_api.html
        self.figure = Figure(constrained_layout=False) #To use tight layout
        # Add the figure tool bar
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)    
        # Add the figure into the result_layout
        self.result_layout.addWidget(toolbar)
        self.result_layout.addWidget(self.canvas)   

        self._y_limits = None


    def load_results(self):      

        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if cache is not None:       

            # Get the data needed from the cache
            self.signals = cache['signals']
            self.intersections_df = cache['intersections_df'] 
            #self.min_height_z = cache['min_height_z'] # TODO change this

            # Extract the number of channels
            channel_lst = [signal.channel for signal in self.signals]
            self.n_chan =  len(np.unique(np.array(channel_lst)))

            if not isinstance(self.signals,list):
                self.signals = [self.signals]
            self.signals_events = SignalModel.get_attribute(self.signals, None, 'start_time')
            self.start_events = np.unique(SignalModel.get_attribute(self.signals, 'start_time', 'start_time'), axis=1)
            self.duration_events = np.unique(SignalModel.get_attribute(self.signals, 'duration', 'start_time'), axis=1)

            # Set first window
            self.index = 0
            self.prev_but.setEnabled(False)
            self.start = self.start_events[self.index][0]
            self.duration = self.duration_events[self.index][0]

            # extract events based on the self.start and self.duration
            self._get_intersections()

            # Create a list of SignalModel for all the channels with the selected start_sec from the event
            self.signal_event = self.signals_events[self.index]

            # Update event
            self._update_event_info()

            # Plot first signal
            self._plot_det_info()

            # Desable the button if its impossible to press the button another time.
            self.prev_but.setEnabled(False)
            if self.index + 1 > (len(self.signals_events) - 1):
                self.next_but.setEnabled(False)
            else:
                self.next_but.setEnabled(True)

        else:
            # When the cache is erased, dont show signals
            self.figure.clear()
            self.canvas.draw()

    def _update_event_info( self):

         # Fill info for first signal
        if self.duration>30:
            self.duration_lineEdit.setText(str(30))
        else:
            self.duration_lineEdit.setText(str(self.duration))
        self.event_index_lineEdit.setText(str(self.index))

        # Set the time elapsed
        nhour = int(self.start/3600)
        sec_tmp = self.start-nhour*3600
        nmin = int(sec_tmp/60)
        nsec = self.start-nhour*3600-nmin*60
        time_elapsed = "{0:02d}:{1:02d}:{2:0.2f}".format(nhour,nmin,nsec)
        self.time_lineedit.setText(time_elapsed)


    def on_event_index_changed( self):
        if int(self.event_index_lineEdit.text()) >= 0 and int(self.event_index_lineEdit.text()) <= (len(self.signals_events) - 1):
            self.index = int(self.event_index_lineEdit.text())
            self._on_navigate()
        else:
            self.event_index_lineEdit.setText(str(self.index))
            print("Error index outside of range")


    # Called when the user uncheck/check the checkBox_ylim_norm or finish editing the lineEdit_ylim_fixed
    def y_limits_change_slot(self):
        # The line edit is enabled if the checkBox_ylim_norm is not checked
        self.lineEdit_ylim_fixed.setEnabled(not self.checkBox_ylim_norm.isChecked())
        y_limits = self.lineEdit_ylim_fixed.text()
        # evaluate the string to be number only (no letters)
        try: 
            y_limits = float(y_limits)
            self._y_limits = y_limits
            self._plot_det_info()
        except:
            WarningDialog("Please enter a single number as y-axis limits (symmetric axis)")
            self.lineEdit_ylim_fixed.setText('')
            self._y_limits = None
        

    def _plot_det_info( self):
        """ 
        Plot eeg signal and detection info.
        use self.signal_event : Dictionnary of SignalModel
                A dictionary of channels with SignalModel with properties :
                name:          The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording

        """
        
        # Manage the figure
        self.figure.clear() # reset the hold on 

        #----------------------------------------------------------------------

        # Plot both eeg signal on the same plot
        gs = self.figure.add_gridspec(1, hspace=0)
        ax1 = gs.subplots(sharex=True, sharey=False)

        #for signal in self.signal_event:
        fs = self.signal_event[0].sample_rate
        chan_name = "EOG channels"

        # Extract peaks for the current channel
        # peaks_cur_chan = self.peaks[self.peaks["channel"] == chan_name]

        # Cannot plot too long vector 
        if self.duration > 30:
            duration = 30
            self.signal_event[0].samples = self.signal_event[0].samples[0:int(fs*duration)]
            self.signal_event[1].samples = self.signal_event[1].samples[0:int(fs*duration)]
        else:
            duration = self.duration

        # Define the y-axis limits
        if (not self.checkBox_ylim_norm.isChecked()) and (self._y_limits is not None):
            ylim=[-self._y_limits,self._y_limits]
        else:
            min_value = min([min(signal.samples) for signal in self.signal_event])
            max_value = max([max(signal.samples) for signal in self.signal_event])
            ylim=[min_value, max_value]

        # # Add vertical lines for sec
        # nsec = int(duration)
        # for sec_i in range(nsec):
        #     ax1.vlines(x=sec_i, ymin=ylim[0],ymax=ylim[1], linewidth=0.5, color='k', linestyles='--')      

        # Add horizontal lines at zeros
        ax1.hlines(y=0, xmin=0, xmax=duration, linewidth=0.5, color='k', linestyles='--')

        # Plot the signals
        time_vect = np.linspace(0, duration, num = int(fs*duration))
        ax1.plot(time_vect, self.signal_event[0].samples, 'b', linewidth=1, alpha=0.75)             
        ax1.plot(time_vect, self.signal_event[1].samples, 'r', linewidth=1, alpha=0.75) 

        # Plot the intersections
        # Iterate through the dataframe
        for index, intersection in self.intersections.iterrows():
            ax1.vlines(x=intersection["start_sec"], ymin=ylim[0],ymax=ylim[1], linewidth=1, color='g', linestyles='-')      

        ax1.set_ylabel(chan_name, loc='center', rotation=0, labelpad=30)
        ax1.set_xlabel('time [s]')
        ax1.set_xlim((time_vect[0], time_vect[-1]))
        ax1.set_ylim(ylim)
        if not self.checkBox_display_y.isChecked():
            # Turn off tick labels
            ax1.set_yticklabels([])

        # Redraw the figure, needed when the show button is pressed more than once
        self.canvas.draw()


    def on_next_button( self):
        """A slot called when >> button is pressed by the user.
        The user wants to display the following window.
        """  
        self._on_navigate(next_on=1)


    def on_prev_button( self):
        """A slot called when << button is pressed by the user.
        The user wants to display the previous window.
        """    
        self._on_navigate(next_on=-1)


    def _on_navigate(self, next_on=0):
        ''' Call when the user presses the >>, << or enter after editing the time.
        '''

        # Change index of event
        self.index = self.index + next_on
        self.start = self.start_events[self.index][0]
        self.duration = self.duration_events[self.index][0]

        # Create a list of SignalModel for all the channels with the selected start_sec from the event
        self.signal_event = self.signals_events[self.index]     

        # Extract peaks event that occur in the selected time window
        # Create a list of events self.peaks = [start_sec, amplitude, channel]
        self._get_intersections()

        # Update event
        self._update_event_info()
        
        # Desable the button if its impossible to press the button another time.
        if self.index - 1 < 0:
            self.prev_but.setEnabled(False)
        else:
            self.prev_but.setEnabled(True)
        if self.index + 1 > (len(self.signals_events) - 1):
            self.next_but.setEnabled(False)
        else:
            self.next_but.setEnabled(True)

        # Plot eeg signal.
        self._plot_det_info()


    # Extract intersection event that occur in the selected time window
    # Create a list of events self.intersections = [start_sec]
    def _get_intersections(self):
        intersections = self.intersections_df[(self.intersections_df['start_sec'] >= self.start) &\
             (self.intersections_df['start_sec'] <= (self.start + self.duration))]
        offset_start = intersections['start_sec'] - self.start
        # Convert to pandas data frame
        self.intersections = pd.DataFrame({'start_sec': offset_start})


    def update_y_axis_label_slot(self):
        # Plot eeg signal with the update checkbox to display or not y axis label.
        self._plot_det_info()