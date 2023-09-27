import itertools
from myGUI.myWidget import MyWidget

class MyContainer (MyWidget):
    def __init__(self, x,y,w,h):
        super().__init__(x,y,w,h)
        self.widget = []

    def draw(self, ctx):
        print("draw MyContainer with", self)
        for w in self.widget:
            w.draw(ctx)

    def handle_mouse(self, x, y):
        for w in self.widget:
            if(w.contains(x,y)):
                w.handle_mouse(x,y)
                break

    def add_widget(self, w):
        self.widget.append(w)

    def __str__(self):
        return f"MyContainer {super().__str__()}" 