# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sampo\Python\PycharmProjects\scinode\scinodes_poc\src\main\python\plugins\SignalsCombine\Ui_SignalsCombineResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_SignalsCombineResultsView(object):
    def setupUi(self, SignalsCombineResultsView):
        SignalsCombineResultsView.setObjectName("SignalsCombineResultsView")
        SignalsCombineResultsView.resize(927, 262)
        self.verticalLayout = QtWidgets.QVBoxLayout(SignalsCombineResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signal_layout = QtWidgets.QVBoxLayout()
        self.signal_layout.setObjectName("signal_layout")
        self.verticalLayout.addLayout(self.signal_layout)

        self.retranslateUi(SignalsCombineResultsView)
        QtCore.QMetaObject.connectSlotsByName(SignalsCombineResultsView)

    def retranslateUi(self, SignalsCombineResultsView):
        _translate = QtCore.QCoreApplication.translate
        SignalsCombineResultsView.setWindowTitle(_translate("SignalsCombineResultsView", "Form"))
