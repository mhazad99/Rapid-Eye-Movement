# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CreateTupleResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_CreateTupleResultsView(object):
    def setupUi(self, CreateTupleResultsView):
        if not CreateTupleResultsView.objectName():
            CreateTupleResultsView.setObjectName(u"CreateTupleResultsView")
        CreateTupleResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        CreateTupleResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(CreateTupleResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(CreateTupleResultsView)

        QMetaObject.connectSlotsByName(CreateTupleResultsView)
    # setupUi

    def retranslateUi(self, CreateTupleResultsView):
        CreateTupleResultsView.setWindowTitle(QCoreApplication.translate("CreateTupleResultsView", u"Form", None))
    # retranslateUi

