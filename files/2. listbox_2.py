#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Решите задачу: напишите программу по следующему описанию.
Нажатие Enter в однострочном текстовом поле приводит к
перемещению текста из него в список (экземпляр Listbox ).
При двойном клике ( <Double-Button-1> ) по элементу-строке списка,
она должна копироваться в текстовое поле.

"""

import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QListWidget
)


def main():
    app = QApplication(sys.argv)
    window = ListBox()
    window.show()
    sys.exit(app.exec_())


class ListBox(QWidget):
    def __init__(self):
        super().__init__()
        self.list = QListWidget()
        self.line_edit = QLineEdit()

        self.initial_ui()

    def initial_ui(self):
        self.setGeometry(350, 350, 500, 350)
        self.setWindowTitle("Список")

        self.list.itemDoubleClicked.connect(self.copy_text)
        self.line_edit.returnPressed.connect(self.move_text)

        layout = QVBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    def copy_text(self):
        list = self.list.selectedItems()
        if not list:
            return
        for item in list:
            self.line_edit.setText(item.text())

    def move_text(self):
        self.list.addItem(self.line_edit.text())
        self.line_edit.clear()


if __name__ == "__main__":
    main()
