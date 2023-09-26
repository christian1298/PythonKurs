class Rect:
    def __init__(self, x, y, w, h, n) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = n
    
    def contains(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        if ((dx < 0) or (dx >= self.w)): return
        if ((dy < 0) or (dy >= self.h)): return
        print(f"test point ({tx},{ty}) inside rect '{self.name}'")


if __name__ == "__main__":
    r = [
        Rect(10, 5, 5, 5, "menu"),
        Rect(0, 0, 200, 20, "titlebar"),
        Rect(50, 30, 15, 5, "end button")
    ]
    tx = 60
    ty = 32
    for i in r:
        i.contains(tx, ty)