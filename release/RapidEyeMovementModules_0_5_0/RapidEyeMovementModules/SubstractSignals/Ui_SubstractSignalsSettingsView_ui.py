# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SubstractSignalsSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SubstractSignalsSettingsView(object):
    def setupUi(self, SubstractSignalsSettingsView):
        if not SubstractSignalsSettingsView.objectName():
            SubstractSignalsSettingsView.setObjectName(u"SubstractSignalsSettingsView")
        SubstractSignalsSettingsView.resize(348, 161)
        self.gridLayout_2 = QGridLayout(SubstractSignalsSettingsView)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(SubstractSignalsSettingsView)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(SubstractSignalsSettingsView)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.channel_lineEdit = QLineEdit(SubstractSignalsSettingsView)
        self.channel_lineEdit.setObjectName(u"channel_lineEdit")

        self.gridLayout.addWidget(self.channel_lineEdit, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.label_2 = QLabel(SubstractSignalsSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.channel_to_sub_lineEdit = QLineEdit(SubstractSignalsSettingsView)
        self.channel_to_sub_lineEdit.setObjectName(u"channel_to_sub_lineEdit")

        self.gridLayout.addWidget(self.channel_to_sub_lineEdit, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.line = QFrame(SubstractSignalsSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 0, 1, 2)

        self.label_3 = QLabel(SubstractSignalsSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.new_chan_name_lineEdit = QLineEdit(SubstractSignalsSettingsView)
        self.new_chan_name_lineEdit.setObjectName(u"new_chan_name_lineEdit")

        self.gridLayout.addWidget(self.new_chan_name_lineEdit, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SubstractSignalsSettingsView)

        QMetaObject.connectSlotsByName(SubstractSignalsSettingsView)
    # setupUi

    def retranslateUi(self, SubstractSignalsSettingsView):
        SubstractSignalsSettingsView.setWindowTitle(QCoreApplication.translate("SubstractSignalsSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("SubstractSignalsSettingsView", u"SubstractSignals settings", None))
        self.label.setText(QCoreApplication.translate("SubstractSignalsSettingsView", u"channel", None))
#if QT_CONFIG(tooltip)
        self.channel_lineEdit.setToolTip(QCoreApplication.translate("SubstractSignalsSettingsView", u"Name of the initial channel (separate additional channel with a comma without space) ", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("SubstractSignalsSettingsView", u"channel to substract", None))
#if QT_CONFIG(tooltip)
        self.channel_to_sub_lineEdit.setToolTip(QCoreApplication.translate("SubstractSignalsSettingsView", u"Name of the channel to substract to channel.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("SubstractSignalsSettingsView", u"new channel name", None))
#if QT_CONFIG(tooltip)
        self.new_chan_name_lineEdit.setToolTip(QCoreApplication.translate("SubstractSignalsSettingsView", u"To rename the new substracted channel (valid only when a single channel is substracted).  The default name is \"channel - channel to substract\".", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

