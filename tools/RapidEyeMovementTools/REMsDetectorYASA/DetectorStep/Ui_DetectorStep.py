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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_DetectorStep(object):
    def setupUi(self, DetectorStep):
        if not DetectorStep.objectName():
            DetectorStep.setObjectName(u"DetectorStep")
        DetectorStep.resize(755, 590)
        self.gridLayout_2 = QGridLayout(DetectorStep)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(DetectorStep)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setLineWidth(0)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 14, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 9, 3, 1, 1)

        self.label_8 = QLabel(DetectorStep)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setFamilies([u"Roboto-Regular"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setLineWidth(0)

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.frame_5 = QFrame(DetectorStep)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox = QCheckBox(self.frame_5)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_5.addWidget(self.checkBox)


        self.gridLayout.addWidget(self.frame_5, 9, 2, 1, 1)

        self.label_15 = QLabel(DetectorStep)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setLineWidth(-3)

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 2)

        self.label_4 = QLabel(DetectorStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font)
        self.label_4.setLineWidth(0)

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 4, 3, 1, 1)

        self.frame_7 = QFrame(DetectorStep)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)


        self.gridLayout.addWidget(self.frame_7, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.frame = QFrame(DetectorStep)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout.addWidget(self.label_18)

        self.spinBox_2 = QSpinBox(self.frame)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(10000)

        self.horizontalLayout.addWidget(self.spinBox_2)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout.addWidget(self.label_17)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(10000)

        self.horizontalLayout.addWidget(self.spinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.frame, 4, 2, 1, 1)

        self.frame_2 = QFrame(DetectorStep)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setSingleStep(0.010000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_6)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setSingleStep(0.010000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.frame_2, 5, 2, 1, 1)

        self.label_3 = QLabel(DetectorStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font)
        self.label_3.setLineWidth(0)
        self.label_3.setWordWrap(True)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.frame_6 = QFrame(DetectorStep)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.gridLayout.addWidget(self.frame_6, 1, 2, 1, 1)

        self.frame_4 = QFrame(DetectorStep)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setSingleStep(0.010000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.gridLayout.addWidget(self.frame_4, 7, 2, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 6, 3, 1, 1)

        self.label_2 = QLabel(DetectorStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setFont(font)
        self.label_2.setLineWidth(0)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 8, 3, 1, 1)

        self.frame_3 = QFrame(DetectorStep)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.doubleSpinBox = QDoubleSpinBox(self.frame_3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setSingleStep(0.010000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_3.addWidget(self.label_14)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.frame_3)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setSingleStep(0.010000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout.addWidget(self.frame_3, 6, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 5, 3, 1, 1)

        self.label = QLabel(DetectorStep)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setFont(font)
        self.label.setLineWidth(0)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)

        self.frame_8 = QFrame(DetectorStep)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_3 = QLineEdit(self.frame_8)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_8.addWidget(self.lineEdit_3)


        self.gridLayout.addWidget(self.frame_8, 8, 2, 1, 1)

        self.label_16 = QLabel(DetectorStep)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setLineWidth(0)

        self.gridLayout.addWidget(self.label_16, 8, 0, 1, 1)

        self.label_7 = QLabel(DetectorStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLineWidth(0)

        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(DetectorStep)

        QMetaObject.connectSlotsByName(DetectorStep)
    # setupUi

    def retranslateUi(self, DetectorStep):
        DetectorStep.setWindowTitle("")
        DetectorStep.setStyleSheet(QCoreApplication.translate("DetectorStep", u"font: 10pt \"Roboto-Regular\";", None))
        self.label_9.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p>REMs Event Name<br/><span style=\" font-size:8pt;\">The event name in the annotation file.</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p>Amplitude (uV)<br/><span style=\" font-size:8pt;\">Minimum and maximum amplitude of the peak of the REM.</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("DetectorStep", u"Yes", None))
        self.label_15.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p>REMs Event group<br/><span style=\" font-size:8pt;\">The group category in the annotation file.</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p>Relative Prominence<br/><span style=\" font-size:8pt;\">scales the minimum prominence threshold as a fraction of minimum amplitude.<br/>(e.g., relative prominence = 0.5 means peaks must stand out by at least 50%<br/>of the minimum amplitude.)</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("DetectorStep", u"Min:", None))
        self.label_17.setText(QCoreApplication.translate("DetectorStep", u"Max:", None))
        self.label_11.setText(QCoreApplication.translate("DetectorStep", u"Min:", None))
        self.label_12.setText(QCoreApplication.translate("DetectorStep", u"Max:", None))
        self.label_3.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p>REM Frequency (Hz)<br/><span style=\" font-size:8pt;\">Frequency range of REMs.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("DetectorStep", u"Value:", None))
        self.label_2.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p>Duration (s)<br/><span style=\" font-size:8pt;\">Minimum and maximum duration of the REMs.</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("DetectorStep", u"Min:", None))
        self.label_14.setText(QCoreApplication.translate("DetectorStep", u"Max:", None))
        self.label.setText(QCoreApplication.translate("DetectorStep", u"There are 6 main parameters for this tool:", None))
        self.label_16.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p>Include<br/><span style=\" font-size:8pt;\">If the hypnogram is loaded, the detection will only be applied<br/>to the values defiend in &quot;Include&quot;: Default = 5 (REM)</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p>Remove Outliers<br/><span style=\" font-size:8pt;\">If &quot;Yes&quot;, YASA will automatically detect and remove REMs outliers using<br/>its algorithm. </span><span style=\" font-size:8pt; font-weight:600;\">Note</span><span style=\" font-size:8pt;\"> that this step will only be applied if there are more<br/>than 50 detected REMs in the first place.</span></p></body></html>", None))
    # retranslateUi

