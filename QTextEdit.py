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
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        buttonText = QPushButton('显示文本')

        layout = QVBoxLayout()
        layout.addWidget(textEdit)
        layout.addWidget(buttonText)
        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onclink)

    def onclink(self):
        self.textEdit.setPlainText('hello')
        # self.textEdit.setHtml('<font color="blue" >world </font>')
        # self.textEdit.toHtml('')
        # self.textEdit.toPlainText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QText()
    main.show()
    sys.exit(app.exec_())
