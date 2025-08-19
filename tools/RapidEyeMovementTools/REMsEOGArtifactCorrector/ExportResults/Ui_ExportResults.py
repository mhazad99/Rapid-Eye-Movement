# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ExportResults.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_ExportResults(object):
    def setupUi(self, ExportResults):
        if not ExportResults.objectName():
            ExportResults.setObjectName(u"ExportResults")
        ExportResults.setEnabled(True)
        ExportResults.resize(862, 682)
        self.verticalLayout = QVBoxLayout(ExportResults)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(ExportResults)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.Suffix_lineEdit = QLineEdit(ExportResults)
        self.Suffix_lineEdit.setObjectName(u"Suffix_lineEdit")

        self.gridLayout.addWidget(self.Suffix_lineEdit, 2, 1, 1, 1)

        self.label = QLabel(ExportResults)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.label_2 = QLabel(ExportResults)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(ExportResults)

        QMetaObject.connectSlotsByName(ExportResults)
    # setupUi

    def retranslateUi(self, ExportResults):
        ExportResults.setWindowTitle("")
        ExportResults.setStyleSheet(QCoreApplication.translate("ExportResults", u"font: 10pt \"Roboto-Regular\";", None))
        self.label_3.setText(QCoreApplication.translate("ExportResults", u"<html><head/><body><p><span style=\" font-size:12pt;\">Add a suffix for the corrected files' names:</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("ExportResults", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Export Results</span></p></body></html>", None))
        self.label_2.setText("")
    # retranslateUi

