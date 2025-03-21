# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DisplayAnnotationsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DisplayAnnotationsView(object):
    def setupUi(self, DisplayAnnotationsView):
        if not DisplayAnnotationsView.objectName():
            DisplayAnnotationsView.setObjectName(u"DisplayAnnotationsView")
        DisplayAnnotationsView.resize(677, 383)
        self.horizontalLayout = QHBoxLayout(DisplayAnnotationsView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(DisplayAnnotationsView)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_8 = QLabel(DisplayAnnotationsView)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)

        self.pushButtonA = QPushButton(DisplayAnnotationsView)
        self.pushButtonA.setObjectName(u"pushButtonA")

        self.gridLayout_2.addWidget(self.pushButtonA, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.tableWidget = QTableWidget(DisplayAnnotationsView)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_2.addWidget(self.tableWidget, 2, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(DisplayAnnotationsView)
        self.pushButtonA.clicked.connect(DisplayAnnotationsView.slot_UI_buttonA)

        QMetaObject.connectSlotsByName(DisplayAnnotationsView)
    # setupUi

    def retranslateUi(self, DisplayAnnotationsView):
        DisplayAnnotationsView.setWindowTitle(QCoreApplication.translate("DisplayAnnotationsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("DisplayAnnotationsView", u"Display Annotations 0.0.0", None))
        self.pushButtonA.setText(QCoreApplication.translate("DisplayAnnotationsView", u"UI Button A", None))
    # retranslateUi

