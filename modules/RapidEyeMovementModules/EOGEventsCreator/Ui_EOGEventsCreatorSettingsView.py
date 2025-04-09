# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EOGEventsCreatorSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_EOGEventsCreatorSettingsView(object):
    def setupUi(self, EOGEventsCreatorSettingsView):
        if not EOGEventsCreatorSettingsView.objectName():
            EOGEventsCreatorSettingsView.setObjectName(u"EOGEventsCreatorSettingsView")
        EOGEventsCreatorSettingsView.resize(1092, 558)
        EOGEventsCreatorSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_5 = QVBoxLayout(EOGEventsCreatorSettingsView)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSpacer = QSpacerItem(659, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(EOGEventsCreatorSettingsView)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.label = QLabel(EOGEventsCreatorSettingsView)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(EOGEventsCreatorSettingsView)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(600, 0))

        self.horizontalLayout.addWidget(self.label_5)

        self.doubleSpinBox_timeWin = QDoubleSpinBox(EOGEventsCreatorSettingsView)
        self.doubleSpinBox_timeWin.setObjectName(u"doubleSpinBox_timeWin")
        self.doubleSpinBox_timeWin.setDecimals(3)
        self.doubleSpinBox_timeWin.setMaximum(5.000000000000000)
        self.doubleSpinBox_timeWin.setSingleStep(0.010000000000000)
        self.doubleSpinBox_timeWin.setValue(0.665000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_timeWin)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(EOGEventsCreatorSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.checkBox_angle = QCheckBox(EOGEventsCreatorSettingsView)
        self.checkBox_angle.setObjectName(u"checkBox_angle")
        self.checkBox_angle.setMinimumSize(QSize(600, 0))
        self.checkBox_angle.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_angle)

        self.doubleSpinBox_deflection_angle = QDoubleSpinBox(EOGEventsCreatorSettingsView)
        self.doubleSpinBox_deflection_angle.setObjectName(u"doubleSpinBox_deflection_angle")
        self.doubleSpinBox_deflection_angle.setDecimals(0)
        self.doubleSpinBox_deflection_angle.setMaximum(90.000000000000000)
        self.doubleSpinBox_deflection_angle.setSingleStep(5.000000000000000)
        self.doubleSpinBox_deflection_angle.setValue(45.000000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_deflection_angle)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(EOGEventsCreatorSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.checkBox_max_diff_angle = QCheckBox(EOGEventsCreatorSettingsView)
        self.checkBox_max_diff_angle.setObjectName(u"checkBox_max_diff_angle")
        self.checkBox_max_diff_angle.setMinimumSize(QSize(600, 0))

        self.horizontalLayout_4.addWidget(self.checkBox_max_diff_angle)

        self.doubleSpinBox_diff_angle = QDoubleSpinBox(EOGEventsCreatorSettingsView)
        self.doubleSpinBox_diff_angle.setObjectName(u"doubleSpinBox_diff_angle")
        self.doubleSpinBox_diff_angle.setEnabled(True)
        self.doubleSpinBox_diff_angle.setDecimals(0)
        self.doubleSpinBox_diff_angle.setMinimum(5.000000000000000)
        self.doubleSpinBox_diff_angle.setMaximum(45.000000000000000)
        self.doubleSpinBox_diff_angle.setSingleStep(5.000000000000000)
        self.doubleSpinBox_diff_angle.setValue(15.000000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_diff_angle)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.label_6 = QLabel(EOGEventsCreatorSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_6)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_8 = QSpacerItem(20, 18, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.checkBox_slope = QCheckBox(EOGEventsCreatorSettingsView)
        self.checkBox_slope.setObjectName(u"checkBox_slope")

        self.horizontalLayout_6.addWidget(self.checkBox_slope)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.label_9 = QLabel(EOGEventsCreatorSettingsView)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.label_10 = QLabel(EOGEventsCreatorSettingsView)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(600, 0))

        self.horizontalLayout_5.addWidget(self.label_10)

        self.doubleSpinBox_deflection_slope = QDoubleSpinBox(EOGEventsCreatorSettingsView)
        self.doubleSpinBox_deflection_slope.setObjectName(u"doubleSpinBox_deflection_slope")
        self.doubleSpinBox_deflection_slope.setDecimals(2)
        self.doubleSpinBox_deflection_slope.setMaximum(5.000000000000000)
        self.doubleSpinBox_deflection_slope.setSingleStep(0.250000000000000)
        self.doubleSpinBox_deflection_slope.setValue(1.500000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_deflection_slope)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.label_7 = QLabel(EOGEventsCreatorSettingsView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_7)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(1071, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.checkBox_min_z_2nd_chan = QCheckBox(EOGEventsCreatorSettingsView)
        self.checkBox_min_z_2nd_chan.setObjectName(u"checkBox_min_z_2nd_chan")
        self.checkBox_min_z_2nd_chan.setMinimumSize(QSize(600, 0))

        self.horizontalLayout_3.addWidget(self.checkBox_min_z_2nd_chan)

        self.doubleSpinBox_min_z_2nd_chan = QDoubleSpinBox(EOGEventsCreatorSettingsView)
        self.doubleSpinBox_min_z_2nd_chan.setObjectName(u"doubleSpinBox_min_z_2nd_chan")
        self.doubleSpinBox_min_z_2nd_chan.setMaximum(2.000000000000000)
        self.doubleSpinBox_min_z_2nd_chan.setSingleStep(0.250000000000000)
        self.doubleSpinBox_min_z_2nd_chan.setValue(0.250000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_min_z_2nd_chan)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.label_8 = QLabel(EOGEventsCreatorSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_8)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.retranslateUi(EOGEventsCreatorSettingsView)
        self.checkBox_max_diff_angle.clicked.connect(EOGEventsCreatorSettingsView.change_parameters_slot)
        self.checkBox_angle.clicked.connect(EOGEventsCreatorSettingsView.change_parameters_slot)
        self.checkBox_slope.clicked.connect(EOGEventsCreatorSettingsView.change_parameters_slot)
        self.checkBox_min_z_2nd_chan.clicked.connect(EOGEventsCreatorSettingsView.change_parameters_slot)

        QMetaObject.connectSlotsByName(EOGEventsCreatorSettingsView)
    # setupUi

    def retranslateUi(self, EOGEventsCreatorSettingsView):
        EOGEventsCreatorSettingsView.setWindowTitle(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">EOG Events Creator</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"To identify the onset, the peak and the end of a REM (Rapid Eye Movement).  Some artifacts are also identified.", None))
        self.label_5.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"<html><head/><body><p>Time window (sec) to find the nearest intersections, one before the peak and one after the peak.</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"Default value is 0.665 sec", None))
        self.checkBox_angle.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"Minimum deflection angle (degree) to class the event as a REM", None))
        self.label_3.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"Default value is 45 degree angle", None))
        self.checkBox_max_diff_angle.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"Maximum deflection angle (degree) difference between EOG channels", None))
        self.label_6.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"Default value is 15 degree angle", None))
        self.checkBox_slope.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"REM slope consistency", None))
        self.label_9.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"The slope between the intersection and the peak is divided into 4 parts.  Only events with a slope variation under the threshold are marked as REM.", None))
        self.label_10.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"Maximum standard deviation of the deflection slope", None))
        self.label_7.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"Default value is 1.5", None))
        self.checkBox_min_z_2nd_chan.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"Minimum amplitude (z-score) of the second EOG channel", None))
        self.label_8.setText(QCoreApplication.translate("EOGEventsCreatorSettingsView", u"Default value is 0.25", None))
    # retranslateUi

