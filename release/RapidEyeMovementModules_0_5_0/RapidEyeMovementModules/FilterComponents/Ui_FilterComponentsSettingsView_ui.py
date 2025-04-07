# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FilterComponentsSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FilterComponentsSettingsView(object):
    def setupUi(self, FilterComponentsSettingsView):
        if not FilterComponentsSettingsView.objectName():
            FilterComponentsSettingsView.setObjectName(u"FilterComponentsSettingsView")
        FilterComponentsSettingsView.resize(555, 423)
        self.verticalLayout = QVBoxLayout(FilterComponentsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(FilterComponentsSettingsView)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(336, 0))
        self.Title.setMaximumSize(QSize(336, 16777215))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Title)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(FilterComponentsSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(110, 0))
        self.label_2.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.threshold_doubleSpinBox = QDoubleSpinBox(FilterComponentsSettingsView)
        self.threshold_doubleSpinBox.setObjectName(u"threshold_doubleSpinBox")
        self.threshold_doubleSpinBox.setEnabled(False)
        self.threshold_doubleSpinBox.setMinimumSize(QSize(80, 0))
        self.threshold_doubleSpinBox.setMaximumSize(QSize(80, 16777215))
        self.threshold_doubleSpinBox.setDecimals(3)
        self.threshold_doubleSpinBox.setMaximum(10000.000000000000000)
        self.threshold_doubleSpinBox.setSingleStep(0.010000000000000)
        self.threshold_doubleSpinBox.setValue(2.000000000000000)

        self.horizontalLayout_4.addWidget(self.threshold_doubleSpinBox)

        self.threshold_checkBox = QCheckBox(FilterComponentsSettingsView)
        self.threshold_checkBox.setObjectName(u"threshold_checkBox")

        self.horizontalLayout_4.addWidget(self.threshold_checkBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(FilterComponentsSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.group_lineEdit = QLineEdit(FilterComponentsSettingsView)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setMinimumSize(QSize(133, 0))
        self.group_lineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.group_lineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(FilterComponentsSettingsView)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(110, 0))
        self.label.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_5.addWidget(self.label)

        self.events_name_lineEdit = QLineEdit(FilterComponentsSettingsView)
        self.events_name_lineEdit.setObjectName(u"events_name_lineEdit")
        self.events_name_lineEdit.setMinimumSize(QSize(133, 0))
        self.events_name_lineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.events_name_lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(FilterComponentsSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(110, 0))
        self.label_4.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout.addWidget(self.label_4)

        self.channel_lineEdit = QLineEdit(FilterComponentsSettingsView)
        self.channel_lineEdit.setObjectName(u"channel_lineEdit")
        self.channel_lineEdit.setMinimumSize(QSize(133, 0))
        self.channel_lineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.channel_lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 246, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(FilterComponentsSettingsView)
        self.threshold_checkBox.clicked.connect(FilterComponentsSettingsView.threshold_changed)

        QMetaObject.connectSlotsByName(FilterComponentsSettingsView)
    # setupUi

    def retranslateUi(self, FilterComponentsSettingsView):
        FilterComponentsSettingsView.setWindowTitle(QCoreApplication.translate("FilterComponentsSettingsView", u"Form", None))
        self.Title.setText(QCoreApplication.translate("FilterComponentsSettingsView", u"FilterComponents settings", None))
        self.label_2.setText(QCoreApplication.translate("FilterComponentsSettingsView", u"threshold", None))
#if QT_CONFIG(tooltip)
        self.threshold_doubleSpinBox.setToolTip(QCoreApplication.translate("FilterComponentsSettingsView", u"Threshold to choose which component is deleted. The one with the highest value above the threshold will be chosen.", None))
#endif // QT_CONFIG(tooltip)
        self.threshold_checkBox.setText(QCoreApplication.translate("FilterComponentsSettingsView", u"Manual entry", None))
        self.label_3.setText(QCoreApplication.translate("FilterComponentsSettingsView", u"Event Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("FilterComponentsSettingsView", u"New group for event...", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("FilterComponentsSettingsView", u"Event Name", None))
#if QT_CONFIG(tooltip)
        self.events_name_lineEdit.setToolTip(QCoreApplication.translate("FilterComponentsSettingsView", u"New event name...", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("FilterComponentsSettingsView", u"Event Channel", None))
    # retranslateUi

