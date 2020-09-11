import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from login_window import Ui_login_window
from register_function import Register
from data_operation import judge_in, judge_match
from ability import select

class QSSLoad:
    def __init__(self):
        pass

    @staticmethod
    def readQssFile(qssFileName):
        with open(qssFileName, 'r', encoding="utf-8") as file:
            return file.read()

class Login(Ui_login_window, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self._name = ""
        self._pwd = ""
        self.setFixedSize(self.width(), self.height())   # 固定窗口大小

    def initUi(self):
        self.loginButton.clicked.connect(self.login_button_click)
        self.registerButton.clicked.connect(self.register_button_click)
        self.lineEditName.textChanged.connect(self.show_tip)

    def show_tip(self):    # 登陆界面用户名不存在提示，后续需修改：tip_label失去焦点时才触发判断用户名存在的事件
        if not judge_in(self.lineEditName.text()) and self.lineEditName.text() != "":
            self.tipLabel.setText("用户名不存在！")
        else:
            self.tipLabel.setText("")

    def login_button_click(self):
        # self._name = self.lineEdit_name.text()
        # self._pwd = self.lineEdit_pwd.text()
        if judge_in(self.lineEditName.text()) and judge_match(self.lineEditName.text(), self.lineEditPwd.text()):
            #reply = QMessageBox.information(self, "登录成功", "登录成功", QMessageBox.Yes)
            messageBox1 = QMessageBox()
            messageBox1.setWindowTitle("提示")
            messageBox1.setText("登录成功！")
            messageBox1.addButton(QPushButton("确定"), QMessageBox.YesRole)
            messageBox1.exec_()
            if messageBox1.clickedButton():
                self.select = select()
                qssFileName = "./pattern/select.qss"
                qssFile = QSSLoad.readQssFile(qssFileName)
                self.select.setStyleSheet(qssFile)
                self.select.show()  # 登陆成功后跳转新界面
                self.close()
        else:
            messageBox2 = QMessageBox()
            messageBox2.setWindowTitle("提示")
            messageBox2.setText("用户名或密码错误！")
            messageBox2.addButton(QPushButton("确定"), QMessageBox.YesRole)
            messageBox2.exec_()
            #QMessageBox.warning(self, "登录失败", "用户名或密码错误", QMessageBox.Yes)
            self.lineEditPwd.setText("")
            self.lineEditPwd.setFocus()


    def register_button_click(self):
        qssFileName = "./pattern/register.qss"
        qssFile = QSSLoad.readQssFile(qssFileName)
        self.registerWindow = Register()
        self.registerWindow.setStyleSheet(qssFile)
        self.registerWindow.show()
        self.lineEditName.setText("")
        self.lineEditPwd.setText("")
        self.tipLabel.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = Login()
    loginWindow.show()
    sys.exit(app.exec_())
