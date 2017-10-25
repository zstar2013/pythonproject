import threading
import pymysql as pdb
import contextlib


class PyDbHelper:
    # 默认数据库ip
    db_ip = "127.0.0.1"
    # 默认用户
    user_name = "root"
    # 默认密码
    usr_pwd = ""
    # 默认库名
    #db_name="bus_db"
    db_name = "mysql_car"
    # 默认charset
    charset = 'utf8'
    instance = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    # 设置配置信息
    def set_config(self, host=db_ip, user=user_name, passwd=usr_pwd, db=db_name):
        self.db_ip = host
        self.user_name = user
        self.usr_pwd = passwd
        self.db_name = db

    # 获取单例
    @staticmethod
    def GetInstance():
        if (PyDbHelper.instance == None):
            PyDbHelper.mutex.acquire()
            if (PyDbHelper.instance == None):
                # print('初始化实例')
                PyDbHelper.instance = PyDbHelper()
            else:
                # print('单例已经实例化')
                PyDbHelper.mutex.release()

        return PyDbHelper.instance

    # 定义上下文管理器，连接后自动关闭连接
    @contextlib.contextmanager
    def mysql(self, host=db_ip, user=user_name, passwd=usr_pwd, db=db_name, charset='utf8'):
        conn = pdb.connect(host=host, user=user, passwd=passwd, db=db, charset=charset)
        cursor = conn.cursor(cursor=pdb.cursors.DictCursor)
        try:
            yield cursor
        finally:
            conn.commit()
            cursor.close()
            conn.close()

    # 获得查询数据json数值
    def get_items(self, querySQl):
        with self.mysql() as cursor:
            cursor.execute(querySQl)
        return cursor.fetchall()

    # 获得查询数据总数
    def getSize(self, querySQL):
        with self.mysql() as cursor:
            cursor.execute(querySQL)
        return cursor.fetchone().get('COUNT(*)')

    # 获得查询数据总数
    def insert(self, insertSQL):
        with self.mysql() as cursor:
            result = cursor.execute(insertSQL)
        return result

    #进行数据更新操作
    def update(self,updateSQL):
        with self.mysql() as cursor:
            result = cursor.execute(updateSQL)
        return result


    # 测试指定参数下数据库连接
    def test_connect(self, host=db_ip, user=user_name, passwd=usr_pwd, db=db_name, charset='utf8'):
        result = "ok"
        conn = None
        cursor = None
        try:
            conn = pdb.connect(host=host, user=user, passwd=passwd, db=db, charset=charset)
            cursor = conn.cursor(cursor=pdb.cursors.DictCursor)
        except Exception as err:
            print(err)
            result = err
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
            return result


if __name__ == "__main__":
    pyd = PyDbHelper.GetInstance()
