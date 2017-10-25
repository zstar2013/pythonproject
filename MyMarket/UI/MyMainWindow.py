from PyQt5 import QtWidgets

from UIC.MainWindow import Ui_MainWindow
from toolset.dialogTools import showInputPathDialog
from toolset.dialogTools import showFilePathDialog
import traceback


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 类初始化
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(lambda :showInputPathDialog(self, self.label_2.text(), lambda x: self.label_2.setText(x)))


    def close(self):
        sys.exit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dlg = MyMainWindow()
    dlg.show()

    sys.exit(app.exec_())
