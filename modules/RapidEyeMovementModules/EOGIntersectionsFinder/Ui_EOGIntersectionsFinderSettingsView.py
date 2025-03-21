# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EOGIntersectionsFinderSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_EOGIntersectionsFinderSettingsView(object):
    def setupUi(self, EOGIntersectionsFinderSettingsView):
        if not EOGIntersectionsFinderSettingsView.objectName():
            EOGIntersectionsFinderSettingsView.setObjectName(u"EOGIntersectionsFinderSettingsView")
        EOGIntersectionsFinderSettingsView.resize(1045, 604)
        EOGIntersectionsFinderSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_2 = QHBoxLayout(EOGIntersectionsFinderSettingsView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(EOGIntersectionsFinderSettingsView)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label = QLabel(EOGIntersectionsFinderSettingsView)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(EOGIntersectionsFinderSettingsView)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.doubleSpinBox_timeWin = QDoubleSpinBox(EOGIntersectionsFinderSettingsView)
        self.doubleSpinBox_timeWin.setObjectName(u"doubleSpinBox_timeWin")
        self.doubleSpinBox_timeWin.setMaximum(5.000000000000000)
        self.doubleSpinBox_timeWin.setSingleStep(0.010000000000000)
        self.doubleSpinBox_timeWin.setValue(0.160000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_timeWin)

        self.label_2 = QLabel(EOGIntersectionsFinderSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(292, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.retranslateUi(EOGIntersectionsFinderSettingsView)

        QMetaObject.connectSlotsByName(EOGIntersectionsFinderSettingsView)
    # setupUi

    def retranslateUi(self, EOGIntersectionsFinderSettingsView):
        EOGIntersectionsFinderSettingsView.setWindowTitle(QCoreApplication.translate("EOGIntersectionsFinderSettingsView", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("EOGIntersectionsFinderSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">EOG Intersections finder</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("EOGIntersectionsFinderSettingsView", u"To identify the primary intersection points in time between two EOG signals.", None))
        self.label_5.setText(QCoreApplication.translate("EOGIntersectionsFinderSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Time Window</span> : Time window (sec) to average closely occurring intersection points, preserving the main ones.</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("EOGIntersectionsFinderSettingsView", u"Default value is 0.16.", None))
    # retranslateUi

