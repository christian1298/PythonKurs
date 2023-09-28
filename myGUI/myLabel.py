from myGUI.myWidget import MyWidget
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PySide6.QtCore import Qt

class MyLabel (MyWidget):
    def __init__(self, text, x,y,w,h):
        self.text = text
        super().__init__(x,y,w,h)

    def draw(self, ctx : QPainter):
        ctx.setFont(QFont("Decorative", 10))
        ctx.setPen(Qt.black)
        ctx.drawText(self.x+2,self.y+2,self.w,self.h,0,self.text)

        # ctx.setBrush(Qt.transparent)
        # ctx.setPen(Qt.white)
        # ctx.drawRect(self.x,self.y,self.w,self.h)
        #print("draw", self)

    def __str__(self):
        return f"MyLabel with txt={self.text}, {super().__str__()}"

