# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EOGPeaksMatchesSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_EOGPeaksMatchesSettingsView(object):
    def setupUi(self, EOGPeaksMatchesSettingsView):
        if not EOGPeaksMatchesSettingsView.objectName():
            EOGPeaksMatchesSettingsView.setObjectName(u"EOGPeaksMatchesSettingsView")
        EOGPeaksMatchesSettingsView.resize(814, 333)
        EOGPeaksMatchesSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_2 = QHBoxLayout(EOGPeaksMatchesSettingsView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(EOGPeaksMatchesSettingsView)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(EOGPeaksMatchesSettingsView)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.doubleSpinBox_matchP_timeWin = QDoubleSpinBox(EOGPeaksMatchesSettingsView)
        self.doubleSpinBox_matchP_timeWin.setObjectName(u"doubleSpinBox_matchP_timeWin")
        self.doubleSpinBox_matchP_timeWin.setMaximum(5.000000000000000)
        self.doubleSpinBox_matchP_timeWin.setSingleStep(0.010000000000000)
        self.doubleSpinBox_matchP_timeWin.setValue(0.160000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_matchP_timeWin)

        self.label = QLabel(EOGPeaksMatchesSettingsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(156, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.retranslateUi(EOGPeaksMatchesSettingsView)

        QMetaObject.connectSlotsByName(EOGPeaksMatchesSettingsView)
    # setupUi

    def retranslateUi(self, EOGPeaksMatchesSettingsView):
        EOGPeaksMatchesSettingsView.setWindowTitle(QCoreApplication.translate("EOGPeaksMatchesSettingsView", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("EOGPeaksMatchesSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">EOG Peaks matches</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("EOGPeaksMatchesSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Time Window</span> : Allowable time window to match peaks between EOG signals (sec)</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("EOGPeaksMatchesSettingsView", u"Default value is 0.16", None))
    # retranslateUi

