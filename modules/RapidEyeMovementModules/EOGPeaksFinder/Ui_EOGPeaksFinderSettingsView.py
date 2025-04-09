# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EOGPeaksFinderSettingsView.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_EOGPeaksFinderSettingsView(object):
    def setupUi(self, EOGPeaksFinderSettingsView):
        if not EOGPeaksFinderSettingsView.objectName():
            EOGPeaksFinderSettingsView.setObjectName(u"EOGPeaksFinderSettingsView")
        EOGPeaksFinderSettingsView.resize(886, 318)
        EOGPeaksFinderSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_2 = QHBoxLayout(EOGPeaksFinderSettingsView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(EOGPeaksFinderSettingsView)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(EOGPeaksFinderSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.doubleSpinBox_findP_minZ = QDoubleSpinBox(EOGPeaksFinderSettingsView)
        self.doubleSpinBox_findP_minZ.setObjectName(u"doubleSpinBox_findP_minZ")
        self.doubleSpinBox_findP_minZ.setMinimum(-1.000000000000000)
        self.doubleSpinBox_findP_minZ.setMaximum(10.000000000000000)
        self.doubleSpinBox_findP_minZ.setSingleStep(0.250000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_findP_minZ, 0, 1, 1, 1)

        self.label_4 = QLabel(EOGPeaksFinderSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_3 = QLabel(EOGPeaksFinderSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.doubleSpinBox_findP_minInterv = QDoubleSpinBox(EOGPeaksFinderSettingsView)
        self.doubleSpinBox_findP_minInterv.setObjectName(u"doubleSpinBox_findP_minInterv")
        self.doubleSpinBox_findP_minInterv.setMaximum(30.000000000000000)
        self.doubleSpinBox_findP_minInterv.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_findP_minInterv, 1, 1, 1, 1)

        self.label_5 = QLabel(EOGPeaksFinderSettingsView)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(64, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.retranslateUi(EOGPeaksFinderSettingsView)
        self.doubleSpinBox_findP_minInterv.editingFinished.connect(EOGPeaksFinderSettingsView.update_parameters_slot)
        self.doubleSpinBox_findP_minZ.editingFinished.connect(EOGPeaksFinderSettingsView.update_parameters_slot)

        QMetaObject.connectSlotsByName(EOGPeaksFinderSettingsView)
    # setupUi

    def retranslateUi(self, EOGPeaksFinderSettingsView):
        EOGPeaksFinderSettingsView.setWindowTitle(QCoreApplication.translate("EOGPeaksFinderSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("EOGPeaksFinderSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">EOG Peaks Finder</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("EOGPeaksFinderSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Min Height</span> : Required height of peaks. (z-score threshold)</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("EOGPeaksFinderSettingsView", u"Default value is 1.5", None))
        self.label_3.setText(QCoreApplication.translate("EOGPeaksFinderSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Min Interval</span> : Required minimal time window between neighbouring peaks (sec)</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("EOGPeaksFinderSettingsView", u"Default value is 0.5", None))
    # retranslateUi

