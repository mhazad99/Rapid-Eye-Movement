# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SVDFilterSettingsView.ui'
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

class Ui_SVDFilterSettingsView(object):
    def setupUi(self, SVDFilterSettingsView):
        if not SVDFilterSettingsView.objectName():
            SVDFilterSettingsView.setObjectName(u"SVDFilterSettingsView")
        SVDFilterSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        SVDFilterSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(SVDFilterSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(SVDFilterSettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(SVDFilterSettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(SVDFilterSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(SVDFilterSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.events_names_horizontalLayout = QHBoxLayout()
        self.events_names_horizontalLayout.setObjectName(u"events_names_horizontalLayout")
        self.events_names_label = QLabel(SVDFilterSettingsView)
        self.events_names_label.setObjectName(u"events_names_label")

        self.events_names_horizontalLayout.addWidget(self.events_names_label)

        self.events_names_lineedit = QLineEdit(SVDFilterSettingsView)
        self.events_names_lineedit.setObjectName(u"events_names_lineedit")

        self.events_names_horizontalLayout.addWidget(self.events_names_lineedit)


        self.verticalLayout.addLayout(self.events_names_horizontalLayout)

        self.configuration_horizontalLayout = QHBoxLayout()
        self.configuration_horizontalLayout.setObjectName(u"configuration_horizontalLayout")
        self.configuration_label = QLabel(SVDFilterSettingsView)
        self.configuration_label.setObjectName(u"configuration_label")

        self.configuration_horizontalLayout.addWidget(self.configuration_label)

        self.configuration_lineedit = QLineEdit(SVDFilterSettingsView)
        self.configuration_lineedit.setObjectName(u"configuration_lineedit")

        self.configuration_horizontalLayout.addWidget(self.configuration_lineedit)


        self.verticalLayout.addLayout(self.configuration_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SVDFilterSettingsView)

        QMetaObject.connectSlotsByName(SVDFilterSettingsView)
    # setupUi

    def retranslateUi(self, SVDFilterSettingsView):
        SVDFilterSettingsView.setWindowTitle(QCoreApplication.translate("SVDFilterSettingsView", u"Form", None))
        self.signals_label.setText(QCoreApplication.translate("SVDFilterSettingsView", u"signals", None))
        self.events_label.setText(QCoreApplication.translate("SVDFilterSettingsView", u"events", None))
        self.events_names_label.setText(QCoreApplication.translate("SVDFilterSettingsView", u"events_names", None))
        self.configuration_label.setText(QCoreApplication.translate("SVDFilterSettingsView", u"configuration", None))
    # retranslateUi

