#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Изучите приведенную программу и самостоятельно запрограммируйте
постепенное движение фигуры в ту точку холста, где пользователь
кликает левой кнопкой мыши. Координаты события хранятся в его
атрибутах x и y (event.x , event.y)
"""

from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import QPropertyAnimation, QPoint
import sys


def main():
    app = QApplication(sys.argv)
    window = Ball()
    window.show()
    sys.exit(app.exec_())


class Ball(QWidget):
    def __init__(self):
        super().__init__()
        self.ball = QWidget(self)
        self.animation = QPropertyAnimation(self.ball, b"pos")

        self.initial_ui()

    def initial_ui(self):
        self.setGeometry(350, 350, 350, 350)
        self.setWindowTitle("Шарик")

        self.ball.setStyleSheet("background-color: red ;border-radius: 25%;")
        self.ball.resize(50, 50)
        self.animation.setDuration(1000)

    def mousePressEvent(self, event):
        self.animation.setEndValue(QPoint(event.x() - 25, event.y() - 25))
        self.animation.start()


if __name__ == "__main__":
    main()
