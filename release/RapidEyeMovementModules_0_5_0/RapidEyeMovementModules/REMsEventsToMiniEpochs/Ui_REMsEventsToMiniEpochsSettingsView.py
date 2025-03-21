# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_REMsEventsToMiniEpochsSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_REMsEventsToMiniEpochsSettingsView(object):
    def setupUi(self, REMsEventsToMiniEpochsSettingsView):
        if not REMsEventsToMiniEpochsSettingsView.objectName():
            REMsEventsToMiniEpochsSettingsView.setObjectName(u"REMsEventsToMiniEpochsSettingsView")
        REMsEventsToMiniEpochsSettingsView.resize(838, 425)
        REMsEventsToMiniEpochsSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(REMsEventsToMiniEpochsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(REMsEventsToMiniEpochsSettingsView)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(REMsEventsToMiniEpochsSettingsView)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(REMsEventsToMiniEpochsSettingsView)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_group = QLineEdit(REMsEventsToMiniEpochsSettingsView)
        self.lineEdit_group.setObjectName(u"lineEdit_group")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_group)

        self.label_2 = QLabel(REMsEventsToMiniEpochsSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_name_MOR = QLineEdit(REMsEventsToMiniEpochsSettingsView)
        self.lineEdit_name_MOR.setObjectName(u"lineEdit_name_MOR")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_name_MOR)

        self.label_3 = QLabel(REMsEventsToMiniEpochsSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_name_NO = QLineEdit(REMsEventsToMiniEpochsSettingsView)
        self.lineEdit_name_NO.setObjectName(u"lineEdit_name_NO")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_name_NO)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 316, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(REMsEventsToMiniEpochsSettingsView)

        QMetaObject.connectSlotsByName(REMsEventsToMiniEpochsSettingsView)
    # setupUi

    def retranslateUi(self, REMsEventsToMiniEpochsSettingsView):
        REMsEventsToMiniEpochsSettingsView.setWindowTitle(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Define the labels of the 3 s mini-epoch for Rapid Eye Movements (REM).</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"Each event belongs to a group and is labeled by a name. ", None))
        self.label.setText(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"Group for the 3 s mini-epoch", None))
        self.label_2.setText(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"Name for the 3 s mini-epoch with at least one REM", None))
        self.label_3.setText(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"Name for the 3 s mini-epoch without REMs", None))
    # retranslateUi

