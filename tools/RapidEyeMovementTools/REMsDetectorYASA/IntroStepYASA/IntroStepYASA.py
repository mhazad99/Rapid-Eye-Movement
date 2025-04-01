#! /usr/bin/env python3
"""
    IntroStep
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView

from RapidEyeMovementTools.REMsDetectorYASA.IntroStepYASA.Ui_IntroStepYASA import Ui_IntroStepYASA

from qtpy import QtWidgets

class IntroStepYASA(BaseStepView, Ui_IntroStepYASA, QtWidgets.QWidget):
    """
        IntroStep
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
