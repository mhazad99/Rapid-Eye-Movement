# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EOGNormalizationResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_EOGNormalizationResultsView(object):
    def setupUi(self, EOGNormalizationResultsView):
        if not EOGNormalizationResultsView.objectName():
            EOGNormalizationResultsView.setObjectName(u"EOGNormalizationResultsView")
        EOGNormalizationResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        EOGNormalizationResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(EOGNormalizationResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(EOGNormalizationResultsView)

        QMetaObject.connectSlotsByName(EOGNormalizationResultsView)
    # setupUi

    def retranslateUi(self, EOGNormalizationResultsView):
        EOGNormalizationResultsView.setWindowTitle(QCoreApplication.translate("EOGNormalizationResultsView", u"Form", None))
    # retranslateUi

