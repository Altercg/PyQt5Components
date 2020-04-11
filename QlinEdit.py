'''
QLineEdit的回显模式(EchoMode)
1.Normal    正常显示
2.NoEcho    不显示但是其实已经输入了
3.Password  密码模式
4.PasswordEchoOnEdit
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QFormLayout, QLineEdit


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
        formLayout.addRow("Normal", normalEdit)
        formLayout.addRow("NoEcho", noEchoEdit)
        formLayout.addRow("password", passwordEdit)
        formLayout.addRow("passwordEchoOnEdit", passwordEchoOnEdit)

        # setPlaceholderText()   输入提示

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
