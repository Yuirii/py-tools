# from openpyxl import Workbook
# from openpyxl import load_workbook
#
# # wb = Workbook()
# # ws = wb.create_sheet("first sheet", 0)
# # ws.active_cell
# # ws.SHEETSTATE_VISIBLE = 'visible'
# # ws2 =wb.create_sheet("second sheet", 2)
# # ws2.SHEETSTATE_VISIBLE = 'visible'
#
# wb = load_workbook("1.xlsx")
# print(wb.sheetnames)
# sheet = wb.active
# sheet.sheet_state = 'visible'
# # ws.title = "1st"
# # ws2.title = "2nd"
#
# # sheet.sheet_properties.tabColor = "1072BA"
# # # ws2.sheet_properties.tabColor = "1022BA"
# # print("*" * 10)
# # # print("ws.sheet_properties.tabColor:\n", ws.sheet_properties.tabColor)
# # # print("wb.sheetnames:", ws.sheet_properties.tabColor, wb.sheetnames)
# #
# sheet['E1'] = '11111111111'
# # # ws2['b1'] = '111111111111'
# # sheet.append(["A2","B2"])
# # # ws2.append(['aaa'])
# # print(sheet.max_row,sheet.max_column)
#
# wb.save("1"+".xlsx")
#
# from openpyxl import load_workbook
# wb2 = load_workbook('aaaaa.xlsx')
__auther__ = 'Yoole'

from PyQt5.Qt import *
from TlinkPowerCalc import Window1

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # super(Window, self).__init__()
        self.setWindowTitle('test')
        self.resize(640, 480)
        self.setup_ui()


    def setup_ui(self):
        self.window2 = Window1()
        self.window2.setup_ui()
        self.window2.show()
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
