# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DerivativeApproxSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_DerivativeApproxSettingsView(object):
    def setupUi(self, DerivativeApproxSettingsView):
        if not DerivativeApproxSettingsView.objectName():
            DerivativeApproxSettingsView.setObjectName(u"DerivativeApproxSettingsView")
        DerivativeApproxSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(DerivativeApproxSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.order_horizontalLayout = QHBoxLayout()
        self.order_horizontalLayout.setObjectName(u"order_horizontalLayout")
        self.order_label = QLabel(DerivativeApproxSettingsView)
        self.order_label.setObjectName(u"order_label")

        self.order_horizontalLayout.addWidget(self.order_label)

        self.order_spinBox = QSpinBox(DerivativeApproxSettingsView)
        self.order_spinBox.setObjectName(u"order_spinBox")
        self.order_spinBox.setMinimumSize(QSize(100, 0))
        self.order_spinBox.setMinimum(1)
        self.order_spinBox.setMaximum(10000)

        self.order_horizontalLayout.addWidget(self.order_spinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.order_horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.order_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DerivativeApproxSettingsView)

        QMetaObject.connectSlotsByName(DerivativeApproxSettingsView)
    # setupUi

    def retranslateUi(self, DerivativeApproxSettingsView):
        DerivativeApproxSettingsView.setWindowTitle(QCoreApplication.translate("DerivativeApproxSettingsView", u"Form", None))
        self.order_label.setText(QCoreApplication.translate("DerivativeApproxSettingsView", u"order", None))
    # retranslateUi

