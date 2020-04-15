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

    textItem = QTableWidgetItem('小明')
    tableWidget.setItem(0,0,textItem)   # cell里面加文本
    combox.setStyleSheet('QComboBox{margin:3px};')  # QSS，设置combox控件样式
    tableWidget.setCellWidget(0,1,combox)   #cell里面加combox

    findItems(text,QtCore.Qt.MatchExactly) # 数据定位，Qt.MatchStartsWith以此开头，Qt.MatchExactly精确定位，返回列表
    item.setBackground(QBrush(QColor(0,255,0)))     # 设置背景色
    item.setForeground(QBrush(QColor(255,0,0)))     # 设置字体色
    newItem.setFont(QFont('Times',14,QFont.Black))  # 设置字体样式
    tableWidget.verticalScrollBar().setSliderPosition(row)
    # setSliderPosition(row)  # 找到满足的单元格，定位单元格所在的行
    # verticalScrollBar()     #获得滚动条

    sortItems(columnIndex，orderType）# 单元格排序  1.指定哪一列,2.升序or降序
    # Qt.DescendingOrder    降序
    # Qt.AscendingOrder     升序

    setTextAlignment(Qt.AlignRight | Qt.AlignBottom)  # 分本对齐方式    Qt.AlignRight   Qt.AlignBottom

    setSpan(行，列，合并多少行数，要合并的列数)  # 合并单元格，1表示不合并

    tableWidget.setRowHeight(0, 80)     # 第1行的高度为80
    tableWidget.setColumnWidth(2, 120)    # 设置cell的尺寸

    newItem = QTableWidgetItem(QIcon('./images/bao1.png'),'背包')# 图片和文本添加到一个单元格中
    setIconSize(QSize(width,height))    # 改变单元格图片的尺寸

    # 在cell显示上下文菜单
    self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)     # 设置允许显示上下文菜单
信号：self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
    def generateMenu(self,pos): # pos的相当于屏幕的坐标系
        self.tableWidget.selectionModel().selection().indexes() # 获取所选择的行
        menu = QMenu()  # 创建菜单项
        item1 = menu.addAction("菜单项1")  # 添加菜单项
        screenPos = self.tableWidget.mapToGlobal(pos)   #转为相对于菜单的
        action = menu.exec(screenPos)   # 不点击就不会动

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