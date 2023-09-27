class MyWidget:
    id_ctr = 0
    def __init__(self, x,y,w,h):
        self.id = MyWidget.id_ctr
        MyWidget.id_ctr += 1

        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, ctx):
        pass

    def handle_mouse(x,y):
        pass 

    def contains(self,x,y) -> bool:
        dx = x - self.x
        dy = y - self.y
        if((dx < 0) or (dx >= self.w) or (dy < 0) or (dy >= self.h)):
            return False
        else:
            return True

    def __str__():
        pass