# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SignalsCombineSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_SignalsCombineSettingsView(object):
    def setupUi(self, SignalsCombineSettingsView):
        if not SignalsCombineSettingsView.objectName():
            SignalsCombineSettingsView.setObjectName(u"SignalsCombineSettingsView")
        SignalsCombineSettingsView.resize(415, 224)
        self.layoutWidget = QWidget(SignalsCombineSettingsView)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 248, 46))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)


        self.retranslateUi(SignalsCombineSettingsView)

        QMetaObject.connectSlotsByName(SignalsCombineSettingsView)
    # setupUi

    def retranslateUi(self, SignalsCombineSettingsView):
        SignalsCombineSettingsView.setWindowTitle(QCoreApplication.translate("SignalsCombineSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("SignalsCombineSettingsView", u"SignalsCombine settings", None))
    # retranslateUi

