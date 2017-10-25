import xlrd
import pymysql as pdb

def getcon(dbname):
    conn=pdb.connect(host="127.0.0.1",user="root",passwd="",db=dbname)
    conn.set_charset('utf8')
    return conn

xlsfile='G:\myfile\车辆信息表（5月版本）.xlsx'
dbname='mypydb'


data=xlrd.open_workbook(xlsfile)
#链接到mysql数据库，获得conn对象
conn=getcon(dbname)
table=data.sheets()[0]
nrows=table.nrows
ncols=table.ncols
cursor = conn.cursor()

for i in range(1,nrows):
    team=table.cell(i,0).value
    route=table.cell(i,1).value
    car_type=table.cell(i,2).value
    length=table.cell(i,3).value
    busload=table.cell(i,4).value
    carId="闽AY"+str(table.cell(i,5).value)[0:4]
    uptime=table.cell(i,6).value
    company="1"
    #print("team:"+str(team)+"------route:"+str(route)+"-----car_type:"+str(car_type)+"-----length:"+str(length)+"------busload:"+str(busload)+"------carId:"+carId+"----uptime:"+str(uptime))
    effect_row = cursor.execute("insert into bus_info(car_id,route,length,busload,uptime,cartype,company,team)values(%s,%s,%s,%s,%s,%s,%s,%s)",(carId,route,length,busload,uptime,car_type,company,team))
    

conn.commit()
cursor.close()
conn.close()

