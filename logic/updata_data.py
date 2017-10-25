import xlrd
import pymysql as pdb

def getcon(dbname):
    conn=pdb.connect(host="127.0.0.1",user="root",passwd="",db=dbname)
    conn.set_charset('utf8')
    return conn

dbname='mysql_car'
#l=["7217","7221","7251","7293","7295","7298"]
#newroute="四队公备"
#newteam="4"
#newdes="2017年5月19日调四队公备"

#链接到mysql数据库，获得conn对象
conn=getcon(dbname)

#for i in range(0,len(l)):
    #carid="闽AY"+str(l[i])
    #effect_row = cursor.execute("update bus_info set route =%s,team =%s,descript=concat_ws(',',descript,%s) where car_id =%s",(newroute,newteam,newdes,carid))
#conn.commit()
#cursor.close()
conn.close()

