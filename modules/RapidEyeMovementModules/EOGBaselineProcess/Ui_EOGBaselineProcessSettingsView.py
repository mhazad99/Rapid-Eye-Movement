# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EOGBaselineProcessSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_EOGBaselineProcessSettingsView(object):
    def setupUi(self, EOGBaselineProcessSettingsView):
        if not EOGBaselineProcessSettingsView.objectName():
            EOGBaselineProcessSettingsView.setObjectName(u"EOGBaselineProcessSettingsView")
        EOGBaselineProcessSettingsView.resize(711, 333)
        EOGBaselineProcessSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(EOGBaselineProcessSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(EOGBaselineProcessSettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(EOGBaselineProcessSettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.sleep_stages_horizontalLayout = QHBoxLayout()
        self.sleep_stages_horizontalLayout.setObjectName(u"sleep_stages_horizontalLayout")
        self.sleep_stages_label = QLabel(EOGBaselineProcessSettingsView)
        self.sleep_stages_label.setObjectName(u"sleep_stages_label")

        self.sleep_stages_horizontalLayout.addWidget(self.sleep_stages_label)

        self.sleep_stages_lineedit = QLineEdit(EOGBaselineProcessSettingsView)
        self.sleep_stages_lineedit.setObjectName(u"sleep_stages_lineedit")

        self.sleep_stages_horizontalLayout.addWidget(self.sleep_stages_lineedit)


        self.verticalLayout.addLayout(self.sleep_stages_horizontalLayout)

        self.parameters_horizontalLayout = QHBoxLayout()
        self.parameters_horizontalLayout.setObjectName(u"parameters_horizontalLayout")
        self.parameters_label = QLabel(EOGBaselineProcessSettingsView)
        self.parameters_label.setObjectName(u"parameters_label")

        self.parameters_horizontalLayout.addWidget(self.parameters_label)

        self.parameters_lineedit = QLineEdit(EOGBaselineProcessSettingsView)
        self.parameters_lineedit.setObjectName(u"parameters_lineedit")

        self.parameters_horizontalLayout.addWidget(self.parameters_lineedit)


        self.verticalLayout.addLayout(self.parameters_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(EOGBaselineProcessSettingsView)

        QMetaObject.connectSlotsByName(EOGBaselineProcessSettingsView)
    # setupUi

    def retranslateUi(self, EOGBaselineProcessSettingsView):
        EOGBaselineProcessSettingsView.setWindowTitle(QCoreApplication.translate("EOGBaselineProcessSettingsView", u"Form", None))
        self.signals_label.setText(QCoreApplication.translate("EOGBaselineProcessSettingsView", u"signals", None))
        self.sleep_stages_label.setText(QCoreApplication.translate("EOGBaselineProcessSettingsView", u"sleep_stages", None))
        self.parameters_label.setText(QCoreApplication.translate("EOGBaselineProcessSettingsView", u"parameters", None))
    # retranslateUi

