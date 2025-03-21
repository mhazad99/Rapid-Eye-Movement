#! /usr/bin/env python3
"""
    FirstStep
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets

from ExampleToolsPackage.ToolA.FirstStep.Ui_FirstStep import Ui_FirstStep
from commons.BaseStepView import BaseStepView

class FirstStep(BaseStepView, Ui_FirstStep, QtWidgets.QWidget):
    """
        FirstStep
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
