'''
树控件（QTreeWidget）的基本用法
添加、删除和修改树控件的点
添加
    item = self.tree.currentItem()  # 先获得现在的item 是一个对象
    node = QTreeWidgetItem(item)
    node.setText(0,"new")   # 第一个数字代表列
修改
    item = self.tree.currentItem()  # 先获得现在的item 是一个对象
    item.setText(0,"修改")
删除
    item = self.tree.currentItem()
    root_parent =  self.tree.invisibleRootItem() # 使根节点可视
    for item in self.tree.selectedItems():
        (item.parent()or root_parent).removeChild(item)
QTreeView控件显示系统当前目录
    model = QDirModel()     # 当前操作系统的目录结构的模型
    tree = QTreeView()
    tree.setModel(model)    # 使用该控件显示目录结构

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt


class BasicTreeWidget(QMainWindow):
    def __init__(self, parent=None):
        super(BasicTreeWidget, self).__init__(parent)
        self.setWindowTitle('树控件（QTreeWidget）的基本用法')
        self.tree = QTreeWidget()   # 创建树控件对象
        self.tree.setColumnCount(1)     # 为树控件指定列数

        # 指定列标签
        self.tree.setHeaderLabels(['Key'])
        root = QTreeWidgetItem(self.tree)
        root.setText(0, '农产品物价信息')
        self.tree.setColumnWidth(0, 160)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, '畜禽类')

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '水产品')

        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '海带鱼')
        child3.setCheckState(0, Qt.Checked)     # 为结点添加复选框

        self.tree.clicked.connect(self.onTreeClicked)
        self.tree.expandAll()   # 所有结点默认直接展开
        self.setCentralWidget(self.tree)    # 树控件充满整个屏幕

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())  # 以自己父节点开始，自己是第几个孩子
        print('key=%s' % (item.text(0)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = BasicTreeWidget()
    tree.show()
    sys.exit(app.exec_())
