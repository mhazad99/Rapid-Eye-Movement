# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetrendSignalSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DetrendSignalSettingsView(object):
    def setupUi(self, DetrendSignalSettingsView):
        if not DetrendSignalSettingsView.objectName():
            DetrendSignalSettingsView.setObjectName(u"DetrendSignalSettingsView")
        DetrendSignalSettingsView.resize(314, 122)
        self.verticalLayout = QVBoxLayout(DetrendSignalSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mode_horizontalLayout = QHBoxLayout()
        self.mode_horizontalLayout.setObjectName(u"mode_horizontalLayout")
        self.mode_label = QLabel(DetrendSignalSettingsView)
        self.mode_label.setObjectName(u"mode_label")

        self.mode_horizontalLayout.addWidget(self.mode_label)

        self.mode_comboBox = QComboBox(DetrendSignalSettingsView)
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.setObjectName(u"mode_comboBox")

        self.mode_horizontalLayout.addWidget(self.mode_comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.mode_horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.mode_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DetrendSignalSettingsView)

        QMetaObject.connectSlotsByName(DetrendSignalSettingsView)
    # setupUi

    def retranslateUi(self, DetrendSignalSettingsView):
        DetrendSignalSettingsView.setWindowTitle(QCoreApplication.translate("DetrendSignalSettingsView", u"Form", None))
        self.mode_label.setText(QCoreApplication.translate("DetrendSignalSettingsView", u"Mode", None))
        self.mode_comboBox.setItemText(0, QCoreApplication.translate("DetrendSignalSettingsView", u"linear", None))
        self.mode_comboBox.setItemText(1, QCoreApplication.translate("DetrendSignalSettingsView", u"p_inv", None))
        self.mode_comboBox.setItemText(2, QCoreApplication.translate("DetrendSignalSettingsView", u"constant", None))

    # retranslateUi

