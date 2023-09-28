import sys

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PySide6.QtCore import Qt, QRect

class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(QLabel("Dezimal", self), 0,0)
        grid.addWidget(QLineEdit("", self), 0,1)
        grid.addWidget(QLabel("Hexal", self), 1,0)
        grid.addWidget(QLineEdit("", self), 1,1)
        
        grid.addWidget(QPushButton("Berechnung", self), 2,0,1,2)

        self.setLayout(grid)
        self.show()
