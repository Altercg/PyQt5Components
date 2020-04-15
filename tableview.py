'''
显示二维表数据（QTableView控件）
    数据源 Model
    需要创建QTableView实例和一个数据源（Model），然后将两者关联
    MVC：Model   Viewer   Controller  MVC的目的是将后端的数据和前端页面的耦合度降低

QTableView的子类，扩展的表格控件（QTableWidget）
每一个Cell（单元格）是一个QTableWidgetItem
    tablewidget = QTableWidget()
    tablewidget.setRowCount(4)  # 设置行数
    tablewidget.setColumnCount(3)   # 设置列数
    tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)   # 禁止编辑
    tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 整行选择

    tablewidget.resizeColumnsToContents()# 根据内容调整列和行
    tablewidget.resizeRowsToContents()

    tablewidget.horizontalHeader().setVisible(False)    # 水平头隐藏
#   tablewidget.verticalHeader().setVisible(False)

    tablewidget.setVerticalHeaderLabels(["a","b"])  # 设置水平头的名称
    tablewidget.setShowGrid(False)  # 隐藏表格线

显示列表数据（QListView控件）
    listview = QListView()
    listModel = QStringListModel()
    self.list = ["列表项1","列表项2", "列表项3"]
    listModel.setStringList(self.list)
    listview.setModel(listModel)
信号：listview.clicked.connect(self.clicked)
def clicked(self,item):
    QMessageBox.information(self,"QListView","您选择了：" + self.list[item.row()])

QListView的子类，扩展的列表控件（QListWidget）
    self.listwidget = QListWidget()
    self.listwidget.addItem("item1")
信号：self.listwidget.itemClicked.connect(self.clicked)
def clicked(self,Index):
    self.listwidget.item(self.listwidget.row(Index)).text())    # 先获得点击的行数的文本，再传入获得文本
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class TableView(QWidget):
    def __init__(self, arg=None):
        super(TableView, self).__init__(arg)
        self.setWindowTitle("QTableView表格视图控件演示")
        self.resize(500, 300);
        self.model = QStandardItemModel(4, 3)   # 设置二维表
        self.model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])    # 设置列

        # 关联QTableView控件和Model
        self.tableview = QTableView()
        self.tableview.setModel(self.model)

        # 添加数据
        item11 = QStandardItem('10')
        item12 = QStandardItem('雷神')
        item13 = QStandardItem('2000')
        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)
        item31 = QStandardItem('30')
        item32 = QStandardItem('死亡女神')
        item33 = QStandardItem('3000')
        self.model.setItem(2, 0, item31)
        self.model.setItem(2, 1, item32)
        self.model.setItem(2, 2, item33)

        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    table = TableView()

    table.show()

    sys.exit(app.exec_())