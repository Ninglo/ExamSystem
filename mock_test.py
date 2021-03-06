import json
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox, QApplication, QPushButton
from exercise import Exercise

lessons = {"马原": "0","近代史": "1", "思修": "2"}
questionType = {"单选": "1", "多选": '2', "判断": '0'}


class MockTest(Exercise):
    def __init__(self):
        super().__init__()
        self.init_time()
        self.pushButton_3.setText("交卷")
        self.pushButton_5.setVisible(False)

    def init_q_n(self):   # 虚继承
        with open("exam_number.json", "r") as f2:
            exam_number = json.load(f2)
        self.q1 = lessons["马原"] + questionType["单选"]
        self.q2 = lessons["马原"] + questionType["多选"]
        self.q3 = lessons["马原"] + questionType["判断"]
        self.n1 = exam_number["Single"]
        self.n2 = exam_number["Multiple"]
        self.n3 = exam_number["Judge"]

    def init_time(self):  # 倒计时功能
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self._minute = 89
        self._second = 60
        self.timer.timeout.connect(self.time_change)

    def time_change(self):   # 设置倒计时功能
        self._second -= 1
        if self._second == 0 and self._minute > 0:
            self._minute -= 1
            self._second = 59
        self.label.setText('{:0>2d}:{:0>2d}'.format(self._minute, self._second))
        if self._second == 0 and self._minute == 0:
            self.timer.stop()
            score = self.calculate_total_score()  # 时间到自动执行交卷功能
            messageBox1 = QMessageBox()
            messageBox1.setWindowTitle("提示")
            messageBox1.setText('时间已到，您的得分为：' + str(score) + '分')
            messageBox1.addButton(QPushButton("确定"), QMessageBox.YesRole)
            messageBox1.exec_()
            #reply = QMessageBox.information(self, '得分', '时间已到，您的得分为：' + str(score) + '分')
            if messageBox1.clickedButton():
                self.close()

    def calculate_total_score(self):  # 计算总的得分
        self._singleChoice.calculate_score()
        self._multipleChoice.calculate_score()
        self._judgmentQuestion.calculate_score()
        return self._singleChoice.get_score() + self._multipleChoice.get_score() + self._judgmentQuestion.get_score()

    def add_last_answer(self):  # 可能会有中途交卷的情况发生，需要将当前页面上的答案录入答案字典
        if self._currentQid < self.n1:
            self.set_answer1()
            self._singleChoice.add_answer(self._currentQid, self._yourAnswer)
        elif self._currentQid < self.n1 + self.n2:
            self.set_answer2()
            self._multipleChoice.add_answer(self._currentQid - self.n1, self._yourAnswer)
        else:
            self.set_answer3()
            self._judgmentQuestion.add_answer(self._currentQid - self.n1 - self.n2, self._yourAnswer)

    def check_(self):  # 交卷并评分
        messageBox1 = QMessageBox()
        messageBox1.setWindowTitle("提示")
        messageBox1.setText('确认要交卷吗？')
        messageBox1.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = messageBox1.button(QMessageBox.Yes)
        buttonY.setText("确定")
        buttonN = messageBox1.button(QMessageBox.No)
        buttonN.setText("取消")
        messageBox1.exec_()
        #reply = QMessageBox.question(self, '提示', '确认要交卷吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if messageBox1.clickedButton() == buttonY:
            self.add_last_answer()
            score = self.calculate_total_score()
            messageBox2 = QMessageBox()
            messageBox2.setWindowTitle("提示")
            messageBox2.setText('您的得分为：' + str(score) + '分')
            messageBox2.addButton(QPushButton("确定"), QMessageBox.YesRole)
            messageBox2.exec_()
            if messageBox2.clickedButton():
                self.close()
            #reply2 = QMessageBox.information(self, '得分', '您的得分为：' + str(score) + '分')
            #if reply2:
                #self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mockTestWindow = MockTest()
    mockTestWindow.show()
    sys.exit(app.exec_())