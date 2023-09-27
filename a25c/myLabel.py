from a25c.myWidget import MyWidget

class MyLabel (MyWidget):
    def __init__(self, text, x,y,w,h):
        self.text = text
        super().__init__(x,y,w,h)

    def draw(self, ctx):
        print("draw", self)

    def __str__(self):
        return f"MyLabel with txt={self.text}, {super().__str__()}"

