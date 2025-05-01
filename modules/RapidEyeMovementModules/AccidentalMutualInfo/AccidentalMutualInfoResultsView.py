"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the SignalFromEvent plugin
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

from RapidEyeMovementModules.AccidentalMutualInfo.Ui_AccidentalMutualInfoResultsView import Ui_AccidentalMutualInfoResultsView

class AccidentalMutualInfoResultsView( Ui_AccidentalMutualInfoResultsView, QtWidgets.QWidget):
   """
      AccidentalMutualInfoView display the epochs list read
   """
   def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
      super(AccidentalMutualInfoResultsView, self).__init__(*args, **kwargs)
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
         self.ami_distribution = cache['ami_distribution']
         self.ami_threshold = cache['ami_threshold']
         self.p_val = cache['confidence_level']
         self.mean = cache['mean']
         self.std = cache['std']
         self.criteria = cache['criteria']

         self.ami_threshold_lineEdit.setText('{:.3f}'.format(self.ami_threshold))
         self.p_val_lineEdit.setText('{:.3f}'.format(self.p_val))
         self.mean_lineEdit.setText('{:.3f}'.format(self.mean))
         self.std_lineEdit.setText('{:.3f}'.format(self.std))
         self.criteria_lineEdit.setText('{:.3f}'.format(self.criteria))

         # Scatter plot
         self._histogram()

         
      else:
         # When the cache is erased, dont show signals
         self.figure.clear()
         self.canvas.draw()

   def _histogram( self):
      """ 
      Plot scores from mutual information.

      Parameters
      -----------
         ami_distribution: Array
               Array of the different MI find randomly between 2 signals at 
               different time.

      """
      
      # Manage the figure
      self.figure.clear() # reset the hold on 

      #----------------------------------------------------------------------
      # Scatter plot
      gs = self.figure.add_gridspec(2, hspace=0.5)
      ax = gs.subplots(sharex=False, sharey=False)

      color = ("blue")

      # AMI distribution
      ax[0].hist(self.ami_distribution, bins=60, range=None, density=False, weights=None, 
      cumulative=False, bottom=None, histtype='bar', align='mid', 
      orientation='vertical', rwidth=None, log=False, color=color, label=None, 
      stacked=False, data=None)
      ax[0].vlines(x=self.ami_threshold, ymin=0, ymax=ax[0].dataLim.height , linewidth=1.5, color='r', linestyles='--')

      # AMI cumulative distribution
      ax[1].hist(self.ami_distribution, bins=60, range=None, density=False, weights=None, 
      cumulative=True, bottom=None, histtype='bar', align='mid', 
      orientation='vertical', rwidth=None, log=False, color=color, label=None, 
      stacked=False, data=None)
      ax[1].vlines(x=self.ami_threshold, ymin=0, ymax=ax[1].dataLim.height, linewidth=1.5, color='r', linestyles='--')

      # Add title and labels
      self.figure.suptitle('Accidental Mutual Info Score distribution')
      ax[0].grid(True)
      ax[0].set_xlabel('Mutual Info score')
      ax[0].set_ylabel('Occurences')

      ax[1].grid(True)
      ax[1].set_xlabel('Mutual Info score')
      ax[1].set_ylabel('Cumulative occurences')

      # Redraw the figure, needed when the show button is pressed more than once
      self.canvas.draw()