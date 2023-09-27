from pseudo_gui_p.myLabel import MyLabel

l = MyLabel("End Program", 0, 0, 30, 10)
print("Identify l")
print(l)
l.draw(None)

for x, y in ((10,5), (40, 20)):
    print(f"l contains point {x},{y}?", l.contains(x, y))