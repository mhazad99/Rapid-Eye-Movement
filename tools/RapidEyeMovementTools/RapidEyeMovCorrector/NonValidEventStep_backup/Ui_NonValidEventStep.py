# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_NonValidEventStep.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QTreeView, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_NonValidEventStep(object):
    def setupUi(self, NonValidEventStep):
        if not NonValidEventStep.objectName():
            NonValidEventStep.setObjectName(u"NonValidEventStep")
        NonValidEventStep.resize(1204, 469)
        self.horizontalLayout_2 = QHBoxLayout(NonValidEventStep)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(NonValidEventStep)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.file_listview = QListView(NonValidEventStep)
        self.file_listview.setObjectName(u"file_listview")

        self.verticalLayout.addWidget(self.file_listview)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(NonValidEventStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.event_treeview = QTreeView(NonValidEventStep)
        self.event_treeview.setObjectName(u"event_treeview")
        self.event_treeview.setEditTriggers(QAbstractItemView.CurrentChanged)
        self.event_treeview.setSelectionMode(QAbstractItemView.NoSelection)
        self.event_treeview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout_2.addWidget(self.event_treeview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_all_checkBox = QCheckBox(NonValidEventStep)
        self.select_all_checkBox.setObjectName(u"select_all_checkBox")

        self.horizontalLayout.addWidget(self.select_all_checkBox)

        self.search_lineEdit = QLineEdit(NonValidEventStep)
        self.search_lineEdit.setObjectName(u"search_lineEdit")

        self.horizontalLayout.addWidget(self.search_lineEdit)

        self.apply_all_pushButton = QPushButton(NonValidEventStep)
        self.apply_all_pushButton.setObjectName(u"apply_all_pushButton")

        self.horizontalLayout.addWidget(self.apply_all_pushButton)

        self.reset_all_files_pushButton = QPushButton(NonValidEventStep)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.horizontalLayout.addWidget(self.reset_all_files_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.reset_excl_event_checkBox = QCheckBox(NonValidEventStep)
        self.reset_excl_event_checkBox.setObjectName(u"reset_excl_event_checkBox")
        self.reset_excl_event_checkBox.setEnabled(False)

        self.verticalLayout_2.addWidget(self.reset_excl_event_checkBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(NonValidEventStep)
        self.file_listview.clicked.connect(NonValidEventStep.on_file_selected)
        self.apply_all_pushButton.clicked.connect(NonValidEventStep.on_apply_to_all_files)
        self.select_all_checkBox.stateChanged.connect(NonValidEventStep.on_select_all_groups)
        self.reset_all_files_pushButton.clicked.connect(NonValidEventStep.on_reset_all_files)
        self.search_lineEdit.textEdited.connect(NonValidEventStep.search_pattern_slot)

        QMetaObject.connectSlotsByName(NonValidEventStep)
    # setupUi

    def retranslateUi(self, NonValidEventStep):
        NonValidEventStep.setWindowTitle(QCoreApplication.translate("NonValidEventStep", u"Form", None))
        NonValidEventStep.setStyleSheet(QCoreApplication.translate("NonValidEventStep", u"font: 10pt \"Roboto-Regular\";", None))
        self.label.setText(QCoreApplication.translate("NonValidEventStep", u"PSG Files", None))
        self.label_2.setText(QCoreApplication.translate("NonValidEventStep", u"Events", None))
        self.select_all_checkBox.setText(QCoreApplication.translate("NonValidEventStep", u"Select All", None))
        self.search_lineEdit.setText("")
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("NonValidEventStep", u"Search Event Group", None))
        self.apply_all_pushButton.setText(QCoreApplication.translate("NonValidEventStep", u"Apply to all files", None))
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("NonValidEventStep", u"Reset all files", None))
        self.reset_excl_event_checkBox.setText(QCoreApplication.translate("NonValidEventStep", u"Reset the signal of excluded events ", None))
    # retranslateUi

