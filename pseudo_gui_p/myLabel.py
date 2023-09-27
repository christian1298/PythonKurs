from pseudo_gui_p.myWidget import MyWidget

class MyLabel(MyWidget):
    def __init__(self, txt, x, y, w, h) -> None:
        self.txt = txt
        super().__init__(x, y, w, h)

    def draw(self, ctx):
        print(f"draw MyLabel with txt={self.txt}, id={self.id} at rect x={self.x}, y={self.y}, w={self.w}, h={self.h}")

    def handle_mouse(x,y):
        pass 

    def contains(self,x,y) -> bool:
        dx = x - self.x
        dy = y - self.y
        if((dx < 0) or (dx >= self.w) or (dy < 0) or (dy >= self.h)):
            return False
        else:
            return True

    def __str__(self):
        return f"MyLabel with txt={self.txt}, id={self.id} at rect x={self.x}, y={self.y}, w={self.w}, h={self.h}"
    