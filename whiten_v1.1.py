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
        MainWindow.setObjectName("Whitening_v1.1")
        MainWindow.resize(1278, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.title_origin = QtWidgets.QLabel(self.centralwidget)
        self.title_origin.setObjectName("title_origin")
        self.gridLayout.addWidget(self.title_origin, 0, 0, 1, 1)

        # 输入框
        self.origindata = QtWidgets.QLineEdit(self.centralwidget)
        # self.origindata.setInputMask("")
        self.origindata.setObjectName("origindata")
        self.origindata.setMaximumHeight(50)
        self.gridLayout.addWidget(self.origindata, 0, 1, 1, 1)

        # button
        self.wtbtn = QtWidgets.QPushButton(self.centralwidget)
        self.wtbtn.setObjectName("wtbtn")
        self.gridLayout.addWidget(self.wtbtn, 0, 2, 1, 1)

        self.title_wt = QtWidgets.QLabel(self.centralwidget)
        self.title_wt.setObjectName("title_wt")
        self.gridLayout.addWidget(self.title_wt, 1, 0, 1, 1)

        # 白化数据hex显示框
        self.whtdata = QtWidgets.QTextBrowser(self.centralwidget)
        self.whtdata.setObjectName("whtdata")
        self.whtdata.setMaximumHeight(50)
        self.gridLayout.addWidget(self.whtdata, 1, 1, 1, 1)

        self.titlebin = QtWidgets.QLabel(self.centralwidget)
        self.titlebin.setObjectName("titlebin")
        self.gridLayout.addWidget(self.titlebin, 2, 0, 1, 1)
        self.displaybin = QtWidgets.QTextBrowser(self.centralwidget)
        self.displaybin.setObjectName("displaybin")
        self.gridLayout.addWidget(self.displaybin, 2, 1, 1, 1)
        self.titlehex = QtWidgets.QLabel(self.centralwidget)
        self.titlehex.setObjectName("titlehex")
        self.gridLayout.addWidget(self.titlehex, 3, 0, 1, 1)
        self.displayhex = QtWidgets.QTextBrowser(self.centralwidget)
        self.displayhex.setObjectName("displayhex")
        self.gridLayout.addWidget(self.displayhex, 3, 1, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Whitening_v1.1"))
        self.title_origin.setText(_translate("MainWindow", "原始数据："))
        self.origindata.setText(_translate("MainWindow", "输入hex形式的数据,无0x及空格。"))
        self.wtbtn.setText(_translate("MainWindow", "开始白化"))
        self.title_wt.setText(_translate("MainWindow", "白化数据："))
        self.titlebin.setText(_translate("MainWindow", "     BIN："))
        self.titlehex.setText(_translate("MainWindow", "     HEX："))

    def dataprocess_btn(self):
        white_seq = [1, 0, 1, 1, 0, 0, 0, 1,
                     0, 1, 0, 0, 1, 0, 1, 1,
                     1, 1, 1, 0, 1, 0, 1, 0,
                     1, 0, 0, 0, 0, 1, 0, 1,
                     1, 0, 1, 1, 1, 1, 0, 0,
                     1, 1, 1, 0, 0, 1, 0, 1,
                     0, 1, 1, 0, 0, 1, 1, 0,
                     0, 0, 0, 0, 1, 1, 0, 1,
                     1, 0, 1, 0, 1, 1, 1, 0,
                     1, 0, 0, 0, 1, 1, 0, 0,
                     1, 0, 0, 0, 1, 0, 0, 0,
                     0, 0, 0, 1, 0, 0, 1, 0,
                     0, 1, 1, 0, 1, 0, 0, 1,
                     1, 1, 1, 0, 1, 1, 1, 0,
                     0, 0, 0, 1, 1, 1, 1, 1,
                     1, 1, 0, 0, 0, 1, 1]

        white_seq_8bit = [0b10001101,0b11010010,\
                          0b01010111,0b10100001,\
                          0b00111101,0b10100111,\
                          0b01100110,0b10110000,\
                          0b01110101,0b00110001,\
                          0b00010001,0b01001000,\
                          0b10010110,0b01110111,\
                          0b11111000,0b11100011]

        def cao():
            origin_data = self.origindata.text()
            len_data = int(len(origin_data)/2)

            # process data
            whitened_data = [0]*len_data
            print(whitened_data)

            for index in range(int(len_data)):
                process_data = eval('0x'+origin_data[slice(2*index,2*index+2,1)])
                result_data = process_data^white_seq_8bit[index]
                whitened_data[index] = str(hex(result_data)[slice(2,4,1)])
                print('result_data',type(result_data))
                print(whitened_data)

            # ???
            self.whtdata.setText(whitened_data)
            print('cao end.')

        self.wtbtn.clicked.connect(cao)
        print('dataprocess_btn end.')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv) # 创建QApplication对象，作为GUI主程序入口

    window = Ui_MainWindow() # 创建主窗体对象，实例化Ui_MainWindow
    window.show() # 显示主窗体

    sys.exit(app.exec_()) # 循环中等待退出程序