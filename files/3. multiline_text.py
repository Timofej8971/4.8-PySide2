#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Напишите программу по описанию. Размеры многострочного текстового поля
определяются значениями, введенными в однострочные текстовые поля.
Изменение размера происходит при нажатии мышью на кнопку, а также при
нажатии клавиши Enter. Цвет фона экземпляра Text светлосерый (lightgrey),
когда поле не в фокусе, и белый, когда имеет фокус. Для справки: фокус
перемещается по виджетам при нажатии Tab, Ctrl+Tab, Shift+Tab, а также
при клике по ним мышью (к кнопкам последнее не относится)
"""


import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
)


def main():
    app = QApplication(sys.argv)
    window = MultilineText()
    window.show()
    sys.exit(app.exec_())


class MultilineText(QWidget):
    def __init__(self):
        super().__init__()
        self.line_edit_first = QLineEdit()
        self.line_edit_second = QLineEdit()
        self.text_edit = QTextEdit()
        self.button = QPushButton("button")
        self.initial_ui()

    def initial_ui(self):
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("multiline text")

        QApplication.instance().focusChanged.connect(self.focus)
        self.button.clicked.connect(self.text_edit_resize)
        self.line_edit_second.returnPressed.connect(self.text_edit_resize)

        horizontal_layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()
        horizontal_layout.addWidget(self.line_edit_first)
        horizontal_layout.addWidget(self.line_edit_second)
        horizontal_layout.addWidget(self.button)
        vertical_layout.addWidget(self.text_edit)
        vertical_layout.addLayout(horizontal_layout)
        self.setLayout(vertical_layout)

    def focus(self, old, new):
        if self.text_edit == new:
            self.text_edit.setStyleSheet("background-color: #fff;")
        elif self.text_edit == old:
            self.text_edit.setStyleSheet("background-color: #d3d3d3;")

    def text_edit_resize(self):
        self.text_edit.resize(
            int(self.line_edit_first.text()), int(self.line_edit_second.text())
        )


if __name__ == "__main__":
    main()
