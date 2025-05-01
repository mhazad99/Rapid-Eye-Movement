"""
@ Valorisation Recherche HSCM, Societe en Commandite 2024
See the file LICENCE for full license details.

    Results viewer of the EOGBaselineProcess plugin
"""
import numpy as np
import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from qtpy import QtWidgets

from RapidEyeMovementModules.EOGBaselineProcess.Ui_EOGBaselineProcessResultsView import Ui_EOGBaselineProcessResultsView

class EOGBaselineProcessResultsView(Ui_EOGBaselineProcessResultsView, QtWidgets.QWidget):
    """
        EOGBaselineProcessResultsView to display the baseline distribution.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(EOGBaselineProcessResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

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
            self.n_N3_epochs = cache['n_N3_epochs']
            self.channels_list = cache['channels_list']
            self.baseline_stats = cache['baseline_stats'] # N3-mean, N3-std, R-std
            self.baseline_samples = cache['baseline_samples']

            # Distribution
            self._histogram()

        else:
            # When the cache is erased, dont show signals
            self.figure.clear()
            self.canvas.draw()


    def _histogram(self):
        """ 
        Plot the baseline distribution of each EOG channel

        Parameters
        -----------

        """

        # Manage the figure
        self.figure.clear() # reset the hold on 
        n_chans = len(self.channels_list)

        #----------------------------------------------------------------------
        # Scatter plot
        gs = self.figure.add_gridspec(n_chans, hspace=0.5) 
        ax = gs.subplots(sharex=False, sharey=False)

        for i_eog_chan, channel in enumerate(self.channels_list):
            ax[i_eog_chan].hist(self.baseline_samples[channel], bins=60, \
                range=None, density=False, weights=None, cumulative=False, bottom=None, \
                histtype='bar', align='mid', orientation='vertical', rwidth=None,\
                log=False, color='b', label=None, stacked=False, data=None)
            mean_value = self.baseline_stats[channel][0]
            std_value = round(self.baseline_stats[channel][1],2)
            r_std = round(self.baseline_stats[channel][2],2)
            ax[i_eog_chan].vlines(x=mean_value, ymin=0, ymax=ax[0].dataLim.height , linewidth=1.5, color='r', linestyles='-')
            ax[i_eog_chan].vlines(x=mean_value + std_value, ymin=0, ymax=ax[0].dataLim.height , linewidth=1.5, color='k', linestyles='--')
            ax[i_eog_chan].vlines(x=mean_value - std_value, ymin=0, ymax=ax[0].dataLim.height , linewidth=1.5, color='k', linestyles='--')
            # Write on the plot the std value (std_value) in green color on a white background
            ax[i_eog_chan].text(std_value, ax[0].dataLim.height/2, f'{std_value}', ha='center', va='center', fontsize=10, color='g', backgroundcolor='w')

            # Add title and labels
            if self.n_N3_epochs>1:
                ax[i_eog_chan].set_title(f'{channel} : N3 distribution (0.1% to 99.9%) ({self.n_N3_epochs} epochs) (stage R std={r_std})')
            else:
                ax[i_eog_chan].set_title(f'{channel} : R distribution (0.1% to 99.9%) (stage R std={r_std})')
            ax[i_eog_chan].grid(True)
            ax[i_eog_chan].set_xlabel('Samples values')
            ax[i_eog_chan].set_ylabel('Occurences')
            # PLot the distribution from 0.1% to 99.9%
            ax[i_eog_chan].set_xlim(np.percentile(self.baseline_samples[channel], 0.1),np.percentile(self.baseline_samples[channel], 99.9))
            

        # Redraw the figure, needed when the show button is pressed more than once
        self.canvas.draw()