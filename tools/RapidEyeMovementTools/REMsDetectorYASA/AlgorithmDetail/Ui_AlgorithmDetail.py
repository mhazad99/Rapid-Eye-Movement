# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AlgorithmDetail.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import Detail_res_rc_rc

class Ui_AlgorithmDetail(object):
    def setupUi(self, AlgorithmDetail):
        if not AlgorithmDetail.objectName():
            AlgorithmDetail.setObjectName(u"AlgorithmDetail")
        AlgorithmDetail.resize(986, 691)
        self.gridLayout_2 = QGridLayout(AlgorithmDetail)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(AlgorithmDetail)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.label)

        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1134, 690))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/image/Eyes_movement.PNG"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(AlgorithmDetail)

        QMetaObject.connectSlotsByName(AlgorithmDetail)
    # setupUi

    def retranslateUi(self, AlgorithmDetail):
        AlgorithmDetail.setWindowTitle("")
        AlgorithmDetail.setStyleSheet(QCoreApplication.translate("AlgorithmDetail", u"font: 10pt \"Roboto-Regular\";", None))
        self.label.setText(QCoreApplication.translate("AlgorithmDetail", u"Details of the YASA REMs detector algorithm", None))
        self.textEdit.setHtml(QCoreApplication.translate("AlgorithmDetail", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto-Regular'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This algorithm uses the idea from the methodologies proposed in [1] and [2], primarily building upon Agwal\u2019s [1] approach, which applies amplitude thresholding to the negative product of the LOC and ROC filtered signals. Using this technique, the algorithm identifies signal peaks and extracts key features, including the duration of the REM period, the peak absolute values of ROC and LOC, as well as the absolute rise and fall slopes for both signals.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\">To ensure reliable performance, the algorithm requires a minimum of 50 detected REMs to apply its model, which is based on the IsolationForest random forest classifier. Additionally, if the user selects the &quot;remove outlier&quot; option as <span style=\" font-style:italic;\">True</span>, any outliers detected after applying the IsolationForest will be excluded from the final detection results.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Usage points</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- All output parameters of this algorithm are computed using the filtered LOC and ROC signals. The filtering process is based on the thresholds defined in the <span style=\" font-style:italic;\">DetectionStep</span>.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- For optimal results, the user should apply this detection only to artifact-free REM sleep data.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText("")
    # retranslateUi

