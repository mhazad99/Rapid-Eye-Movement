# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_RemDetectorSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_RemDetectorSettingsView(object):
    def setupUi(self, RemDetectorSettingsView):
        if not RemDetectorSettingsView.objectName():
            RemDetectorSettingsView.setObjectName(u"RemDetectorSettingsView")
        RemDetectorSettingsView.resize(711, 333)
        self.horizontalLayout = QHBoxLayout(RemDetectorSettingsView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.percentile_spinBox = QSpinBox(RemDetectorSettingsView)
        self.percentile_spinBox.setObjectName(u"percentile_spinBox")
        self.percentile_spinBox.setMinimumSize(QSize(50, 0))
        self.percentile_spinBox.setMaximumSize(QSize(150, 16777215))
        self.percentile_spinBox.setMaximum(100)
        self.percentile_spinBox.setValue(65)

        self.gridLayout.addWidget(self.percentile_spinBox, 4, 1, 1, 1)

        self.group_lineEdit = QLineEdit(RemDetectorSettingsView)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setMinimumSize(QSize(50, 0))
        self.group_lineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.group_lineEdit, 0, 1, 1, 1)

        self.percentile_label = QLabel(RemDetectorSettingsView)
        self.percentile_label.setObjectName(u"percentile_label")
        self.percentile_label.setMinimumSize(QSize(170, 0))

        self.gridLayout.addWidget(self.percentile_label, 4, 0, 1, 1)

        self.border_effect_label = QLabel(RemDetectorSettingsView)
        self.border_effect_label.setObjectName(u"border_effect_label")

        self.gridLayout.addWidget(self.border_effect_label, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.name_lineEdit = QLineEdit(RemDetectorSettingsView)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(50, 0))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.name_lineEdit, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 2, 1, 1)

        self.border_effect_spinBox = QSpinBox(RemDetectorSettingsView)
        self.border_effect_spinBox.setObjectName(u"border_effect_spinBox")
        self.border_effect_spinBox.setMinimumSize(QSize(50, 0))
        self.border_effect_spinBox.setMaximumSize(QSize(150, 16777215))
        self.border_effect_spinBox.setMaximum(100)
        self.border_effect_spinBox.setValue(10)

        self.gridLayout.addWidget(self.border_effect_spinBox, 3, 1, 1, 1)

        self.label_2 = QLabel(RemDetectorSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(RemDetectorSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label = QLabel(RemDetectorSettingsView)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.channel_lineEdit = QLineEdit(RemDetectorSettingsView)
        self.channel_lineEdit.setObjectName(u"channel_lineEdit")

        self.gridLayout.addWidget(self.channel_lineEdit, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(316, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(RemDetectorSettingsView)

        QMetaObject.connectSlotsByName(RemDetectorSettingsView)
    # setupUi

    def retranslateUi(self, RemDetectorSettingsView):
        RemDetectorSettingsView.setWindowTitle(QCoreApplication.translate("RemDetectorSettingsView", u"Form", None))
        self.percentile_label.setText(QCoreApplication.translate("RemDetectorSettingsView", u"Threshold in Percentile", None))
        self.border_effect_label.setText(QCoreApplication.translate("RemDetectorSettingsView", u"Border effect (%)", None))
        self.label_2.setText(QCoreApplication.translate("RemDetectorSettingsView", u"Event Group", None))
        self.label_3.setText(QCoreApplication.translate("RemDetectorSettingsView", u"Event Name", None))
        self.label.setText(QCoreApplication.translate("RemDetectorSettingsView", u"Event Channel", None))
    # retranslateUi

