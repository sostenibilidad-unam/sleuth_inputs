# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sleuth_inputs_dialog_base.ui'
#
# Created: Thu Jun 22 13:09:16 2017
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from builtins import object
from qgis.PyQt import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SleuthInputsDialogBase(object):
    def setupUi(self, SleuthInputsDialogBase):
        SleuthInputsDialogBase.setObjectName(_fromUtf8("SleuthInputsDialogBase"))
        SleuthInputsDialogBase.resize(400, 300)
        self.pushButton = QtGui.QPushButton(SleuthInputsDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(280, 40, 83, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(SleuthInputsDialogBase)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 90, 83, 24))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textBrowser = QtGui.QTextBrowser(SleuthInputsDialogBase)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(SleuthInputsDialogBase)
        QtCore.QMetaObject.connectSlotsByName(SleuthInputsDialogBase)

    def retranslateUi(self, SleuthInputsDialogBase):
        SleuthInputsDialogBase.setWindowTitle(QtGui.QApplication.translate("SleuthInputsDialogBase", "Sleuth Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("SleuthInputsDialogBase", "rasters", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("SleuthInputsDialogBase", "shape", None, QtGui.QApplication.UnicodeUTF8))

