#! /usr/bin/env python3
"""
    DetectorStep
    TODO CLASS DESCRIPTION
"""
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState


from RapidEyeMovementTools.REMsDetectorYASA.DetectorStep.Ui_DetectorStep import Ui_DetectorStep

from qtpy import QtWidgets

class DetectorStep(BaseStepView, Ui_DetectorStep, QtWidgets.QWidget):
    """
        DetectorStep
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to


        # Subscribe to the publisher for each node you want to talk to


        # The event name to compare with is added to the event combine plugin 
        # to change the event channel.  To evaluate the performance we need 
        # to have the events on the same channel.
      
        
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        pass

    def on_apply_settings(self):
        pass
        
 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        pass
        
    # Slot called when the user wants to write the filename
    def on_choose(self):
        pass

    def on_active_validation(self):
        pass

    # Called when the user delete an instance of the plugin
    def __del__(self):
        pass