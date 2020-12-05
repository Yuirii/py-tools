__auther__ = 'Yoole'

from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton,QTextBrowser,QWidget,QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('计算功耗v1.1.2')
        self.resize(960, 760)
        self.setup_ui()

    def setup_ui(self):
        self.labal_init()
        self.line_init()
        self.display_init()
        self.buttonclicked()
        pass

    def labal_init(self):
        font = QFont()
        font.setPointSize(12)

        self.title1 = QLabel(self)
        self.title1.setText('工作功耗：')
        self.title1.move(1,10)
        self.title2 = QLabel(self)
        self.title2.setText('休眠功耗：')
        self.title2.move(1,545)

        self.a1 = QLabel(self)
        self.a1.setText('A1 /mA: ')
        self.a1.setFont(font)
        self.a1.move(10, 50)
        self.t1 = QLabel(self)
        self.t1.setText('T1 /us: ')
        self.t1.setFont(font)
        self.t1.move(410, 50)

        self.a2 = QLabel(self)
        self.a2.setText('A2 /mA: ')
        self.a2.setFont(font)
        self.a2.move(10, 100)
        self.t2 = QLabel(self)
        self.t2.setText('T2 /us: ')
        self.t2.setFont(font)
        self.t2.move(410, 100)

        self.a3 = QLabel(self)
        self.a3.setText('A3 /mA: ')
        self.a3.setFont(font)
        self.a3.move(10, 150)
        self.t3 = QLabel(self)
        self.t3.setText('T3 /us: ')
        self.t3.setFont(font)
        self.t3.move(410, 150)

        self.a4 = QLabel(self)
        self.a4.setText('A4 /mA: ')
        self.a4.setFont(font)
        self.a4.move(10, 200)
        self.t4 = QLabel(self)
        self.t4.setText('T4 /us: ')
        self.t4.setFont(font)
        self.t4.move(410, 200)

        self.a5 = QLabel(self)
        self.a5.setText('A5 /mA: ')
        self.a5.setFont(font)
        self.a5.move(10, 250)
        self.t5 = QLabel(self)
        self.t5.setText('T5 /us: ')
        self.t5.setFont(font)
        self.t5.move(410, 250)

        self.a6 = QLabel(self)
        self.a6.setText('A6 /mA: ')
        self.a6.setFont(font)
        self.a6.move(10, 300)
        self.t6 = QLabel(self)
        self.t6.setText('T6 /us: ')
        self.t6.setFont(font)
        self.t6.move(410, 300)

        self.a7 = QLabel(self)
        self.a7.setText('A7 /mA: ')
        self.a7.setFont(font)
        self.a7.move(10, 350)
        self.t7 = QLabel(self)
        self.t7.setText('T7 /us: ')
        self.t7.setFont(font)
        self.t7.move(410, 350)

        self.a8 = QLabel(self)
        self.a8.setText('A8 /mA: ')
        self.a8.setFont(font)
        self.a8.move(10, 400)
        self.t8 = QLabel(self)
        self.t8.setText('T8 /us: ')
        self.t8.setFont(font)
        self.t8.move(410, 400)

        self.a9 = QLabel(self)
        self.a9.setText('A9 /mA: ')
        self.a9.setFont(font)
        self.a9.move(10, 450)
        self.t9 = QLabel(self)
        self.t9.setText('T9 /us: ')
        self.t9.setFont(font)
        self.t9.move(410, 450)

        self.a10 = QLabel(self)
        self.a10.setText('A10/mA: ')
        self.a10.setFont(font)
        self.a10.move(10, 500)
        self.t10 = QLabel(self)
        self.t10.setText('T10/us: ')
        self.t10.setFont(font)
        self.t10.move(410, 500)

        self.a11 = QLabel(self)
        self.a11.setText('A11/uA: ')
        self.a11.setFont(font)
        self.a11.move(10, 580)
        self.t11 = QLabel(self)
        self.t11.setText('T11/ms: ')
        self.t11.setFont(font)
        self.t11.move(410, 580)

        # interval
        self.labal_interval = QLabel(self)
        self.labal_interval.setText('发包间隔/ms: ')
        self.labal_interval.setFont(font)
        self.labal_interval.move(10, 620)

    def line_init(self):
        self.ma1 = QLineEdit(self)
        self.ma1.move(110, 51)
        self.ma2 = QLineEdit(self)
        self.ma2.move(110, 101)
        self.ma3 = QLineEdit(self)
        self.ma3.move(110, 151)
        self.ma4 = QLineEdit(self)
        self.ma4.move(110, 201)
        self.ma5 = QLineEdit(self)
        self.ma5.move(110, 251)
        self.ma6 = QLineEdit(self)
        self.ma6.move(110, 301)
        self.ma7 = QLineEdit(self)
        self.ma7.move(110, 351)
        self.ma8 = QLineEdit(self)
        self.ma8.move(110, 401)
        self.ma9 = QLineEdit(self)
        self.ma9.move(110, 451)
        self.ma10 = QLineEdit(self)
        self.ma10.move(110, 501)
        self.ma11 = QLineEdit(self)
        self.ma11.move(110, 581)

        self.us1 = QLineEdit(self)
        self.us1.move(510, 51)
        self.us2 = QLineEdit(self)
        self.us2.move(510, 101)
        self.us3 = QLineEdit(self)
        self.us3.move(510, 151)
        self.us4 = QLineEdit(self)
        self.us4.move(510, 201)
        self.us5 = QLineEdit(self)
        self.us5.move(510, 251)
        self.us6 = QLineEdit(self)
        self.us6.move(510, 301)
        self.us7 = QLineEdit(self)
        self.us7.move(510, 351)
        self.us8 = QLineEdit(self)
        self.us8.move(510, 401)
        self.us9 = QLineEdit(self)
        self.us9.move(510, 451)
        self.us10 = QLineEdit(self)
        self.us10.move(510, 501)
        self.us11 = QLineEdit(self)
        self.us11.move(510, 581)

        self.line_interval = QLineEdit(self)
        self.line_interval.move(130, 621)

    def display_init(self):
        self.display1 = QTextBrowser(self)
        self.display1.resize(400, 100)
        self.display1.move(130, 670)

    def buttonclicked(self):
        # self.obj = QObject()

        btn1 = QPushButton(self)
        btn1.setText('开始计算')
        btn1.move(580, 650)

        def cao():
            A1_str = self.ma1.text()
            A2_str = self.ma2.text()
            A3_str = self.ma3.text()
            A4_str = self.ma4.text()
            A5_str = self.ma5.text()
            A6_str = self.ma6.text()
            A7_str = self.ma7.text()
            A8_str = self.ma8.text()
            A9_str = self.ma9.text()
            A10_str = self.ma10.text()
            A11_str = self.ma11.text()

            T1_str = self.us1.text()
            T2_str = self.us2.text()
            T3_str = self.us3.text()
            T4_str = self.us4.text()
            T5_str = self.us5.text()
            T6_str = self.us6.text()
            T7_str = self.us7.text()
            T8_str = self.us8.text()
            T9_str = self.us9.text()
            T10_str = self.us10.text()
            T11_str = self.us11.text()

            Interval_str = self.line_interval.text()

            if Interval_str == '' or Interval_str == ' ':
                Interval_float = 1000
            else:
                Interval_float = float(Interval_str)

            if A1_str == '' or A1_str == ' ':
                A1_float = 0
            else:
                A1_float = float(A1_str)

            if A2_str == ''or A2_str == ' ':
                A2_float = 0
            else:
                A2_float = float(A2_str)
            if A3_str == ''or A3_str == ' ':
                A3_float = 0
            else:
                A3_float = float(A3_str)
            if A4_str == ''or A4_str == ' ':
                A4_float = 0
            else:
                A4_float = float(A4_str)
            if A5_str == ''or A5_str == ' ':
                A5_float = 0
            else:
                A5_float = float(A5_str)
            if A6_str == ''or A6_str == ' ':
                A6_float = 0
            else:
                A6_float = float(A6_str)
            if A7_str == ''or A7_str == ' ':
                A7_float = 0
            else:
                 A7_float = float(A7_str)
            if A8_str == ''or A8_str == ' ':
                A8_float = 0
            else:
                A8_float = float(A8_str)
            if A9_str == ''or A9_str == ' ':
                A9_float = 0
            else:
                A9_float = float(A9_str)
            if A10_str == ''or A10_str == ' ':
                A10_float = 0
            else:
                A10_float = float(A10_str)
            if A11_str == ''or A11_str == ' ':
                A11_float = 0
            else:
                A11_float = float(A11_str)

            if T1_str == ''or T1_str == ' ':
                T1_float = 0
            else:
                T1_float = float(T1_str)
            if T2_str == ''or T2_str == ' ':
                T2_float = 0
            else:
                T2_float = float(T2_str)

            if T3_str == ''or T3_str == ' ':
                T3_float = 0
            else:
                T3_float = float(T3_str)

            if T4_str == ''or T4_str == ' ':
                T4_float = 0
            else:
                T4_float = float(T4_str)

            if T5_str == ''or T5_str == ' ':
                T5_float = 0
            else:
                T5_float = float(T5_str)
            if T6_str == ''or T6_str == ' ':
                T6_float = 0
            else:
                T6_float = float(T6_str)
            if T7_str == ''or T7_str == ' ':
                T7_float = 0
            else:
                T7_float = float(T7_str)
            if T8_str == ''or T8_str == ' ':
                T8_float = 0
            else:
                T8_float = float(T8_str)
            if T9_str == ''or T9_str == ' ':
                T9_float = 0
            else:
                T9_float = float(T9_str)
            if T10_str == ''or T10_str == ' ':
                T10_float = 0
            else:
                T10_float = float(T10_str)
            if T11_str == ''or T11_str == ' ':
                T11_float = 0
            else:
                T11_float = float(T11_str)

            P1_float = (A1_float * T1_float \
                       + A2_float * T2_float \
                       + A3_float * T3_float \
                       + A4_float * T4_float \
                       + A5_float * T5_float \
                       + A6_float * T6_float \
                       + A7_float * T7_float \
                       + A8_float * T8_float \
                       + A9_float * T9_float \
                       + A10_float * T10_float)/1000
            P2_float = (A11_float * T11_float)/1000
            P3_float = P2_float + P1_float
            P4_float = P3_float * ((24)/Interval_float)

            P1_str = str(P1_float)
            P2_str = str(P2_float)
            P3_str = str(P3_float)
            P4_str = str(P4_float)


            self.display1.setText('工作功耗为'+P1_str+'mA·ms ,休眠功耗为'+P2_str+'mA·ms ,一个周期功耗为'+P3_str+'mA·ms ,一天功耗为'+P4_str+'mah')

        btn1.clicked.connect(cao)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window1()
    window.show()

    sys.exit(app.exec_())
