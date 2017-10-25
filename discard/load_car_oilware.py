import xlrd
import pymysql as pdb

def getcon(dbname):
    conn=pdb.connect(host="127.0.0.1",user="root",passwd="",db=dbname)
    conn.set_charset('utf8')
    return conn

#xlsfile='G:\\车机类\\年度总公里\\2017年总公里.xlsx'
xlsfile='G:\\油耗\\一队油表.xls'
dbname='mysql_car'


data=xlrd.open_workbook(xlsfile)
#链接到mysql数据库，获得conn对象
conn=getcon(dbname)
table=data.sheet_by_name('K2路统计表')
nrows=table.nrows
ncols=table.ncols
cursor = conn.cursor()
time='2017-01'

for i in range(5,nrows-1):
    #carId = str(table.cell(i, 1).value)
    print(table.cell(i,3).value)
    if table.cell(i,3).value is "":
        continue
    carId="闽AY"+str(table.cell(i,3).value)[0:4]
    oilwear=table.cell(i,7).value
    maintain=table.cell(i,11).value
    follow=table.cell(i,12).value
    keyid=carId+"-"+time
    if oilwear is "":
        oilwear=0
    if maintain is "":
        maintain=0
    if follow is "":
        follow =0


    #print("maintain:"+str(maintain))
    #print("follow:"+str(follow))

    print(keyid,carId,time,oilwear,maintain,follow)
    effect_row = cursor.execute("insert into car_oilwear(id,car_id,month,oilwear,maintain,follow)values(%s,%s,%s,%s,%s,%s)",(keyid,carId,time,oilwear,maintain,follow))

conn.commit()
cursor.close()
conn.close()

