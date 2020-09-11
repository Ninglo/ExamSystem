# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(520, 360)
        self.centralwidget = QtWidgets.QWidget(login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(0.93)

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(180, 45, 250, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")

        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(70, 250, 160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")

        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(270, 250, 160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.registerButton.setFont(font)
        self.registerButton.setObjectName("registerButton")

        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(470, 10, 23, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setToolTip("关闭")
        self.closeButton.clicked.connect(self.Exit)

        self.minButton = QtWidgets.QPushButton(self.centralwidget)
        self.minButton.setGeometry(QtCore.QRect(430, 10, 23, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.minButton.setFont(font)
        self.minButton.setObjectName("minButton")
        self.minButton.setToolTip("最小化")
        self.minButton.clicked.connect(self.WindowMin)

        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(70, 120, 360, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEditName.setFont(font)
        self.lineEditName.setFocus()
        self.lineEditName.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEditName.setObjectName("lineEditName")

        self.lineEditPwd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPwd.setGeometry(QtCore.QRect(70, 185, 360, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEditPwd.setFont(font)
        self.lineEditPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPwd.returnPressed.connect(self.login_button_click)
        self.lineEditPwd.setObjectName("lineEditPwd")

        self.tipLabel = QtWidgets.QLabel(self.centralwidget)
        self.tipLabel.setGeometry(QtCore.QRect(435, 125, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tipLabel.setFont(font)
        self.tipLabel.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tipLabel.setToolTip("")
        self.tipLabel.setToolTipDuration(-1)
        self.tipLabel.setStyleSheet("color: #F76677;")
        self.tipLabel.setText("")
        self.tipLabel.setObjectName("tipLabel")

        login_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 26))
        self.menubar.setObjectName("menubar")
        login_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login_window)
        self.statusbar.setObjectName("statusbar")
        login_window.setStatusBar(self.statusbar)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "鸿蒙考试系统"))
        self.titleLabel.setText(_translate("login_window", "鸿蒙考试系统"))
        self.loginButton.setText(_translate("login_window", "登录"))
        self.registerButton.setText(_translate("login_window", "注册"))
        self.lineEditName.setPlaceholderText(_translate("login_window", "用户名"))
        self.lineEditPwd.setPlaceholderText(_translate("login_window", "密码"))

    def Exit(self):
        exit()

    def WindowMin(self):
        self.setWindowState(Qt.WindowMinimized)

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