# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MovingAverageResultsView.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MovingAverageResultsView(object):
    def setupUi(self, MovingAverageResultsView):
        if not MovingAverageResultsView.objectName():
            MovingAverageResultsView.setObjectName(u"MovingAverageResultsView")
        MovingAverageResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(MovingAverageResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(MovingAverageResultsView)

        QMetaObject.connectSlotsByName(MovingAverageResultsView)
    # setupUi

    def retranslateUi(self, MovingAverageResultsView):
        MovingAverageResultsView.setWindowTitle(QCoreApplication.translate("MovingAverageResultsView", u"Form", None))
    # retranslateUi

