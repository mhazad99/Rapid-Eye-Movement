# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FilterComponentsResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FilterComponentsResultsView(object):
    def setupUi(self, FilterComponentsResultsView):
        if not FilterComponentsResultsView.objectName():
            FilterComponentsResultsView.setObjectName(u"FilterComponentsResultsView")
        FilterComponentsResultsView.resize(633, 139)
        self.gridLayout = QGridLayout(FilterComponentsResultsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(FilterComponentsResultsView)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(FilterComponentsResultsView)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.event_index_lineEdit = QLineEdit(FilterComponentsResultsView)
        self.event_index_lineEdit.setObjectName(u"event_index_lineEdit")

        self.horizontalLayout.addWidget(self.event_index_lineEdit)

        self.prev_but = QPushButton(FilterComponentsResultsView)
        self.prev_but.setObjectName(u"prev_but")
        self.prev_but.setEnabled(True)

        self.horizontalLayout.addWidget(self.prev_but)

        self.next_but = QPushButton(FilterComponentsResultsView)
        self.next_but.setObjectName(u"next_but")
        self.next_but.setEnabled(True)

        self.horizontalLayout.addWidget(self.next_but)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(FilterComponentsResultsView)
        self.next_but.clicked.connect(FilterComponentsResultsView.on_next_button)
        self.prev_but.clicked.connect(FilterComponentsResultsView.on_prev_button)
        self.event_index_lineEdit.editingFinished.connect(FilterComponentsResultsView.on_event_index_changed)

        QMetaObject.connectSlotsByName(FilterComponentsResultsView)
    # setupUi

    def retranslateUi(self, FilterComponentsResultsView):
        FilterComponentsResultsView.setWindowTitle(QCoreApplication.translate("FilterComponentsResultsView", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("FilterComponentsResultsView", u"Display signals from events", None))
        self.label_4.setText(QCoreApplication.translate("FilterComponentsResultsView", u"Event Number", None))
        self.event_index_lineEdit.setText(QCoreApplication.translate("FilterComponentsResultsView", u"0", None))
#if QT_CONFIG(tooltip)
        self.prev_but.setToolTip(QCoreApplication.translate("FilterComponentsResultsView", u"Display the previous window (window length will be added to the time elapsed).", None))
#endif // QT_CONFIG(tooltip)
        self.prev_but.setText(QCoreApplication.translate("FilterComponentsResultsView", u"<<", None))
#if QT_CONFIG(tooltip)
        self.next_but.setToolTip(QCoreApplication.translate("FilterComponentsResultsView", u"Display the next window (window length will be added to the time elapsed).", None))
#endif // QT_CONFIG(tooltip)
        self.next_but.setText(QCoreApplication.translate("FilterComponentsResultsView", u">>", None))
    # retranslateUi

