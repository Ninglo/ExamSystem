# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(0.93)

        self.button_exam = QtWidgets.QPushButton(self.centralwidget)
        self.button_exam.setGeometry(QtCore.QRect(240, 130, 150, 150))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.button_exam.setFont(font)
        self.button_exam.setObjectName("button_exam")

        self.button_exercise = QtWidgets.QPushButton(self.centralwidget)
        self.button_exercise.setGeometry(QtCore.QRect(410, 130, 150, 150))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.button_exercise.setFont(font)
        self.button_exercise.setObjectName("button_exercise")

        self.button_wrong = QtWidgets.QPushButton(self.centralwidget)
        self.button_wrong.setGeometry(QtCore.QRect(240, 300, 150, 150))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.button_wrong.setFont(font)
        self.button_wrong.setObjectName("button_wrong")

        self.button_star = QtWidgets.QPushButton(self.centralwidget)
        self.button_star.setGeometry(QtCore.QRect(410, 300, 150, 150))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.button_star.setFont(font)
        self.button_star.setObjectName("button_star")

        self.minButton = QtWidgets.QPushButton(self.centralwidget)
        self.minButton.setGeometry(QtCore.QRect(710, 10, 23, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.minButton.setFont(font)
        self.minButton.setObjectName("minButton")
        self.minButton.setToolTip("最小化")
        self.minButton.clicked.connect(self.WindowMin)

        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(750, 10, 23, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setToolTip("关闭")
        self.closeButton.clicked.connect(self.Exit)

        self.labelSub = QtWidgets.QLabel(self.centralwidget)
        self.labelSub.setGeometry(QtCore.QRect(50, 48, 100, 20))
        self.labelSub.setObjectName("labelSub")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(160, 50, 200, 20))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(385, 50, 150, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(560, 50, 200, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "思政考试系统"))
        self.button_exam.setText(_translate("MainWindow", "模拟考试"))
        self.button_exercise.setText(_translate("MainWindow", "专项练习"))
        self.button_wrong.setText(_translate("MainWindow", "错题集"))
        self.button_star.setText(_translate("MainWindow", "收藏集"))
        self.labelSub.setText(_translate("MainWindow", "请选择科目："))
        self.radioButton.setText(_translate("MainWindow", "马克思主义基本原理概论"))
        self.radioButton_2.setText(_translate("MainWindow", "中国近现代史纲要"))
        self.radioButton_3.setText(_translate("MainWindow", "思想道德修养与法律基础"))

    def WindowMin(self):
        self.setWindowState(Qt.WindowMinimized)

    def Exit(self):
        messageBox1 = QMessageBox()
        messageBox1.setWindowTitle("提示")
        messageBox1.setText('确定要关闭吗？')
        messageBox1.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = messageBox1.button(QMessageBox.Yes)
        buttonY.setText("确定")
        buttonN = messageBox1.button(QMessageBox.No)
        buttonN.setText("取消")
        messageBox1.exec_()

        if messageBox1.clickedButton() == buttonY:
            exit()

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