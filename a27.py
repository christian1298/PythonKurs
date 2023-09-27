from Dateien.Uebung.myapp import MyApp
from myGUI.myButton import *
from myGUI.myContainer import *


def clicked(widget, x,y ):
    print(f"callback: clicked at x={x}, y={y}")
    app.exit()

l=MyLabel("End Program", 0, 0, 30, 10)
b=MyButton("Click", 40, 0, 20, 10)
b.set_callback(clicked)
c=MyContainer(0,0, 100, 50)
c.add_widget(l)
c.add_widget(b)
app = MyApp()
app.add_widget(c)
app.run()