import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    #创建一个名为closeApp的信号
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #获取一个closeApp信号
        self.c = Communicate()
        #将这个信号的结果绑定至窗口关闭事件
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Emit signal")
        self.show()

    def mousePressEvent(self, event):
        #触发closeApp信号
        self.c.closeApp.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())