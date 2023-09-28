
# qt_myapp.py

import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PySide6.QtCore import Qt, QRect

class MyAppWindow(QWidget):
    def __init__(self):
        self.widgets = []
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("qt_app")
        self.resize(300,200)
        self.show()

    def paintEvent(self, ev):
        ctx = QPainter()
        w, h = self.width(), self.height()
        ctx.begin(self)

        for i in self.widgets:
            i.draw(ctx)
        
        ctx.end()

    def mousePressEvent(self, ev):
        pos=ev.position()
        #print(pos)
        x,y = int(pos.x()), int(pos.y())
        for i in self.widgets:
            i.handle_mouse(x,y)

    def add_widget(self, w):
        self.widgets.append(w)
        

