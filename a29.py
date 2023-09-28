import sys

from PySide6.QtWidgets import QApplication, QWidget
from dezhex import Calc
def clicked(widget, x,y ):
    print(f"callback: clicked at x={x}, y={y}")
    app.closeAllWindows()


app = QApplication(sys.argv)
w=Calc()
sys.exit(app.exec())