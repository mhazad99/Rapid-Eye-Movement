# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\scinodes_poc\src\main\python\plugins\SubstractSignals\Ui_SubstractSignalsSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_SubstractSignalsSettingsView(object):
    def setupUi(self, SubstractSignalsSettingsView):
        SubstractSignalsSettingsView.setObjectName("SubstractSignalsSettingsView")
        SubstractSignalsSettingsView.resize(348, 161)
        self.gridLayout_2 = QtWidgets.QGridLayout(SubstractSignalsSettingsView)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(SubstractSignalsSettingsView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(SubstractSignalsSettingsView)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.channel_lineEdit = QtWidgets.QLineEdit(SubstractSignalsSettingsView)
        self.channel_lineEdit.setObjectName("channel_lineEdit")
        self.gridLayout.addWidget(self.channel_lineEdit, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(SubstractSignalsSettingsView)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.channel_to_sub_lineEdit = QtWidgets.QLineEdit(SubstractSignalsSettingsView)
        self.channel_to_sub_lineEdit.setObjectName("channel_to_sub_lineEdit")
        self.gridLayout.addWidget(self.channel_to_sub_lineEdit, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.line = QtWidgets.QFrame(SubstractSignalsSettingsView)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(SubstractSignalsSettingsView)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.new_chan_name_lineEdit = QtWidgets.QLineEdit(SubstractSignalsSettingsView)
        self.new_chan_name_lineEdit.setObjectName("new_chan_name_lineEdit")
        self.gridLayout.addWidget(self.new_chan_name_lineEdit, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(SubstractSignalsSettingsView)
        QtCore.QMetaObject.connectSlotsByName(SubstractSignalsSettingsView)

    def retranslateUi(self, SubstractSignalsSettingsView):
        _translate = QtCore.QCoreApplication.translate
        SubstractSignalsSettingsView.setWindowTitle(_translate("SubstractSignalsSettingsView", "Form"))
        self.label_8.setText(_translate("SubstractSignalsSettingsView", "SubstractSignals settings"))
        self.label.setText(_translate("SubstractSignalsSettingsView", "channel"))
        self.channel_lineEdit.setToolTip(_translate("SubstractSignalsSettingsView", "Name of the initial channel (separate additional channel with a comma without space) "))
        self.label_2.setText(_translate("SubstractSignalsSettingsView", "channel to substract"))
        self.channel_to_sub_lineEdit.setToolTip(_translate("SubstractSignalsSettingsView", "Name of the channel to substract to channel."))
        self.label_3.setText(_translate("SubstractSignalsSettingsView", "new channel name"))
        self.new_chan_name_lineEdit.setToolTip(_translate("SubstractSignalsSettingsView", "To rename the new substracted channel (valid only when a single channel is substracted).  The default name is \"channel - channel to substract\"."))
