# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercise_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_ExerciseWindow(object):
    def setupUi(self, ExerciseWindow):
        ExerciseWindow.setObjectName("ExerciseWindow")
        ExerciseWindow.resize(811, 594)
        self.centralwidget = QtWidgets.QWidget(ExerciseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setWindowOpacity(0.93)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(250, 60, 531, 311))
        self.textEdit.setObjectName("textEdit")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(310, 400, 115, 19))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(440, 400, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(570, 400, 115, 19))
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(700, 400, 115, 19))
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(440, 400, 115, 19))
        self.radioButton_5.setObjectName("radioButton_5")

        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(570, 400, 115, 19))
        self.radioButton_6.setObjectName("radioButton_6")

        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(800, 580, 115, 19))
        self.radioButton_7.setObjectName("radioButton_7")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(310, 400, 91, 19))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(440, 400, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(570, 400, 91, 19))
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(700, 400, 91, 19))
        self.checkBox_4.setObjectName("checkBox_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(375, 450, 90, 30))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(475, 450, 90, 30))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 500, 90, 30))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(575, 450, 90, 30))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 500, 90, 30))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        ExerciseWindow.setCentralWidget(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 211, 461))
        self.listWidget.setObjectName("listWidget")

        self.menubar = QtWidgets.QMenuBar(ExerciseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 26))
        self.menubar.setObjectName("menubar")
        ExerciseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExerciseWindow)
        self.statusbar.setObjectName("statusbar")
        ExerciseWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ExerciseWindow)
        QtCore.QMetaObject.connectSlotsByName(ExerciseWindow)

    def retranslateUi(self, ExerciseWindow):
        _translate = QtCore.QCoreApplication.translate
        ExerciseWindow.setWindowTitle(_translate("ExerciseWindow", "练习系统"))
        self.radioButton.setText(_translate("ExerciseWindow", "A"))
        self.radioButton_2.setText(_translate("ExerciseWindow", "B"))
        self.radioButton_3.setText(_translate("ExerciseWindow", "C"))
        self.radioButton_4.setText(_translate("ExerciseWindow", "D"))
        self.radioButton_5.setText(_translate("ExerciseWindow", "Y"))
        self.radioButton_6.setText(_translate("ExerciseWindow", "N"))
        self.radioButton_7.setText(_translate("ExerciseWindow", "RadioButton"))
        self.checkBox.setText(_translate("ExerciseWindow", "A"))
        self.checkBox_2.setText(_translate("ExerciseWindow", "B"))
        self.checkBox_3.setText(_translate("ExerciseWindow", "C"))
        self.checkBox_4.setText(_translate("ExerciseWindow", "D"))
        self.pushButton.setText(_translate("ExerciseWindow", "上一题"))
        self.pushButton_2.setText(_translate("ExerciseWindow", "下一题"))
        self.pushButton_3.setText(_translate("ExerciseWindow", "检查"))
        self.pushButton_4.setText(_translate("ExerciseWindow", "收藏"))
        self.pushButton_5.setText(_translate("ExerciseWindow", "退出"))

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