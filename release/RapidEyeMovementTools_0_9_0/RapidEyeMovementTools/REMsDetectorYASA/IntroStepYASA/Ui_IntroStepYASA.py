# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IntroStepYASA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_IntroStepYASA(object):
    def setupUi(self, IntroStepYASA):
        if not IntroStepYASA.objectName():
            IntroStepYASA.setObjectName(u"IntroStepYASA")
        IntroStepYASA.resize(1091, 906)
        IntroStepYASA.setStyleSheet(u"font: 10pt \"Roboto-Regular\"; QLabel {background-color: rgb(255, 255, 255);}")
        self.horizontalLayout = QHBoxLayout(IntroStepYASA)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter_2 = QSplitter(IntroStepYASA)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 100))
        self.label_2.setMaximumSize(QSize(500, 60))
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
        self.textEdit.setMinimumSize(QSize(0, 200))
        self.textEdit.setMaximumSize(QSize(16777215, 200))
        self.textEdit.setLayoutDirection(Qt.LeftToRight)
        self.textEdit.setStyleSheet(u"")
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

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
        self.label_4.setFrameShadow(QFrame.Plain)
        self.label_4.setLineWidth(0)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.textEdit_2 = QTextEdit(self.layoutWidget2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 250))
        self.textEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_2.setFrameShape(QFrame.HLine)
        self.textEdit_2.setFrameShadow(QFrame.Plain)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.splitter.addWidget(self.layoutWidget2)

        self.verticalLayout_4.addWidget(self.splitter)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.textEdit_3 = QTextEdit(self.layoutWidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setFrameShape(QFrame.NoFrame)
        self.textEdit_3.setLineWidth(0)

        self.verticalLayout_4.addWidget(self.textEdit_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.splitter_2.addWidget(self.layoutWidget)

        self.horizontalLayout.addWidget(self.splitter_2)


        self.retranslateUi(IntroStepYASA)

        QMetaObject.connectSlotsByName(IntroStepYASA)
    # setupUi

    def retranslateUi(self, IntroStepYASA):
        IntroStepYASA.setWindowTitle(QCoreApplication.translate("IntroStepYASA", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("IntroStepYASA", u"<html><head/><body><p><span style=\" font-weight:600;\">YASA RAPID EYE MOVEMENTS DETECTOR</span></p><p>This tool utilizes the (Yet Another Spindle Algorithm) <span style=\" font-weight:600;\">YASA</span> rapid eye movements (<span style=\" font-weight:600;\">REMs</span>) detector algorithm.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("IntroStepYASA", u"<html><head/><body><p><span style=\" font-weight:600;\">Input</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("IntroStepYASA", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto-Regular'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PSG files including header and events are needed (all saved in the same directory).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt; European Data Format (EDF) : .edf and .tsv files with the exact same filename.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-ri"
                        "ght:0px; -qt-block-indent:0; text-indent:0px;\">-&gt; Stellate : .sig and .sts files with the exact same filename.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt; NATUS : <span style=\" font-family:'MS Shell Dlg 2';\"> the whole NATUS subject folder</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">The annotations files have to include the sleep staging.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Channels:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool re"
                        "quires the selection of <span style=\" font-weight:600;\">2</span> <span style=\" font-weight:600;\">EOG</span> <span style=\" font-weight:600;\">channels</span> per recording for REMs detection.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("IntroStepYASA", u"<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("IntroStepYASA", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto-Regular'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">The REMs detected events are added in the annotations files (.tsv, .sts or .ent) depending of the format used.<br /></span>If the annotations file already includes the group event to be added, the existing entries will be removed before adding the new ones.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Each events is defined by : </span><br />-&gt; 1. group : The group where the e"
                        "vents are added (i.e. REM).<br />-&gt; 2. name : The name of the event (i.e. YASA_REM)<br />-&gt; 3. start_sec : The onset of the event in second. <br />-&gt; 4. duration_sec : The duration of the event in second.<br />-&gt; 5. channels : The list of channels on which the event occurs.<br /><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("IntroStepYASA", u"<html><head/><body><p><span style=\" font-weight:600;\">References</span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("IntroStepYASA", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto-Regular'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; color:#222222; background-color:#ffffff;\">Yetton, B. D., et al. (2016). Automatic detection of rapid eye movements (REMs):A machine learning approach. </span><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#222222; background-color:#ffffff;\">Journal of neuroscience methods</span><span style=\" font-family:'Arial','sans-serif'; color:#222222; background-color:#ffffff;\">, </span><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#222222; background-color:#fff"
                        "fff;\">259</span><span style=\" font-family:'Arial','sans-serif'; color:#222222; background-color:#ffffff;\">, 72-82.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial','sans-serif'; color:#222222; background-color:#ffffff;\">Agarwal, R., et al. (2005). Detection of rapid-eye movements in sleep studies. </span><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#222222; background-color:#ffffff;\">IEEE Transactions on biomedical engineering</span><span style=\" font-family:'Arial','sans-serif'; color:#222222; background-color:#ffffff;\">, </span><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#222222; background-color:#ffffff;\">52</span><span style=\" font-family:'Arial','sans-serif'; color:#222222; background-color:#ffffff;\">(8), 1390-1396.</span></p></body></html>", None))
    # retranslateUi

