'''
使用打印机
 printDialog = QPageSetupDialog(self.printer,self)  # 打印设置对话框
 printdialog = QPrintDialog(self.printer,self)  # 打印对话框
'''
from PyQt5 import QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import *
import sys


class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport,self).__init__()
        self.setGeometry(500, 200, 300, 300)
        self.button = QPushButton('打印QTextEdit控件中的内容',self)
        self.button.setGeometry(20, 20, 260, 30)
        self.editor = QTextEdit('默认文本', self)
        self.editor.setGeometry(20, 60, 260, 200)
        self.button.clicked.connect(self.print)

    def print(self):
        printer = QtPrintSupport.QPrinter()

        painter = QtGui.QPainter()

        painter.begin(printer)      # 将绘制的目标重定向到打印机
        screen = self.editor.grab()         # 获得editor的内容
        painter.drawPixmap(10, 10, screen)
        painter.end()
        print("print")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = PrintSupport()
    gui.show()
    app.exec_()
