from pseudo_gui_p.myLabel import MyLabel

class MyButton(MyLabel):
    def __init__(self, txt, x, y, w, h): 
        super().__init__(txt, x, y, w, h)

    def draw(self): pass
    def handle_mouse(self, x, y):
        self.cb(self, x, y)

    def __str__(self):
        return f"MyButton with txt={self.txt}, id={self.id} at rect x={self.x}, y={self.y}, w={self.w}, h={self.h}"
    
    def set_callback(self, cb): 
        self.cb = cb

