from myGUI.myWidget import MyWidget
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PySide6.QtCore import Qt

class MyContainer (MyWidget):
    def __init__(self, x,y,w,h):
        super().__init__(x,y,w,h)
        self.widget = []

    def draw(self, ctx : QPainter):
        ctx.setBrush(Qt.white)
        ctx.setPen(Qt.white)
        ctx.drawRect(self.x,self.y,self.w,self.h)
        # print("draw MyContainer with MyContainer" + super().__str__())
        for w in self.widget:
            w.draw(ctx)

    def handle_mouse(self, x, y):
        for w in self.widget:
            if(w.contains(x,y)):
                w.handle_mouse(x,y)
                break

    def add_widget(self, w):
        self.widget.append(w)