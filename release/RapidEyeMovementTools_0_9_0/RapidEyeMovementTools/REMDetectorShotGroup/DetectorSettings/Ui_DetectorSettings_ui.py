# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectorSettings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_DetectorSettings(object):
    def setupUi(self, DetectorSettings):
        if not DetectorSettings.objectName():
            DetectorSettings.setObjectName(u"DetectorSettings")
        DetectorSettings.resize(791, 555)
        DetectorSettings.setStyleSheet(u"font: 10pt \"Roboto-Regular\";")
        self.verticalLayout_7 = QVBoxLayout(DetectorSettings)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(DetectorSettings)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(DetectorSettings)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_zscore = QCheckBox(DetectorSettings)
        self.checkBox_zscore.setObjectName(u"checkBox_zscore")
        self.checkBox_zscore.setChecked(True)

        self.horizontalLayout_4.addWidget(self.checkBox_zscore)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_zn3 = QRadioButton(DetectorSettings)
        self.buttonGroup_2 = QButtonGroup(DetectorSettings)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_zn3)
        self.radioButton_zn3.setObjectName(u"radioButton_zn3")
        self.radioButton_zn3.setEnabled(False)
        self.radioButton_zn3.setChecked(False)

        self.verticalLayout.addWidget(self.radioButton_zn3)

        self.radioButton_zr = QRadioButton(DetectorSettings)
        self.buttonGroup_2.addButton(self.radioButton_zr)
        self.radioButton_zr.setObjectName(u"radioButton_zr")
        self.radioButton_zr.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_zr)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(DetectorSettings)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.checkBox_wr = QCheckBox(DetectorSettings)
        self.checkBox_wr.setObjectName(u"checkBox_wr")
        self.checkBox_wr.setChecked(False)

        self.verticalLayout_5.addWidget(self.checkBox_wr)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 315, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.retranslateUi(DetectorSettings)
        self.checkBox_wr.clicked.connect(DetectorSettings.update_normalization_slot)
        self.checkBox_zscore.clicked.connect(DetectorSettings.update_normalization_slot)
        self.radioButton_zn3.clicked.connect(DetectorSettings.update_normalization_slot)
        self.radioButton_zr.clicked.connect(DetectorSettings.update_normalization_slot)

        QMetaObject.connectSlotsByName(DetectorSettings)
    # setupUi

    def retranslateUi(self, DetectorSettings):
        DetectorSettings.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("DetectorSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Normalization</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("DetectorSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Z-score transform based on the baseline.</span></p></body></html>", None))
        self.checkBox_zscore.setText(QCoreApplication.translate("DetectorSettings", u"Z-score transform EOG signals", None))
        self.radioButton_zn3.setText(QCoreApplication.translate("DetectorSettings", u"Normalize each EOG channel with its standard deviation got from N3 sleep.", None))
        self.radioButton_zr.setText(QCoreApplication.translate("DetectorSettings", u"Normalize each EOG channel with its standard deviation got from R sleep.", None))
        self.label_3.setText(QCoreApplication.translate("DetectorSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Weight the EOG channels based on the REM sleep.</span></p></body></html>", None))
        self.checkBox_wr.setText(QCoreApplication.translate("DetectorSettings", u"Weight the EOG channel with the smallest standard deviation in REM sleep to match the second EOG channel.\n"
"\n"
"large_std_R : The largest standard deviation value obtained from the two EOG channels during REM sleep.\n"
"small_std_R :  The smallest standard deviation value obtained from the two EOG channels during REM sleep.\n"
"weight coefficient : large_std_R / small_std_R.\n"
"scaling : EOG chan (with smallest std in R) x weight coefficient", None))
    # retranslateUi

