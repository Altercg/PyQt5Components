"""
QSpinBox 计数器控件
    setRange(1,7)   # 设置范围
    setValue()  # 设置默认值
    setSingleStep   # 设置步长

QSlider 滑块控件
    QSlider(Qt.Horizontal)  # 水平滑块  vertical 垂直滑块
    setMininum(12)
    setMaxinum(48)
    setSingleStep(3)
    setValue(18)    # 设置默认
    setTickPosition(QSlider.TicksBelow) #设置刻度的位置，在下方  QSlider.TicksLeft在左边
    setTickInterval(6)  # 设置刻度的间隔
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QDialog, QPushButton, QRadioButton, QCheckBox, QComboBox, QLabel, \
    QWidget, QSpinBox


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.sb = QSpinBox()
        self.sb.valueChanged.connect(self.valuechange)

        layout = QVBoxLayout()
        layout.addWidget(self.sb)
        self.setLayout(layout)

    def valuechange(self):
        print(str(self.sb.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())
