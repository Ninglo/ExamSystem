import json
import sys
from PyQt5.QtCore import Qt
from ChoiceType import Ui_Dialog
from PyQt5.QtWidgets import QApplication
from matplotlib.backends.backend_qt5 import MainWindow
# from distribute_questions import distribute_question as _distribute_question
from exercise import Exercise

class QSSLoad:
    def __init__(self):
        pass

    @staticmethod
    def readQssFile(qssFileName):
        with open(qssFileName, 'r', encoding="utf-8") as file:
            return file.read()

class ChoiceType(Ui_Dialog, MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(self.width(), self.height())
        self.setupUi(self)


    def selectionChange(self):
        global d_Judge_num, d_Sgl_num, d_Mul_num
        d_Judge_num = self.comboBox_Judge.currentIndex()
        d_Sgl_num = self.comboBox_Sgl.currentIndex()
        d_Mul_num = self.comboBox_Mul.currentIndex()

    def Continue(self):
        d_type = "012"
        # print(distribute_question(d_chap, d_type))
        with open('exam_number.json', 'w', encoding='utf-8') as f1:
            dic = {"Judge": d_Judge_num + 1, "Single": d_Sgl_num + 1, "Multiple": d_Mul_num + 1}
            json.dump(dic, f1, ensure_ascii=False, indent=4)
        with open('exam_bank.json', 'w', encoding='utf-8') as f2:
            seq = []
            dic1 = {}
            dic2 = {}
            for question in distribute_question(d_chap, d_type):
                seq.append(question[-1])
                dic1.update(dic2.fromkeys(seq, question[0:-1]))
                seq = []
                dic2 = {}
            json.dump(dic1, f2, ensure_ascii=False, indent=4)
        qssFileName = "./pattern/exercise.qss"
        qssFile = QSSLoad.readQssFile(qssFileName)
        self.e = Exercise()
        self.e.setStyleSheet(qssFile)
        self.close()
        self.e.show()

    def Exit(self):
        self.close()

    def chapState(self, btn):
        global d_chap
        d_chap = set()
        str_name = "self.Chap0{0}.isChecked()"

        for i in range(0, 8):
            if eval(str_name.format(i)) == 1:
                d_chap.add(str(i))
            else:
                d_chap.discard(str(i))
        d_chap = ''.join(list(d_chap))

    def btnstate(self, btn):
        judge2 = False
        str_name = "self.Chap0{0}.isChecked()"

        for i in range(0, 8):
            if eval(str_name.format(i)) == 1:
                judge2 = True

        if judge2:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

def get_data(index):
    with open('questions.json', 'r', encoding='utf-8') as f:
        file_data = json.load(f)
        data_list = []
        num = len(index)
        for key, _ in file_data.items():
            if key[:num].find(index) == 0:
                data = file_data[key]
                data.append(key)
                data_list.append(data)
        return data_list[1:]

def read():
    with open('questions.json', 'r', encoding='utf-8') as f:
        file_data = json.load(f)
    return list(file_data.keys())[0][0]

def distribute_question(d_chap, d_type):
    d_questions = list()
    for i in d_type:
        for j in d_chap:
            d_index = read() + i + j.rjust(2, '0')
            d_questions.extend(get_data(d_index))
    # print(d_questions)
    return d_questions


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qssFileName = "./pattern/exercise.qss"
    qssFile = QSSLoad.readQssFile(qssFileName)
    c = ChoiceType()
    c.setStyleSheet(qssFile)
    c.show()
    sys.exit(app.exec_())