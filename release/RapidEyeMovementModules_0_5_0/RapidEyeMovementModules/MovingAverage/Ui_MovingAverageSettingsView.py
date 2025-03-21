# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MovingAverageSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MovingAverageSettingsView(object):
    def setupUi(self, MovingAverageSettingsView):
        if not MovingAverageSettingsView.objectName():
            MovingAverageSettingsView.setObjectName(u"MovingAverageSettingsView")
        MovingAverageSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(MovingAverageSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.win_len_sec_horizontalLayout = QHBoxLayout()
        self.win_len_sec_horizontalLayout.setObjectName(u"win_len_sec_horizontalLayout")
        self.win_len_sec_label = QLabel(MovingAverageSettingsView)
        self.win_len_sec_label.setObjectName(u"win_len_sec_label")
        self.win_len_sec_label.setMinimumSize(QSize(105, 0))

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_label)

        self.win_len_sec_lineedit = QLineEdit(MovingAverageSettingsView)
        self.win_len_sec_lineedit.setObjectName(u"win_len_sec_lineedit")

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_lineedit)


        self.verticalLayout.addLayout(self.win_len_sec_horizontalLayout)

        self.win_step_sec_horizontalLayout = QHBoxLayout()
        self.win_step_sec_horizontalLayout.setObjectName(u"win_step_sec_horizontalLayout")
        self.win_step_sec_label = QLabel(MovingAverageSettingsView)
        self.win_step_sec_label.setObjectName(u"win_step_sec_label")
        self.win_step_sec_label.setMinimumSize(QSize(105, 0))

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_label)

        self.win_step_sec_lineedit = QLineEdit(MovingAverageSettingsView)
        self.win_step_sec_lineedit.setObjectName(u"win_step_sec_lineedit")
        self.win_step_sec_lineedit.setEnabled(False)

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_lineedit)


        self.verticalLayout.addLayout(self.win_step_sec_horizontalLayout)

        self.checkBox_win_step_1sample = QCheckBox(MovingAverageSettingsView)
        self.checkBox_win_step_1sample.setObjectName(u"checkBox_win_step_1sample")
        self.checkBox_win_step_1sample.setEnabled(False)
        self.checkBox_win_step_1sample.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_win_step_1sample)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MovingAverageSettingsView)
        self.checkBox_win_step_1sample.clicked.connect(MovingAverageSettingsView.update_window_step_slot)

        QMetaObject.connectSlotsByName(MovingAverageSettingsView)
    # setupUi

    def retranslateUi(self, MovingAverageSettingsView):
        MovingAverageSettingsView.setWindowTitle(QCoreApplication.translate("MovingAverageSettingsView", u"Form", None))
        self.win_len_sec_label.setText(QCoreApplication.translate("MovingAverageSettingsView", u"Window length (sec)", None))
        self.win_step_sec_label.setText(QCoreApplication.translate("MovingAverageSettingsView", u"Window step (sec)", None))
        self.checkBox_win_step_1sample.setText(QCoreApplication.translate("MovingAverageSettingsView", u"Window step is a single sample", None))
    # retranslateUi

