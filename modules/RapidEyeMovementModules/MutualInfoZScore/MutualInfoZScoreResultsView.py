"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the MutualInfoZScore plugin
"""

import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

from qtpy import QtWidgets
from qtpy import QtGui

from CEAMSModules.PSGReader.SignalModel import SignalModel
from RapidEyeMovementModules.MutualInfoZScore.Ui_MutualInfoZScoreResultsView import Ui_MutualInfoZScoreResultsView

class MutualInfoZScoreResultsView( Ui_MutualInfoZScoreResultsView, QtWidgets.QWidget):
   """
      MutualInfoZScoreView display the epochs_to_process list read
   """
   def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
      super(MutualInfoZScoreResultsView, self).__init__(*args, **kwargs)
      self._parent_node = parent_node
      self._pub_sub_manager = pub_sub_manager
      self._cache_manager = cache_manager

      self.filename = ''
      self.disk_cache = {}

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

   def load_results(self):      

      # Clear the cache from the loaded file, usefull for the second run
      self.disk_cache = {}

      # Read result cache
      cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

      if cache is not None:       
         # Get the data needed from the cache
         z_values = cache['z_values']
         self.criteria_lst = cache['criteria']
         self.z_values_events = SignalModel.get_attribute(z_values, None, 'start_time')
         self.start_events = np.unique(SignalModel.get_attribute(z_values, 'start_time', 'start_time'), axis=1)
         self.duration_events = np.unique(SignalModel.get_attribute(z_values, 'duration', 'start_time'), axis=1)

         # Set first window
         self.index = 0
         self.prev_but.setEnabled(False)
         self.z_value = self.z_values_events[self.index]
         self.start = self.start_events[self.index][0]
         self.duration = self.duration_events[self.index][0]
         if isinstance(self.criteria_lst, str) and self.criteria_lst == '':
             self.criteria=''
         else:
            self.criteria = self.criteria_lst[self.index]

         # Update event
         self._update_event_info()

         # Scatter plot
         self._scatter_score()

         
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
      if int(self.event_index_lineEdit.text()) >= 0 and int(self.event_index_lineEdit.text()) <= (len(self.z_values_events) - 1):
         self.index = int(self.event_index_lineEdit.text())
         self._on_navigate()
      else:
         self.event_index_lineEdit.setText(str(self.index))
         print("Error index outside of range")


   def _scatter_score(self):
      """ 
      Plot scores from mutual information.

      Parameters
      -----------
         scores    : List
               List of all the mutual information score by epoch and by event

      """
      # Manage the figure
      self.figure.clear() # reset the hold on 
      #----------------------------------------------------------------------
      # Scatter plot
      ax = self.figure.add_subplot(1, 1, 1)
      y_vect = np.array([score.meta['z_value'] for score in self.z_value])
      x_vect = range(self.z_value.shape[0])
      ax.scatter(x_vect, y_vect, alpha=0.8, edgecolors='none', s=30)
      if isinstance(self.criteria, str) and self.criteria == '':
         pass
      else:
         label = "criteria = " + str(round(self.criteria,2))
         ax.hlines(y=self.criteria, xmin=0, xmax=max(x_vect) , linewidth=1.5, color='r', linestyles='--', label=label)

      # Add title
      self.figure.suptitle('Z value by event')

      ax.set_xticks(x_vect)
      ax.grid(True)
      ax.set_xlabel('Signal number')
      ax.set_ylabel('Z value')
      # ax.legend(loc='lower right')

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
      self.z_value = self.z_values_events[self.index]
      self.start = self.start_events[self.index][0]
      self.duration = self.duration_events[self.index][0]
      if isinstance(self.criteria_lst, str) and self.criteria_lst == '':
            self.criteria=''
      else:
         self.criteria = self.criteria_lst[self.index]

      # Update event
      self._update_event_info()
      
      # Desable the button if its impossible to press the button another time.
      if self.index - 1 < 0:
         self.prev_but.setEnabled(False)
      else:
         self.prev_but.setEnabled(True)
      if self.index + 1 > (len(self.z_values_events) - 1):
         self.next_but.setEnabled(False)
      else:
         self.next_but.setEnabled(True)

      # Scatter plot
      self._scatter_score()
