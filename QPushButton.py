"""
控件按钮
父类：QAbstractButton
QPushButton
    setEnabled(False)   # 设置不可用的按钮
    setIcon(QIcon(QPixmap('./bg.jpg'))) #设置按钮的图标
    self.pushButton.setCheckable(True)  # 设置开关，按一下不可以抬起，再按一下可以
    self.pushButton.toggle()    # 切换 默认选中
    信号：self.pushutton.clicked.connect(self.buttonState)

QRadioButton    单选按钮,当有两个单选按钮，改变了一个另一个也改变了
     self.radioButton1.setChecked(True)   # 默认选中
     信号：self.radioButton2.toggled.connect(self.radioState)

QToolButton     工具条按钮

QCheckBox   复选框控件
     self.checkBox1.setChecked(True)
     self.checkBox1.setTristate(True)    # 半选中
     self.checkBox3.setCheckState(Qt.PartiallyChecked)   # 当前是半选中
     信号：self.checkBox1.stateChanged.connect(self.checkBox)

QComboBox   下拉列表项
    self.cb.addItem('c++') #设置选项单个
    self.cb.addItems(['Html', 'Java', 'Python']) #设置选项多个
    self.cb.count()   # 选项个数
    self.cb.itemText(count) # 显示选项内容
    self.cb.currentText()   # 显示现在选项
    信号： self.cb.currentIndexChanged.connect(self.selectionChange)
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QDialog, QPushButton, QRadioButton, QCheckBox, QComboBox, QLabel


class Qbutton(QDialog):
    def __init__(self):
        super(Qbutton, self).__init__()
        self.initUI()

    def initUI(self):
        Vbox = QVBoxLayout()

        self.pushButton = QPushButton('普通按钮')
        self.pushButton.setCheckable(True)  # 设置开关，按一下不可以抬起，再按一下可以
        self.pushButton.toggle()    # 默认为按下去的
        # 多个信号绑定一个槽
        self.pushButton.clicked.connect(lambda: self.whichButton(self.pushButton))
        # 或者使用self.pushutton.clicked.connect(self.buttonState)

        self.radioButton1 = QRadioButton('单选按钮1')
        self.radioButton1.setChecked(True)   # 默认选中
        self.radioButton1.toggled.connect(self.radioState)
        self.radioButton2 = QRadioButton('单选按钮2')
        self.radioButton2.toggled.connect(self.radioState)

        self.checkBox1 = QCheckBox('复选框1')
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(self.checkBox)
        self.checkBox2 = QCheckBox('复选框2')
        self.checkBox2.stateChanged.connect(self.checkBox)
        self.checkBox3 = QCheckBox('复选框3')
        self.checkBox3.setTristate(True)    # 半选中
        self.checkBox3.setCheckState(Qt.PartiallyChecked)   # 当前是半选中方式
        self.checkBox3.stateChanged.connect(self.checkBox)

        self.cb = QComboBox()
        self.cb.addItem('c++')
        self.cb.addItems(['Html', 'Java', 'Python'])
        self.cb.currentIndexChanged.connect(self.selectionChange)

        Vbox.addWidget(self.pushButton)
        Vbox.addWidget(self.radioButton1)
        Vbox.addWidget(self.radioButton2)
        Vbox.addWidget(self.checkBox1)
        Vbox.addWidget(self.checkBox2)
        Vbox.addWidget(self.checkBox3)
        Vbox.addWidget(self.cb)
        self.setLayout(Vbox)
        self.setWindowTitle('按钮控件展示')

    def whichButton(self, btn):
        print('被单击的是'+btn.text())

    def radioState(self):
        btn = self.sender()
        if btn.isChecked() == True:
            print('被选中的是'+btn.text())
        else:
            print('被取消的是'+btn.text())

    def checkBox(self):
        btn = self.sender()
        check1 = str(self.checkBox1.isChecked())
        check2 = str(self.checkBox2.isChecked())
        check3 = str(self.checkBox3.isChecked())
        print(check1 + check2 + check3)

    def selectionChange(self, i):   # 默认传两个
        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
        print('current index', i, 'selection change', self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Qbutton()
    main.show()
    sys.exit(app.exec_())
