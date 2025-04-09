# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectorStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_DetectorStep(object):
    def setupUi(self, DetectorStep):
        if not DetectorStep.objectName():
            DetectorStep.setObjectName(u"DetectorStep")
        DetectorStep.resize(730, 590)
        self.verticalLayout = QVBoxLayout(DetectorStep)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(DetectorStep)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.validation_checkBox = QCheckBox(DetectorStep)
        self.validation_checkBox.setObjectName(u"validation_checkBox")
        self.validation_checkBox.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.validation_checkBox.setFont(font1)

        self.gridLayout.addWidget(self.validation_checkBox, 17, 0, 1, 1)

        self.filename_label = QLabel(DetectorStep)
        self.filename_label.setObjectName(u"filename_label")
        self.filename_label.setEnabled(False)
        self.filename_label.setMaximumSize(QSize(16777215, 16777215))
        self.filename_label.setFont(font1)

        self.gridLayout.addWidget(self.filename_label, 19, 0, 1, 1)

        self.filename_pushButton = QPushButton(DetectorStep)
        self.filename_pushButton.setObjectName(u"filename_pushButton")
        self.filename_pushButton.setEnabled(False)
        self.filename_pushButton.setMaximumSize(QSize(95, 16777215))

        self.gridLayout.addWidget(self.filename_pushButton, 19, 4, 1, 1)

        self.event_name_lineEdit = QLineEdit(DetectorStep)
        self.event_name_lineEdit.setObjectName(u"event_name_lineEdit")
        self.event_name_lineEdit.setEnabled(False)
        self.event_name_lineEdit.setMaximumSize(QSize(300, 16777215))
        self.event_name_lineEdit.setFont(font1)
        self.event_name_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.event_name_lineEdit, 18, 1, 1, 1)

        self.percentile_spinBox = QSpinBox(DetectorStep)
        self.percentile_spinBox.setObjectName(u"percentile_spinBox")
        self.percentile_spinBox.setMaximumSize(QSize(300, 16777215))
        self.percentile_spinBox.setFont(font1)
        self.percentile_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.percentile_spinBox.setMaximum(100)
        self.percentile_spinBox.setValue(65)

        self.gridLayout.addWidget(self.percentile_spinBox, 8, 1, 1, 1)

        self.label_9 = QLabel(DetectorStep)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_4 = QLabel(DetectorStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)

        self.label_7 = QLabel(DetectorStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)

        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)

        self.label_2 = QLabel(DetectorStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.window_sec_doubleSpinBox = QDoubleSpinBox(DetectorStep)
        self.window_sec_doubleSpinBox.setObjectName(u"window_sec_doubleSpinBox")
        self.window_sec_doubleSpinBox.setMaximumSize(QSize(300, 16777215))
        self.window_sec_doubleSpinBox.setFont(font1)
        self.window_sec_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.window_sec_doubleSpinBox.setValue(3.000000000000000)

        self.gridLayout.addWidget(self.window_sec_doubleSpinBox, 5, 1, 1, 1)

        self.label_5 = QLabel(DetectorStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 7, 2, 1, 1)

        self.filename_lineEdit = QLineEdit(DetectorStep)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")
        self.filename_lineEdit.setEnabled(False)
        self.filename_lineEdit.setMaximumSize(QSize(300, 16777215))
        self.filename_lineEdit.setFont(font1)
        self.filename_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.filename_lineEdit, 19, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 20, 0, 1, 1)

        self.label_3 = QLabel(DetectorStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setWordWrap(True)

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.label_8 = QLabel(DetectorStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.order_spinBox = QSpinBox(DetectorStep)
        self.order_spinBox.setObjectName(u"order_spinBox")
        self.order_spinBox.setMaximumSize(QSize(300, 16777215))
        self.order_spinBox.setFont(font1)
        self.order_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.order_spinBox.setMaximum(1000)
        self.order_spinBox.setValue(11)

        self.gridLayout.addWidget(self.order_spinBox, 6, 1, 1, 1)

        self.line = QFrame(DetectorStep)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 10, 0, 1, 5)

        self.event_name_label = QLabel(DetectorStep)
        self.event_name_label.setObjectName(u"event_name_label")
        self.event_name_label.setEnabled(False)
        self.event_name_label.setMaximumSize(QSize(200, 16777215))
        self.event_name_label.setFont(font1)

        self.gridLayout.addWidget(self.event_name_label, 18, 0, 1, 1)

        self.border_effect_doubleSpinBox = QDoubleSpinBox(DetectorStep)
        self.border_effect_doubleSpinBox.setObjectName(u"border_effect_doubleSpinBox")
        self.border_effect_doubleSpinBox.setMaximumSize(QSize(300, 16777215))
        self.border_effect_doubleSpinBox.setFont(font1)
        self.border_effect_doubleSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.border_effect_doubleSpinBox.setMaximum(50.000000000000000)
        self.border_effect_doubleSpinBox.setValue(10.000000000000000)

        self.gridLayout.addWidget(self.border_effect_doubleSpinBox, 7, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 19, 5, 1, 1)

        self.label_11 = QLabel(DetectorStep)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 16, 0, 1, 1)

        self.events_name_lineEdit = QLineEdit(DetectorStep)
        self.events_name_lineEdit.setObjectName(u"events_name_lineEdit")
        self.events_name_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.events_name_lineEdit, 1, 1, 1, 1)

        self.label_10 = QLabel(DetectorStep)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setItalic(True)
        self.label_10.setFont(font2)

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.label_6 = QLabel(DetectorStep)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 50))
        self.label_6.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(DetectorStep)
        self.filename_pushButton.clicked.connect(DetectorStep.on_choose)
        self.validation_checkBox.clicked.connect(DetectorStep.on_active_validation)

        QMetaObject.connectSlotsByName(DetectorStep)
    # setupUi

    def retranslateUi(self, DetectorStep):
        DetectorStep.setWindowTitle("")
        DetectorStep.setStyleSheet(QCoreApplication.translate("DetectorStep", u"font: 10pt \"Roboto-Regular\";", None))
        self.label.setText(QCoreApplication.translate("DetectorStep", u"There is only 4 main parameters for this tool:", None))
        self.validation_checkBox.setText(QCoreApplication.translate("DetectorStep", u"Activate validation", None))
        self.filename_label.setText(QCoreApplication.translate("DetectorStep", u"Filename to save the performance results", None))
        self.filename_pushButton.setText(QCoreApplication.translate("DetectorStep", u"Browse...", None))
        self.label_9.setText(QCoreApplication.translate("DetectorStep", u"REMs Event Name", None))
        self.label_4.setText(QCoreApplication.translate("DetectorStep", u"Percentile", None))
        self.label_7.setText(QCoreApplication.translate("DetectorStep", u"[Optional]", None))
        self.label_2.setText(QCoreApplication.translate("DetectorStep", u"Order of the derivative approximation", None))
#if QT_CONFIG(tooltip)
        self.window_sec_doubleSpinBox.setToolTip(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p>Must be a divider of the sleep stage's window lenght (30 sec in most case)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("DetectorStep", u"%", None))
        self.label_3.setText(QCoreApplication.translate("DetectorStep", u"Border effect (% of signal to remove each side)", None))
        self.label_8.setText(QCoreApplication.translate("DetectorStep", u"Time window length (s)", None))
        self.event_name_label.setText(QCoreApplication.translate("DetectorStep", u"Event Name to compare with", None))
        self.label_11.setText(QCoreApplication.translate("DetectorStep", u"Parameters to validate against another set of events", None))
        self.label_10.setText(QCoreApplication.translate("DetectorStep", u"REMs detection within the time window (i.e. 3 s)", None))
        self.label_6.setText("")
    # retranslateUi

