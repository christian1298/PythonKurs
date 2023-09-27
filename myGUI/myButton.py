from myGUI.myLabel import MyLabel

class MyButton (MyLabel):
    def __init__(self,text, x, y, w, h):
        super().__init__(text,x,y,w,h)

    def set_callback(self, cb):
        self.callback = cb

    def draw(self, ctx):
        print("draw", self)

    def handle_mouse(self, x, y):
        self.callback(self, x, y)

    def __str__(self):
        return f"MyButton with txt={self.text} , id={self.id} at rect x={self.x} , y={self.y}, w={self.w},h={self.h}"
