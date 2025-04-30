# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MutualInfoZScoreResultsView.ui'
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

class Ui_MutualInfoZScoreResultsView(object):
    def setupUi(self, MutualInfoZScoreResultsView):
        if not MutualInfoZScoreResultsView.objectName():
            MutualInfoZScoreResultsView.setObjectName(u"MutualInfoZScoreResultsView")
        MutualInfoZScoreResultsView.resize(633, 139)
        self.gridLayout = QGridLayout(MutualInfoZScoreResultsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(MutualInfoZScoreResultsView)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(MutualInfoZScoreResultsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(78, 0))
        self.label_4.setMaximumSize(QSize(78, 16777215))

        self.horizontalLayout.addWidget(self.label_4)

        self.event_index_lineEdit = QLineEdit(MutualInfoZScoreResultsView)
        self.event_index_lineEdit.setObjectName(u"event_index_lineEdit")
        self.event_index_lineEdit.setMinimumSize(QSize(180, 0))
        self.event_index_lineEdit.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout.addWidget(self.event_index_lineEdit)

        self.prev_but = QPushButton(MutualInfoZScoreResultsView)
        self.prev_but.setObjectName(u"prev_but")
        self.prev_but.setEnabled(True)

        self.horizontalLayout.addWidget(self.prev_but)

        self.next_but = QPushButton(MutualInfoZScoreResultsView)
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
        self.label = QLabel(MutualInfoZScoreResultsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.event_lineEdit = QLineEdit(MutualInfoZScoreResultsView)
        self.event_lineEdit.setObjectName(u"event_lineEdit")
        self.event_lineEdit.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.event_lineEdit)

        self.time_label = QLabel(MutualInfoZScoreResultsView)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setLayoutDirection(Qt.LeftToRight)
        self.time_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.time_label)

        self.time_lineedit = QLineEditLive(MutualInfoZScoreResultsView)
        self.time_lineedit.setObjectName(u"time_lineedit")
        self.time_lineedit.setEnabled(False)
        self.time_lineedit.setText(u"00:00:00")

        self.horizontalLayout_3.addWidget(self.time_lineedit)

        self.duration_label = QLabel(MutualInfoZScoreResultsView)
        self.duration_label.setObjectName(u"duration_label")

        self.horizontalLayout_3.addWidget(self.duration_label)

        self.duration_lineEdit = QLineEdit(MutualInfoZScoreResultsView)
        self.duration_lineEdit.setObjectName(u"duration_lineEdit")
        self.duration_lineEdit.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.duration_lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(MutualInfoZScoreResultsView)
        self.next_but.clicked.connect(MutualInfoZScoreResultsView.on_next_button)
        self.prev_but.clicked.connect(MutualInfoZScoreResultsView.on_prev_button)
        self.event_index_lineEdit.editingFinished.connect(MutualInfoZScoreResultsView.on_event_index_changed)

        QMetaObject.connectSlotsByName(MutualInfoZScoreResultsView)
    # setupUi

    def retranslateUi(self, MutualInfoZScoreResultsView):
        MutualInfoZScoreResultsView.setWindowTitle(QCoreApplication.translate("MutualInfoZScoreResultsView", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("MutualInfoZScoreResultsView", u"Display Z values by event", None))
        self.label_4.setText(QCoreApplication.translate("MutualInfoZScoreResultsView", u"Event Number", None))
#if QT_CONFIG(tooltip)
        self.event_index_lineEdit.setToolTip(QCoreApplication.translate("MutualInfoZScoreResultsView", u"The index of the event display ", None))
#endif // QT_CONFIG(tooltip)
        self.event_index_lineEdit.setText(QCoreApplication.translate("MutualInfoZScoreResultsView", u"0", None))
#if QT_CONFIG(tooltip)
        self.prev_but.setToolTip(QCoreApplication.translate("MutualInfoZScoreResultsView", u"Display the previous window (window length will be added to the time elapsed).", None))
#endif // QT_CONFIG(tooltip)
        self.prev_but.setText(QCoreApplication.translate("MutualInfoZScoreResultsView", u"<<", None))
#if QT_CONFIG(tooltip)
        self.next_but.setToolTip(QCoreApplication.translate("MutualInfoZScoreResultsView", u"Display the next window (window length will be added to the time elapsed).", None))
#endif // QT_CONFIG(tooltip)
        self.next_but.setText(QCoreApplication.translate("MutualInfoZScoreResultsView", u">>", None))
        self.label.setText(QCoreApplication.translate("MutualInfoZScoreResultsView", u"Event", None))
        self.time_label.setText(QCoreApplication.translate("MutualInfoZScoreResultsView", u"Time elapsed (HH:MM:SS)", None))
#if QT_CONFIG(tooltip)
        self.time_lineedit.setToolTip(QCoreApplication.translate("MutualInfoZScoreResultsView", u"Time elapsed since the beginning of the recording (ex. 01:10:5.5)\n"
"Press enter to display the detection window.", None))
#endif // QT_CONFIG(tooltip)
        self.duration_label.setText(QCoreApplication.translate("MutualInfoZScoreResultsView", u"Duration (sec)", None))
    # retranslateUi

