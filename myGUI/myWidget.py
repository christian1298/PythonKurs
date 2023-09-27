import itertools
class MyWidget:
    __ID = itertools.count()
    def __init__(self,x,y,w,h):
        self.id = next(self.__ID)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, ctx):
        pass

    def handle_mouse(self, x, y):
        pass

    def contains(self,x,y):
        dx = x - self.x
        dy = y - self.y
        if((dx < 0) or (dx >= self.w) or (dy < 0) or (dy >= self.h)):
            return False
        else:
            return True

    def __str__(self):
        return f"id={self.id} at rect x={self.x}, y={self.y} , w={self.w} , h={self.h}"