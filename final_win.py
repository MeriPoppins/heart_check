from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from instr import *


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(QLabel(txt_index), alignment=Qt.AlignCenter)
        self.layout_line.addWidget(QLabel(txt_workheart), alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
