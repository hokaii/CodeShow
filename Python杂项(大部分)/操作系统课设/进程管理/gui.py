# -*- coding: utf-8 -*-
import random

from PyQt5 import QtCore, QtGui, QtWidgets
import Dynamic_partition_allocation
from PyQt5.QtGui import QTextCursor

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(678, 478)
        Form.setMinimumSize(678, 478)
        Form.setMaximumSize(678, 478)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 675, 475))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 445, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.new_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.new_label.setObjectName("new_label")
        self.horizontalLayout.addWidget(self.new_label)
        self.new_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.new_lineEdit.setObjectName("new_lineEdit")
        self.horizontalLayout.addWidget(self.new_lineEdit)
        self.gridLayout.addWidget(self.widget, 3, 0, 1, 2)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout.addWidget(self.plainTextEdit_3, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.new_horizontalLayout = QtWidgets.QHBoxLayout()
        self.new_horizontalLayout.setObjectName("new_horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.new_horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.new_horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.new_horizontalLayout, 3, 4, 1, 1)

        self.radioButton.setChecked(True)
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit.setReadOnly(True)
        self.new_lineEdit.setPlaceholderText("640")

        # 设置每次刷新都使光标到文字最后
        self.cursor = QTextCursor()
        self.cursor = self.plainTextEdit.textCursor()
        self.cursor_1 = QTextCursor()
        self.cursor_1 = self.plainTextEdit_2.textCursor()
        self.cursor_2 = QTextCursor()
        self.cursor_2 = self.plainTextEdit_3.textCursor()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "hold"))
        self.radioButton_2.setText(_translate("Form", "free"))
        self.label_4.setText(_translate("Form", "任务号"))
        self.label_5.setText(_translate("Form", "空间大小"))
        self.new_label.setText(_translate("Form", "初始大小"))
        self.label.setText(_translate("Form", "首次适应算法"))
        self.label_3.setText(_translate("Form", "最坏适应算法"))
        self.label_2.setText(_translate("Form", "最佳适应算法"))
        self.pushButton.setText(_translate("Form", "运行"))
        self.pushButton.clicked.connect(Form.pushButton_click)
        self.pushButton_2.setText(_translate("Form", "随机生成"))
        self.pushButton_2.clicked.connect(Form.pushButton_2_click)

class MyWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.demo = Dynamic_partition_allocation.DistributedSimulate()
        self.demo_1 = Dynamic_partition_allocation.DistributedSimulate(target=2)
        self.demo_2 = Dynamic_partition_allocation.DistributedSimulate(target=3)
        #self.demo.enter_data()
        #self.demo_1.enter_data()
        #self.demo_2.enter_data()
        self.flag = True
        self.num = 1

    def pushButton_click(self):

        input_text = self.lineEdit.text()
        input_text_1 = self.lineEdit_2.text()
        input_text_2 = self.new_lineEdit.text()
        if input_text and input_text_1:
            if input_text_2:
                if self.flag:
                    print(" input_", input_text_2)
                    print(self.demo.partition_list[0].size)
                    self.demo.partition_list[0].size = int(input_text_2)
                    print(self.demo.partition_list[0].size)
                    self.demo_1.partition_list[0].size = int(input_text_2)
                    self.demo_2.partition_list[0].size = int(input_text_2)
                    self.flag = False
                    self.new_lineEdit.setEnabled(False)
            else:
                self.flag = False
                self.new_lineEdit.setEnabled(False)

            if self.radioButton.isChecked() == True:
                self.demo.target(int(input_text_1), int(input_text))
                self.demo_1.target(int(input_text_1), int(input_text))
                self.demo_2.target(int(input_text_1), int(input_text))
                self.plainTextEdit.setPlainText(self.demo.return_text)
                self.plainTextEdit_2.setPlainText(self.demo_1.return_text)
                self.plainTextEdit_3.setPlainText(self.demo_2.return_text)
            else:
                self.demo.free(int(input_text), int(input_text_1))
                self.demo_1.free(int(input_text), int(input_text_1))
                self.demo_2.free(int(input_text), int(input_text_1))
                self.plainTextEdit.setPlainText(self.demo.return_text)
                self.plainTextEdit_2.setPlainText(self.demo_1.return_text)
                self.plainTextEdit_3.setPlainText(self.demo_2.return_text)
            self.cursor.movePosition(QTextCursor.End)
            self.plainTextEdit.setTextCursor(self.cursor)
            self.cursor_1.movePosition(QTextCursor.End)
            self.plainTextEdit_2.setTextCursor(self.cursor_1)
            self.cursor_2.movePosition(QTextCursor.End)
            self.plainTextEdit_3.setTextCursor(self.cursor_2)

    def pushButton_2_click(self):
        input_text_2 = self.new_lineEdit.text()
        store_list = []
        if input_text_2:
            if self.flag:
                print(" input_", input_text_2)
                print(self.demo.partition_list[0].size)
                self.demo.partition_list[0].size = int(input_text_2)
                print(self.demo.partition_list[0].size)
                self.demo_1.partition_list[0].size = int(input_text_2)
                self.demo_2.partition_list[0].size = int(input_text_2)
                self.flag = False
                self.new_lineEdit.setEnabled(False)
        else:
            self.flag = False
            self.new_lineEdit.setEnabled(False)
        for i in range(100):
            random_num = random.randint(0, 2)
            append_list = []

            if random_num == 0 and store_list:
                op_list = random.choice(store_list)
                random_num_2 = random.randint(1, op_list[1] * 2)
                print("作业号: ", str(op_list[0]), "释放: ", str(random_num_2))
                self.demo.free(op_list[0], random_num_2)
                self.plainTextEdit.setPlainText(self.demo.return_text)
                self.demo_1.free(op_list[0], random_num_2)
                self.plainTextEdit_2.setPlainText(self.demo_1.return_text)
                self.demo_2.free(op_list[0], random_num_2)
                self.plainTextEdit_3.setPlainText(self.demo_2.return_text)
                if random_num_2 >= op_list[1]:
                    store_list.remove(op_list)
                else:
                    op_list[1] -= random_num_2
            else:
                random_num_1 = random.randint(10, 200)
                print("作业号: ", str(self.num), "申请: ", str(random_num_1))
                flag = self.demo.target(random_num_1, self.num)
                self.plainTextEdit.setPlainText(self.demo.return_text)
                self.demo_1.target(random_num_1, self.num)
                self.plainTextEdit_2.setPlainText(self.demo_1.return_text)
                self.demo_2.target(random_num_1, self.num)
                self.plainTextEdit_3.setPlainText(self.demo_2.return_text)
                if flag:
                    append_list.append(self.num)
                    append_list.append(random_num_1)
                    store_list.append(append_list)
                self.num += 1
        self.plainTextEdit.appendPlainText("分配次数: " + str(self.demo.log_dict['num']) + " 成功次数: " +
                                           str(self.demo.log_dict['success']) + " 紧凑次数: " +
                                           str(self.demo.log_dict['compact']) + " 失败次数: " +
                                           str(self.demo.log_dict['failure']) + " 产生的碎片数: " +
                                           str(self.demo.log_dict['debris']))
        self.plainTextEdit_2.appendPlainText("分配次数: " + str(self.demo_1.log_dict['num']) + " 成功次数: " +
                                           str(self.demo_1.log_dict['success']) + " 紧凑次数: " +
                                           str(self.demo_1.log_dict['compact']) + " 失败次数: " +
                                           str(self.demo_1.log_dict['failure'])+ " 产生的碎片数: " +
                                           str(self.demo_1.log_dict['debris']))
        self.plainTextEdit_3.appendPlainText("分配次数: " + str(self.demo_2.log_dict['num']) + " 成功次数: " +
                                           str(self.demo_2.log_dict['success']) + " 紧凑次数: " +
                                           str(self.demo_2.log_dict['compact']) + " 失败次数: " +
                                           str(self.demo_2.log_dict['failure'])+ " 产生的碎片数: " +
                                           str(self.demo_2.log_dict['debris']))
        self.cursor.movePosition(QTextCursor.End)
        self.plainTextEdit.setTextCursor(self.cursor)
        self.cursor_1.movePosition(QTextCursor.End)
        self.plainTextEdit_2.setTextCursor(self.cursor_1)
        self.cursor_2.movePosition(QTextCursor.End)
        self.plainTextEdit_3.setTextCursor(self.cursor_2)

        try:
            f = open(".\static.txt", "a")
            f.write(str(self.demo.log_dict['debris']) + " " + str(self.demo_1.log_dict['debris']) + " " +
                    str(self.demo_2.log_dict['debris']) + "\n")
        except:
            pass


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())