"""
绘图API 必须在paintEvent事件方法中绘制元素，创建自动调用

painter = QPainter()    # 类似于打开一个画板
painter.begin()

1.文本 painter.drawText(区域，位置，内容)
    self.text = '绘图'
    painter.setFont(QFont('SimSun', 25))
    painter.drawText(event.rect(), Qt.AlignCenter, self.text)   # 整个窗口的尺寸
2.图形 drawPoint(x,y)
    pen.setStyle()
    pen.setStyle(Qt.CustomDashLine)     # 自定义
    pen.setDashPattern([1, 10, 5, 8])   # 奇数位定义的是空格，偶数位(0开始)为线长
    不同类型的直线：Qt.SolidLine，Qt.DashLine，Qt.DashDotDotLine，Qt.DotLine，Qt.DashDotDotLine
3.图像
    rect = QRect(x,y,width,height)
    drawArc(rect, 0, 50*16)   # 绘制弧 360*16为圆 第二个参数为起始角度，第三个为结束角度 单位：1 alen=1/16 度
    drawChord()     # 绘制带弦的弧
    drawPie()       # 绘制扇形
    #绘制多边形
    drawEllipse(120, 120, 150, 100) # 绘制椭圆
    point1 = QPoint(x1, y1) ...     # 多个点
    poly = QPolygon(point1, ...)   # 创建多边形对象
    drawPolygon(poly)   #绘制多边形
    # 绘制图像
    image = QImage('./bg.jpg')  #加载图像
    image.save('./bg1.jpg')
    rect = QRect(10, 400,image.width()/3,image.height()/3)  # 起始，大小
4.画刷填充图形区域
    brush = QBrush(Qt.SolidPattern)     # Qt.Dense1Pattern ...
    painter.setBrush(brush)
    painter.drawRect(10,15,90,60)
painter.end()
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtWidgets import QApplication, QWidget


class DrawDemo(QWidget):
    def __init__(self):
        super(DrawDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Draw案例')
        self.resize(500, 500)

    def paintEvent(self, event):    # 方法固定
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.red, 3, Qt.SolidLine)     # 实线

        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)   # 虚线
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotDotLine)     # 点划线
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)    # 点线
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)     #
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)     # 自定义
        pen.setDashPattern([1, 10, 5, 8])   # 奇数位定义的是空格，偶数位(0开始)为线长
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawDemo()
    main.show()
    sys.exit(app.exec_())
