'''
让控件支持拖拽动作
A.setDragEnabled(True)
B.setAcceptDrops(True)

B需要两个事件
1. dragEnterEvent   将A拖到B触发
2. dropEvent        在B的区域放下A时触发
'''

import sys
from PyQt5.QtWidgets import *


class MyComboBox(QComboBox):    # QComboBox 下拉控件
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():  # 文本数据
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())   # 添加词条


class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel("请将左边的文本拖拽到右边的下拉列表中"))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)  # 让QLineEdit控件可拖动

        combo = MyComboBox()
        formLayout.addRow(lineEdit, combo)  # A,B
        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()
    sys.exit(app.exec_())
