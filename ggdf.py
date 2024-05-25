from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QLabel,
    QMessageBox, QRadioButton
)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс від Craze People')
main_win.resize(400,200)



question = QLabel('В якому році канал отримав золоту кнопку від YouTube?')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')


layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()


layoutH1.addWidget(question, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment=Qt.AlignCenter)


layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)


main_win.setLayout(layout_main)


def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Правильно! Ви виграли гіроскутер')
    victory_win.exec_()


def show_lose():
    victory_lose = QMessageBox()
    victory_lose.setText('Ні, в 2015 році. Ви виграли фірмовий плакат')
    victory_lose.exec_()



btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_win)
btn_answer4.clicked.connect(show_lose)


main_win.show()
app.exec_()
