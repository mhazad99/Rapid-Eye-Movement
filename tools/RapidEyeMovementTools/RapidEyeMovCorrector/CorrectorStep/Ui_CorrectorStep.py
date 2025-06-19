# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CorrectorStep.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_CorrectorStep(object):
    def setupUi(self, CorrectorStep):
        if not CorrectorStep.objectName():
            CorrectorStep.setObjectName(u"CorrectorStep")
        CorrectorStep.resize(556, 772)
        self.horizontalLayout_3 = QHBoxLayout(CorrectorStep)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(CorrectorStep)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout.addWidget(self.label_6)

        self.label_15 = QLabel(CorrectorStep)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setFamilies([u"Roboto-Regular"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_15.setFont(font)

        self.verticalLayout.addWidget(self.label_15)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_16 = QLabel(CorrectorStep)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(380, 0))
        self.label_16.setMaximumSize(QSize(500, 16777215))

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.lineEdit_group_to_cor = QLineEdit(CorrectorStep)
        self.lineEdit_group_to_cor.setObjectName(u"lineEdit_group_to_cor")

        self.gridLayout_4.addWidget(self.lineEdit_group_to_cor, 0, 1, 1, 1)

        self.label_17 = QLabel(CorrectorStep)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)

        self.lineEdit_name_to_cor = QLineEdit(CorrectorStep)
        self.lineEdit_name_to_cor.setObjectName(u"lineEdit_name_to_cor")

        self.gridLayout_4.addWidget(self.lineEdit_name_to_cor, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_7 = QLabel(CorrectorStep)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label = QLabel(CorrectorStep)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Roboto-Regular"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(CorrectorStep)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(380, 0))
        self.label_10.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.group_lineEdit = QLineEdit(CorrectorStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setMinimumSize(QSize(0, 0))
        self.group_lineEdit.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.group_lineEdit, 0, 1, 1, 1)

        self.label_12 = QLabel(CorrectorStep)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)

        self.name_lineEdit = QLineEdit(CorrectorStep)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.name_lineEdit, 1, 1, 1, 1)

        self.label_8 = QLabel(CorrectorStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(500, 16777215))
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.window_sec_doubleSpinBox = QDoubleSpinBox(CorrectorStep)
        self.window_sec_doubleSpinBox.setObjectName(u"window_sec_doubleSpinBox")
        self.window_sec_doubleSpinBox.setEnabled(False)
        self.window_sec_doubleSpinBox.setMaximumSize(QSize(300, 16777215))
        self.window_sec_doubleSpinBox.setFont(font)
        self.window_sec_doubleSpinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.window_sec_doubleSpinBox.setMaximum(50000.000000000000000)
        self.window_sec_doubleSpinBox.setValue(10.000000000000000)

        self.gridLayout.addWidget(self.window_sec_doubleSpinBox, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_13 = QLabel(CorrectorStep)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout.addWidget(self.label_13)

        self.label_14 = QLabel(CorrectorStep)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cycle_radioButton = QRadioButton(CorrectorStep)
        self.cycle_radioButton.setObjectName(u"cycle_radioButton")
        self.cycle_radioButton.setEnabled(False)
        self.cycle_radioButton.setMinimumSize(QSize(190, 0))
        self.cycle_radioButton.setChecked(False)

        self.horizontalLayout.addWidget(self.cycle_radioButton)

        self.recording_radioButton = QRadioButton(CorrectorStep)
        self.recording_radioButton.setObjectName(u"recording_radioButton")
        self.recording_radioButton.setMinimumSize(QSize(190, 0))
        self.recording_radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.recording_radioButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(CorrectorStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(380, 0))
        self.label_3.setMaximumSize(QSize(16777215, 500))
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.p_val_doubleSpinBox = QDoubleSpinBox(CorrectorStep)
        self.p_val_doubleSpinBox.setObjectName(u"p_val_doubleSpinBox")
        self.p_val_doubleSpinBox.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_val_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.p_val_doubleSpinBox.setSizePolicy(sizePolicy)
        self.p_val_doubleSpinBox.setMaximumSize(QSize(300, 16777215))
        self.p_val_doubleSpinBox.setFont(font)
        self.p_val_doubleSpinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.p_val_doubleSpinBox.setMaximum(1.000000000000000)
        self.p_val_doubleSpinBox.setValue(0.900000000000000)

        self.gridLayout_2.addWidget(self.p_val_doubleSpinBox, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.label_9 = QLabel(CorrectorStep)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(500, 16777215))
        self.label_9.setFont(font)

        self.verticalLayout.addWidget(self.label_9)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.n_iter_spinBox = QSpinBox(CorrectorStep)
        self.n_iter_spinBox.setObjectName(u"n_iter_spinBox")
        self.n_iter_spinBox.setEnabled(False)
        sizePolicy.setHeightForWidth(self.n_iter_spinBox.sizePolicy().hasHeightForWidth())
        self.n_iter_spinBox.setSizePolicy(sizePolicy)
        self.n_iter_spinBox.setMaximumSize(QSize(300, 16777215))
        self.n_iter_spinBox.setFont(font)
        self.n_iter_spinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.n_iter_spinBox.setMaximum(500000)
        self.n_iter_spinBox.setValue(500)

        self.gridLayout_3.addWidget(self.n_iter_spinBox, 0, 1, 1, 1)

        self.label_5 = QLabel(CorrectorStep)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(380, 0))
        self.label_5.setMaximumSize(QSize(500, 16777215))
        self.label_5.setFont(font)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.eeg_bin_spinBox = QSpinBox(CorrectorStep)
        self.eeg_bin_spinBox.setObjectName(u"eeg_bin_spinBox")
        self.eeg_bin_spinBox.setEnabled(False)
        sizePolicy.setHeightForWidth(self.eeg_bin_spinBox.sizePolicy().hasHeightForWidth())
        self.eeg_bin_spinBox.setSizePolicy(sizePolicy)
        self.eeg_bin_spinBox.setMaximumSize(QSize(300, 16777215))
        self.eeg_bin_spinBox.setFont(font)
        self.eeg_bin_spinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.eeg_bin_spinBox.setMaximum(10000)
        self.eeg_bin_spinBox.setValue(90)

        self.gridLayout_3.addWidget(self.eeg_bin_spinBox, 1, 1, 1, 1)

        self.label_2 = QLabel(CorrectorStep)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMaximumSize(QSize(500, 16777215))
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(CorrectorStep)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMaximumSize(QSize(500, 16777215))
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)

        self.eog_bin_spinBox = QSpinBox(CorrectorStep)
        self.eog_bin_spinBox.setObjectName(u"eog_bin_spinBox")
        self.eog_bin_spinBox.setEnabled(False)
        sizePolicy.setHeightForWidth(self.eog_bin_spinBox.sizePolicy().hasHeightForWidth())
        self.eog_bin_spinBox.setSizePolicy(sizePolicy)
        self.eog_bin_spinBox.setMaximumSize(QSize(300, 16777215))
        self.eog_bin_spinBox.setFont(font)
        self.eog_bin_spinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.eog_bin_spinBox.setMaximum(10000)
        self.eog_bin_spinBox.setValue(30)

        self.gridLayout_3.addWidget(self.eog_bin_spinBox, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.expert_mode_checkBox = QCheckBox(CorrectorStep)
        self.expert_mode_checkBox.setObjectName(u"expert_mode_checkBox")

        self.verticalLayout.addWidget(self.expert_mode_checkBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_18 = QLabel(CorrectorStep)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.verticalLayout.addWidget(self.label_18)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(CorrectorStep)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(380, 0))
        self.label_11.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_2.addWidget(self.label_11)

        self.n_max_comp_rm_spinBox = QSpinBox(CorrectorStep)
        self.n_max_comp_rm_spinBox.setObjectName(u"n_max_comp_rm_spinBox")
        sizePolicy.setHeightForWidth(self.n_max_comp_rm_spinBox.sizePolicy().hasHeightForWidth())
        self.n_max_comp_rm_spinBox.setSizePolicy(sizePolicy)
        self.n_max_comp_rm_spinBox.setMaximumSize(QSize(300, 16777215))
        self.n_max_comp_rm_spinBox.setMinimum(1)
        self.n_max_comp_rm_spinBox.setMaximum(5)
        self.n_max_comp_rm_spinBox.setSingleStep(1)
        self.n_max_comp_rm_spinBox.setDisplayIntegerBase(10)

        self.horizontalLayout_2.addWidget(self.n_max_comp_rm_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(236, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.retranslateUi(CorrectorStep)
        self.expert_mode_checkBox.clicked.connect(CorrectorStep.expert_mode_slot)

        QMetaObject.connectSlotsByName(CorrectorStep)
    # setupUi

    def retranslateUi(self, CorrectorStep):
        CorrectorStep.setWindowTitle("")
        CorrectorStep.setStyleSheet(QCoreApplication.translate("CorrectorStep", u"font: 10pt \"Roboto-Regular\";", None))
        self.label_6.setText("")
        self.label_15.setText(QCoreApplication.translate("CorrectorStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Events to correct</span> (previously added in the accessory file)</p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("CorrectorStep", u"Event Group of the events to correct", None))
        self.label_17.setText(QCoreApplication.translate("CorrectorStep", u"Event Name of the events to correct", None))
        self.label_7.setText("")
        self.label.setText(QCoreApplication.translate("CorrectorStep", u"<html><head/><body><p><span style=\" font-weight:600;\">ICA</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("CorrectorStep", u"Event Group of the corrected REMs", None))
        self.group_lineEdit.setText(QCoreApplication.translate("CorrectorStep", u"REMs_Poulin", None))
        self.label_12.setText(QCoreApplication.translate("CorrectorStep", u"Event Name of the corrected REMs", None))
        self.name_lineEdit.setText(QCoreApplication.translate("CorrectorStep", u"REMs_Poulin_Cor", None))
        self.label_8.setText(QCoreApplication.translate("CorrectorStep", u"Computational window length (s)", None))
#if QT_CONFIG(tooltip)
        self.window_sec_doubleSpinBox.setToolTip(QCoreApplication.translate("CorrectorStep", u"Must be a divider of the sleep stage's window lenght (30 sec in most case). Check Expert Mode to edit.", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("CorrectorStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Accidental mutual information</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("CorrectorStep", u"Component is removed based on a threshold:", None))
#if QT_CONFIG(tooltip)
        self.cycle_radioButton.setToolTip(QCoreApplication.translate("CorrectorStep", u"A threshold value is computed for each channel at each sleep cycle.", None))
#endif // QT_CONFIG(tooltip)
        self.cycle_radioButton.setText(QCoreApplication.translate("CorrectorStep", u" for each sleep cycle", None))
#if QT_CONFIG(tooltip)
        self.recording_radioButton.setToolTip(QCoreApplication.translate("CorrectorStep", u"A threshold value is computed for each channel for the whole recording.", None))
#endif // QT_CONFIG(tooltip)
        self.recording_radioButton.setText(QCoreApplication.translate("CorrectorStep", u"for the whole recording", None))
        self.label_3.setText(QCoreApplication.translate("CorrectorStep", u"Threshold based on a confidence level of", None))
#if QT_CONFIG(tooltip)
        self.p_val_doubleSpinBox.setToolTip(QCoreApplication.translate("CorrectorStep", u"The null hypothesis is 2 signals share an expected (normal) mutual information. \n"
"We want to reject the null hypothesis with a degree of confidence. Check Expert Mode to edit.", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("CorrectorStep", u"Probability distribution of EEG and EOG values", None))
#if QT_CONFIG(tooltip)
        self.n_iter_spinBox.setToolTip(QCoreApplication.translate("CorrectorStep", u"Check Expert Mode to edit. The number of iteration to compute the Accidental Mutual Infomation, do not confuse with the iteration for the ICA.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("CorrectorStep", u"Number of iteration", None))
#if QT_CONFIG(tooltip)
        self.eeg_bin_spinBox.setToolTip(QCoreApplication.translate("CorrectorStep", u"Rescaling parameter to compute probability. Check Expert Mode to edit.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("CorrectorStep", u"Number of bin to encode the EEG", None))
        self.label_4.setText(QCoreApplication.translate("CorrectorStep", u"Number of bin to encore the EOG", None))
#if QT_CONFIG(tooltip)
        self.eog_bin_spinBox.setToolTip(QCoreApplication.translate("CorrectorStep", u"Rescaling parameter to compute probability. Check Expert Mode to edit.", None))
#endif // QT_CONFIG(tooltip)
        self.expert_mode_checkBox.setText(QCoreApplication.translate("CorrectorStep", u"Expert Mode", None))
        self.label_18.setText(QCoreApplication.translate("CorrectorStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Filter/reduce components</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("CorrectorStep", u"Maximum number of components to remove", None))
    # retranslateUi

