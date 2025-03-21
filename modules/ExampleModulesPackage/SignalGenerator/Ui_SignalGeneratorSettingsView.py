# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SignalGeneratorSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignalGeneratorSettingsView(object):
    def setupUi(self, SignalGeneratorSettingsView):
        if not SignalGeneratorSettingsView.objectName():
            SignalGeneratorSettingsView.setObjectName(u"SignalGeneratorSettingsView")
        SignalGeneratorSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(SignalGeneratorSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.duration_label = QLabel(SignalGeneratorSettingsView)
        self.duration_label.setObjectName(u"duration_label")
        self.duration_label.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.duration_label)

        self.duration_lineedit = QLineEdit(SignalGeneratorSettingsView)
        self.duration_lineedit.setObjectName(u"duration_lineedit")
        self.duration_lineedit.setMaximumSize(QSize(50, 16777215))
        self.duration_lineedit.setInputMask(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.duration_lineedit)

        self.sample_rate_label = QLabel(SignalGeneratorSettingsView)
        self.sample_rate_label.setObjectName(u"sample_rate_label")
        self.sample_rate_label.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.sample_rate_label)

        self.sample_rate_lineedit = QLineEdit(SignalGeneratorSettingsView)
        self.sample_rate_lineedit.setObjectName(u"sample_rate_lineedit")
        self.sample_rate_lineedit.setMaximumSize(QSize(50, 16777215))
        self.sample_rate_lineedit.setInputMask(u"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sample_rate_lineedit)

        self.frequency_label = QLabel(SignalGeneratorSettingsView)
        self.frequency_label.setObjectName(u"frequency_label")
        self.frequency_label.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.frequency_label)

        self.frequency_lineedit = QLineEdit(SignalGeneratorSettingsView)
        self.frequency_lineedit.setObjectName(u"frequency_lineedit")
        self.frequency_lineedit.setMaximumSize(QSize(50, 16777215))
        self.frequency_lineedit.setInputMask(u"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.frequency_lineedit)

        self.phase_label = QLabel(SignalGeneratorSettingsView)
        self.phase_label.setObjectName(u"phase_label")
        self.phase_label.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.phase_label)

        self.amplitude_label = QLabel(SignalGeneratorSettingsView)
        self.amplitude_label.setObjectName(u"amplitude_label")
        self.amplitude_label.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.amplitude_label)

        self.amplitude_lineedit = QLineEdit(SignalGeneratorSettingsView)
        self.amplitude_lineedit.setObjectName(u"amplitude_lineedit")
        self.amplitude_lineedit.setMaximumSize(QSize(50, 16777215))
        self.amplitude_lineedit.setInputMask(u"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.amplitude_lineedit)

        self.phase_spinBox = QSpinBox(SignalGeneratorSettingsView)
        self.phase_spinBox.setObjectName(u"phase_spinBox")
        self.phase_spinBox.setMaximumSize(QSize(50, 16777215))
        self.phase_spinBox.setMaximum(360)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.phase_spinBox)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.figure_layout = QVBoxLayout()
        self.figure_layout.setObjectName(u"figure_layout")

        self.horizontalLayout.addLayout(self.figure_layout)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SignalGeneratorSettingsView)
        self.duration_lineedit.textEdited.connect(SignalGeneratorSettingsView.duration_changed)
        self.sample_rate_lineedit.textEdited.connect(SignalGeneratorSettingsView.sample_rate_changed)
        self.frequency_lineedit.textEdited.connect(SignalGeneratorSettingsView.frequency_changed)
        self.amplitude_lineedit.textEdited.connect(SignalGeneratorSettingsView.amplitude_changed)
        self.phase_spinBox.valueChanged.connect(SignalGeneratorSettingsView.phase_changed)

        QMetaObject.connectSlotsByName(SignalGeneratorSettingsView)
    # setupUi

    def retranslateUi(self, SignalGeneratorSettingsView):
        SignalGeneratorSettingsView.setWindowTitle(QCoreApplication.translate("SignalGeneratorSettingsView", u"Form", None))
        self.duration_label.setText(QCoreApplication.translate("SignalGeneratorSettingsView", u"Duration (s)", None))
        self.sample_rate_label.setText(QCoreApplication.translate("SignalGeneratorSettingsView", u"Sample rate", None))
        self.frequency_label.setText(QCoreApplication.translate("SignalGeneratorSettingsView", u"Frequency (Hz)", None))
        self.phase_label.setText(QCoreApplication.translate("SignalGeneratorSettingsView", u"Phase (radians)", None))
        self.amplitude_label.setText(QCoreApplication.translate("SignalGeneratorSettingsView", u"Amplitude", None))
    # retranslateUi

