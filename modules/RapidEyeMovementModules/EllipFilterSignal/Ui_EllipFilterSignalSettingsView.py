# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EllipFilterSignalSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QLabel,
    QLayout, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_EllipFilterSignalSettingsView(object):
    def setupUi(self, EllipFilterSignalSettingsView):
        if not EllipFilterSignalSettingsView.objectName():
            EllipFilterSignalSettingsView.setObjectName(u"EllipFilterSignalSettingsView")
        EllipFilterSignalSettingsView.resize(992, 548)
        self.formLayout = QFormLayout(EllipFilterSignalSettingsView)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(EllipFilterSignalSettingsView)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.line_4 = QFrame(EllipFilterSignalSettingsView)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.IR_comboBox = QComboBox(EllipFilterSignalSettingsView)
        self.IR_comboBox.addItem("")
        self.IR_comboBox.addItem("")
        self.IR_comboBox.setObjectName(u"IR_comboBox")

        self.gridLayout.addWidget(self.IR_comboBox, 0, 1, 1, 1)

        self.type_combobox = QComboBox(EllipFilterSignalSettingsView)
        self.type_combobox.addItem("")
        self.type_combobox.addItem("")
        self.type_combobox.addItem("")
        self.type_combobox.addItem("")
        self.type_combobox.setObjectName(u"type_combobox")

        self.gridLayout.addWidget(self.type_combobox, 0, 2, 1, 1)

        self.label_2 = QLabel(EllipFilterSignalSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(160, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_11 = QLabel(EllipFilterSignalSettingsView)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(130, 0))

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.cutoff_lineedit = QLineEdit(EllipFilterSignalSettingsView)
        self.cutoff_lineedit.setObjectName(u"cutoff_lineedit")

        self.gridLayout.addWidget(self.cutoff_lineedit, 1, 1, 1, 2)

        self.label_4 = QLabel(EllipFilterSignalSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(160, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setInputMethodHints(Qt.ImhNoEditMenu|Qt.ImhNoTextHandles)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.freq_resp_unit_comboBox = QComboBox(EllipFilterSignalSettingsView)
        self.freq_resp_unit_comboBox.addItem("")
        self.freq_resp_unit_comboBox.addItem("")
        self.freq_resp_unit_comboBox.setObjectName(u"freq_resp_unit_comboBox")

        self.gridLayout.addWidget(self.freq_resp_unit_comboBox, 3, 1, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_9 = QLabel(EllipFilterSignalSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout.addWidget(self.label_9)

        self.line_3 = QFrame(EllipFilterSignalSettingsView)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_12 = QLabel(EllipFilterSignalSettingsView)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_13 = QLabel(EllipFilterSignalSettingsView)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(160, 0))

        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_10 = QLabel(EllipFilterSignalSettingsView)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(130, 0))
        self.label_10.setMaximumSize(QSize(100, 16777215))
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)

        self.iir_order_lineEdit = QLineEdit(EllipFilterSignalSettingsView)
        self.iir_order_lineEdit.setObjectName(u"iir_order_lineEdit")

        self.gridLayout_4.addWidget(self.iir_order_lineEdit, 1, 1, 1, 1)

        self.radioButton_ellip = QRadioButton(EllipFilterSignalSettingsView)
        self.buttonGroup_IIRFamily = QButtonGroup(EllipFilterSignalSettingsView)
        self.buttonGroup_IIRFamily.setObjectName(u"buttonGroup_IIRFamily")
        self.buttonGroup_IIRFamily.addButton(self.radioButton_ellip)
        self.radioButton_ellip.setObjectName(u"radioButton_ellip")

        self.gridLayout_4.addWidget(self.radioButton_ellip, 0, 1, 1, 1)

        self.radioButton_butter = QRadioButton(EllipFilterSignalSettingsView)
        self.buttonGroup_IIRFamily.addButton(self.radioButton_butter)
        self.radioButton_butter.setObjectName(u"radioButton_butter")
        self.radioButton_butter.setMinimumSize(QSize(130, 0))
        self.radioButton_butter.setChecked(True)

        self.gridLayout_4.addWidget(self.radioButton_butter, 0, 0, 1, 1)

        self.doubleSpinBox_maxripple = QDoubleSpinBox(EllipFilterSignalSettingsView)
        self.doubleSpinBox_maxripple.setObjectName(u"doubleSpinBox_maxripple")
        self.doubleSpinBox_maxripple.setEnabled(False)
        self.doubleSpinBox_maxripple.setSingleStep(0.500000000000000)
        self.doubleSpinBox_maxripple.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_maxripple, 2, 1, 1, 1)

        self.label_14 = QLabel(EllipFilterSignalSettingsView)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 3, 0, 1, 1)

        self.lineEdit_stopHz = QLineEdit(EllipFilterSignalSettingsView)
        self.lineEdit_stopHz.setObjectName(u"lineEdit_stopHz")
        self.lineEdit_stopHz.setEnabled(False)

        self.gridLayout_4.addWidget(self.lineEdit_stopHz, 3, 1, 1, 1)

        self.doubleSpinBox_stopdB = QDoubleSpinBox(EllipFilterSignalSettingsView)
        self.doubleSpinBox_stopdB.setObjectName(u"doubleSpinBox_stopdB")
        self.doubleSpinBox_stopdB.setEnabled(False)
        self.doubleSpinBox_stopdB.setValue(6.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_stopdB, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.textEdit = QTextEdit(EllipFilterSignalSettingsView)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(380, 70))
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.label_8 = QLabel(EllipFilterSignalSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)

        self.line_2 = QFrame(EllipFilterSignalSettingsView)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label = QLabel(EllipFilterSignalSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.window_combobox = QComboBox(EllipFilterSignalSettingsView)
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.setObjectName(u"window_combobox")
        self.window_combobox.setEnabled(False)

        self.gridLayout_2.addWidget(self.window_combobox, 3, 1, 1, 1)

        self.sleep_std_radiobutton = QRadioButton(EllipFilterSignalSettingsView)
        self.buttonGroup_OrderDef = QButtonGroup(EllipFilterSignalSettingsView)
        self.buttonGroup_OrderDef.setObjectName(u"buttonGroup_OrderDef")
        self.buttonGroup_OrderDef.addButton(self.sleep_std_radiobutton)
        self.sleep_std_radiobutton.setObjectName(u"sleep_std_radiobutton")
        self.sleep_std_radiobutton.setEnabled(False)
        self.sleep_std_radiobutton.setMinimumSize(QSize(130, 0))
        self.sleep_std_radiobutton.setMaximumSize(QSize(100, 16777215))
        self.sleep_std_radiobutton.setChecked(False)

        self.gridLayout_2.addWidget(self.sleep_std_radiobutton, 0, 0, 1, 1)

        self.std_order_lineedit = QLineEdit(EllipFilterSignalSettingsView)
        self.std_order_lineedit.setObjectName(u"std_order_lineedit")
        self.std_order_lineedit.setEnabled(False)
        self.std_order_lineedit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.std_order_lineedit, 0, 1, 1, 1)

        self.custom_radiobutton = QRadioButton(EllipFilterSignalSettingsView)
        self.buttonGroup_OrderDef.addButton(self.custom_radiobutton)
        self.custom_radiobutton.setObjectName(u"custom_radiobutton")
        self.custom_radiobutton.setEnabled(False)
        self.custom_radiobutton.setMinimumSize(QSize(160, 0))
        self.custom_radiobutton.setMaximumSize(QSize(100, 16777215))
        self.custom_radiobutton.setChecked(True)

        self.gridLayout_2.addWidget(self.custom_radiobutton, 2, 0, 1, 1)

        self.custom_order_lineedit = QLineEdit(EllipFilterSignalSettingsView)
        self.custom_order_lineedit.setObjectName(u"custom_order_lineedit")
        self.custom_order_lineedit.setEnabled(False)

        self.gridLayout_2.addWidget(self.custom_order_lineedit, 2, 1, 1, 1)

        self.label_3 = QLabel(EllipFilterSignalSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(160, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.line = QFrame(EllipFilterSignalSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_7 = QLabel(EllipFilterSignalSettingsView)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(EllipFilterSignalSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(160, 0))
        self.label_6.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.sample_rate_lineedit = QLineEdit(EllipFilterSignalSettingsView)
        self.sample_rate_lineedit.setObjectName(u"sample_rate_lineedit")

        self.gridLayout_3.addWidget(self.sample_rate_lineedit, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer = QSpacerItem(17, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

        self.freq_resp_layout = QVBoxLayout()
        self.freq_resp_layout.setObjectName(u"freq_resp_layout")
        self.freq_resp_layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.freq_resp_layout)


        self.retranslateUi(EllipFilterSignalSettingsView)
        self.type_combobox.currentTextChanged.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.sleep_std_radiobutton.clicked.connect(EllipFilterSignalSettingsView.on_order_type_changed)
        self.custom_radiobutton.clicked.connect(EllipFilterSignalSettingsView.on_order_type_changed)
        self.cutoff_lineedit.returnPressed.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.window_combobox.currentTextChanged.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.sample_rate_lineedit.editingFinished.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.custom_order_lineedit.textChanged.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.IR_comboBox.currentTextChanged.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.iir_order_lineEdit.editingFinished.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.freq_resp_unit_comboBox.currentTextChanged.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.buttonGroup_IIRFamily.buttonClicked.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.doubleSpinBox_maxripple.editingFinished.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.lineEdit_stopHz.returnPressed.connect(EllipFilterSignalSettingsView.on_settings_changed)
        self.doubleSpinBox_stopdB.editingFinished.connect(EllipFilterSignalSettingsView.on_settings_changed)

        self.window_combobox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(EllipFilterSignalSettingsView)
    # setupUi

    def retranslateUi(self, EllipFilterSignalSettingsView):
        EllipFilterSignalSettingsView.setWindowTitle(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Filter settings", None))
        self.IR_comboBox.setItemText(0, QCoreApplication.translate("EllipFilterSignalSettingsView", u"IIR", None))
        self.IR_comboBox.setItemText(1, QCoreApplication.translate("EllipFilterSignalSettingsView", u"FIR", None))

#if QT_CONFIG(tooltip)
        self.IR_comboBox.setToolTip(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Select the Infinite Impulse Response Filter (IIR) or the Finite Impulse Filter (FIR).", None))
#endif // QT_CONFIG(tooltip)
        self.type_combobox.setItemText(0, QCoreApplication.translate("EllipFilterSignalSettingsView", u"bandpass", None))
        self.type_combobox.setItemText(1, QCoreApplication.translate("EllipFilterSignalSettingsView", u"lowpass", None))
        self.type_combobox.setItemText(2, QCoreApplication.translate("EllipFilterSignalSettingsView", u"highpass", None))
        self.type_combobox.setItemText(3, QCoreApplication.translate("EllipFilterSignalSettingsView", u"bandstop", None))

        self.label_2.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Cutoff", None))
        self.label_11.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Frequency response units", None))
#if QT_CONFIG(tooltip)
        self.cutoff_lineedit.setToolTip(QCoreApplication.translate("EllipFilterSignalSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">bandpass</span> : edit low and high frequency cutoff in Hz separated by a space. ex)0.3 100</p><p><span style=\" font-weight:600;\">lowpass</span> : edit high frequency cutoff in Hz.</p><p><span style=\" font-weight:600;\">highpass</span> : edit low frequency cutoff in Hz.</p><p><span style=\" font-weight:600;\">stopband</span> : edit the low and high frequency cutoff in Hz separated by a space. ex)59 61</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cutoff_lineedit.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"0.3 100", None))
        self.label_4.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Type", None))
        self.freq_resp_unit_comboBox.setItemText(0, QCoreApplication.translate("EllipFilterSignalSettingsView", u"Attenuation (dB)", None))
        self.freq_resp_unit_comboBox.setItemText(1, QCoreApplication.translate("EllipFilterSignalSettingsView", u"Amplitude (%)", None))

        self.label_9.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"IIR Filter Settings", None))
        self.label_12.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Stopband (dB)", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("EllipFilterSignalSettingsView", u"The maximum lost in dB in the passband.", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Max ripple in the passband (dB)", None))
        self.label_10.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Order", None))
        self.iir_order_lineEdit.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"6", None))
        self.radioButton_ellip.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Elliptic (Cauer)", None))
        self.radioButton_butter.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Butterworth", None))
#if QT_CONFIG(tooltip)
        self.label_14.setToolTip(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Elliptic filter is designed with a stop band outside the bandpass zone. Define the frequency of the stop band.", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Stopband (Hz)", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_stopHz.setToolTip(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Define the stopband frequency point (Hz) (outside the passband zone) to reach the desired stopband attenuation (dB).  If the desired filter is a bandpass or a stopband, the stopband is expected to be a list of 2 items sepatated by a space (i.e. lowfreq highfreq).", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_stopHz.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"0.1 120", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_stopdB.setToolTip(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Define the stopband attenuation point (dB) (outside the passband zone) to reach the desired stopband frequency (Hz).", None))
#endif // QT_CONFIG(tooltip)
        self.textEdit.setHtml(QCoreApplication.translate("EllipFilterSignalSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:12pt;\">The IIR filter is applied forward and backward to cancel the phase delay.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:12pt;\">The order is divided by 2 when applied since is it applied twice.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; f"
                        "ont-size:12pt;\">ex) An ordre of 6 is sufficient for a bandpass filter </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:12pt;\">      0.3-100 Hz with a sample rate=256 Hz</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"FIR Filter Settings", None))
        self.label.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Order", None))
        self.window_combobox.setItemText(0, QCoreApplication.translate("EllipFilterSignalSettingsView", u"boxcar", None))
        self.window_combobox.setItemText(1, QCoreApplication.translate("EllipFilterSignalSettingsView", u"trlang", None))
        self.window_combobox.setItemText(2, QCoreApplication.translate("EllipFilterSignalSettingsView", u"blackman", None))
        self.window_combobox.setItemText(3, QCoreApplication.translate("EllipFilterSignalSettingsView", u"hamming", None))
        self.window_combobox.setItemText(4, QCoreApplication.translate("EllipFilterSignalSettingsView", u"hann", None))
        self.window_combobox.setItemText(5, QCoreApplication.translate("EllipFilterSignalSettingsView", u"bartlett", None))
        self.window_combobox.setItemText(6, QCoreApplication.translate("EllipFilterSignalSettingsView", u"flattop", None))
        self.window_combobox.setItemText(7, QCoreApplication.translate("EllipFilterSignalSettingsView", u"parzen", None))
        self.window_combobox.setItemText(8, QCoreApplication.translate("EllipFilterSignalSettingsView", u"bohman", None))
        self.window_combobox.setItemText(9, QCoreApplication.translate("EllipFilterSignalSettingsView", u"blackmanharris", None))
        self.window_combobox.setItemText(10, QCoreApplication.translate("EllipFilterSignalSettingsView", u"nuttall", None))
        self.window_combobox.setItemText(11, QCoreApplication.translate("EllipFilterSignalSettingsView", u"barthann", None))
        self.window_combobox.setItemText(12, QCoreApplication.translate("EllipFilterSignalSettingsView", u"kaiser", None))
        self.window_combobox.setItemText(13, QCoreApplication.translate("EllipFilterSignalSettingsView", u"gaussian", None))
        self.window_combobox.setItemText(14, QCoreApplication.translate("EllipFilterSignalSettingsView", u"general_gaussian", None))
        self.window_combobox.setItemText(15, QCoreApplication.translate("EllipFilterSignalSettingsView", u"dpss", None))
        self.window_combobox.setItemText(16, QCoreApplication.translate("EllipFilterSignalSettingsView", u"chebwin", None))
        self.window_combobox.setItemText(17, QCoreApplication.translate("EllipFilterSignalSettingsView", u"exponential", None))
        self.window_combobox.setItemText(18, QCoreApplication.translate("EllipFilterSignalSettingsView", u"tukey", None))
        self.window_combobox.setItemText(19, QCoreApplication.translate("EllipFilterSignalSettingsView", u"taylor", None))

        self.window_combobox.setCurrentText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"hamming", None))
#if QT_CONFIG(tooltip)
        self.sleep_std_radiobutton.setToolTip(QCoreApplication.translate("EllipFilterSignalSettingsView", u"The standard in sleep medicine is to use an order equals to: 5*sample_rate/lower_frequency", None))
#endif // QT_CONFIG(tooltip)
        self.sleep_std_radiobutton.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Sleep standard", None))
        self.custom_radiobutton.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Custom", None))
        self.custom_order_lineedit.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"101", None))
        self.label_3.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Window", None))
        self.label_7.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"(Only used for the visualisation)", None))
        self.label_6.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"Sample Rate", None))
        self.sample_rate_lineedit.setText(QCoreApplication.translate("EllipFilterSignalSettingsView", u"256", None))
    # retranslateUi

