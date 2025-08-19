"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    NonValidEventStep
    Step in the PSA interface to exclude non valid events for the PSA analysis.
    The file was copied from the CEAMSTools and adapted for the REMs corrector.
    Doc to open and read to understand : 
    Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
    View : QAbstractItemView -> QTreeView
"""
import ast
import os
from qtpy import QtWidgets, QtCore, QtGui
from qtpy.QtCore import Qt

from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from widgets.WarningDialog import WarningDialog

from RapidEyeMovementTools.REMsEOGArtifactCorrector.REMSelectionEventStep.Ui_REMSelectionEventStep import Ui_REMSelectionEventStep
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep

DEBUG = True

class REMSelectionEventStep(NonValidEventStep):

    node_id_ResetSignalArtefact_0 = None # reset the signal during artifact
    node_id_Dictionary_group = "571b06e1-5911-4718-a8f8-6770e06d927a" # select the list of group for the current filename
    node_id_Dictionary_name = "178a20fb-e8ae-462f-bda5-43a7f85862ad" # select the list of name for the current filename    
    """
        NonValidEventStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform "Reset Signal Interface" and "Discard Events" modules.
    """

