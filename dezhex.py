import sys

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PySide6.QtCore import Qt, QRect

class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.hex = None
        self.dez = None
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(QLabel("Dezimal", self), 0,0)
        self.dez = QLineEdit("", self)
        grid.addWidget(self.dez, 0,1)
        grid.addWidget(QLabel("Hexal", self), 1,0)
        self.hex =QLineEdit("", self)
        self.hex.setReadOnly(True)
        grid.addWidget(self.hex, 1,1)
        
        b = QPushButton("Berechnung", self)
        grid.addWidget(b, 2,0,1,2)
        b.clicked.connect(self.buttonPressed)

        self.setLayout(grid)
        self.show()

    def buttonPressed(self):
        self.hex.setText(hex(int(self.dez.text())))