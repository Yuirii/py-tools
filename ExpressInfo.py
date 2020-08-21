# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '快递信息识别.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 494)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.read_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.read_edit.setObjectName("read_edit")
        self.gridLayout.addWidget(self.read_edit, 3, 1, 1, 1)
        self.file_ads_label = QtWidgets.QLabel(self.centralwidget)
        self.file_ads_label.setObjectName("file_ads_label")
        self.gridLayout.addWidget(self.file_ads_label, 0, 1, 1, 1)
        self.write_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.write_display.setObjectName("write_display")
        self.gridLayout.addWidget(self.write_display, 6, 1, 1, 2)
        self.read_label = QtWidgets.QLabel(self.centralwidget)
        self.read_label.setObjectName("read_label")
        self.gridLayout.addWidget(self.read_label, 2, 1, 1, 1)
        self.Startbtn = QtWidgets.QPushButton(self.centralwidget)
        self.Startbtn.setObjectName("Startbtn")
        self.gridLayout.addWidget(self.Startbtn, 4, 1, 1, 1)
        self.file_ads_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.file_ads_edit.setObjectName("file_ads_edit")
        self.gridLayout.addWidget(self.file_ads_edit, 1, 1, 1, 1)
        self.write_label = QtWidgets.QLabel(self.centralwidget)
        self.write_label.setObjectName("write_label")
        self.gridLayout.addWidget(self.write_label, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_ads_label.setText(_translate("MainWindow", "文件地址："))
        self.read_label.setText(_translate("MainWindow", "识别信息："))
        self.Startbtn.setText(_translate("MainWindow", "开始识别并写入"))
        self.write_label.setText(_translate("MainWindow", "写入信息："))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv) # 创建QApplication对象，作为GUI主程序入口

    window = Ui_MainWindow() # 创建主窗体对象，实例化Ui_MainWindow
    window.show() # 显示主窗体

    sys.exit(app.exec_()) # 循环中等待退出程序