from logic.PyDbHelper import PyDbHelper
from tools.sqltool import sqltool


class BusMileageDAO:
    # 记录当前查询数据索引
    index_count = 0
    # 页面大小
    pagesize = 15
    pdh = None
    st = None
    header = ['车辆id', '线路', '所属车队', '月份', '行驶公里', '备注']
    keymap = ['car_id', 'route', 'team', 'month', 'mileage', 'descript']
    mDict = None
    mLikeDict = None

    def __init__(self):
        self.pdh = PyDbHelper.GetInstance()
        self.st = sqltool()

    # 默认查询方法
    def defaultQuery(self):
        list = self.pdh.get_items(self.default_query)
        return list
