# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'whitening_v1.1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Handle imformation from txt")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.file_path_title = QtWidgets.QLabel(self.centralwidget)
        self.file_path_title.setObjectName("file_path_title")
        self.gridLayout.addWidget(self.file_path_title, 0, 0, 1, 1)
        # 输入框
        self.file_path = QtWidgets.QLineEdit(self.centralwidget)
        # self.file_path.setInputMask("")
        self.file_path.setObjectName("file_path")
        self.file_path.setMaximumHeight(43)
        self.gridLayout.addWidget(self.file_path, 0, 1, 1, 1)

        self.file_name_title = QtWidgets.QLabel(self.centralwidget)
        self.file_name_title.setObjectName("file_name_title")
        self.gridLayout.addWidget(self.file_name_title, 1, 0, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.centralwidget)
        # self.file_name.setInputMask("")
        self.file_name.setObjectName("file_name")
        self.file_name.setMaximumHeight(43)
        self.gridLayout.addWidget(self.file_name, 1, 1, 1, 1)

        # button
        self.wtbtn = QtWidgets.QPushButton(self.centralwidget)
        self.wtbtn.setObjectName("wtbtn")
        self.wtbtn.setMaximumHeight(43)
        self.gridLayout.addWidget(self.wtbtn, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1278, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.dataprocess_btn()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Handle imformation from txt"))
        self.file_path_title.setText(_translate("MainWindow", "文件路径："))
        self.file_name_title.setText(_translate("MainWindow", "文件名："))
        self.file_path.setText(_translate("MainWindow", "输入文件的绝对路径"))
        self.file_name.setText(_translate("MainWindow", "输入文件名（带后缀）"))
        self.wtbtn.setText(_translate("MainWindow", "开始处理"))
    def dataprocess_btn(self):


        def cao():
            filepath = self.file_path.text()
            filename = self.file_name.text()
            file = filepath+'\\'+filename
            file_ = [0] * len(file)
            print(type(len(file)))
            print(len(file))
            print(file[9])
            file[9]='/'
            print(file[9])
            # for i in range(len(file)):
            #     if file[i] == '\\':
            #         file[i] = '/'
            #
            # print(file)
            #
            # # process data
            # with open(file) as file_object:
            #     lines = file_object.readlines()

            # print(lines)

            # ???


        self.wtbtn.clicked.connect(cao)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv) # 创建QApplication对象，作为GUI主程序入口

    window = Ui_MainWindow() # 创建主窗体对象，实例化Ui_MainWindow
    window.show() # 显示主窗体

    sys.exit(app.exec_()) # 循环中等待退出程序