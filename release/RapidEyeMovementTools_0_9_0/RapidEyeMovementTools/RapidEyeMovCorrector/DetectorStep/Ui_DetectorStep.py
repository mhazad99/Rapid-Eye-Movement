# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectorStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_DetectorStep(object):
    def setupUi(self, DetectorStep):
        if not DetectorStep.objectName():
            DetectorStep.setObjectName(u"DetectorStep")
        DetectorStep.resize(956, 774)
        self.horizontalLayout = QHBoxLayout(DetectorStep)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(DetectorStep)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.mutual_info_radioButton = QRadioButton(DetectorStep)
        self.mutual_info_radioButton.setObjectName(u"mutual_info_radioButton")

        self.verticalLayout.addWidget(self.mutual_info_radioButton)

        self.expert_annot_radioButton = QRadioButton(DetectorStep)
        self.expert_annot_radioButton.setObjectName(u"expert_annot_radioButton")

        self.verticalLayout.addWidget(self.expert_annot_radioButton)

        self.REMs_Det_radioButton = QRadioButton(DetectorStep)
        self.REMs_Det_radioButton.setObjectName(u"REMs_Det_radioButton")
        self.REMs_Det_radioButton.setEnabled(True)
        self.REMs_Det_radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.REMs_Det_radioButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_12 = QLabel(DetectorStep)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.verticalLayout.addWidget(self.label_12)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.expert_label_label = QLabel(DetectorStep)
        self.expert_label_label.setObjectName(u"expert_label_label")
        self.expert_label_label.setEnabled(True)
        self.expert_label_label.setMinimumSize(QSize(300, 0))

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.expert_label_label)

        self.expert_label_lineEdit = QLineEdit(DetectorStep)
        self.expert_label_lineEdit.setObjectName(u"expert_label_lineEdit")
        self.expert_label_lineEdit.setEnabled(False)
        self.expert_label_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.expert_label_lineEdit)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_10 = QLabel(DetectorStep)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout.addWidget(self.label_10)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_7 = QLabel(DetectorStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(300, 0))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.name_lineEdit = QLineEdit(DetectorStep)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.name_lineEdit)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.label_9 = QLabel(DetectorStep)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setItalic(True)
        self.label_9.setFont(font1)

        self.verticalLayout.addWidget(self.label_9)

        self.label_6 = QLabel(DetectorStep)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label = QLabel(DetectorStep)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(500, 0))
        self.label.setMaximumSize(QSize(500, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.label.setFont(font2)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_8 = QLabel(DetectorStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(300, 0))
        font3 = QFont()
        font3.setPointSize(11)
        self.label_8.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.window_sec_doubleSpinBox = QDoubleSpinBox(DetectorStep)
        self.window_sec_doubleSpinBox.setObjectName(u"window_sec_doubleSpinBox")
        self.window_sec_doubleSpinBox.setEnabled(False)
        self.window_sec_doubleSpinBox.setMaximumSize(QSize(300, 16777215))
        self.window_sec_doubleSpinBox.setFont(font3)
        self.window_sec_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.window_sec_doubleSpinBox.setMaximum(50000.000000000000000)
        self.window_sec_doubleSpinBox.setValue(3.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.window_sec_doubleSpinBox)

        self.label_2 = QLabel(DetectorStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(300, 16777215))
        self.label_2.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.order_spinBox = QSpinBox(DetectorStep)
        self.order_spinBox.setObjectName(u"order_spinBox")
        self.order_spinBox.setEnabled(False)
        self.order_spinBox.setMaximumSize(QSize(300, 16777215))
        self.order_spinBox.setFont(font3)
        self.order_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_spinBox.setMaximum(1000)
        self.order_spinBox.setValue(11)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.order_spinBox)

        self.label_3 = QLabel(DetectorStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(500, 16777215))
        self.label_3.setFont(font3)
        self.label_3.setWordWrap(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.border_effect_doubleSpinBox = QDoubleSpinBox(DetectorStep)
        self.border_effect_doubleSpinBox.setObjectName(u"border_effect_doubleSpinBox")
        self.border_effect_doubleSpinBox.setEnabled(False)
        self.border_effect_doubleSpinBox.setMaximumSize(QSize(300, 16777215))
        self.border_effect_doubleSpinBox.setFont(font3)
        self.border_effect_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.border_effect_doubleSpinBox.setMaximum(50.000000000000000)
        self.border_effect_doubleSpinBox.setValue(10.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.border_effect_doubleSpinBox)

        self.label_4 = QLabel(DetectorStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(200, 16777215))
        self.label_4.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.percentile_spinBox = QSpinBox(DetectorStep)
        self.percentile_spinBox.setObjectName(u"percentile_spinBox")
        self.percentile_spinBox.setMaximumSize(QSize(300, 16777215))
        self.percentile_spinBox.setFont(font3)
        self.percentile_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.percentile_spinBox.setMaximum(100)
        self.percentile_spinBox.setValue(65)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.percentile_spinBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.expert_checkBox = QCheckBox(DetectorStep)
        self.expert_checkBox.setObjectName(u"expert_checkBox")

        self.verticalLayout.addWidget(self.expert_checkBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(427, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(DetectorStep)
        self.expert_checkBox.clicked.connect(DetectorStep.expert_mode_slot)
        self.REMs_Det_radioButton.clicked.connect(DetectorStep.on_active_detector)
        self.expert_annot_radioButton.clicked.connect(DetectorStep.on_active_detector)
        self.mutual_info_radioButton.clicked.connect(DetectorStep.on_active_detector)

        QMetaObject.connectSlotsByName(DetectorStep)
    # setupUi

    def retranslateUi(self, DetectorStep):
        DetectorStep.setWindowTitle("")
        DetectorStep.setStyleSheet(QCoreApplication.translate("DetectorStep", u"font: 10pt \"Roboto-Regular\";", None))
        self.label_5.setText(QCoreApplication.translate("DetectorStep", u"The REMs correction is based on :", None))
        self.mutual_info_radioButton.setText(QCoreApplication.translate("DetectorStep", u"on mutual information exclusively", None))
        self.expert_annot_radioButton.setText(QCoreApplication.translate("DetectorStep", u"annotations from the expert", None))
        self.REMs_Det_radioButton.setText(QCoreApplication.translate("DetectorStep", u"REMs Detector (Poulin)", None))
        self.label_12.setText(QCoreApplication.translate("DetectorStep", u"Annotations from the expert", None))
        self.expert_label_label.setText(QCoreApplication.translate("DetectorStep", u"REMs label (event name)", None))
        self.expert_label_lineEdit.setText(QCoreApplication.translate("DetectorStep", u"MOR_C", None))
        self.label_10.setText(QCoreApplication.translate("DetectorStep", u"REMs detector", None))
        self.label_7.setText(QCoreApplication.translate("DetectorStep", u"REMs Event Name", None))
        self.label_9.setText(QCoreApplication.translate("DetectorStep", u"REMs detection within the time window (i.e. 3 s)", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("DetectorStep", u"REMs detector parameters :", None))
        self.label_8.setText(QCoreApplication.translate("DetectorStep", u"Window length (s) of the detected event", None))
#if QT_CONFIG(tooltip)
        self.window_sec_doubleSpinBox.setToolTip(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p>Must be a divider of the sleep stage's window lenght (30 sec in most case)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DetectorStep", u"Order of the derivative approximation", None))
        self.label_3.setText(QCoreApplication.translate("DetectorStep", u"Border effect (% of signal to remove each side)", None))
        self.label_4.setText(QCoreApplication.translate("DetectorStep", u"Percentile", None))
        self.expert_checkBox.setText(QCoreApplication.translate("DetectorStep", u"Expert Mode", None))
    # retranslateUi

