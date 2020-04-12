'''
QLineEdit的回显模式(EchoMode)
1.Normal    正常显示
2.NoEcho    不显示但是其实已经输入了
3.Password  密码模式
4.PasswordEchoOnEdit
'''
'''
QLineEdit的限制输入
setValidator()
QLineEdit的掩码限制输入
setInputMask('')
A ASCII字母字符是必须的，取值空间是A-Z,a-z
a ASCII字母字符是允许的但不是必须的.
N ASCII字母字符是必须的. A-Z, a-z, 0-9.
n ASCII 字母字符是允许的但不是必须的.
X 任何字符都可以，是必须需要的.
x 任何字符都允许的，但不是必须需要的.
9 ASCII 数字是必须要的. 0-9.
0 ASCII 数字是允许的，但不是必须要的.
D ASCII  数字是必须要的. 1-9.
d ASCII 数字是允许的，但不是必须要的 (1-9).
# ASCII 数字是或加减符号允许的，但不是必须要的.
H 十六进制数据字符是必须要的. A-F, a-f, 0-9.
h 十六进制数据字符是允许的，但不是必须要的.
B 二进制数据字符是必须要的. 0-1.
b 二进制数据字符是允许的，但不是必须要的.
> 所有的字符字母都都大写的.
< 所有的字符字幕都是小写的.
! 关闭大小写.
\ 使用 \ 去转义上面的字符，如果再需要显示上述字符的时候.
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

        # 使用掩码
        # normalEdit.setInputMask('000.000.000.000;_') 以这个形式输入，;表示没有就是下划线
        # normalEdit.setInputMask('>AAAAA-AAAAA-AAAAA;#')

        self.setLayout(formLayout)
        self.setWindowTitle('QLineEdit')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
