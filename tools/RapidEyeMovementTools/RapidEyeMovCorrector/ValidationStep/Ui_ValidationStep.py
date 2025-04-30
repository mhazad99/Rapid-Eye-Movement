# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ValidationStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QSizePolicy, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_ValidationStep(object):
    def setupUi(self, ValidationStep):
        if not ValidationStep.objectName():
            ValidationStep.setObjectName(u"ValidationStep")
        ValidationStep.setEnabled(True)
        ValidationStep.resize(730, 590)
        self.validation_checkBox = QCheckBox(ValidationStep)
        self.validation_checkBox.setObjectName(u"validation_checkBox")
        self.validation_checkBox.setGeometry(QRect(0, 0, 200, 30))
        self.validation_checkBox.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(11)
        self.validation_checkBox.setFont(font)
        self.validation_checkBox.setChecked(True)
        self.verticalLayout = QVBoxLayout(ValidationStep)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.retranslateUi(ValidationStep)
        self.validation_checkBox.toggled.connect(ValidationStep.on_active_validation)

        QMetaObject.connectSlotsByName(ValidationStep)
    # setupUi

    def retranslateUi(self, ValidationStep):
        ValidationStep.setWindowTitle("")
        ValidationStep.setStyleSheet(QCoreApplication.translate("ValidationStep", u"font: 10pt \"Roboto-Regular\";", None))
        self.validation_checkBox.setText(QCoreApplication.translate("ValidationStep", u"Use validation step", None))
    # retranslateUi

