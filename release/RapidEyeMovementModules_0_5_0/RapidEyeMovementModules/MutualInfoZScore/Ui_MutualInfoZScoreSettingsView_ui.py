# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MutualInfoZScoreSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MutualInfoZScoreSettingsView(object):
    def setupUi(self, MutualInfoZScoreSettingsView):
        if not MutualInfoZScoreSettingsView.objectName():
            MutualInfoZScoreSettingsView.setObjectName(u"MutualInfoZScoreSettingsView")
        MutualInfoZScoreSettingsView.resize(790, 209)
        self.gridLayout = QGridLayout(MutualInfoZScoreSettingsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(MutualInfoZScoreSettingsView)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.computing_win_len = QLabel(MutualInfoZScoreSettingsView)
        self.computing_win_len.setObjectName(u"computing_win_len")
        self.computing_win_len.setMinimumSize(QSize(140, 0))
        self.computing_win_len.setMaximumSize(QSize(140, 16777215))
        self.computing_win_len.setWordWrap(True)

        self.horizontalLayout.addWidget(self.computing_win_len)

        self.mean_doubleSpinBox = QDoubleSpinBox(MutualInfoZScoreSettingsView)
        self.mean_doubleSpinBox.setObjectName(u"mean_doubleSpinBox")
        self.mean_doubleSpinBox.setEnabled(False)
        self.mean_doubleSpinBox.setMinimumSize(QSize(80, 0))
        self.mean_doubleSpinBox.setMaximumSize(QSize(80, 16777215))
        self.mean_doubleSpinBox.setDecimals(3)
        self.mean_doubleSpinBox.setMinimum(0.000000000000000)
        self.mean_doubleSpinBox.setMaximum(9999.000000000000000)
        self.mean_doubleSpinBox.setSingleStep(0.010000000000000)
        self.mean_doubleSpinBox.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.mean_doubleSpinBox)

        self.mean_checkBox = QCheckBox(MutualInfoZScoreSettingsView)
        self.mean_checkBox.setObjectName(u"mean_checkBox")

        self.horizontalLayout.addWidget(self.mean_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(MutualInfoZScoreSettingsView)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(140, 0))
        self.label.setMaximumSize(QSize(140, 16777215))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.std_doubleSpinBox = QDoubleSpinBox(MutualInfoZScoreSettingsView)
        self.std_doubleSpinBox.setObjectName(u"std_doubleSpinBox")
        self.std_doubleSpinBox.setEnabled(False)
        self.std_doubleSpinBox.setMinimumSize(QSize(80, 0))
        self.std_doubleSpinBox.setMaximumSize(QSize(80, 16777215))
        self.std_doubleSpinBox.setDecimals(3)
        self.std_doubleSpinBox.setMaximum(10000.000000000000000)
        self.std_doubleSpinBox.setSingleStep(0.001000000000000)
        self.std_doubleSpinBox.setValue(0.050000000000000)

        self.horizontalLayout_3.addWidget(self.std_doubleSpinBox)

        self.std_checkBox = QCheckBox(MutualInfoZScoreSettingsView)
        self.std_checkBox.setObjectName(u"std_checkBox")

        self.horizontalLayout_3.addWidget(self.std_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(MutualInfoZScoreSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(140, 0))
        self.label_2.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.criteria_doubleSpinBox = QDoubleSpinBox(MutualInfoZScoreSettingsView)
        self.criteria_doubleSpinBox.setObjectName(u"criteria_doubleSpinBox")
        self.criteria_doubleSpinBox.setEnabled(False)
        self.criteria_doubleSpinBox.setMinimumSize(QSize(80, 0))
        self.criteria_doubleSpinBox.setMaximumSize(QSize(80, 16777215))
        self.criteria_doubleSpinBox.setDecimals(3)
        self.criteria_doubleSpinBox.setMaximum(10000.000000000000000)
        self.criteria_doubleSpinBox.setSingleStep(0.010000000000000)
        self.criteria_doubleSpinBox.setValue(2.000000000000000)

        self.horizontalLayout_4.addWidget(self.criteria_doubleSpinBox)

        self.criteria_checkBox = QCheckBox(MutualInfoZScoreSettingsView)
        self.criteria_checkBox.setObjectName(u"criteria_checkBox")

        self.horizontalLayout_4.addWidget(self.criteria_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(MutualInfoZScoreSettingsView)
        self.criteria_checkBox.clicked.connect(MutualInfoZScoreSettingsView.criteria_changed)
        self.std_checkBox.clicked.connect(MutualInfoZScoreSettingsView.std_changed)
        self.mean_checkBox.clicked.connect(MutualInfoZScoreSettingsView.mean_changed)

        QMetaObject.connectSlotsByName(MutualInfoZScoreSettingsView)
    # setupUi

    def retranslateUi(self, MutualInfoZScoreSettingsView):
        MutualInfoZScoreSettingsView.setWindowTitle(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"Form", None))
        self.Title.setText(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"MutualInfoZScore settings", None))
        self.computing_win_len.setText(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"Mean", None))
#if QT_CONFIG(tooltip)
        self.mean_doubleSpinBox.setToolTip(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"The mean of the distribution from random mutual information found in a recording.", None))
#endif // QT_CONFIG(tooltip)
        self.mean_checkBox.setText(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"Manual entry", None))
        self.label.setText(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"Standard deviation", None))
#if QT_CONFIG(tooltip)
        self.std_doubleSpinBox.setToolTip(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"The standard deviation of the distribution from random mutual information found in a recording.", None))
#endif // QT_CONFIG(tooltip)
        self.std_checkBox.setText(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"Manual entry", None))
        self.label_2.setText(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"Criteria", None))
#if QT_CONFIG(tooltip)
        self.criteria_doubleSpinBox.setToolTip(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"Threshold to add in result view.", None))
#endif // QT_CONFIG(tooltip)
        self.criteria_checkBox.setText(QCoreApplication.translate("MutualInfoZScoreSettingsView", u"Manual entry", None))
    # retranslateUi

