from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

from instr import *
from final_win import FinalWin


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.l_line = QVBoxLayout()
        self.name = QLineEdit(txt_hintname)
        self.age = QLineEdit(txt_hintage)
        self.pulse_1 = QLineEdit(txt_hinttest1)
        self.pulse_2 = QLineEdit(txt_hinttest2)
        self.pulse_3 = QLineEdit(txt_hinttest3)
        self.start_1 = QPushButton(txt_starttest1)
        self.start_2 = QPushButton(txt_starttest2)
        self.start_3 = QPushButton(txt_starttest3)
        self.btn_next = QPushButton(txt_sendresults)
        self.l_line.addWidget(QLabel(txt_name), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_age), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_test1), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.start_1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.pulse_1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_test2), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.start_2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(QLabel(txt_test3), alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.start_3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.pulse_2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.pulse_3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.r_line = QVBoxLayout()
        self.text_timer = QLabel(txt_timer)
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)

        self.h_line = QHBoxLayout()
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def next_click(self):
        self.fin_win = FinalWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
