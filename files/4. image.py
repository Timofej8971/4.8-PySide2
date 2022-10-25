#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать изображение на холсте
"""

import sys
import random
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPainter, QBrush, QPen, QPolygon, QColor
from PySide2.QtWidgets import QApplication, QWidget


class HomePainting(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рисунок")
        self.setGeometry(500, 500, 500, 400)
        self.setStyleSheet("background-color: #87ceeb;")

    def paintEvent(self, event):
        painter = QPainter(self)
        self.house(painter)
        self.sun(painter)
        self.grass(painter)
        # self.kit(painter)

    def house(self, painter):
        painter.setBrush(QColor(255, 255, 51))
        painter.drawRect(170, 138, 180, 250)  # Корпус дома

        painter.setBrush(QColor(255, 178, 102))
        roof_points = QPolygon(
            [QPoint(170, 138),
             QPoint(260, 57),
             QPoint(350, 138)]
        )
        painter.drawPolygon(roof_points)  # Крыша

        painter.setBrush(QColor(230, 230, 250))
        painter.drawEllipse(240, 85, 40, 40)
        painter.drawLine(260, 85, 260, 125)
        painter.drawLine(240, 105, 280, 105)  # Окно на крыше

        painter.setBrush(QColor(230, 230, 250))
        x = 190
        y = 150
        while y < 330:
            painter.drawRect(x, y, 60, 40)
            painter.drawLine(x, y + 20, x + 60, y + 20)
            painter.drawLine(x + 30, y, x + 30, y + 40)
            x2 = x + 80
            painter.drawRect(x2, y, 60, 40)
            painter.drawLine(x2, y + 20, x2 + 60, y + 20)
            painter.drawLine(x2 + 30, y, x2 + 30, y + 40)
            y += 60

        painter.setBrush(QColor(255, 248, 220))
        painter.drawRect(250, 340, 20, 40)
        painter.drawEllipse(265, 360, 5, 5)  # Дверь

        painter.setBrush(QColor(0, 0, 255))
        painter.drawRect(178, 325, 45, 20)
        painter.drawText(180, 340, "Kotik st")  # обозначение улицы

    def sun(self, painter):
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
        painter.drawEllipse(400, 20, 80, 80)

    def grass(self, painter):
        painter.setPen(QPen(Qt.darkGreen, 2, Qt.SolidLine))
        for i in range(35):
            painter.drawArc(
                random.randint(1, 5),
                330,
                i * 15,
                250,
                0,
                random.randint(50, 55) * 11,
            )


"""
    def kit(self, painter):
        painter.drawEllipse(290, 330, 40, 35)
        painter.drawEllipse(295, 340, 10, 10)
        painter.drawEllipse(315, 340, 10, 10)
        noise_points = QPolygon(
            [QPoint(305, 355),
             QPoint(310, 345),
             QPoint(315, 355)]
        )
        painter.drawPolygon(noise_points)
        right_points = QPolygon(
            [QPoint(345, 320),
             QPoint(325, 335),
             QPoint(335, 345)]
        )
        painter.drawPolygon(right_points)
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomePainting()
    window.show()
    sys.exit(app.exec_())
