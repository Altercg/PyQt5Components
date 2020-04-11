'''
setBuddy()	#设置伙伴关系
setAlignment()#设置文本对齐方式
setIndent()	#设置文本缩进
text()		#获取文本内容
setText()		#设置文本内容
selectedText()	#返回所选的字符
setWordWrap()	#设置是否允许换行
setAlignment(Qt.AlignCenter)	#文本居中对齐
setToolTip('xxx')	#设置提示

常用的信号：
linkHovered：划过控件触发
linkActivated：单击控件触发
'''
'''
QLabel与伙伴关系
mainLaout.addWidget(控件对象, rowIndex,columnIndex, row,column) 前两个数是控件在栅格的位置，后两个数是空间的尺寸
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QVBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)

        label1.setText("<a href='#'><font color=yellow>text</font></a>")
        label1.setAutoFillBackground(True)  # 自动填充背景
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)  # 设置背景颜色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setAlignment(Qt.AlignCenter)
        label2.setToolTip('xxx')
        label2.setPixmap(QPixmap("./bg.jpg"))   # 显示图片

        label3.setOpenExternalLinks(False)   # True可以打开html< a >的连接
        label3.setText("<a href='#'>xxxx</a>")

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)

        label1.linkHovered.connect(self.link_hovered)   # label1与label3的text一定要是超链接
        label3.linkActivated.connect(self.linkClicked)

        ''' 
        伙伴控件
        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)
        
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLabel, 0, 1, 1, 2)
        '''
        self.setLayout(vbox)
        self.setWindowTitle('QLabel')

    def link_hovered(self):
        print('linkHovered')

    def linkClicked(self):
        print('linkActivated')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
