"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the SignalsCombine plugin
"""

from qtpy import QtWidgets

from RapidEyeMovementModules.SignalsCombine.Ui_SignalsCombineSettingsView import Ui_SignalsCombineSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SignalsCombineSettingsView( BaseSettingsView,  Ui_SignalsCombineSettingsView, QtWidgets.QWidget):
    """
        SignalsCombineView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass