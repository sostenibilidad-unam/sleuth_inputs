# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sleuth_inputs_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SleuthInputsDialogBase(object):
    def setupUi(self, SleuthInputsDialogBase):
        SleuthInputsDialogBase.setObjectName("SleuthInputsDialogBase")
        SleuthInputsDialogBase.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(SleuthInputsDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(280, 40, 83, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SleuthInputsDialogBase)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 90, 83, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(SleuthInputsDialogBase)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(SleuthInputsDialogBase)
        QtCore.QMetaObject.connectSlotsByName(SleuthInputsDialogBase)

    def retranslateUi(self, SleuthInputsDialogBase):
        _translate = QtCore.QCoreApplication.translate
        SleuthInputsDialogBase.setWindowTitle(_translate("SleuthInputsDialogBase", "Sleuth Inputs"))
        self.pushButton.setText(_translate("SleuthInputsDialogBase", "rasters"))
        self.pushButton_2.setText(_translate("SleuthInputsDialogBase", "shape"))

