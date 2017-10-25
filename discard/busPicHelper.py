import os
class BusPicHelper:
    def __init__(self):
        pass

    import os

    # 遍历指定目录，显示目录下的所有文件名
    def eachFile(filepath):
        pathDir = os.listdir(filepath)
        for allDir in pathDir:
            child = os.path.join('%s%s' % (filepath, allDir))
            print
            child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题





    if __name__ == '__main__':
        filePath = "D:\\FileDemo\\Java\\myJava.txt"
        filePathI = "D:\\FileDemo\\Python\\pt.py"
        filePathC = "C:\\"
        eachFile(filePathC)
