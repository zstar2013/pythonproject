import os
import xlrd
from logic.PyDbHelper import PyDbHelper
from tools.sqltool import sqltool
from tools.strtool import containsAny

gConst = {"attr": ["paytime", "cardnum", "printnum", "carid", "oiltype", "oilstation", "charge"]}
mPdh = None
mSt = None
mTime = None
filepath = "G:\\油耗\\油料中心\\8月"


# #读取数据文件
# def load_data(table,item):
#     nrows = table.nrows
#     ncols = table.ncols
#     list = []
#     indexR=item[0]
#     carNoC=item[1]
#     oilwearC=item[2]
#     maintainC=item[3]
#     followC=item[4]
#     mileageC=item[5]
#     for i in range(indexR, nrows):
#         # carId = str(table.cell(i, 1).value)
#         print(table.cell(i, carNoC).value)
#         if table.cell(i, carNoC).value is "":
#             continue
#         carId = "闽AY" + str(table.cell(i, carNoC).value)[0:4]
#         oilwear = table.cell(i, oilwearC).value
#         maintain = table.cell(i, maintainC).value
#         follow = table.cell(i, followC).value
#         mileage=table.cell(i,mileageC).value
#         keyid = carId + "-" + mTime
#         if oilwear is "":
#             oilwear = 0
#         if maintain is "":
#             maintain = 0
#         if follow is "":
#             follow = 0
#         item = {}
#         item["keyid"] = keyid
#         item["carId"] = carId
#         item["time"] = mTime
#         item["oilwear"] = oilwear
#         item["maintain"] = maintain
#         item["follow"] = follow
#         item["mileage"]=mileage
#         list.append(item)
#     return list

def load_xml_data(table):
    # 获取当前表格的行数
    nrows = table.nrows
    # 获取当前表格的列数
    ncols = table.ncols
    list = []
    index = getStartIndex(table)
    for i in range(index, nrows):
        # carId = str(table.cell(i, 1).value)
        if table.cell(i, 0).value is "":
            continue
        if containsAny(table.cell(i, 0).value, "合计"):
            continue
        paytime = table.cell(i, 0).value
        carNum = table.cell(i, 1).value
        printnum = table.cell(i, 2).value
        carId = "闽AY" + str(table.cell(i, 3).value)[0:4]
        oiltpye = table.cell(i, 4).value
        station = table.cell(i, 5).value
        charge = table.cell(i, 6).value
        item = {}
        item["paytime"] = paytime
        item["cardnum"] = carNum
        item["printnum"] = printnum
        item["carid"] = carId
        item["oiltype"] = oiltpye
        item["oilstation"] = station
        item["charge"] = charge
        list.append(item)

    return list


# 获取起始值
def getStartIndex(table):
    rowindex = None
    nrows = table.nrows
    ncols = table.ncols
    for i in range(0, nrows):
        for j in range(0, ncols):
            if table.cell(i, j).value == "交易时间":
                rowindex = i + 1
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
            if os.path.splitext(filepath)[1] == ".xls" and containsAny(filepath, "明细"):
                print(filepath)
                data = xlrd.open_workbook(filepath)
                table = data.sheet_by_name("1")
                list = load_xml_data(table)
                for item in list:
                    items.append(item)
                    # sql=mSt.get_i_sql("station_charge", item)
                    # sqlcontent+=sql+";"
    return items


if __name__ == "__main__":
    mPdh = PyDbHelper.GetInstance()
    mSt = sqltool()
    items = searchforFile(filepath)
    sql = ""
    for item in items:
        sql += mSt.get_i_sql("station_charge", item) + ";"
    mPdh.insert(sql)
