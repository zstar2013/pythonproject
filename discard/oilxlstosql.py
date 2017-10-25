import xlrd
import xlwt
from xlutils.copy import copy
from tools import strtool as st

gConst = {"xls": {"sheetName": "新页面", "fileName": "G:\\油耗\\测试数据.xlsx"}}
mFilename=["G:\\油耗\\一队油表.xls","G:\\油耗\\三车队油表.xls","G:\\油耗\\四队油表.xls","G:\\油耗\\五队油表.xls","G:\\油耗\\营达车队.xls"]
mTime="2017-08"

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
    item=[rowindex+3,colindex,colindex+4,colindex+8,colindex+9,colindex+1]
    return item

def writetofile(list,sheetname):


    # styleBoldRed = xlwt.easyxf('font: color-index red, bold on');
    # headerStyle = styleBoldRed;
    # wb = xlwt.Workbook();
    # ws = wb.add_sheet(self.gConst['xls']['sheetName']);
    # ws.write(0, 0, "序号", headerStyle)
    # ws.write(0, 1, "车号", headerStyle)
    # ws.write(0, 2, "月份", headerStyle)
    # ws.write(0, 3, "油耗", headerStyle)
    # ws.write(0,4,"二保",headerStyle)
    # ws.write(0,5,"跟车",headerStyle)
    # wb.save(self.gConst['xls']['fileName']);

    # open existed xls file
    # newWb = xlutils.copy(gConst['xls']['fileName']);
    # newWb = copy(gConst['xls']['fileName']);
    oldWb = xlrd.open_workbook(gConst['xls']['fileName'], formatting_info=True)
    newWb = copy(oldWb);
    newWs = newWb.get_sheet(gConst['xls']['sheetName'])
    index=getlastrowindex()
    end=len(list)
    for i in range(0,end):
        newWs.write(i+index, 0, index+i);
        newWs.write(i+index, 1, list[i].get("carId"))
        newWs.write(i +index, 2, list[i].get("time"))
        newWs.write(i+index, 3, list[i].get("oilwear"))
        newWs.write(i+index, 4, list[i].get("maintain"));
        newWs.write(i+index, 5, list[i].get("follow"));
        newWs.write(i+index,6,list[i].get("mileage"))
    print
    "write new values ok";
    newWb.save(gConst['xls']['fileName']);
    print
    "save with same name ok";



#读取数据文件
def load_data(table,item):
    nrows = table.nrows
    ncols = table.ncols
    list = []
    indexR=item[0]
    carNoC=item[1]
    oilwearC=item[2]
    maintainC=item[3]
    followC=item[4]
    mileageC=item[5]
    for i in range(indexR, nrows):
        # carId = str(table.cell(i, 1).value)
        print(table.cell(i, carNoC).value)
        if table.cell(i, carNoC).value is "":
            continue
        carId = "闽AY" + str(table.cell(i, carNoC).value)[0:4]
        oilwear = table.cell(i, oilwearC).value
        maintain = table.cell(i, maintainC).value
        follow = table.cell(i, followC).value
        mileage=table.cell(i,mileageC).value
        keyid = carId + "-" + mTime
        if oilwear is "":
            oilwear = 0
        if maintain is "":
            maintain = 0
        if follow is "":
            follow = 0
        item = {}
        item["keyid"] = keyid
        item["carId"] = carId
        item["time"] = mTime
        item["oilwear"] = oilwear
        item["maintain"] = maintain
        item["follow"] = follow
        item["mileage"]=mileage
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
    for i in range(0,len(mFilename)):
        data=xlrd.open_workbook(mFilename[i])
        for sheet in data.sheets():
            print(sheet.name)
            if st.containsAny(sheet.name,"统计"):
                table = data.sheet_by_name(sheet.name)
                item=getStartIndex(table)
                list=load_data(table,item)
                writetofile(list,sheet.name)

if __name__=="__main__":
    scanfiles()
