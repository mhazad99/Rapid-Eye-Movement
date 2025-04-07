# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpectralPowerSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SpectralPowerSettingsView(object):
    def setupUi(self, SpectralPowerSettingsView):
        if not SpectralPowerSettingsView.objectName():
            SpectralPowerSettingsView.setObjectName(u"SpectralPowerSettingsView")
        SpectralPowerSettingsView.resize(658, 431)
        self.gridLayout = QGridLayout(SpectralPowerSettingsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(SpectralPowerSettingsView)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.abs_radioButton = QRadioButton(SpectralPowerSettingsView)
        self.abs_radioButton.setObjectName(u"abs_radioButton")
        self.abs_radioButton.setChecked(False)

        self.horizontalLayout.addWidget(self.abs_radioButton)

        self.rel_radioButton = QRadioButton(SpectralPowerSettingsView)
        self.rel_radioButton.setObjectName(u"rel_radioButton")
        self.rel_radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.rel_radioButton)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_11 = QLabel(SpectralPowerSettingsView)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.line_2 = QFrame(SpectralPowerSettingsView)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(SpectralPowerSettingsView)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setUnderline(True)
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.delta_checkBox = QCheckBox(SpectralPowerSettingsView)
        self.delta_checkBox.setObjectName(u"delta_checkBox")
        self.delta_checkBox.setMinimumSize(QSize(88, 0))
        self.delta_checkBox.setChecked(False)

        self.horizontalLayout_6.addWidget(self.delta_checkBox)

        self.delta_lineEdit = QLineEdit(SpectralPowerSettingsView)
        self.delta_lineEdit.setObjectName(u"delta_lineEdit")
        self.delta_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_6.addWidget(self.delta_lineEdit)

        self.label_3 = QLabel(SpectralPowerSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.theta_checkBox = QCheckBox(SpectralPowerSettingsView)
        self.theta_checkBox.setObjectName(u"theta_checkBox")
        self.theta_checkBox.setMinimumSize(QSize(88, 0))
        self.theta_checkBox.setChecked(False)

        self.horizontalLayout_7.addWidget(self.theta_checkBox)

        self.theta_lineEdit = QLineEdit(SpectralPowerSettingsView)
        self.theta_lineEdit.setObjectName(u"theta_lineEdit")
        self.theta_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.theta_lineEdit)

        self.label_4 = QLabel(SpectralPowerSettingsView)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.alpha_checkBox = QCheckBox(SpectralPowerSettingsView)
        self.alpha_checkBox.setObjectName(u"alpha_checkBox")
        self.alpha_checkBox.setMinimumSize(QSize(88, 0))

        self.horizontalLayout_8.addWidget(self.alpha_checkBox)

        self.alpha_lineEdit = QLineEdit(SpectralPowerSettingsView)
        self.alpha_lineEdit.setObjectName(u"alpha_lineEdit")
        self.alpha_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.alpha_lineEdit)

        self.label_5 = QLabel(SpectralPowerSettingsView)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.beta_checkBox = QCheckBox(SpectralPowerSettingsView)
        self.beta_checkBox.setObjectName(u"beta_checkBox")
        self.beta_checkBox.setMinimumSize(QSize(88, 0))

        self.horizontalLayout_9.addWidget(self.beta_checkBox)

        self.beta_lineEdit = QLineEdit(SpectralPowerSettingsView)
        self.beta_lineEdit.setObjectName(u"beta_lineEdit")
        self.beta_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_9.addWidget(self.beta_lineEdit)

        self.label_6 = QLabel(SpectralPowerSettingsView)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gamma_checkBox = QCheckBox(SpectralPowerSettingsView)
        self.gamma_checkBox.setObjectName(u"gamma_checkBox")
        self.gamma_checkBox.setMinimumSize(QSize(88, 0))

        self.horizontalLayout_10.addWidget(self.gamma_checkBox)

        self.gamma_lineEdit = QLineEdit(SpectralPowerSettingsView)
        self.gamma_lineEdit.setObjectName(u"gamma_lineEdit")
        self.gamma_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_10.addWidget(self.gamma_lineEdit)

        self.label_7 = QLabel(SpectralPowerSettingsView)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.others_checkBox = QCheckBox(SpectralPowerSettingsView)
        self.others_checkBox.setObjectName(u"others_checkBox")
        self.others_checkBox.setMinimumSize(QSize(88, 0))

        self.horizontalLayout_11.addWidget(self.others_checkBox)

        self.others_lineEdit = QLineEdit(SpectralPowerSettingsView)
        self.others_lineEdit.setObjectName(u"others_lineEdit")
        self.others_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_11.addWidget(self.others_lineEdit)

        self.label_8 = QLabel(SpectralPowerSettingsView)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.total_checkBox = QCheckBox(SpectralPowerSettingsView)
        self.total_checkBox.setObjectName(u"total_checkBox")
        self.total_checkBox.setMinimumSize(QSize(88, 0))

        self.horizontalLayout_12.addWidget(self.total_checkBox)

        self.total_lineEdit = QLineEdit(SpectralPowerSettingsView)
        self.total_lineEdit.setObjectName(u"total_lineEdit")
        self.total_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_12.addWidget(self.total_lineEdit)

        self.label_9 = QLabel(SpectralPowerSettingsView)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(SpectralPowerSettingsView)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.line = QFrame(SpectralPowerSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(SpectralPowerSettingsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.filename_lineEdit = QLineEdit(SpectralPowerSettingsView)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")
        self.filename_lineEdit.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_5.addWidget(self.filename_lineEdit)

        self.choose_pushButton = QPushButton(SpectralPowerSettingsView)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.horizontalLayout_5.addWidget(self.choose_pushButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(SpectralPowerSettingsView)
        self.choose_pushButton.clicked.connect(SpectralPowerSettingsView.on_choose)
        self.abs_radioButton.clicked.connect(SpectralPowerSettingsView.on_change_mode)
        self.rel_radioButton.clicked.connect(SpectralPowerSettingsView.on_change_mode)

        QMetaObject.connectSlotsByName(SpectralPowerSettingsView)
    # setupUi

    def retranslateUi(self, SpectralPowerSettingsView):
        SpectralPowerSettingsView.setWindowTitle(QCoreApplication.translate("SpectralPowerSettingsView", u"Form", None))
        self.Title.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"SpectralPower settings", None))
        self.abs_radioButton.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Absolute", None))
        self.rel_radioButton.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Relative", None))
        self.label_11.setText("")
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("SpectralPowerSettingsView", u"<html><head/><body><p>Check the bandpowers you want to get the spectral power from.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Frequency band:", None))
        self.delta_checkBox.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Delta", None))
        self.delta_lineEdit.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"0.3-4", None))
        self.label_3.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Hz", None))
        self.theta_checkBox.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Theta", None))
        self.theta_lineEdit.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"4-8", None))
        self.label_4.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Hz", None))
        self.alpha_checkBox.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Alpha", None))
        self.alpha_lineEdit.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"8-12", None))
        self.label_5.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Hz", None))
        self.beta_checkBox.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Beta", None))
        self.beta_lineEdit.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"12-30", None))
        self.label_6.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Hz", None))
        self.gamma_checkBox.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Gamma", None))
        self.gamma_lineEdit.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"30-100", None))
        self.label_7.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Hz", None))
        self.others_checkBox.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Others", None))
#if QT_CONFIG(tooltip)
        self.others_lineEdit.setToolTip(QCoreApplication.translate("SpectralPowerSettingsView", u"<html><head/><body><p>Specify other bandwith. Separate by a semicolon (;).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Hz", None))
        self.total_checkBox.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Total band", None))
        self.total_lineEdit.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"0.3-40", None))
        self.label_9.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Hz", None))
        self.label_10.setText("")
        self.label.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Output filename:", None))
        self.choose_pushButton.setText(QCoreApplication.translate("SpectralPowerSettingsView", u"Choose file...", None))
    # retranslateUi

