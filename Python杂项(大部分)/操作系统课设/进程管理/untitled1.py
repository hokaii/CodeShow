# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Dynamic_partition_allocation

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 470)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 671, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout.addWidget(self.plainTextEdit_3, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        #self.plainTextEdit.setPlainText("sdfsdfjskdf")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.pushButton.clicked.connect(Form.pushButton_click)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "首次适应算法"))
        self.label_3.setText(_translate("Form", "最坏适应算法"))
        self.label_2.setText(_translate("Form", "最佳适应算法"))
        self.pushButton.setText(_translate("Form", "输入"))
        self.pushButton_2.setText(_translate("Form", "随机生成"))


class MyWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.demo = Dynamic_partition_allocation.DistributedSimulate()
        self.demo.enter_data()
        self.text = ""

    def pushButton_click(self):

        input_text = self.lineEdit.text()
        #self.plainTextEdit.appendPlainText(input_text)
        input_list = input_text.split(",")
        #for i in input_list:
        #    self.plainTextEdit.appendPlainText(i)
        if input_list:
            if input_list[0] == "hold":
                #self.text += self.demo.target(int(input_list[2]), int(input_list[1]))
                self.demo.target(int(input_list[2]), int(input_list[1]))
                print("return_text", self.demo.return_text)
                self.plainTextEdit.setPlainText(self.demo.return_text)
            elif input_list[0] == "free":
                #self.text += self.demo.free(int(input_list[1]), int(input_list[2]))
                self.demo.free(int(input_list[1]), int(input_list[2]))
                self.plainTextEdit.setPlainText(self.demo.return_text)
            else:
                return 0


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())