from myGUI.myLabel import MyLabel
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PySide6.QtCore import Qt

class MyButton (MyLabel):
    def __init__(self,text, x, y, w, h):
        super().__init__(text,x,y,w,h)
        self.callback = None

    def set_callback(self, cb):
        self.callback = cb

    def draw(self, ctx : QPainter):
        ctx.setBrush(Qt.white)
        ctx.setPen(Qt.gray)
        ctx.drawRect(self.x,self.y,self.w,self.h)

        super().draw(ctx)
        # ctx.setFont(QFont("Decorative", 10))
        # ctx.setPen(Qt.black)
        # ctx.drawText(self.x+2,self.y+2,self.w,self.h,0,self.text)
        #print("draw", self)

    def handle_mouse(self, x, y):
        if(self.callback):
            self.callback(self, x, y)

    def __str__(self):
        return f"MyButton with txt={self.text} , {super(MyLabel, self).__str__()}"
        #return f"MyButton with txt={self.text} , id={self.id} at rect x={self.x} , y={self.y}, w={self.w},h={self.h}"
