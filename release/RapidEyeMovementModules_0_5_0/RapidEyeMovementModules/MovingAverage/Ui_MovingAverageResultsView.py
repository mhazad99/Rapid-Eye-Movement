# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MovingAverageResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MovingAverageResultsView(object):
    def setupUi(self, MovingAverageResultsView):
        if not MovingAverageResultsView.objectName():
            MovingAverageResultsView.setObjectName(u"MovingAverageResultsView")
        MovingAverageResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(MovingAverageResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(MovingAverageResultsView)

        QMetaObject.connectSlotsByName(MovingAverageResultsView)
    # setupUi

    def retranslateUi(self, MovingAverageResultsView):
        MovingAverageResultsView.setWindowTitle(QCoreApplication.translate("MovingAverageResultsView", u"Form", None))
    # retranslateUi

