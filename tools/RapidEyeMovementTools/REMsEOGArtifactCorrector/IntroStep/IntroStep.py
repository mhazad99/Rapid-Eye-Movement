#! /usr/bin/env python3
"""
    IntroStep
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView

from RapidEyeMovementTools.REMsEOGArtifactCorrector.IntroStep.Ui_IntroStep import Ui_IntroStep

from qtpy import QtWidgets

class IntroStep(BaseStepView, Ui_IntroStep, QtWidgets.QWidget):
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
