# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
from backstage import Backstage
from HomePage import Home_Page, Ui_HomePage


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMaximumSize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 120, 41, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 120, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 160, 41, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 160, 151, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 311, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./image/Snipaste_2020-01-03_19-24-51.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 230, 88, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 230, 88, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.register_page = RegisterPage()

        self.backstage = Backstage()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "账号"))
        self.label_2.setText(_translate("Form", "密码"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "注册"))



# 注册界面
class RegisterPage(QtWidgets.QDialog):
    def __init__(self):
        super(RegisterPage, self).__init__()
        self.setWindowTitle("注册")
        self.user_label = QtWidgets.QLabel('用户名', self)
        self.pwd_label = QtWidgets.QLabel('密码', self)
        self.pwd_label_2 = QtWidgets.QLabel('重复密码', self)
        self.label_3 = QtWidgets.QLabel('手机号码', self)
        self.label_4 = QtWidgets.QLabel('电子邮箱', self)

        #self.label_4 = QtWidgets.QLabel('头像', self)

        self.user_lineEdit = QtWidgets.QLineEdit(self)
        self.pwd_lineEdit = QtWidgets.QLineEdit(self)
        self.pwd_lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.register_button = QtWidgets.QPushButton('注册', self)
        self.user_layout = QtWidgets.QHBoxLayout()
        self.layout_3 = QtWidgets.QHBoxLayout()
        self.layout_4 = QtWidgets.QHBoxLayout()
        self.pwd_layout = QtWidgets.QHBoxLayout()
        self.pwd_layout_2 = QtWidgets.QHBoxLayout()
        self.all_layout = QtWidgets.QVBoxLayout()

        self.line_edit_init()
        self.button_init()
        self.layout_init()

        self.backstage = Backstage()

    def line_edit_init(self):
        self.pwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_lineEdit.textChanged.connect(self.check_input_func)
        self.pwd_lineEdit_2.textChanged.connect(self.check_input_func)
        self.user_lineEdit.textChanged.connect(self.check_input_func)

    def button_init(self):
        self.register_button.setEnabled(False)
        self.register_button.clicked.connect(self.check_register_func)

    def layout_init(self):
        self.user_layout.addWidget(self.user_label)
        self.user_layout.addWidget(self.user_lineEdit)
        self.layout_3.addWidget(self.label_3)
        self.layout_3.addWidget(self.lineEdit_3)
        self.layout_4.addWidget(self.label_4)
        self.layout_4.addWidget(self.lineEdit_4)
        self.pwd_layout.addWidget(self.pwd_label)
        self.pwd_layout.addWidget(self.pwd_lineEdit)
        self.pwd_layout_2.addWidget(self.pwd_label_2)
        self.pwd_layout_2.addWidget(self.pwd_lineEdit_2)
        self.all_layout.addLayout(self.user_layout)
        self.all_layout.addLayout(self.layout_3)
        self.all_layout.addLayout(self.layout_4)
        self.all_layout.addLayout(self.pwd_layout)
        self.all_layout.addLayout(self.pwd_layout_2)
        self.all_layout.addWidget(self.register_button)

        self.setLayout(self.all_layout)

    def check_input_func(self):
        if self.user_lineEdit.text() and self.pwd_lineEdit.text() and self.pwd_lineEdit_2.text():
            self.register_button.setEnabled(True)
        else:
            self.register_button.setEnabled(False)

    def check_register_func(self):
        if self.pwd_lineEdit.text() != self.pwd_lineEdit_2.text():
            QtWidgets.QMessageBox.critical(self, '错误', '两个密码不一致!')
        elif self.user_lineEdit.text():
            print(type(self.user_lineEdit.text()))
            if self.backstage.insert_register({"user_id": self.user_lineEdit.text(), "phone_number": self.lineEdit_3.text(),
                                            "email": self.lineEdit_4.text(), "register_time": datetime.datetime.now(),
                                            "password": self.pwd_lineEdit.text()}):
                QtWidgets.QMessageBox.information(self, '信息', '注册成功')
            else:
                QtWidgets.QMessageBox.warning(self, '警告', '该用户名已被注册!')
            self.close()
        self.user_lineEdit.clear()
        self.pwd_lineEdit.clear()
        self.pwd_lineEdit_2.clear()


class MyWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.line_edit_init()
        self.pushbutton_init()


    def line_edit_init(self):
        self.lineEdit.setPlaceholderText("请输入账号")
        self.lineEdit_2.setPlaceholderText("请输入密码")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.textChanged.connect(self.check_input_func)
        self.lineEdit_2.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

    def pushbutton_init(self):
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.check_login_func)
        self.pushButton_2.clicked.connect(self.check_register_func)

    def check_login_func(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            if self.backstage.verify(self.lineEdit.text(), self.lineEdit_2.text()):
                app.setStyleSheet("")
                homepage.initialize(self.lineEdit.text())
                homepage.show()
                self.close()
            else:
                QtWidgets.QMessageBox.critical(self, '错误', '账号或密码错误!')
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def check_register_func(self):
        self.register_page.exec()
        self.lineEdit.clear()
        self.lineEdit_2.clear()

# 程序入口
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mywindow = MyWindow()
    homepage = Home_Page()
    mywindow.show()
    sys.exit(app.exec_())
