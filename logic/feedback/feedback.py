import xlrd
from xlutils.copy import copy
from tools import strtool as st
import logic.feedback.carDetail
import re

gConst = {"xls": {"sheetName": "新页面", "fileName": "G:\\油耗\\测试数据.xlsx"}}
mFilename = ["G:\\油耗\\9月\\1队\\2017年9月一车队油耗和汇总表.xls"]
mTime = "2017-09"


def getStartIndex(table):
    rowindex = None
    colindex = None
    nrows = table.nrows
    ncols = table.ncols
    for i in range(0, nrows):
        for j in range(0, ncols):
            if table.cell(i, j).value == "车号":
                rowindex = i
                colindex = j
                break
    if rowindex is None:
        return None
    item = [rowindex + 3, colindex]
    return item


def writetofile(list):
    oldWb = xlrd.open_workbook(gConst['xls']['fileName'], formatting_info=True)
    newWb = copy(oldWb);
    newWs = newWb.get_sheet(gConst['xls']['sheetName'])
    index = getlastrowindex()
    end = len(list)
    for i in range(0, end):
        newWs.write(i + index, 0, index + i + 1);
        jend = len(list[i])
        for j in range(0, jend):
            newWs.write(i + index, 1 + j, list[i][j])

    newWb.save(gConst['xls']['fileName']);


def getRoute(tablename):
    if st.contains(tablename, "专线"):
        return "海峡专线"
    if st.contains(tablename, "夜班"):
        return "夜班一号线"
    if st.contains(tablename.lower(), "k2"):
        return "k2"
    route = re.findall(r"\d+\.?\d*", tablename)
    return route[0]


# 对车辆id进行处理
def getCar_id(id, tablename):
    s = str(id)
    if (st.contains(str(id), "路")):
        s = str(id).split("路")[1].strip()
    if (st.contains(str(id), "线")):
        s = str(id).split("线")[1].strip()
    if st.contains(s, ".") or len(s) == 3:
        s = s.split(".")[0]
        if len(s)==4:
            return s
        route = getRoute(tablename)
        if route == "1" or route == "17" or route == "28" or route == "161":
            s = "A" + s
        elif route == "501":
            s = "B" + s
    return s


# 获取当前文件最后一行
def getlastrowindex():
    data = xlrd.open_workbook(gConst['xls']['fileName'])
    table = data.sheet_by_name(gConst['xls']['sheetName'])
    nrows = table.nrows
    return nrows


# 扫描文件
def scanfiles():
    list = []
    for i in range(0, len(mFilename)):
        data = xlrd.open_workbook(mFilename[i])
        for sheet in data.sheets():
            # if st.contains(sheet.name,"统计"):
            #     table = data.sheet_by_name(sheet.name)
            #     item=getStartIndex(table)
            #     list1.extend(load_sum_data(table, item))
            if st.contains(sheet.name, "汇总"):
                table = data.sheet_by_name(sheet.name)
                item = getStartIndex(table)
                if item is None:
                    continue
                list.extend(logic.feedback.carDetail.load_detail_data(table, item))
    return list


if __name__ == "__main__":
    list = scanfiles()
    print(list)
    writetofile(list)
