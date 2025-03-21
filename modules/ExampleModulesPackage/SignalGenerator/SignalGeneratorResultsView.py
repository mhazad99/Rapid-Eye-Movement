"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Results viewer of the SignalGenerator plugin
"""
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
from qtpy import QtWidgets

from ExampleModulesPackage.SignalGenerator.Ui_SignalGeneratorResultsView import Ui_SignalGeneratorResultsView

class SignalGeneratorResultsView(Ui_SignalGeneratorResultsView, QtWidgets.QWidget):
    """
        SignalGeneratorResultsView nohting to show.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(SignalGeneratorResultsView, self).__init__(*args, **kwargs)
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
        # discards the old graph
        self.figure.clear() # reset the hold on 
        
         # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
        
        if cache is not None:
            fs = int(cache['sample_rate'])
            signal_length = len(cache['samples'])
            x = np.linspace(0, signal_length/fs, num=signal_length)

            # create an axis
            ax1 = self.figure.add_subplot(111)
            ax1.plot(x, cache['samples'],  label='Signal', 
                                            color=[0.25, 0.25, 0.25], 
                                            linewidth=1)
            ax1.set_ylabel('µV')
            ax1.set_title('Signal generated')
            ax1.grid()

        # refresh canvas
        self.canvas.draw()