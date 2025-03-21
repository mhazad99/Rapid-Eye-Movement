"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Results viewer of the EOGNormalization plugin
"""
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from qtpy import QtWidgets
from RapidEyeMovementModules.EOGNormalization.Ui_EOGNormalizationResultsView import Ui_EOGNormalizationResultsView

class EOGNormalizationResultsView(Ui_EOGNormalizationResultsView, QtWidgets.QWidget):
    """
        EOGNormalizationResultsView.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(EOGNormalizationResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)
        self.disk_cache = {}

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
            self.channels_list = cache['channels_list']
            self.signals = cache['signals'] #
            # Distribution
            self._histogram()
        else:
            # When the cache is erased, dont show signals
            self.figure.clear()
            self.canvas.draw()


    def _histogram(self):
        """ 
        Plot the baseline distribution of each EOG channel.

        """
        # Manage the figure
        self.figure.clear() # reset the hold on 
        n_chans = len(self.channels_list)
        gs = self.figure.add_gridspec(n_chans, hspace=0.5) 
        ax = gs.subplots(sharex=False, sharey=False)

        for i_eog_chan, channel in enumerate(self.channels_list):
            ax[i_eog_chan].hist(self.signals[i_eog_chan], bins=100, \
                range=None, density=False, weights=None, cumulative=False, bottom=None, \
                histtype='bar', align='mid', orientation='vertical', rwidth=None,\
                log=False, color='b', label=None, stacked=False, data=None)
            mean_value = np.mean(self.signals[i_eog_chan])
            std_value = np.std(self.signals[i_eog_chan])
            ax[i_eog_chan].vlines(x=mean_value, ymin=0, ymax=ax[0].dataLim.height,\
                 linewidth=1.5, color='r', linestyles='-')
            ax[i_eog_chan].vlines(x=mean_value + std_value, ymin=0, ymax=ax[0].dataLim.height,\
                 linewidth=1.5, color='k', linestyles='--')
            ax[i_eog_chan].vlines(x=mean_value - std_value, ymin=0, ymax=ax[0].dataLim.height,\
                 linewidth=1.5, color='k', linestyles='--')

            # Add title and labels
            ax[i_eog_chan].set_title(f'{channel} : R distribution (0.1% to 99.9%) mean={round(mean_value,2)}, std={round(std_value,2)}')
            ax[i_eog_chan].grid(True)
            ax[i_eog_chan].set_xlabel('Samples values')
            ax[i_eog_chan].set_ylabel('Occurences')
            # PLot the distribution from 0.1% to 99.9%
            ax[i_eog_chan].set_xlim(np.percentile(self.signals[i_eog_chan], 0.1),\
                 np.percentile(self.signals[i_eog_chan], 99.9))

        # Redraw the figure, needed when the show button is pressed more than once
        self.canvas.draw()