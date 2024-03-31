from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

from instr import *
from final_win import FinalWin


class Experiment():
    def __init__(self, age, pulse_1, pulse_2, pulse_3):
        self.age = age
        self.p1 = pulse_1
        self.p2 = pulse_2
        self.p3 = pulse_3


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
        self.text_timer.setFont(QFont("Times", 30, QFont.Bold))
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)

        self.h_line = QHBoxLayout()
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def next_click(self):
        self.exp = Experiment(int(self.age.text()), int(self.pulse_1.text()), int(self.pulse_2.text()), int(self.pulse_3.text()))
        self.fin_win = FinalWin(self.exp)
        self.hide()

    def timer_start(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        time = time.addSecs(1)
        if time.toString('hh:mm:ss') == '00:00:31':
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        if 15 < int(time.toString('hh:mm:ss')[6:8]) < 45:
            self.text_timer.setStyleSheet("color: red")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.start_1.clicked.connect(self.timer_start)
        self.start_2.clicked.connect(self.timer_sits)
        self.start_3.clicked.connect(self.timer_final)
