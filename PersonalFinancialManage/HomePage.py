# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QComboBox, QHeaderView, QItemDelegate

from backstage import Backstage
import csv
from paint import paint


class Ui_HomePage(object):
    def setupUi(self, Form, User_Id):
        Form.setObjectName("Form")
        Form.resize(1051, 791)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.user_id = User_Id
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 130, 1051, 141))
        self.widget.setStyleSheet(".QWidget{background-color:rgb(244, 245, 250);}")
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(190, 30, 691, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(190, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.label_5.setObjectName("label_5")
        self.dateEdit_2 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateEdit_2.setGeometry(QtCore.QRect(410, 50, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.dateEdit_2.setDate(QDate.currentDate())
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(389, 50, 16, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.dateEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.dateEdit.setGeometry(QtCore.QRect(270, 50, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.dateEdit.setDate(QDate.currentDate())
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(210, 50, 51, 21))
        self.label.setObjectName("label")
        self.label.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(210, 80, 41, 21))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(270, 80, 421, 21))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet(".QGroupBox{color:black;background-color:rgb(244, 245, 250);}")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(0, 0, 61, 21))
        self.radioButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(60, 0, 61, 21))
        self.radioButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_6.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setGeometry(QtCore.QRect(120, 0, 61, 21))
        self.radioButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_7.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_8.setGeometry(QtCore.QRect(180, 0, 61, 21))
        self.radioButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_8.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_9.setGeometry(QtCore.QRect(240, 0, 61, 21))
        self.radioButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_9.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_10.setGeometry(QtCore.QRect(300, 0, 61, 21))
        self.radioButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_10.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_11.setGeometry(QtCore.QRect(360, 0, 61, 21))
        self.radioButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_11.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(770, 10, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(810, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setText(User_Id)
        self.label_10.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(210, 110, 61, 21))
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 110, 351, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("color:black;background-color:rgb(244, 245, 250);")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(690, 110, 120, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 110, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(".QPushButton {color: rgb(255, 255, 255); background-color: rgb(0, 170, 238)}")
        self.pushButton_6.setAutoExclusive(False)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(690, 80, 41, 21))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(".QPushButton {color: rgb(255, 255, 255); background-color: rgb(0, 170, 238)}")
        self.pushButton_7.setAutoExclusive(False)
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(530, 50, 41, 21))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(".QPushButton {color: rgb(255, 255, 255); background-color: rgb(0, 170, 238)}")
        self.pushButton_8.setAutoExclusive(False)
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(820, 110, 41, 21))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(".QPushButton {color: rgb(255, 255, 255); background-color: rgb(0, 170, 238)}")
        self.pushButton_9.setAutoExclusive(False)
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(0, 270, 1051, 521))
        self.widget_2.setStyleSheet(".QWidget{background-color:rgb(255, 255, 255);}")
        self.widget_2.setObjectName("widget_2")
        self.tableView = QtWidgets.QTableView(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(0, 130, 531, 291))
        self.widget_3.setStyleSheet(".QWidget{background-color:rgb(255, 255, 255);}")
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setVisible(False)
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setGeometry(QtCore.QRect(530, 130, 521, 291))
        self.widget_5.setStyleSheet(".QWidget{background-color:rgb(255, 255, 255);}")
        self.widget_5.setObjectName("widget_5")
        self.widget_5.setVisible(False)
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(0, 130, 1051, 661))
        self.widget_4.setStyleSheet(".QWidget{background-color:rgb(255, 255, 255);}")
        self.widget_4.setObjectName("widget_4")
        self.v_layout_2 = QtWidgets.QVBoxLayout()
        self.widget_4.setLayout(self.v_layout_2)
        self.widget_4.setVisible(False)
        self.tableView.setGeometry(QtCore.QRect(190, 0, 701, 521))
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 1051, 131))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 0, 171, 131))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"background-color:rgb(25, 35, 45);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"padding-top:10px;\n"
"font-size:25px;\n"
"Width:30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(440, 0, 171, 131))
        self.label_6.setStyleSheet(".QLabel{background-color: rgb(25, 35, 45);\n"
"\n"
"font-size:100px;}")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 20, 101, 101))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"\n"
"font-size:45px;\n"
"border-radius:50px;\n"
"\n"
"border-image: url(D:/Python/Python3.6.6/MyPythonScripts/PersonalFinancialManage/image/T11K0yXipdXXXXXXXX.jpg);}\n"
"\n"
"QPushButton:hover {\n"
"font-size:40px;\n"
"border-radius:45px;\n"
"border-image: url(D:/Python/Python3.6.6/MyPythonScripts/PersonalFinancialManage/image/T11K0yXipdXXXXXXXX.jpg);\n"
"}\n"
"QPushButton:pressed {\n"
"font-size:70px;\n"
"border-radius:75px;\n"
"border-width:3;\n"
"border-color:orange;\n"
"border-style:solid;;\n"
"background-color:cyan;\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setIconSize(QtCore.QSize(96, 96))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(270, 0, 171, 131))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color:rgb(25, 35, 45);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"padding-top:10px;\n"
"font-size:25px;\n"
"Width:30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 101, 131))
        self.label_7.setStyleSheet(".QLabel{background-color: rgb(25, 35, 45);\n"
"\n"
"font-size:100px;}")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 0, 171, 131))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"background-color:rgb(25, 35, 45);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"padding-top:10px;\n"
"font-size:25px;\n"
"Width:30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(780, 0, 171, 131))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"background-color:rgb(25, 35, 45);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"padding-top:10px;\n"
"font-size:25px;\n"
"Width:30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")

        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(950, 0, 101, 131))
        self.label_8.setStyleSheet(".QLabel{background-color: rgb(25, 35, 45);\n"
"\n"
"font-size:100px;}")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.record_page = RecordPage(User_Id)
        self.alter_page = AlterPage(User_Id)
        self.pushButton_2.clicked.connect(self.check_static_func)
        self.pushButton.clicked.connect(self.check_log_func)
        self.pushButton_3.clicked.connect(self.check_record_func)
        self.pushButton_4.clicked.connect(self.check_alter_func)
        self.pushButton_8.clicked.connect(self.check_time_func)
        self.pushButton_7.clicked.connect(self.check_type_func)
        self.pushButton_6.clicked.connect(self.check_keyword_func)
        self.pushButton_9.clicked.connect(self.check_del_func)
        self.pushButton_5.clicked.connect(self.check_export_func)

        self.backstage = Backstage()
        self.results = self.backstage.select_user_name(User_Id)
        self.label_10.setText(self.results[0][0]["user_id"])
        self.results = self.backstage.select_all_info(User_Id)
        self.table_change()

    def table_change(self):
        self.model = QStandardItemModel()
        self.title = ['收支ID', '用户ID', '收支时间', '收支类型', '收支名称', '收支金额', '备注']
        self.model.setHorizontalHeaderLabels(self.title)
        self.show_list = []
        self.result_0_num = 0
        for i in range(len(self.results)):
            if self.results[i] == None:
                continue
            for dic in self.results[i]:
                self.show_list.append(dic)
                if i == 0:
                    self.result_0_num += 1
        print("show_list", self.show_list)
        self.show_list_1 = []
        for linedata in self.show_list:
            self.show_list_1.append(list(linedata.values()))
        print("show_list_1", self.show_list_1)
        for row, linedata in enumerate(self.show_list_1):
            for col, itemdata in enumerate(linedata):
                item = QStandardItem(str(itemdata)) if itemdata != None else QStandardItem('')
                self.model.setItem(row, col, item)
        self.tableView.setModel(self.model)
        self.tableView.setItemDelegateForColumn(0, EmptyDelegate(self))
        self.tableView.setItemDelegateForColumn(1, EmptyDelegate(self))
        self.model.itemChanged.connect(self.edit_func)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "我的账单"))
        self.label_2.setText(_translate("Form", "-"))
        self.label.setText(_translate("Form", "时间: "))
        self.label_4.setText(_translate("Form", "分类: "))
        self.radioButton_5.setText(_translate("Form", "全部"))
        self.radioButton_6.setText(_translate("Form", "购物"))
        self.radioButton_7.setText(_translate("Form", "线下"))
        self.radioButton_8.setText(_translate("Form", "缴费"))
        self.radioButton_9.setText(_translate("Form", "还款"))
        self.radioButton_10.setText(_translate("Form", "理财"))
        self.radioButton_11.setText(_translate("Form", "充值"))
        self.label_9.setText(_translate("Form", "你好，"))
        self.label_11.setText(_translate("Form", "关键词："))
        self.lineEdit.setPlaceholderText(_translate("Form", "输入关键词搜索"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "输入要删除的行"))
        self.pushButton_6.setText(_translate("Form", "确定"))
        self.pushButton_7.setText(_translate("Form", "确定"))
        self.pushButton_8.setText(_translate("Form", "确定"))
        self.pushButton_3.setText(_translate("Form", "记账"))
        self.pushButton.setText(_translate("Form", "我的账单"))
        self.pushButton_2.setText(_translate("Form", "统计"))
        self.pushButton_5.setText(_translate("Form", "导出"))
        self.pushButton_9.setText(_translate("Form", "删除"))

    # 根据类型查找
    def check_type_func(self):
        if self.radioButton_5.isChecked():
            self.results = self.backstage.select_type("全部", self.user_id)
        elif self.radioButton_6.isChecked():
            self.results = self.backstage.select_type("购物", self.user_id)
        elif self.radioButton_7.isChecked():
            self.results = self.backstage.select_type("线下", self.user_id)
        elif self.radioButton_8.isChecked():
            self.results = self.backstage.select_type("缴费", self.user_id)
        elif self.radioButton_9.isChecked():
            self.results = self.backstage.select_type("还款", self.user_id)
        elif self.radioButton_10.isChecked():
            self.results = self.backstage.select_type("理财", self.user_id)
        elif self.radioButton_11.isChecked():
            self.results = self.backstage.select_type("充值", self.user_id)
        self.table_change()

    # 编辑功能
    def edit_func(self):
        row_num = self.tableView.currentIndex().row()
        column_num = self.tableView.currentIndex().column()
        currunt_data = self.tableView.currentIndex().data()
        item = self.model.index(row_num, 0)
        print("row_num", row_num, "co_num", column_num, "current_data", currunt_data)

        if row_num < self.result_0_num:
            if column_num == 2:
                key = "income_time"
            elif column_num == 3:
                key = "income_type"
            elif column_num == 4:
                key = "income_name"
            elif column_num == 5:
                key = "income_num"
            else:
                key = "income_remark"
            if self.backstage.update_table_data(self.show_list_1[row_num][0], key, repr(currunt_data), True):
                QtWidgets.QMessageBox.information(self, '成功', '修改成功!')
            else:
                self.results = self.backstage.select_all_info(self.user_id)
                self.table_change()
                self.radioButton_5.setChecked(True)
                QtWidgets.QMessageBox.warning(self, '失败', '修改失败!')
        else:
            if column_num == 2:
                key = "pay_time"
            elif column_num == 3:
                key = "pay_type"
            elif column_num == 4:
                key = "pay_name"
            elif column_num == 5:
                key = "pay_num"
            else:
                key = "pay_remark"
            if self.backstage.update_table_data(self.show_list_1[row_num][0], key, repr(currunt_data), False):
                QtWidgets.QMessageBox.information(self, '成功', '修改成功!')
            else:
                self.results = self.backstage.select_all_info(self.user_id)
                self.table_change()
                self.radioButton_5.setChecked(True)
                QtWidgets.QMessageBox.warning(self, '失败', '修改失败!')

    # 删除功能
    def check_del_func(self):
        if self.lineEdit_2.text():
            if int(self.lineEdit_2.text()) <= self.result_0_num and int(self.lineEdit_2.text())>0:
                # 收入
                del_data_dict = self.show_list[int(self.lineEdit_2.text())-1]
                print("del_data_dict", del_data_dict['income_id'])
                if self.backstage.del_data(del_data_dict['income_id'], True):
                    QtWidgets.QMessageBox.information(self, '成功', '删除成功!')
                    self.results = self.backstage.select_all_info(self.user_id)
                    self.table_change()
                else:
                    QtWidgets.QMessageBox.warning(self, '失败', '删除失败!')
            else:
                # 支出
                del_data_dict = self.show_list[int(self.lineEdit_2.text()) - 1]
                print("del_data_dict", del_data_dict['pay_id'])
                if self.backstage.del_data(del_data_dict['pay_id'], False):
                    QtWidgets.QMessageBox.information(self, '成功', '删除成功!')
                    self.results = self.backstage.select_all_info(self.user_id)
                    self.table_change()
                else:
                    QtWidgets.QMessageBox.warning(self, '失败', '删除失败!')

    # 根据时间查找
    def check_time_func(self):
        print(self.dateEdit.dateTime().toString('yyyy-MM-dd hh:mm:ss'))
        print(self.dateEdit_2.dateTime().toString('yyyy-MM-dd hh:mm:ss'))
        self.results = self.backstage.select_time(self.dateEdit.dateTime().toString('yyyy-MM-dd hh:mm:ss'),
                                   self.dateEdit_2.dateTime().toString('yyyy-MM-dd hh:mm:ss'),
                                   self.user_id)
        print("results", self.results)
        self.table_change()

    # 统计功能
    def check_static_func(self):
        self.widget.setVisible(False)
        self.widget_2.setVisible(False)
        self.widget_3.setVisible(True)
        self.widget_5.setVisible(True)
        self.widget_4.setVisible(False)
        static = paint()
        print("num", self.result_0_num)
        try:
            png = static.main(self.result_0_num, self.show_list)
        except:
            print("图片生成失败")
        self.widget_3.setStyleSheet("border-image: url(./01.png);\n")
        self.widget_5.setStyleSheet("border-image: url(./02.png);\n")

    def check_log_func(self):
        self.widget_3.setVisible(False)
        self.widget_5.setVisible(False)
        self.widget.setVisible(True)
        self.widget_2.setVisible(True)
        self.widget_4.setVisible(False)

    # 新增信息功能
    def check_record_func(self):
        self.record_page.exec()
        self.results = self.backstage.select_all_info(self.user_id)
        self.table_change()

    # 根据关键词查找
    def check_keyword_func(self):
        if self.lineEdit.text():
            self.results = self.backstage.select_keyword(self.lineEdit.text(), self.user_id)
            self.table_change()
        else:
            self.results = self.backstage.select_all_info(self.user_id)
            self.table_change()

    # 修改个人信息
    def check_alter_func(self):
        self.alter_page.exec()

    # 导出功能
    def check_export_func(self):
        with open('./log.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in self.show_list_1:
                writer.writerow(row)
        QtWidgets.QMessageBox.information(self, '提示', '导出为log.csv文件!')

class Home_Page(QtWidgets.QMainWindow, Ui_HomePage):
    def __init__(self):
        super(Home_Page, self).__init__()
        self.user_id = ""

    def initialize(self, user_id):
        self.setupUi(self, user_id)

# 新增记录页面
class RecordPage(QtWidgets.QDialog):
    def __init__(self, user_id):
        super(RecordPage, self).__init__()
        self.setWindowTitle("记账")
        self.user_id = user_id
        self.user_label = QtWidgets.QLabel('收支', self)
        self.pwd_label = QtWidgets.QLabel('收支时间', self)
        self.pwd_label_2 = QtWidgets.QLabel('收支类型', self)
        self.label_3 = QtWidgets.QLabel('收支名称', self)
        self.label_4 = QtWidgets.QLabel('收支金额', self)
        self.label_5 = QtWidgets.QLabel('备注', self)
        self.choice_list = ["收入", "支出"]

        self.combobox = QComboBox(self)
        self.combobox.addItems(self.choice_list)
        self.user_lineEdit = QtWidgets.QLineEdit(self)
        self.pwd_lineEdit = QtWidgets.QLineEdit(self)
        self.pwd_lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)

        self.register_button = QtWidgets.QPushButton('保存', self)
        self.user_layout = QtWidgets.QHBoxLayout()
        self.layout_3 = QtWidgets.QHBoxLayout()
        self.layout_4 = QtWidgets.QHBoxLayout()
        self.pwd_layout = QtWidgets.QHBoxLayout()
        self.pwd_layout_2 = QtWidgets.QHBoxLayout()
        self.layout_5 = QtWidgets.QHBoxLayout()
        self.all_layout = QtWidgets.QVBoxLayout()

        self.line_edit_init()
        self.button_init()
        self.layout_init()

        self.backstage = Backstage()

    def line_edit_init(self):
        self.pwd_lineEdit.textChanged.connect(self.check_input_func)
        self.pwd_lineEdit_2.textChanged.connect(self.check_input_func)
        self.lineEdit_3.textChanged.connect(self.check_input_func)
        self.lineEdit_4.textChanged.connect(self.check_input_func)

    def button_init(self):
        self.register_button.setEnabled(False)
        self.register_button.clicked.connect(self.check_register_func)

    def layout_init(self):
        self.user_layout.addWidget(self.user_label)
        self.user_layout.addWidget(self.combobox)
        self.layout_3.addWidget(self.label_3)
        self.layout_3.addWidget(self.lineEdit_3)
        self.layout_4.addWidget(self.label_4)
        self.layout_4.addWidget(self.lineEdit_4)
        self.pwd_layout.addWidget(self.pwd_label)
        self.pwd_layout.addWidget(self.pwd_lineEdit)
        self.pwd_layout_2.addWidget(self.pwd_label_2)
        self.pwd_layout_2.addWidget(self.pwd_lineEdit_2)
        self.layout_5.addWidget(self.label_5)
        self.layout_5.addWidget(self.user_lineEdit)
        self.all_layout.addLayout(self.user_layout)
        self.all_layout.addLayout(self.layout_3)
        self.all_layout.addLayout(self.layout_4)
        self.all_layout.addLayout(self.pwd_layout)
        self.all_layout.addLayout(self.pwd_layout_2)
        self.all_layout.addLayout(self.layout_5)
        self.all_layout.addWidget(self.register_button)
        self.setLayout(self.all_layout)

    def check_input_func(self):
        if self.lineEdit_3.text() and self.pwd_lineEdit.text() and self.pwd_lineEdit_2.text() and self.lineEdit_4.text():
            self.register_button.setEnabled(True)
        else:
            self.register_button.setEnabled(False)

    def check_register_func(self):
        if self.combobox.currentText() == "收入":
            num = self.backstage.select_max_id("income", "income_id")
            if self.backstage.insert_bill({"user_id": eval(self.user_id), "income_id": num+1, "income_time": self.pwd_lineEdit.text(),
                                        "income_type": self.pwd_lineEdit_2.text(), "income_name": self.lineEdit_3.text(),
                                        "income_num": self.lineEdit_4.text(), "income_remark": self.user_lineEdit.text()}, True):
                QtWidgets.QMessageBox.information(self, '信息', '记录插入成功')
            else:
                QtWidgets.QMessageBox.warning(self, '警告', '记录插入失败!')
        else:
            num = self.backstage.select_max_id("pay", "pay_id")
            print("user_id", type(self.user_id))
            if self.backstage.insert_bill({"user_id": eval(self.user_id), "pay_id": num+1, "pay_time": self.pwd_lineEdit.text(),
                                        "pay_type": self.pwd_lineEdit_2.text(), "pay_name": self.lineEdit_3.text(),
                                        "pay_num": self.lineEdit_4.text(), "pay_remark": self.user_lineEdit.text()}, False):
                QtWidgets.QMessageBox.information(self, '信息', '记录插入成功')
            else:
                QtWidgets.QMessageBox.warning(self, '警告', '记录插入失败!')
        self.close()
        self.lineEdit_4.clear()
        self.lineEdit_3.clear()
        self.user_lineEdit.clear()
        self.pwd_lineEdit.clear()
        self.pwd_lineEdit_2.clear()

# 修改信息页面
class AlterPage(QtWidgets.QDialog):
    def __init__(self, user_id):
        super(AlterPage, self).__init__()
        self.setWindowTitle("修改信息")
        self.user_id = user_id
        self.label_3 = QtWidgets.QLabel('手机号码', self)
        self.label_4 = QtWidgets.QLabel('邮箱地址', self)
        self.label_5 = QtWidgets.QLabel('密码', self)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_5 = QtWidgets.QLineEdit(self)

        self.register_button = QtWidgets.QPushButton('保存', self)
        self.layout_3 = QtWidgets.QHBoxLayout()
        self.layout_4 = QtWidgets.QHBoxLayout()
        self.layout_5 = QtWidgets.QHBoxLayout()
        self.all_layout = QtWidgets.QVBoxLayout()

        self.line_edit_init()
        self.button_init()
        self.layout_init()

        self.backstage = Backstage()
        result = self.backstage.select_user_name(self.user_id)
        print("result",result)
        if result:
            if result[0]:
                self.lineEdit_3.setPlaceholderText(result[0][0]['phone_number'])
                self.lineEdit_4.setPlaceholderText(result[0][0]['email'])
                self.lineEdit_5.setPlaceholderText(result[0][0]['password'])


    def line_edit_init(self):
        self.lineEdit_5.textChanged.connect(self.check_input_func)

    def button_init(self):
        self.register_button.setEnabled(False)
        self.register_button.clicked.connect(self.check_register_func)

    def layout_init(self):
        self.layout_3.addWidget(self.label_3)
        self.layout_3.addWidget(self.lineEdit_3)
        self.layout_4.addWidget(self.label_4)
        self.layout_4.addWidget(self.lineEdit_4)
        self.layout_5.addWidget(self.label_5)
        self.layout_5.addWidget(self.lineEdit_5)

        self.all_layout.addLayout(self.layout_3)
        self.all_layout.addLayout(self.layout_4)
        self.all_layout.addLayout(self.layout_5)
        self.all_layout.addWidget(self.register_button)
        self.setLayout(self.all_layout)

    def check_input_func(self):
        if self.lineEdit_5.text():
            self.register_button.setEnabled(True)
        else:
            self.register_button.setEnabled(False)

    def check_register_func(self):
        if not self.lineEdit_3.text():
            text_3 = "null"
        else:
            text_3 = self.lineEdit_3.text()
        if not self.lineEdit_4.text():
            text_4 = "null"
        else:
            text_4 = self.lineEdit_4.text().replace("@", "#")

        if self.backstage.update_data(phone_num=text_3, email=text_4, password=self.lineEdit_5.text(), id=self.user_id):
            QtWidgets.QMessageBox.information(self, '信息', '信息修改成功')
        else:
            QtWidgets.QMessageBox.warning(self, '警告', '信息修改失败!')
        self.close()
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()
        self.lineEdit_3.clear()

# 实现使某列item不可修改
class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None

# 测试
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myhomepage = Home_Page()
    myhomepage.initialize("50")
    myhomepage.show()
    sys.exit(app.exec_())