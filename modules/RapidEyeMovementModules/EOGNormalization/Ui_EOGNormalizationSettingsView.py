# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EOGNormalizationSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_EOGNormalizationSettingsView(object):
    def setupUi(self, EOGNormalizationSettingsView):
        if not EOGNormalizationSettingsView.objectName():
            EOGNormalizationSettingsView.setObjectName(u"EOGNormalizationSettingsView")
        EOGNormalizationSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        EOGNormalizationSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(EOGNormalizationSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filename_horizontalLayout = QHBoxLayout()
        self.filename_horizontalLayout.setObjectName(u"filename_horizontalLayout")
        self.filename_label = QLabel(EOGNormalizationSettingsView)
        self.filename_label.setObjectName(u"filename_label")

        self.filename_horizontalLayout.addWidget(self.filename_label)

        self.filename_lineedit = QLineEdit(EOGNormalizationSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")

        self.filename_horizontalLayout.addWidget(self.filename_lineedit)


        self.verticalLayout.addLayout(self.filename_horizontalLayout)

        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(EOGNormalizationSettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(EOGNormalizationSettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.baseline_stats_horizontalLayout = QHBoxLayout()
        self.baseline_stats_horizontalLayout.setObjectName(u"baseline_stats_horizontalLayout")
        self.baseline_stats_label = QLabel(EOGNormalizationSettingsView)
        self.baseline_stats_label.setObjectName(u"baseline_stats_label")

        self.baseline_stats_horizontalLayout.addWidget(self.baseline_stats_label)

        self.baseline_stats_lineedit = QLineEdit(EOGNormalizationSettingsView)
        self.baseline_stats_lineedit.setObjectName(u"baseline_stats_lineedit")

        self.baseline_stats_horizontalLayout.addWidget(self.baseline_stats_lineedit)


        self.verticalLayout.addLayout(self.baseline_stats_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(EOGNormalizationSettingsView)

        QMetaObject.connectSlotsByName(EOGNormalizationSettingsView)
    # setupUi

    def retranslateUi(self, EOGNormalizationSettingsView):
        EOGNormalizationSettingsView.setWindowTitle(QCoreApplication.translate("EOGNormalizationSettingsView", u"Form", None))
        self.filename_label.setText(QCoreApplication.translate("EOGNormalizationSettingsView", u"filename", None))
        self.signals_label.setText(QCoreApplication.translate("EOGNormalizationSettingsView", u"signals", None))
        self.baseline_stats_label.setText(QCoreApplication.translate("EOGNormalizationSettingsView", u"baseline_stats", None))
    # retranslateUi

