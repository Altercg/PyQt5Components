'''

停靠控件（QDockWidget）

'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DockDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DockDemo, self).__init__(parent)
        self.setWindowTitle("停靠控件（QDockWidget）")
        layout = QHBoxLayout()
        self.items = QDockWidget('Dockable', self)  # 创建
        self.listWidget = QListWidget()     # 扩展的列表控件
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')
        self.items.setWidget(self.listWidget)   # 添加
        self.setCentralWidget(QLineEdit())
        self.items.setFloating(True)    # 允许浮动

        self.addDockWidget(Qt.RightDockWidgetArea, self.items)   # 停靠区域


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DockDemo()
    demo.show()
    sys.exit(app.exec_())
