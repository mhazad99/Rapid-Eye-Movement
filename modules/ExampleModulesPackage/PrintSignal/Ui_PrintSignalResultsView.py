# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_PrintSignalResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PrintSignalResultsView(object):
    def setupUi(self, PrintSignalResultsView):
        if not PrintSignalResultsView.objectName():
            PrintSignalResultsView.setObjectName(u"PrintSignalResultsView")
        PrintSignalResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(PrintSignalResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(PrintSignalResultsView)

        QMetaObject.connectSlotsByName(PrintSignalResultsView)
    # setupUi

    def retranslateUi(self, PrintSignalResultsView):
        PrintSignalResultsView.setWindowTitle(QCoreApplication.translate("PrintSignalResultsView", u"Form", None))
    # retranslateUi

