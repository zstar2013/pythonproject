# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connseting.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 325)
        self.formLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(30, 20, 341, 201))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(10, 30, 10, 0)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.lburn = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lburn.setFont(font)
        self.lburn.setObjectName("lburn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lburn)
        self.ledb = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.ledb.setObjectName("ledb")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ledb)
        self.lbdb = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbdb.setFont(font)
        self.lbdb.setObjectName("lbdb")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbdb)
        self.leusr = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.leusr.setObjectName("leusr")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leusr)
        self.lbpwd = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbpwd.setFont(font)
        self.lbpwd.setObjectName("lbpwd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbpwd)
        self.lepwd = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lepwd.setObjectName("lepwd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lepwd)
        self.lbdbname = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbdbname.setFont(font)
        self.lbdbname.setObjectName("lbdbname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbdbname)
        self.ledbname = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.ledbname.setObjectName("ledbname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ledbname)
        self.pbsavelink = QtWidgets.QPushButton(Dialog)
        self.pbsavelink.setGeometry(QtCore.QRect(160, 240, 75, 23))
        self.pbsavelink.setObjectName("pbsavelink")
        self.pbcancel = QtWidgets.QPushButton(Dialog)
        self.pbcancel.setGeometry(QtCore.QRect(270, 240, 75, 23))
        self.pbcancel.setObjectName("pbcancel")
        self.pbtestlink = QtWidgets.QPushButton(Dialog)
        self.pbtestlink.setGeometry(QtCore.QRect(50, 240, 75, 23))
        self.pbtestlink.setObjectName("pbtestlink")
        self.lbstatus = QtWidgets.QLabel(Dialog)
        self.lbstatus.setGeometry(QtCore.QRect(10, 270, 381, 51))
        self.lbstatus.setText("")
        self.lbstatus.setObjectName("lbstatus")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lburn.setText(_translate("Dialog", "数据库ip："))
        self.ledb.setPlaceholderText(_translate("Dialog", "127.0.0.1"))
        self.lbdb.setText(_translate("Dialog", "用户名："))
        self.leusr.setPlaceholderText(_translate("Dialog", "root"))
        self.lbpwd.setText(_translate("Dialog", "密码："))
        self.lepwd.setPlaceholderText(_translate("Dialog", "root"))
        self.lbdbname.setText(_translate("Dialog", "库名："))
        self.ledbname.setPlaceholderText(_translate("Dialog", "root"))
        self.pbsavelink.setText(_translate("Dialog", "保存"))
        self.pbcancel.setText(_translate("Dialog", "关闭"))
        self.pbtestlink.setText(_translate("Dialog", "测试连接"))

