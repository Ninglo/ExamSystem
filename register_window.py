# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_register_window(object):
    def setupUi(self, register_window):
        register_window.setObjectName("register_window")
        register_window.resize(520, 370)
        self.centralwidget = QtWidgets.QWidget(register_window)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.Tool)
        self.setWindowOpacity(0.93)

        self.lineEditRegisterName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRegisterName.setGeometry(QtCore.QRect(70, 60, 360, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEditRegisterName.setFont(font)
        self.lineEditRegisterName.setObjectName("lineEditRegisterName")

        self.lineEditRegisterPwd1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRegisterPwd1.setGeometry(QtCore.QRect(70, 140, 360, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEditRegisterPwd1.setFont(font)
        self.lineEditRegisterPwd1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditRegisterPwd1.setObjectName("lineEditRegisterPwd1")

        self.lineEditRegisterPwd2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRegisterPwd2.setGeometry(QtCore.QRect(70, 220, 360, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEditRegisterPwd2.setFont(font)
        self.lineEditRegisterPwd2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditRegisterPwd2.setObjectName("lineEditRegisterPwd2")

        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(70, 300, 160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")

        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(270, 300, 160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.returnButton.setFont(font)
        self.returnButton.setObjectName("returnButton")

        self.tipLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.tipLabel2.setGeometry(QtCore.QRect(330, 110, 140, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tipLabel2.setFont(font)
        self.tipLabel2.setStyleSheet("color: rgb(255, 52, 12);")
        self.tipLabel2.setText("")
        self.tipLabel2.setWordWrap(True)
        self.tipLabel2.setObjectName("tipLabel2")

        self.tipLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.tipLabel3.setGeometry(QtCore.QRect(310, 270, 150, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tipLabel3.setFont(font)
        self.tipLabel3.setStyleSheet("color: rgb(255, 52, 12);")
        self.tipLabel3.setLineWidth(0)
        self.tipLabel3.setText("")
        self.tipLabel3.setWordWrap(True)
        self.tipLabel3.setObjectName("tipLabel3")

        self.tipLabel4 = QtWidgets.QLabel(self.centralwidget)
        self.tipLabel4.setGeometry(QtCore.QRect(180, 190, 391, 20))
        self.tipLabel4.setObjectName("tipLabel4")
        register_window.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(register_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 26))
        self.menubar.setObjectName("menubar")
        register_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(register_window)
        self.statusbar.setObjectName("statusbar")
        register_window.setStatusBar(self.statusbar)

        self.retranslateUi(register_window)
        QtCore.QMetaObject.connectSlotsByName(register_window)

    def retranslateUi(self, register_window):
        _translate = QtCore.QCoreApplication.translate
        register_window.setWindowTitle(_translate("register_window", "注册"))
        self.confirmButton.setText(_translate("register_window", "确定"))
        self.returnButton.setText(_translate("register_window", "返回"))
        self.tipLabel4.setText(_translate("register_window", "密码只能含有数字和字母，并且只能以字母开头"))
        self.lineEditRegisterName.setPlaceholderText(_translate("register_window", "用户名"))
        self.lineEditRegisterPwd1.setPlaceholderText(_translate("register_window", "密码"))
        self.lineEditRegisterPwd2.setPlaceholderText(_translate("register_window", "确认密码"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False