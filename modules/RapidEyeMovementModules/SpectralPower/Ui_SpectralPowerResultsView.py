# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpectralPowerResultsView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SpectralPowerResultsView(object):
    def setupUi(self, SpectralPowerResultsView):
        if not SpectralPowerResultsView.objectName():
            SpectralPowerResultsView.setObjectName(u"SpectralPowerResultsView")
        SpectralPowerResultsView.resize(633, 109)
        self.gridLayout = QGridLayout(SpectralPowerResultsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(SpectralPowerResultsView)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.delta_checkBox = QCheckBox(SpectralPowerResultsView)
        self.delta_checkBox.setObjectName(u"delta_checkBox")

        self.horizontalLayout.addWidget(self.delta_checkBox)

        self.theta_checkBox = QCheckBox(SpectralPowerResultsView)
        self.theta_checkBox.setObjectName(u"theta_checkBox")

        self.horizontalLayout.addWidget(self.theta_checkBox)

        self.alpha_checkBox = QCheckBox(SpectralPowerResultsView)
        self.alpha_checkBox.setObjectName(u"alpha_checkBox")

        self.horizontalLayout.addWidget(self.alpha_checkBox)

        self.beta_checkBox = QCheckBox(SpectralPowerResultsView)
        self.beta_checkBox.setObjectName(u"beta_checkBox")

        self.horizontalLayout.addWidget(self.beta_checkBox)

        self.gamma_checkBox = QCheckBox(SpectralPowerResultsView)
        self.gamma_checkBox.setObjectName(u"gamma_checkBox")

        self.horizontalLayout.addWidget(self.gamma_checkBox)

        self.other_checkBox = QCheckBox(SpectralPowerResultsView)
        self.other_checkBox.setObjectName(u"other_checkBox")

        self.horizontalLayout.addWidget(self.other_checkBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SpectralPowerResultsView)
        self.theta_checkBox.clicked.connect(SpectralPowerResultsView.scatter_plot)
        self.delta_checkBox.clicked.connect(SpectralPowerResultsView.scatter_plot)
        self.alpha_checkBox.clicked.connect(SpectralPowerResultsView.scatter_plot)
        self.beta_checkBox.clicked.connect(SpectralPowerResultsView.scatter_plot)
        self.gamma_checkBox.clicked.connect(SpectralPowerResultsView.scatter_plot)
        self.other_checkBox.clicked.connect(SpectralPowerResultsView.scatter_plot)

        QMetaObject.connectSlotsByName(SpectralPowerResultsView)
    # setupUi

    def retranslateUi(self, SpectralPowerResultsView):
        SpectralPowerResultsView.setWindowTitle(QCoreApplication.translate("SpectralPowerResultsView", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("SpectralPowerResultsView", u"SpectralPower", None))
        self.delta_checkBox.setText(QCoreApplication.translate("SpectralPowerResultsView", u"Delta", None))
        self.theta_checkBox.setText(QCoreApplication.translate("SpectralPowerResultsView", u"Theta", None))
        self.alpha_checkBox.setText(QCoreApplication.translate("SpectralPowerResultsView", u"Alpha", None))
        self.beta_checkBox.setText(QCoreApplication.translate("SpectralPowerResultsView", u"Beta", None))
        self.gamma_checkBox.setText(QCoreApplication.translate("SpectralPowerResultsView", u"Gamma", None))
        self.other_checkBox.setText(QCoreApplication.translate("SpectralPowerResultsView", u"Other", None))
    # retranslateUi

