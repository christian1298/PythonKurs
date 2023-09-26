class Rect:
    def __init__(self, x, y, w, h, desc) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.desc = desc

    def contains(self,x,y) -> bool:
        dx = x - self.x
        dy = y - self.y
        if((dx < 0) or (dx >= self.w) or (dy < 0) or (dy >= self.h)):
            return False
        else:
            return True


data = [
    Rect(10,5,5,5,"menu"),
    Rect(0,0,200,20,"titlebar"),
    Rect(50,30,15,5,"end button")
]
tx = 60
ty = 32

for i in data:
    if(i.contains(tx,ty)):
        print("test point (%d , %d) inside rect %s\n" % (tx , ty, i.desc))