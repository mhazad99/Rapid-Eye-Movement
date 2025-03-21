"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Results viewer of the AddSignals plugin
"""
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

from qtpy import QtWidgets
from qtpy.QtWidgets import QScrollArea
from ExampleModulesPackage.AddSignals.Ui_AddSignalsResultsView import Ui_AddSignalsResultsView

class AddSignalsResultsView(Ui_AddSignalsResultsView, QtWidgets.QWidget):
    """
        AddSignalsResultsView nohting to show.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(AddSignalsResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

        # Init figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        self.result_layout.addWidget(toolbar)
        self.result_layout.addWidget(self.canvas)


    def load_results(self):
        def create_sub_plot(samples, sample_rate, subplot, title):
            """
            Creates a subplot with a specified title and plots the given samples.
            Parameters:
                samples (array-like): The samples to be plotted.
                sample_rate (float): The sample rate of the signal.
                subplot (int): The subplot number.
                title (str): The title of the subplot.
            Returns:
                None
            """
            fs = sample_rate
            signal_length = len(samples)
            x = np.linspace(0, signal_length/fs, num=signal_length)

            # create an axis
            ax1 = self.figure.add_subplot(subplot)
            ax1.plot(x, samples,  label=title, 
                                            linewidth=1)
            ax1.set_xlabel('Samples')
            ax1.set_ylabel('Amplitude')
            ax1.legend(loc='upper right')
            #ax1.set_title(title)
            ax1.grid()

        # discards the old graph
        self.figure.clear() # reset the hold on 
        
         # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
        
        if cache is not None:
            create_sub_plot(cache['samples1'], cache['sample_rate'], 311, 'Signal 1')
            create_sub_plot(cache['samples2'], cache['sample_rate'], 312, 'Signal 2')
            create_sub_plot(cache['output_samples'], cache['sample_rate'], 313, 'Output signal')

            # refresh canvas
            self.canvas.draw()