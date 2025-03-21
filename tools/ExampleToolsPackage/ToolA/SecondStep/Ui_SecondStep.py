# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SecondStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SecondStep(object):
    def setupUi(self, SecondStep):
        if not SecondStep.objectName():
            SecondStep.setObjectName(u"SecondStep")
        SecondStep.setStyleSheet(u"font: 10pt \"Roboto-Regular\";")
        SecondStep.resize(730, 590)
        self.verticalLayout = QVBoxLayout(SecondStep)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SecondStep)

        QMetaObject.connectSlotsByName(SecondStep)
    # setupUi

    def retranslateUi(self, SecondStep):
        SecondStep.setWindowTitle("")
    # retranslateUi

