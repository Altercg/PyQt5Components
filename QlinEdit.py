'''
QLineEdit的回显模式(EchoMode)
1.Normal    正常显示
2.NoEcho    不显示但是其实已经输入了
3.Password  密码模式
4.PasswordEchoOnEdit
'''
'''
QLineEdit的限制输入

'''
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QFormLayout, QLineEdit
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QDoubleValidator,QRegExpValidator


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        formLayout = QFormLayout()

        normalEdit = QLineEdit()
        noEchoEdit = QLineEdit()
        passwordEdit = QLineEdit()
        passwordEchoOnEdit = QLineEdit()

        # 表单布局
        formLayout.addRow("Normal", normalEdit)     # 整型
        formLayout.addRow("NoEcho", noEchoEdit)
        formLayout.addRow("password", passwordEdit) # 浮点型
        formLayout.addRow("passwordEchoOnEdit", passwordEchoOnEdit)

        # setPlaceholderText()   输入提示

        # 整数
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)
        # 浮点数,小数点2位
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)  # 标准表示法
        doubleValidator.setDecimals(2)
        # 字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)
        # 校验器
        normalEdit.setValidator(intValidator)
        passwordEdit.setValidator(doubleValidator)
        passwordEchoOnEdit.setValidator(validator)

        # setEchoMode() 设置模式
        normalEdit.setEchoMode(QLineEdit.Normal)
        noEchoEdit.setEchoMode(QLineEdit.NoEcho)
        passwordEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)
        self.setWindowTitle('QLineEdit')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
