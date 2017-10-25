import xlrd
import xlwt
from xlutils.copy import copy
from tools import strtool as st

gConst = {"xls": {"sheetName": "新页面", "fileName": "G:\\油耗\\测试数据.xlsx"}}
mFilename=["G:\\油耗\\一队油表.xls","G:\\油耗\\三车队油表.xls","G:\\油耗\\四队油表.xls","G:\\油耗\\五队油表.xls","G:\\油耗\\营达车队.xls"]
mTime="2017-09"

def getStartIndex(table):
    rowindex=None
    colindex=None
    nrows=table.nrows
    ncols=table.ncols
    for i in range(0,nrows):
        for j in range(0,ncols):
            if table.cell(i,j).value=="车号":
                rowindex=i
                colindex=j
                break
    item=[rowindex+3,colindex]
    return item

def writetofile(list):

    oldWb = xlrd.open_workbook(gConst['xls']['fileName'], formatting_info=True)
    newWb = copy(oldWb);
    newWs = newWb.get_sheet(gConst['xls']['sheetName'])
    index=getlastrowindex()
    end=len(list)
    for i in range(0,end):
        newWs.write(i+index, 0, index+i+1);
        jend=len(list[i])
        for j in range(0,jend):
            newWs.write(i+index, 1+j, list[i][j])

    newWb.save(gConst['xls']['fileName']);




#读取数据文件
def load_data(table,item):
    nrows = table.nrows
    list = []
    indexR=item[0]
    carNoC=item[1]
    for i in range(indexR, nrows):
        # carId = str(table.cell(i, 1).value)
        #print(table.cell(i, carNoC).value)
        if table.cell(i, carNoC).value is "":
            continue
        if st.contains(str(table.cell(i,carNoC).value),"小计"):
            continue
        item=[]
        item.append(str(table.cell(i, carNoC).value)[0:4])#车辆id
        item.append(table.cell(i,carNoC+1).value)#车公里
        item.append(table.cell(i,carNoC+2).value)#指标总量
        item.append(table.cell(i, carNoC + 3).value)  # 百公里指标target
        item.append(table.cell(i, carNoC + 4).value)  # 车辆油耗
        #item.append(table.cell(i, carNoC + 5).value)  # 实际百公里
        item.append(table.cell(i, carNoC + 6).value)  # 实际节约
        item.append(table.cell(i, carNoC + 7).value)  # 实际超耗
        item.append(table.cell(i, carNoC + 8).value)  # 二保
        item.append(table.cell(i, carNoC + 9).value)  # 跟车
        list.append(item)
    return list

#获取当前文件最后一行
def getlastrowindex():
    data = xlrd.open_workbook(gConst['xls']['fileName'])
    table = data.sheet_by_name(gConst['xls']['sheetName'])
    nrows = table.nrows
    return nrows

#扫描文件
def scanfiles():
    list=[]
    for i in range(0,len(mFilename)):
        data=xlrd.open_workbook(mFilename[i])
        for sheet in data.sheets():
            if st.contains(sheet.name,"统计"):
                table = data.sheet_by_name(sheet.name)
                item=getStartIndex(table)
                list.extend(load_data(table,item))
    return list


if __name__=="__main__":
    list=scanfiles()
    print(list)
    writetofile(list)
