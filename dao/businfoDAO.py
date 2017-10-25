# DAO
from logic.PyDbHelper import PyDbHelper
from tools.sqltool import sqltool
from logic.GConst import gConst
import traceback


class BusinfoDAO:
    # 记录当前查询数据索引
    index_count = 0
    # 页面大小
    pagesize = 15
    pdh = None
    st = None
    keymap = ['car_id', 'route', 'length', 'busload', 'uptime', 'cartype','scrap', 'team', 'descript']
    mBusInfoDict = None
    mBusInfoLikeDict = None

    # 默认查询语句
    default_query = "select * from bus_info ORDER BY car_id ASC limit "

    def __init__(self):
        self.pdh = PyDbHelper.GetInstance()
        self.st = sqltool()

    # 默认查询方法
    def defaultQuery(self):
        list = self.pdh.get_items(self.default_query+str(self.index_count)+","+str(self.pagesize))
        return list

    def query(self, dict, likedict={}):
        self.mBusInfoDict = dict
        self.mBusInfoLikeDict = likedict
        # sql=self.st.get_s_sql(table="bus_info",keys=self.keymap,conditions=dict,isdistinct=0)
        sql = self.st.get_s_sql_like(table="bus_info", keys=self.keymap, conditions=dict, likedict=likedict,
                                     isdistinct=0)
        list = self.pdh.get_items(
            str(sql) + " ORDER BY car_id ASC limit " + str(self.index_count) + "," + str(self.pagesize))
        return list

    def queryByCarId(self,car_id):
        dict={}
        dict["car_id"]=car_id
        sql = self.st.get_s_sql(table="bus_info", keys=self.keymap, conditions=dict,isdistinct=0)
        list=self.pdh.get_items(sql)
        return list

    def update(self,item):
        dict = {}
        dict["car_id"] = item["car_id"]
        sql = self.st.get_u_sql(table="bus_info",value=item,conditions=dict)
        return self.pdh.update(sql)


    def turntopage(self, pageIndex):
        self.index_count = pageIndex * self.pagesize
        print("indexcount:" + str(self.index_count))
        list = self.query(self.mBusInfoDict,self.mBusInfoLikeDict)
        return list

    def defaultresultcount(self):
        self.mBusInfoDict = {'team': '1'}
        self.mBusInfoLikeDict = {}
        return self.pdh.getSize(self.st.get_count_sql(table="bus_info", conditions=self.mBusInfoDict, isdistinct=0))

    def getresultconut(self, like={}):
        return self.pdh.getSize(self.st.get_count_sql(table="bus_info", conditions=self.mBusInfoDict, like=like, isdistinct=0))

    def getcursor(self):
        cursor = self.pdh.getCursor()
        return cursor

    # 返回表头
    def getHeader(self):
        return gConst["businfo"]["header"]
