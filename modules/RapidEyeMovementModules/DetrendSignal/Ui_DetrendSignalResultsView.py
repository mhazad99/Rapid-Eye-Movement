# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetrendSignalResultsView.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from widgets.QLineEditLive import QLineEditLive

class Ui_DetrendSignalResultsView(object):
    def setupUi(self, DetrendSignalResultsView):
        if not DetrendSignalResultsView.objectName():
            DetrendSignalResultsView.setObjectName(u"DetrendSignalResultsView")
        DetrendSignalResultsView.resize(633, 139)
        self.gridLayout = QGridLayout(DetrendSignalResultsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(DetrendSignalResultsView)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(DetrendSignalResultsView)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.event_index_lineEdit = QLineEdit(DetrendSignalResultsView)
        self.event_index_lineEdit.setObjectName(u"event_index_lineEdit")

        self.horizontalLayout.addWidget(self.event_index_lineEdit)

        self.prev_but = QPushButton(DetrendSignalResultsView)
        self.prev_but.setObjectName(u"prev_but")
        self.prev_but.setEnabled(True)

        self.horizontalLayout.addWidget(self.prev_but)

        self.next_but = QPushButton(DetrendSignalResultsView)
        self.next_but.setObjectName(u"next_but")
        self.next_but.setEnabled(True)

        self.horizontalLayout.addWidget(self.next_but)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(DetrendSignalResultsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.event_lineEdit = QLineEdit(DetrendSignalResultsView)
        self.event_lineEdit.setObjectName(u"event_lineEdit")
        self.event_lineEdit.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.event_lineEdit)

        self.time_label = QLabel(DetrendSignalResultsView)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setLayoutDirection(Qt.LeftToRight)
        self.time_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.time_label)

        self.time_lineedit = QLineEditLive(DetrendSignalResultsView)
        self.time_lineedit.setObjectName(u"time_lineedit")
        self.time_lineedit.setEnabled(False)
        self.time_lineedit.setText(u"00:00:00")

        self.horizontalLayout_3.addWidget(self.time_lineedit)

        self.duration_label = QLabel(DetrendSignalResultsView)
        self.duration_label.setObjectName(u"duration_label")

        self.horizontalLayout_3.addWidget(self.duration_label)

        self.duration_lineEdit = QLineEdit(DetrendSignalResultsView)
        self.duration_lineEdit.setObjectName(u"duration_lineEdit")
        self.duration_lineEdit.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.duration_lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(DetrendSignalResultsView)
        self.next_but.clicked.connect(DetrendSignalResultsView.on_next_button)
        self.prev_but.clicked.connect(DetrendSignalResultsView.on_prev_button)
        self.event_index_lineEdit.editingFinished.connect(DetrendSignalResultsView.on_event_index_changed)

        QMetaObject.connectSlotsByName(DetrendSignalResultsView)
    # setupUi

    def retranslateUi(self, DetrendSignalResultsView):
        DetrendSignalResultsView.setWindowTitle(QCoreApplication.translate("DetrendSignalResultsView", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("DetrendSignalResultsView", u"Display signals from events", None))
        self.label_4.setText(QCoreApplication.translate("DetrendSignalResultsView", u"Event Number", None))
        self.event_index_lineEdit.setText(QCoreApplication.translate("DetrendSignalResultsView", u"0", None))
#if QT_CONFIG(tooltip)
        self.prev_but.setToolTip(QCoreApplication.translate("DetrendSignalResultsView", u"Display the previous window (window length will be added to the time elapsed).", None))
#endif // QT_CONFIG(tooltip)
        self.prev_but.setText(QCoreApplication.translate("DetrendSignalResultsView", u"<<", None))
#if QT_CONFIG(tooltip)
        self.next_but.setToolTip(QCoreApplication.translate("DetrendSignalResultsView", u"Display the next window (window length will be added to the time elapsed).", None))
#endif // QT_CONFIG(tooltip)
        self.next_but.setText(QCoreApplication.translate("DetrendSignalResultsView", u">>", None))
        self.label.setText(QCoreApplication.translate("DetrendSignalResultsView", u"Event", None))
        self.time_label.setText(QCoreApplication.translate("DetrendSignalResultsView", u"Time elapsed (HH:MM:SS)", None))
#if QT_CONFIG(tooltip)
        self.time_lineedit.setToolTip(QCoreApplication.translate("DetrendSignalResultsView", u"Time elapsed since the beginning of the recording (ex. 01:10:5.5)\n"
"Press enter to display the detection window.", None))
#endif // QT_CONFIG(tooltip)
        self.duration_label.setText(QCoreApplication.translate("DetrendSignalResultsView", u"Duration (sec)", None))
    # retranslateUi

