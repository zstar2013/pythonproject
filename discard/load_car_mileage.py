import xlrd
import pymysql as pdb

def getcon(dbname):
    conn=pdb.connect(host="127.0.0.1",user="root",passwd="",db=dbname)
    conn.set_charset('utf8')
    return conn

xlsfile='G:\\车机类\\年度总公里\\2017年总公里.xlsx'
dbname='mysql_car'


data=xlrd.open_workbook(xlsfile)
#链接到mysql数据库，获得conn对象
conn=getcon(dbname)
table=data.sheet_by_name('2017年汇总最新')
nrows=table.nrows
ncols=table.ncols
cursor = conn.cursor()
time='2017-08'

for i in range(1,nrows-1):
    #carId = str(table.cell(i, 1).value)
    carId="闽AY"+str(table.cell(i,3).value)[0:4]
    mileAge=table.cell(i,11).value
    keyid=carId+"-"+time
    print(keyid,carId,time,mileAge)
    effect_row = cursor.execute("insert into car_mileage(id,car_id,month,mileage)values(%s,%s,%s,%s)",(keyid,carId,time,mileAge))

conn.commit()
cursor.close()
conn.close()

