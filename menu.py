'''
创建和使用菜单
信号：triggered
创建工具栏
    tb1 = addToolBar("File")    # 创建工具栏
    new = QAction(QIcon('./images/new.png'),"new",self) # 第二个文本就是提示，默认只显示图标
    tb1.addAction(new)  # 添加活动
    tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 下侧显示文本和图标
信号：actionTriggered
创建状态栏
     self.statusBar = QStatusBar()  # 创建
     self.setStatusBar(self.statusBar)  # 设置
     self.statusBar.showMessage(q.text() + " 菜单被点击了",5000)  # 状态栏显示文字，5000ms
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        bar = self.menuBar()  # 获取菜单栏
        file = bar.addMenu("文件")    # 添加文件菜单
        file.addAction("新建")    # 菜单里面添加动作

        save = QAction("保存", self)
        save.setShortcut("Ctrl + S")    # 快捷键
        save.triggered.connect(self.process)
        file.addAction(save)
        quit = QAction("退出", self)
        file.addAction(quit)

        edit = bar.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")

    def process(self, a):
        print(self.sender().text())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = Menu()

    main.show()

    sys.exit(app.exec_())