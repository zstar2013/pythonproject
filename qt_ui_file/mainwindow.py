# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, -1, 1281, 671))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(250, 30, 931, 481))
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 520, 321, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_tbpre = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_tbpre.setObjectName("btn_tbpre")
        self.horizontalLayout.addWidget(self.btn_tbpre)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.btn_tbnext = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_tbnext.setObjectName("btn_tbnext")
        self.horizontalLayout.addWidget(self.btn_tbnext)
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 120, 171, 144))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbcarid = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbcarid.setObjectName("lbcarid")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbcarid)
        self.edit_carid = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_carid.setObjectName("edit_carid")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_carid)
        self.lb_route = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_route.setObjectName("lb_route")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lb_route)
        self.edit_route = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.edit_route.setObjectName("edit_route")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_route)
        self.lb_team = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_team.setObjectName("lb_team")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lb_team)
        self.lb_powertype = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_powertype.setObjectName("lb_powertype")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lb_powertype)
        self.cbPowertype = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cbPowertype.setObjectName("cbPowertype")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cbPowertype)
        self.cbScrap = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.cbScrap.setObjectName("cbScrap")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cbScrap)
        self.cb_team = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cb_team.setObjectName("cb_team")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_team)
        self.btn_query = QtWidgets.QPushButton(self.tab_2)
        self.btn_query.setGeometry(QtCore.QRect(60, 540, 101, 51))
        self.btn_query.setObjectName("btn_query")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 530, 261, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.pboutput = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        self.pboutput.setProperty("value", 24)
        self.pboutput.setObjectName("pboutput")
        self.horizontalLayout_2.addWidget(self.pboutput)
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 291, 261))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 231, 181))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lb_inputpath = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lb_inputpath.setText("")
        self.lb_inputpath.setObjectName("lb_inputpath")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lb_inputpath)
        self.pbInputPath = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pbInputPath.setObjectName("pbInputPath")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pbInputPath)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lb_outputpath = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lb_outputpath.setMinimumSize(QtCore.QSize(0, 14))
        self.lb_outputpath.setText("")
        self.lb_outputpath.setObjectName("lb_outputpath")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lb_outputpath)
        self.de_oilstation = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.de_oilstation.setDate(QtCore.QDate(2017, 1, 1))
        self.de_oilstation.setObjectName("de_oilstation")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.de_oilstation)
        self.pbOutputPath = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pbOutputPath.setObjectName("pbOutputPath")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pbOutputPath)
        self.pbExport = QtWidgets.QPushButton(self.groupBox)
        self.pbExport.setGeometry(QtCore.QRect(60, 220, 179, 23))
        self.pbExport.setObjectName("pbExport")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 30, 501, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(30, 30, 251, 181))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lb_teamfeedbackinputpath = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.lb_teamfeedbackinputpath.setText("")
        self.lb_teamfeedbackinputpath.setObjectName("lb_teamfeedbackinputpath")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lb_teamfeedbackinputpath)
        self.pb_add_teamfeedbackpath = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.pb_add_teamfeedbackpath.setObjectName("pb_add_teamfeedbackpath")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pb_add_teamfeedbackpath)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lb_teamfeedbackoutputpath = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.lb_teamfeedbackoutputpath.setText("")
        self.lb_teamfeedbackoutputpath.setObjectName("lb_teamfeedbackoutputpath")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lb_teamfeedbackoutputpath)
        self.pb_feedbackoutputpath = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.pb_feedbackoutputpath.setObjectName("pb_feedbackoutputpath")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pb_feedbackoutputpath)
        self.lb_feedback_team = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.lb_feedback_team.setObjectName("lb_feedback_team")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_feedback_team)
        self.cb_feedback_team = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.cb_feedback_team.setObjectName("cb_feedback_team")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cb_feedback_team)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.de_feedback = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.de_feedback.setDate(QtCore.QDate(2017, 1, 1))
        self.de_feedback.setObjectName("de_feedback")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.de_feedback)
        self.pb_teamfeedbackexport = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_teamfeedbackexport.setGeometry(QtCore.QRect(80, 220, 159, 23))
        self.pb_teamfeedbackexport.setObjectName("pb_teamfeedbackexport")
        self.lv_feedback_path = QtWidgets.QListView(self.groupBox_2)
        self.lv_feedback_path.setGeometry(QtCore.QRect(320, 20, 151, 211))
        self.lv_feedback_path.setObjectName("lv_feedback_path")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.twMailage = QtWidgets.QTableWidget(self.tab)
        self.twMailage.setGeometry(QtCore.QRect(250, 30, 931, 481))
        self.twMailage.setAutoScroll(True)
        self.twMailage.setRowCount(15)
        self.twMailage.setColumnCount(9)
        self.twMailage.setObjectName("twMailage")
        self.twMailage.horizontalHeader().setDefaultSectionSize(100)
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuAlter = QtWidgets.QMenu(self.menubar)
        self.menuAlter.setObjectName("menuAlter")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setCheckable(True)
        self.actionSetting.setChecked(False)
        self.actionSetting.setObjectName("actionSetting")
        self.actionlink = QtWidgets.QAction(MainWindow)
        self.actionlink.setObjectName("actionlink")
        self.actiontest = QtWidgets.QAction(MainWindow)
        self.actiontest.setObjectName("actiontest")
        self.menu.addAction(self.actionlink)
        self.menu.addSeparator()
        self.menu.addAction(self.actiontest)
        self.menu_3.addAction(self.actionSetting)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuAlter.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tableWidget, self.btn_tbpre)
        MainWindow.setTabOrder(self.btn_tbpre, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.btn_tbnext)
        MainWindow.setTabOrder(self.btn_tbnext, self.edit_carid)
        MainWindow.setTabOrder(self.edit_carid, self.edit_route)
        MainWindow.setTabOrder(self.edit_route, self.cbPowertype)
        MainWindow.setTabOrder(self.cbPowertype, self.cbScrap)
        MainWindow.setTabOrder(self.cbScrap, self.cb_team)
        MainWindow.setTabOrder(self.cb_team, self.btn_query)
        MainWindow.setTabOrder(self.btn_query, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.pbExport)
        MainWindow.setTabOrder(self.pbExport, self.pb_add_teamfeedbackpath)
        MainWindow.setTabOrder(self.pb_add_teamfeedbackpath, self.pb_feedbackoutputpath)
        MainWindow.setTabOrder(self.pb_feedbackoutputpath, self.pb_teamfeedbackexport)
        MainWindow.setTabOrder(self.pb_teamfeedbackexport, self.twMailage)
        MainWindow.setTabOrder(self.twMailage, self.pbInputPath)
        MainWindow.setTabOrder(self.pbInputPath, self.cb_feedback_team)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "测试程序"))
        self.btn_tbpre.setText(_translate("MainWindow", "上一页"))
        self.label.setText(_translate("MainWindow", "第"))
        self.label_2.setText(_translate("MainWindow", "页"))
        self.btn_tbnext.setText(_translate("MainWindow", "下一页"))
        self.lbcarid.setText(_translate("MainWindow", "车牌号："))
        self.lb_route.setText(_translate("MainWindow", "线路："))
        self.lb_team.setText(_translate("MainWindow", "车队："))
        self.lb_powertype.setText(_translate("MainWindow", "燃料类型："))
        self.cbScrap.setText(_translate("MainWindow", "是否含报废"))
        self.btn_query.setText(_translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "查询车辆"))
        self.label_3.setText(_translate("MainWindow", "进度："))
        self.groupBox.setTitle(_translate("MainWindow", "油料中心"))
        self.label_4.setText(_translate("MainWindow", "选择年月"))
        self.label_7.setText(_translate("MainWindow", "油耗数据目录："))
        self.pbInputPath.setText(_translate("MainWindow", "设置数据目录"))
        self.label_5.setText(_translate("MainWindow", "当前导出目录："))
        self.de_oilstation.setDisplayFormat(_translate("MainWindow", "yyyy/M"))
        self.pbOutputPath.setText(_translate("MainWindow", "设置导出目录"))
        self.pbExport.setText(_translate("MainWindow", "导出数据"))
        self.groupBox_2.setTitle(_translate("MainWindow", "车队反馈报表"))
        self.label_6.setText(_translate("MainWindow", "车队反馈目录："))
        self.pb_add_teamfeedbackpath.setText(_translate("MainWindow", "添加车队反馈目录"))
        self.label_8.setText(_translate("MainWindow", "当前导出："))
        self.pb_feedbackoutputpath.setText(_translate("MainWindow", "设置导出文件"))
        self.lb_feedback_team.setText(_translate("MainWindow", "选择车队"))
        self.label_10.setText(_translate("MainWindow", "选择年月"))
        self.de_feedback.setDisplayFormat(_translate("MainWindow", "yyyy/M"))
        self.pb_teamfeedbackexport.setText(_translate("MainWindow", "导出数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "查询油耗"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "查询公里"))
        self.menu.setTitle(_translate("MainWindow", "连接"))
        self.menuAlter.setTitle(_translate("MainWindow", "修改"))
        self.menu_3.setTitle(_translate("MainWindow", "设置"))
        self.actionSetting.setText(_translate("MainWindow", "模糊检索设定"))
        self.actionlink.setText(_translate("MainWindow", "连接参数"))
        self.actiontest.setText(_translate("MainWindow", "测试连接"))
