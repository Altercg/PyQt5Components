"""
QTextEdit()
setHtml()   # 显示Html
setPlainText() # 显示文本
toHtml()   # 获取Html
toPlainText() # 获取文本
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QTextEdit


class QText(QWidget):
    def __init__(self):
        super(QText, self).__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('显示文本')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onclick)

    def onclick(self):
        self.textEdit.setPlainText('hello')
        # self.textEdit.setHtml('<font color="blue" >world </font>')
        # self.textEdit.toHtml('')
        # self.textEdit.toPlainText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QText()
    main.show()
    sys.exit(app.exec_())
