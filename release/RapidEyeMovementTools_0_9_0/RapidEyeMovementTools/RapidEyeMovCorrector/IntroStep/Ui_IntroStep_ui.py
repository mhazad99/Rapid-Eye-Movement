# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IntroStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_IntroStep(object):
    def setupUi(self, IntroStep):
        if not IntroStep.objectName():
            IntroStep.setObjectName(u"IntroStep")
        IntroStep.resize(1383, 907)
        self.horizontalLayout = QHBoxLayout(IntroStep)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter_2 = QSplitter(IntroStep)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(800, 100))
        self.label_2.setMaximumSize(QSize(800, 70))
        font = QFont()
        font.setFamily(u"Roboto-Regular")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.splitter = QSplitter(self.layoutWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.textEdit = QTextEdit(self.layoutWidget1)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 225))
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setLayoutDirection(Qt.LeftToRight)
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setSizeIncrement(QSize(0, 0))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.textEdit_2 = QTextEdit(self.layoutWidget2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 275))
        self.textEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_2.setFrameShape(QFrame.HLine)
        self.textEdit_2.setFrameShadow(QFrame.Plain)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.splitter.addWidget(self.layoutWidget2)

        self.verticalLayout_4.addWidget(self.splitter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.splitter_2.addWidget(self.layoutWidget)

        self.horizontalLayout.addWidget(self.splitter_2)


        self.retranslateUi(IntroStep)

        QMetaObject.connectSlotsByName(IntroStep)
    # setupUi

    def retranslateUi(self, IntroStep):
        IntroStep.setWindowTitle(QCoreApplication.translate("IntroStep", u"Form", None))
        IntroStep.setStyleSheet(QCoreApplication.translate("IntroStep", u"font: 10pt \"Roboto-Regular\";", None))
        self.label_2.setText(QCoreApplication.translate("IntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">OCULAR MOVEMENT ARTIFACTS CORRECTOR IN REM</span></p><p>This tool <span style=\" font-weight:600;\">corrects </span>EEG signals containing <span style=\" font-weight:600;\">ocular movement artifacts</span> during<span style=\" font-weight:600;\"> REM sleep</span> from PSG files.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("IntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Input</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("IntroStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto-Regular'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PSG file (.edf) with the sleep staging (.tsv) is needed for this tool. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt; PSG : Only the European Data Format (EDF) is supported to correct Rapid Eye Movements artifact.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt; Annotations : The .tsv (Tab Separated Values) file with the same name as the PSG file in the same folder is mandatory.</p>\n"
""
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The .tsv columns of the annotation file are as follows:<br />-&gt; 1. group : The group of the event (i.e. stage for sleep stage).<br />-&gt; 2. name : The name of the event (i.e. 5 for R stage).<br />-&gt; 3. start_sec : The onset of the event in second. <br />-&gt; 4. duration_sec : The duration of the event in second.<br />-&gt; 5. channels : The list of channels on which the event occurs.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("IntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("IntroStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto-Regular'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- A new PSG (.edf) file with the artifact-free signals named as the previous one with the suffix &quot;_corrected&quot;.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />- A new .tsv file named as the corrected PSG file containing the original annotations and the new REMs events (correction and possibly the detection). </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt; The events for the "
                        "corrected (10 s) epochs (i.e. REMs_Poulin_Cor) are added on the first EOG channel of the recording. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt; If the detector is used - the events of the (3 s) epochs where a REM is detected (i.e. REMs_Poulin_det) are added on the first EOG channel of the recording.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The columns of the .tsv file are as follows:<br />-&gt; 1. group : The group of the event (i.e. REMs_det)<br />-&gt; 2. name : The name of the event. (i.e. REMs_Poulin_Cor or REMs_Poulin_Det)<br />-&gt; 3. start_sec : The onset of the event in second. <br />-&gt; 4. duration_sec : The duration of the event in second.<br />-&gt; 5. channels : The list of channels on which the event occurs.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\">- If the validation have been checked, a csv file named with the PSG file name with _spectral_power.csv containing the value of the spectral band before and after the correction.</p></body></html>", None))
    # retranslateUi

