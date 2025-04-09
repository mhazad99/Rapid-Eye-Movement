# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AccidentalMutualInfoSettingsView.ui'
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
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_AccidentalMutualInfoSettingsView(object):
    def setupUi(self, AccidentalMutualInfoSettingsView):
        if not AccidentalMutualInfoSettingsView.objectName():
            AccidentalMutualInfoSettingsView.setObjectName(u"AccidentalMutualInfoSettingsView")
        AccidentalMutualInfoSettingsView.resize(482, 366)
        self.horizontalLayout = QHBoxLayout(AccidentalMutualInfoSettingsView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Title = QLabel(AccidentalMutualInfoSettingsView)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.Title)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(AccidentalMutualInfoSettingsView)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(AccidentalMutualInfoSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.max_iter_spinBox = QSpinBox(AccidentalMutualInfoSettingsView)
        self.max_iter_spinBox.setObjectName(u"max_iter_spinBox")
        self.max_iter_spinBox.setMaximum(1000000)
        self.max_iter_spinBox.setSingleStep(50)
        self.max_iter_spinBox.setValue(1000)

        self.gridLayout.addWidget(self.max_iter_spinBox, 0, 1, 1, 1)

        self.p_val_doubleSpinBox = QDoubleSpinBox(AccidentalMutualInfoSettingsView)
        self.p_val_doubleSpinBox.setObjectName(u"p_val_doubleSpinBox")
        self.p_val_doubleSpinBox.setMaximum(1.000000000000000)
        self.p_val_doubleSpinBox.setSingleStep(0.010000000000000)
        self.p_val_doubleSpinBox.setValue(0.900000000000000)

        self.gridLayout.addWidget(self.p_val_doubleSpinBox, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(AccidentalMutualInfoSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.cycle_radioButton = QRadioButton(AccidentalMutualInfoSettingsView)
        self.cycle_radioButton.setObjectName(u"cycle_radioButton")
        self.cycle_radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.cycle_radioButton)

        self.recording_radioButton = QRadioButton(AccidentalMutualInfoSettingsView)
        self.recording_radioButton.setObjectName(u"recording_radioButton")

        self.verticalLayout.addWidget(self.recording_radioButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(102, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(AccidentalMutualInfoSettingsView)

        QMetaObject.connectSlotsByName(AccidentalMutualInfoSettingsView)
    # setupUi

    def retranslateUi(self, AccidentalMutualInfoSettingsView):
        AccidentalMutualInfoSettingsView.setWindowTitle(QCoreApplication.translate("AccidentalMutualInfoSettingsView", u"Form", None))
        self.Title.setText(QCoreApplication.translate("AccidentalMutualInfoSettingsView", u"AcciendentalMutualInfo settings", None))
        self.label.setText(QCoreApplication.translate("AccidentalMutualInfoSettingsView", u"Max iteration", None))
        self.label_2.setText(QCoreApplication.translate("AccidentalMutualInfoSettingsView", u"Confidence level", None))
#if QT_CONFIG(tooltip)
        self.p_val_doubleSpinBox.setToolTip(QCoreApplication.translate("AccidentalMutualInfoSettingsView", u"Value of acceptable error.\n"
"Ex : p_val of 0.9 accepts an error of 0.1 on the criteria.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("AccidentalMutualInfoSettingsView", u"Compute a criteria (threshold) per :", None))
        self.cycle_radioButton.setText(QCoreApplication.translate("AccidentalMutualInfoSettingsView", u"Component for each sleep cycle", None))
        self.recording_radioButton.setText(QCoreApplication.translate("AccidentalMutualInfoSettingsView", u"Component (a single value for all the recording)", None))
    # retranslateUi

