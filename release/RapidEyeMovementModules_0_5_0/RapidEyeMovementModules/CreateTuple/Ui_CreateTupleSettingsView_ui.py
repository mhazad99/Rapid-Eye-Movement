# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CreateTupleSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_CreateTupleSettingsView(object):
    def setupUi(self, CreateTupleSettingsView):
        if not CreateTupleSettingsView.objectName():
            CreateTupleSettingsView.setObjectName(u"CreateTupleSettingsView")
        CreateTupleSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        CreateTupleSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(CreateTupleSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Idx0_horizontalLayout = QHBoxLayout()
        self.Idx0_horizontalLayout.setObjectName(u"Idx0_horizontalLayout")
        self.Idx0_label = QLabel(CreateTupleSettingsView)
        self.Idx0_label.setObjectName(u"Idx0_label")

        self.Idx0_horizontalLayout.addWidget(self.Idx0_label)

        self.Idx0_lineedit = QLineEdit(CreateTupleSettingsView)
        self.Idx0_lineedit.setObjectName(u"Idx0_lineedit")

        self.Idx0_horizontalLayout.addWidget(self.Idx0_lineedit)


        self.verticalLayout.addLayout(self.Idx0_horizontalLayout)

        self.Idx1_horizontalLayout = QHBoxLayout()
        self.Idx1_horizontalLayout.setObjectName(u"Idx1_horizontalLayout")
        self.Idx1_label = QLabel(CreateTupleSettingsView)
        self.Idx1_label.setObjectName(u"Idx1_label")

        self.Idx1_horizontalLayout.addWidget(self.Idx1_label)

        self.Idx1_lineedit = QLineEdit(CreateTupleSettingsView)
        self.Idx1_lineedit.setObjectName(u"Idx1_lineedit")

        self.Idx1_horizontalLayout.addWidget(self.Idx1_lineedit)


        self.verticalLayout.addLayout(self.Idx1_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(CreateTupleSettingsView)

        QMetaObject.connectSlotsByName(CreateTupleSettingsView)
    # setupUi

    def retranslateUi(self, CreateTupleSettingsView):
        CreateTupleSettingsView.setWindowTitle(QCoreApplication.translate("CreateTupleSettingsView", u"Form", None))
        self.Idx0_label.setText(QCoreApplication.translate("CreateTupleSettingsView", u"Idx0", None))
        self.Idx1_label.setText(QCoreApplication.translate("CreateTupleSettingsView", u"Idx1", None))
    # retranslateUi

