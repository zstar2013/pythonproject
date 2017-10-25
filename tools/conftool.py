import configparser
import tools.filetool as ft
from logic.GConst import gConst

def updateConf(filename,updateItems):
    cf = configparser.ConfigParser()
    for key in updateItems.keys():
        cf.add_section(key)
        item = updateItems[key]
        for inerkey in item.keys():
            cf.set(key, inerkey, item[inerkey])
    with open(filename, "w+") as f:
        cf.write(f)

def updateItem(filename,section,key,value):
    cf = configparser.ConfigParser()
    cf.read(filename)
    cf.set(section, key, value)
    with open(filename, "w+") as f:
        cf.write(f)

def loadOption(settingPath, section, option):
    cf = configparser.ConfigParser()
    cf.read(settingPath)
    return cf.get(section, option)


#创建配置文件
def createConfFile(filename):
    ft.createfile(filename)




if __name__ == '__main__':
    #updateItem("D:\\设置\\settings.ini", "oil", "inputpath", "G:/sss/sss")
    filename=gConst["settings"]["setfilepath"]
    createConfFile(filename=filename)
    items=gConst["defaultSettings"]
    updateConf(filename=filename, updateItems=items)