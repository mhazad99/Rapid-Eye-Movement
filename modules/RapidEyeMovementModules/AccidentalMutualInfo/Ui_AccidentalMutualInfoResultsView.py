# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AccidentalMutualInfoResultsView.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AccidentalMutualInfoResultsView(object):
    def setupUi(self, AccidentalMutualInfoResultsView):
        if not AccidentalMutualInfoResultsView.objectName():
            AccidentalMutualInfoResultsView.setObjectName(u"AccidentalMutualInfoResultsView")
        AccidentalMutualInfoResultsView.resize(633, 231)
        self.gridLayout = QGridLayout(AccidentalMutualInfoResultsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(AccidentalMutualInfoResultsView)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(AccidentalMutualInfoResultsView)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.p_val_lineEdit = QLineEdit(AccidentalMutualInfoResultsView)
        self.p_val_lineEdit.setObjectName(u"p_val_lineEdit")
        self.p_val_lineEdit.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.p_val_lineEdit)

        self.label_6 = QLabel(AccidentalMutualInfoResultsView)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.ami_threshold_lineEdit = QLineEdit(AccidentalMutualInfoResultsView)
        self.ami_threshold_lineEdit.setObjectName(u"ami_threshold_lineEdit")
        self.ami_threshold_lineEdit.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.ami_threshold_lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(AccidentalMutualInfoResultsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.mean_lineEdit = QLineEdit(AccidentalMutualInfoResultsView)
        self.mean_lineEdit.setObjectName(u"mean_lineEdit")
        self.mean_lineEdit.setEnabled(False)

        self.horizontalLayout.addWidget(self.mean_lineEdit)

        self.label_3 = QLabel(AccidentalMutualInfoResultsView)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.std_lineEdit = QLineEdit(AccidentalMutualInfoResultsView)
        self.std_lineEdit.setObjectName(u"std_lineEdit")
        self.std_lineEdit.setEnabled(False)

        self.horizontalLayout.addWidget(self.std_lineEdit)

        self.label_4 = QLabel(AccidentalMutualInfoResultsView)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.criteria_lineEdit = QLineEdit(AccidentalMutualInfoResultsView)
        self.criteria_lineEdit.setObjectName(u"criteria_lineEdit")
        self.criteria_lineEdit.setEnabled(False)

        self.horizontalLayout.addWidget(self.criteria_lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(AccidentalMutualInfoResultsView)

        QMetaObject.connectSlotsByName(AccidentalMutualInfoResultsView)
    # setupUi

    def retranslateUi(self, AccidentalMutualInfoResultsView):
        AccidentalMutualInfoResultsView.setWindowTitle(QCoreApplication.translate("AccidentalMutualInfoResultsView", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("AccidentalMutualInfoResultsView", u"Accidental mutual info distribution", None))
        self.label_5.setText(QCoreApplication.translate("AccidentalMutualInfoResultsView", u"p_val:", None))
        self.label_6.setText(QCoreApplication.translate("AccidentalMutualInfoResultsView", u"Threshold (red line):", None))
        self.label.setText(QCoreApplication.translate("AccidentalMutualInfoResultsView", u"Mean:", None))
        self.label_3.setText(QCoreApplication.translate("AccidentalMutualInfoResultsView", u"Standard deviation:", None))
        self.label_4.setText(QCoreApplication.translate("AccidentalMutualInfoResultsView", u"Criteria:", None))
#if QT_CONFIG(tooltip)
        self.criteria_lineEdit.setToolTip(QCoreApplication.translate("AccidentalMutualInfoResultsView", u"This will be use as a threshold for Z values.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

