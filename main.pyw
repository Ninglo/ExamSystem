import sys
from PyQt5.QtWidgets import QApplication
from login_function import Login

class QSSLoad:
    def __init__(self):
        pass

    @staticmethod
    def readQssFile(qssFileName):
        with open(qssFileName, 'r', encoding="utf-8") as file:
            return file.read()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qssFileName = "./pattern/login.qss"
    qssFile = QSSLoad.readQssFile(qssFileName)

    loginWindow = Login()
    loginWindow.setStyleSheet(qssFile)
    loginWindow.show()
    sys.exit(app.exec_())
