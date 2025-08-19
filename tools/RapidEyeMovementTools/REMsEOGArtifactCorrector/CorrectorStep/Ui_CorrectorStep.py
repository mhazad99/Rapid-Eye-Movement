# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CorrectorStep.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)
import themes_rc

class Ui_CorrectorStep(object):
    def setupUi(self, CorrectorStep):
        if not CorrectorStep.objectName():
            CorrectorStep.setObjectName(u"CorrectorStep")
        CorrectorStep.resize(726, 724)
        self.horizontalLayout_3 = QHBoxLayout(CorrectorStep)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.label_2 = QLabel(CorrectorStep)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.Sharpness_doubleSpinBox = QDoubleSpinBox(CorrectorStep)
        self.Sharpness_doubleSpinBox.setObjectName(u"Sharpness_doubleSpinBox")
        self.Sharpness_doubleSpinBox.setMaximum(1.000000000000000)
        self.Sharpness_doubleSpinBox.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.Sharpness_doubleSpinBox, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.label_6 = QLabel(CorrectorStep)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label = QLabel(CorrectorStep)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(CorrectorStep)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_4 = QLabel(CorrectorStep)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.Number_of_Components_spinBox = QSpinBox(CorrectorStep)
        self.Number_of_Components_spinBox.setObjectName(u"Number_of_Components_spinBox")

        self.gridLayout.addWidget(self.Number_of_Components_spinBox, 2, 1, 1, 1)

        self.label_5 = QLabel(CorrectorStep)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_7 = QLabel(CorrectorStep)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.retranslateUi(CorrectorStep)

        QMetaObject.connectSlotsByName(CorrectorStep)
    # setupUi

    def retranslateUi(self, CorrectorStep):
        CorrectorStep.setWindowTitle("")
        CorrectorStep.setStyleSheet(QCoreApplication.translate("CorrectorStep", u"font: 10pt \"Roboto-Regular\";", None))
        self.label_2.setText(QCoreApplication.translate("CorrectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of Componnents to Remove in SVD</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("CorrectorStep", u"<html><head/><body><p>Defines the number of dominant singular components to remove from the EEG signal<br/>during each REM event segment.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("CorrectorStep", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Common Settings</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("CorrectorStep", u"<html><head/><body><p>Controls the smoothness of the correction's edges. A higher value (e.g., 0.8) means<br/>smoother transitions, while a lower value (e.g., 0.2) means sharper edges.</p></body></html>", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("CorrectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tukey Window Sharpness</span></p></body></html>", None))
        self.label_7.setText("")
    # retranslateUi

