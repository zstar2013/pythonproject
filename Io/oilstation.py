import os
import xlrd
from logic.PyDbHelper import PyDbHelper
from tools.sqltool import sqltool
from tools.strtool import containsAny
from tools.xlstool import writetofile


mPdh = None
mSt = None
mTime = None
filepath = "G:\\油耗\\油料中心\\8月"


def load_xml_data(table):
    # 获取当前表格的行数
    nrows = table.nrows
    # 获取当前表格的列数
    ncols = table.ncols
    list = []
    index = getStartIndex(table)
    print("index:"+str(index))
    total=0
    try:
        total = table.cell(index, 2).value
    except Exception as err:
        print(index)
        print(err)

    item={}
    item["total"] = total

    return item


# 获取起始值
def getStartIndex(table):
    rowindex = None
    nrows = table.nrows
    ncols = table.ncols
    breakfg=0
    for i in range(0, nrows):
        if breakfg:
            break
        for j in range(0, ncols):
            if table.cell(i, j).value == "总计":
                rowindex = i
                breakfg=1
                break
    return rowindex


def searchforFile(path):
    items = []
    dirs = os.listdir(path)
    for file in dirs:
        filepath = path + "\\" + str(file)
        if os.path.isdir(filepath):
            items += searchforFile(filepath)
            # sqlcontent+=searchforFile(filepath)
        if os.path.isfile(filepath):
            if os.path.splitext(filepath)[1] == ".xls" and containsAny(str(file), "汇总"):
                print(filepath)
                data = xlrd.open_workbook(filepath)
                table = data.sheet_by_name("1")
                item = load_xml_data(table)
                item["route"]=str(file).replace("汇总.xls","")
                items.append(item)
    return items


if __name__ == "__main__":
    mPdh = PyDbHelper.GetInstance()
    mSt = sqltool()
    items = searchforFile(filepath)
    sql = ""
    for item in items:
        print(item.keys())
        print (item)

    writetofile(items,"G:\\油耗\\测试数据.xlsx","新页面")
