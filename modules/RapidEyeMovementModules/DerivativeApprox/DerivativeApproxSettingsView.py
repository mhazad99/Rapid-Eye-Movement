"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the DerivativeApprox plugin
"""

from qtpy import QtWidgets

from RapidEyeMovementModules.DerivativeApprox.Ui_DerivativeApproxSettingsView import Ui_DerivativeApproxSettingsView
from commons.BaseSettingsView import BaseSettingsView

class DerivativeApproxSettingsView(BaseSettingsView, Ui_DerivativeApproxSettingsView, QtWidgets.QWidget):
    """
        DerivativeApproxView set the DerivativeApprox settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._order_topic = f'{self._parent_node.identifier}.order'
        self._pub_sub_manager.subscribe(self, self._order_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """

        self._pub_sub_manager.publish(self, self._order_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        
        # Send the settings to the publisher for inputs to DerivativeApprox
        self._pub_sub_manager.publish(self, self._order_topic, self.order_spinBox.value())
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """

        if topic == self._order_topic:
            self.order_spinBox.setValue(int(message))
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._order_topic)
            
            return
        