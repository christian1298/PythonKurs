import sys
from myGUI.myLabel import *
from myGUI.myButton import *
from myGUI.myContainer import *
from myGUI.qt_myapp import MyAppWindow
from PySide6.QtWidgets import QApplication, QWidget

def clicked(widget, x,y ):
    print(f"callback: clicked at x={x}, y={y}")
    app.closeAllWindows()

l=MyLabel("End Program", 20, 50, 80, 20)
b=MyButton("Click", 100, 50, 40, 20)
b.set_callback(clicked)
c=MyContainer(0,0, 300, 200)
c.add_widget(l)
c.add_widget(b)
app = QApplication(sys.argv)
w=MyAppWindow()
w.add_widget(c)
sys.exit(app.exec())