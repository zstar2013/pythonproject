from logic.GConst import gConst
from tools.strtool import contains
from xlutils.copy import copy
import os
import xlrd
import tools.xlstool as xt
import tools.filetool as ft
import traceback
from UI.Mydialog import MyWindow
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from tools.conftool import updateItem ,loadOption
from tools.dialogTools import showPathDialog
import configparser

def initTabOil(self:MyWindow):
    # for i in range(0, len(gConst["oil"]["month"])):
    #     self.cb_month.insertItem(i, gConst["oil"]["month"][i])
    filepath=loadinputPath()
    self.lb_inputpath.setText(filepath)
    filepath=loadOutputPath()
    self.lb_outputpath.setText(filepath+"/"+getSaveFileName(self))
    self.pbExport.clicked.connect(lambda: dataExport(self))
    #self.pbOutputPath.clicked.connect(lambda: showPathDialog(self, loadOutputPath(),))
    #self.pbInputPath.clicked.connect(lambda:showInputPathDialog(self, loadinputPath()))
    #self.cb_month.currentIndexChanged.connect(lambda :monthchange(self))
    self.pboutput.setValue(0)

#combobox发生改变触发时间
def monthchange(self:MyWindow):
    path=os.path.split(self.lb_outputpath.text())[0]
    self.lb_outputpath.setText(path+"/"+getSaveFileName(self))

#获取当前导出目录
def loadOutputPath():
    return  loadOption(gConst["settings"]["setfilepath"],"oil","outputpath")

#获取当前导入目录
def loadinputPath():
    return loadOption(gConst["settings"]["setfilepath"],"oil","inputpath")

def getSaveFileName(self:MyWindow):
    return self.de_oilstation.text().replace("/","年")+"月数据.xls"

def showInputPathDialog(self:MyWindow,filepath):

    if os.path.exists(filepath):
        path = QFileDialog.getExistingDirectory(self, "save Path Dialog", filepath)
        if path!="":
            self.lb_inputpath.setText(str(path))
            updateItem(gConst["settings"]["setfilepath"], "oil", "inputpath", path)
    else:
        QMessageBox.information(self,"提示","目录不存在！")



def showFilePathDialog(self:MyWindow,filepath):
    if os.path.exists(filepath):
        path = QFileDialog.getExistingDirectory(self, "save Path Dialog", filepath)
        if path!="":
            self.lb_outputpath.setText(str(path)+"/"+getSaveFileName(self))
            updateItem(gConst["settings"]["setfilepath"], "oil", "outputpath", path)
    else:
        QMessageBox.information(self,"提示","目录不存在！")

def dataExport(self:MyWindow):
    exportSheet1="明细"
    exportSheet2="汇总"
    items=searchforFile(self.lb_inputpath.text())
    exportPath=self.lb_outputpath.text()
    if not ft.checkfileexist(exportPath):
        xt.createNewFile(exportPath,exportSheet1)
    if not xt.checkSheetExist(exportPath,exportSheet1):
        xt.createSheet(exportPath,exportSheet1)
    try:
        xt.writetofile(items,exportPath,exportSheet1,lambda x:self.pboutput.setValue(x))

        QMessageBox.information(self,"提示","导出成功")
        self.pboutput.setValue(0)
    except:
        traceback.print_exc()

def writehuizong(items,filename,sheetname):
    oldWb = xlrd.open_workbook(filename, formatting_info=True)
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(sheetname)

def getlocation(filename,sheetname):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_name(sheetname)
    nrows = table.nrows
    ncols=table.ncols
    datalist=[]
    for i in range(0,ncols):
        if table.cell(i, 1)!="":
            item ={table.cell(i,1).value:[i,2]}
            datalist.append(item)
    for i in range(0,ncols):
        if table.cell(i, 4)!="":
            item ={table.cell(i,4).value:[i,5]}
            datalist.append(item)
    return datalist



def load_xml_data(table,routename):
    # 获取当前表格的行数
    nrows = table.nrows
    # 获取当前表格的列数
    ncols = table.ncols
    list = []
    index = xt.getStartIndex(table,"交易时间")
    for i in range(index, nrows):
        # carId = str(table.cell(i, 1).value)
        if table.cell(i, 0).value is "":
            continue
        if contains(table.cell(i, 0).value, "合计"):
            continue
        paytime = table.cell(i, 0).value
        carNum = table.cell(i, 1).value
        printnum = table.cell(i, 2).value
        carId = "闽AY" + str(table.cell(i, 3).value)[0:4]
        oiltpye = table.cell(i, 4).value
        station = table.cell(i, 5).value
        charge = table.cell(i, 6).value
        item = {}
        item["route"]=routename
        item["paytime"] = paytime
        item["cardnum"] = carNum
        item["printnum"] = printnum
        item["carid"] = carId
        item["oiltype"] = oiltpye
        item["oilstation"] = station
        item["charge"] = charge
        list.append(item)

    return list


def searchforFile(path):
    items = []
    dirs = os.listdir(path)
    for file in dirs:
        filepath = path + "\\" + str(file)
        if os.path.isdir(filepath):
            items += searchforFile(filepath)
        if os.path.isfile(filepath):
            if os.path.splitext(filepath)[1] == ".xls" and contains(filepath, "明细"):
                print(filepath)
                data = xlrd.open_workbook(filepath)
                table = data.sheet_by_name("1")
                list = load_xml_data(table,os.path.split(filepath)[1][0:-6])
                for item in list:
                    items.append(item)
    return items


