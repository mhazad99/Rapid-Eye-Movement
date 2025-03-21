"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    Results viewer of the SpectralPower plugin
"""

from qtpy import QtWidgets
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

from RapidEyeMovementModules.SpectralPower.Ui_SpectralPowerResultsView import Ui_SpectralPowerResultsView

class SpectralPowerResultsView(Ui_SpectralPowerResultsView, QtWidgets.QWidget):
    """
        SpectralPowerResultsView nohting to show.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(SpectralPowerResultsView, self).__init__(*args, **kwargs)
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

    def load_results(self):
        # Clear the cache from the loaded file, usefull for the second run
        self.disk_cache = {}

        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if cache is not None:       
            # Get the data needed from the cache
            self.chan_spec = cache['chan_spec']
            self.band_key = cache['band_key']

            if 'delta' in self.band_key:
                self.delta_checkBox.setVisible(True)
                self.delta_checkBox.setChecked(True)
            else:
                self.delta_checkBox.setVisible(False)
                self.delta_checkBox.setChecked(False)
            if 'theta' in self.band_key:
                self.theta_checkBox.setVisible(True)
                self.theta_checkBox.setChecked(True)
            else:
                self.theta_checkBox.setVisible(False)
                self.theta_checkBox.setChecked(False)
            if 'alpha' in self.band_key:
                self.alpha_checkBox.setVisible(True)
                self.alpha_checkBox.setChecked(True)
            else:
                self.alpha_checkBox.setVisible(False)
                self.alpha_checkBox.setChecked(False)
            if 'beta' in self.band_key:
                self.beta_checkBox.setVisible(True)
                self.beta_checkBox.setChecked(True)
            else:
                self.beta_checkBox.setVisible(False)
                self.beta_checkBox.setChecked(False)
            if 'gamma' in self.band_key:
                self.gamma_checkBox.setVisible(True)
                self.gamma_checkBox.setChecked(True)
            else:
                self.gamma_checkBox.setVisible(False)
                self.gamma_checkBox.setChecked(False)
            if 'other' in self.band_key:
                self.other_checkBox.setVisible(True)
                self.other_checkBox.setChecked(True)
            else:
                self.other_checkBox.setVisible(False)
                self.other_checkBox.setChecked(False)

            # Scatter plot
            self.scatter_plot()

            self.canvas.draw()

                
        else:
            # When the cache is erased, dont show signals
            self.figure.clear()
            self.canvas.draw()

    def scatter_plot( self):
        """ 
        Plot features in n dimension with labels.
        """
        
        # Manage the figure
        self.figure.clear() # reset the hold on

        nb_graph = self.delta_checkBox.isChecked() + self.theta_checkBox.isChecked() +\
                    self.alpha_checkBox.isChecked() + self.beta_checkBox.isChecked() +\
                    self.gamma_checkBox.isChecked() + self.other_checkBox.isChecked()

        used = []
        if self.delta_checkBox.isChecked():
            used.append('delta')
        if self.theta_checkBox.isChecked():
            used.append('theta')
        if self.alpha_checkBox.isChecked():
            used.append('alpha')
        if self.beta_checkBox.isChecked():
            used.append('beta')
        if self.gamma_checkBox.isChecked():
            used.append('gamma')
        if self.other_checkBox.isChecked():
            used.append('other')
        
        frontal = ['F3', 'F4', 'F7', 'F8', 'Fz']
        central = ['C3', 'C4', 'Cz']
        parietal = ['P3', 'P4', 'Pz']
        occipital = ['O1', 'O2']
        temporal = ['T3', 'T4', 'T5', 'T6']

        compare_power = any(char.isdigit() for word in self.band_key for char in word)
        y_max = np.max(np.max(self.chan_spec))
        y_min = np.min(np.min(self.chan_spec))

        self.ax = self.figure.subplots(nb_graph, 5, sharex=False, sharey=False, gridspec_kw={'hspace': 0.1, 'wspace': 0.2})

        # Plot in the good ax
        for chan in self.chan_spec.index:
            ax_row = 0
            for band_power, value in self.chan_spec.loc[chan].items():
                if not any(char.isdigit() for char in band_power) and (band_power in used):
                    if compare_power:
                        x_val = np.array([0.25, 0.75])
                        idx_2 = np.where(self.chan_spec.loc[chan].index == band_power + '2')[0]
                        y_val = np.array([value, self.chan_spec.loc[chan][idx_2][0]])
                    else:
                        x_val = 0.5
                        y_val = value

                    if any([electrode in chan for electrode in frontal]):
                        ax_col = 0
                    elif any([electrode in chan for electrode in central]):
                        ax_col = 1
                    elif any([electrode in chan for electrode in parietal]):
                        ax_col = 2
                    elif any([electrode in chan for electrode in occipital]):
                        ax_col = 3
                    elif any([electrode in chan for electrode in temporal]):
                        ax_col = 4
                    else:
                        print('Chan not in setup')
                    if nb_graph > 1:
                        self.ax[ax_row, ax_col].plot(x_val, y_val, ls='-', marker='o', label=chan)
                        self.ax[ax_row, ax_col].set_ylim([y_min, y_max])
                    else:
                        self.ax[ax_col].plot(x_val, y_val, ls='-', marker='o', label=chan)
                        self.ax[ax_col].set_ylim([y_min, y_max])
                    
                    ax_row += 1
        
        row_headers = [spec.upper() for spec in self.chan_spec if not any(char.isdigit() for char in spec)]
        col_headers = ['FRONTAL', 'CENTRAL', 'PARIETAL', 'OCCIPITAL', 'TEMPORAL']
        font_kwargs = dict(fontfamily="monospace", fontweight="bold", fontsize="large")
        self.add_headers(self.figure, col_headers=col_headers, row_headers=row_headers, **font_kwargs)
        plt.setp(self.ax, xticks=[])
        # handles, labels = self.ax[-1,-1].get_legend_handles_labels()
        # self.figure.legend(handles, labels, loc='upper center')
        self.figure.legend(labels=self.chan_spec.index, loc="center right",borderaxespad=0.1,title="Channels")
        self.canvas.draw()

    def add_headers(self,fig,*,row_headers=None,col_headers=None,row_pad=1,col_pad=5,\
                    rotate_row_headers=True,**text_kwargs):
        # Based on https://stackoverflow.com/a/25814386

        axes = fig.get_axes()

        for ax in axes:
            sbs = ax.get_subplotspec()

            # Putting headers on cols
            if (col_headers is not None) and sbs.is_first_row():
                ax.annotate(
                    col_headers[sbs.colspan.start],
                    xy=(0.5, 1),
                    xytext=(0, col_pad),
                    xycoords="axes fraction",
                    textcoords="offset points",
                    ha="center",
                    va="baseline",
                    **text_kwargs,
                )

            # Putting headers on rows
            if (row_headers is not None) and sbs.is_first_col():
                ax.annotate(
                    row_headers[sbs.rowspan.start],
                    xy=(0, 0.5),
                    xytext=(-ax.yaxis.labelpad - row_pad, 0),
                    xycoords=ax.yaxis.label,
                    textcoords="offset points",
                    ha="right",
                    va="center",
                    rotation=rotate_row_headers * 90,
                    **text_kwargs,
                )