"""
对话框：QDialog
QMessageBox
    关于对话框：QMessageBox.about(self,'关于','文字')   # 显示关于对话框
    消息对话框：QMessageBox.information(self,'消息','文字',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    警告对话框：QMessageBox.warning(self,'警告','文字',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    提问对话框：QMessageBox.question(self,'提问','文字',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    错误兑换框：QMessageBox.critical(self,'错误','文字',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

QColorDialog
QFontDialog

QFileDialog
    fname, _ = QFileDialog.getOpenFileName(self,'标题','.(路径)','图像文件(*.jpg *png)')
    setFileMode() #打开文件类型，QFileDialog.AnyFile任何文件 QFileDialog.ExistingFile已存在的文件 QFileDialog.Directory文件目录
    setFilter(QDir.Files)   # 过滤器，只显示过滤器允许的文件类型
    selectedFiles()
QInputDialog
    item, ok = QInputDialog.getItem(self,'标题','语言列表'，items)    #items = ('c', 'c++', 'Python')
    text, ok = QInputDialog.getText(self,'标题','输入姓名')
    num, ok = QInputDialog.getInt(self,'标题','输入数字')
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMainWindow, QVBoxLayout, QLabel, QFontDialog, QWidget, \
    QColorDialog


class QDialogDemo(QWidget):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog案例')
        layout = QVBoxLayout()
        self.resize(500, 500)

        self.button = QPushButton('弹出')
        self.button.clicked.connect(self.showDialog)
        self.label = QLabel('Hello，测试字体例子')

        # 字体对话框
        self.fButton = QPushButton('字体')
        self.fButton.clicked.connect(self.gFont)

        # 颜色对话框
        self.colorButton = QPushButton('设置颜色')
        self.colorButton.clicked.connect(self.getColor)
        self.colorButton1 = QPushButton('设置背景颜色')
        self.colorButton1.clicked.connect(self.getBGColor)

        layout.addWidget(self.button)
        layout.addWidget(self.fButton)
        layout.addWidget(self.colorButton)
        layout.addWidget(self.colorButton1)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def gFont(self):
        font, ok = QFontDialog.getFont()    # 更改字体
        if ok:
            self.label.setFont(font)    # 并且显示

    def getColor(self):
        color = QColorDialog.getColor()     # 获取字体颜色
        p = QPalette()
        p.setColor(QPalette.WindowText, color)  # 更改字体颜色
        self.label.setPalette(p)    # 并且显示

    def getBGColor(self):
        color = QColorDialog.getColor()     # 获取背景颜色
        p = QPalette()
        p.setColor(QPalette.Window, color)  # 更改背景颜色
        self.label.setAutoFillBackground(True)  # 自动填充
        self.label.setPalette(p)        # 并且显示

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())
