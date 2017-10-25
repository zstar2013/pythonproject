# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(875, 631)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(30, 30, 820, 500))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 540, 821, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbPrepage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pbPrepage.setObjectName("pbPrepage")
        self.horizontalLayout.addWidget(self.pbPrepage)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pbNextpage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pbNextpage.setObjectName("pbNextpage")
        self.horizontalLayout.addWidget(self.pbNextpage)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pbClose = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pbClose.setObjectName("pbClose")
        self.horizontalLayout.addWidget(self.pbClose)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pbPrepage.setText(_translate("Dialog", "上一页"))
        self.pbNextpage.setText(_translate("Dialog", "下一页"))
        self.pbClose.setText(_translate("Dialog", "关闭"))

