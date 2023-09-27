from pseudo_gui_p.myButton import MyButton

def clicked(widget, x,y ):
    print(f"callback: clicked at x={x}, y={y}")

b=MyButton("Click", 40, 0, 30, 10)
b.set_callback(clicked)
print("Identify b")
print(b)

for x, y in ((10,5), (40, 5)):
    pressed = b.contains(x, y)
    print(f"b contains point ({x},{y})?", pressed)
    if pressed: b.handle_mouse(x, y)