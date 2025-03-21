# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SignalGeneratorResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignalGeneratorResultsView(object):
    def setupUi(self, SignalGeneratorResultsView):
        if not SignalGeneratorResultsView.objectName():
            SignalGeneratorResultsView.setObjectName(u"SignalGeneratorResultsView")
        SignalGeneratorResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(SignalGeneratorResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(SignalGeneratorResultsView)

        QMetaObject.connectSlotsByName(SignalGeneratorResultsView)
    # setupUi

    def retranslateUi(self, SignalGeneratorResultsView):
        SignalGeneratorResultsView.setWindowTitle(QCoreApplication.translate("SignalGeneratorResultsView", u"Form", None))
    # retranslateUi

