#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
напишите программу, состоящую из двух списков Listbox.
В первом будет,например, перечень товаров, заданный программно.
Второй изначально пуст, пусть это будет перечень покупок.
При клике на одну кнопку товар должен переходить из одного списка в другой.
При клике на вторую кнопку – возвращаться (человек передумал покупать).
Предусмотрите возможность множественного
выбора элементов списка и их перемещения.

"""


from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QAbstractItemView,
)
import sys


def main():
    app = QApplication(sys.argv)
    window = ListBox()
    window.show()
    sys.exit(app.exec_())


class ListBox(QWidget):
    def __init__(self):
        super().__init__()
        self.list_left = QListWidget()
        self.list_right = QListWidget()
        self.products = ["Кошачий корм", "Хлеб", "Молоко", "Соль"]
        self.button_to_right = QPushButton(">>>")
        self.button_to_left = QPushButton("<<<")

        self.initial_ui()

    def initial_ui(self):
        self.setGeometry(350, 350, 500, 350)
        self.setWindowTitle("Список покупок")

        horizontal_box = QHBoxLayout()
        vertikal_box = QVBoxLayout()
        vertikal_box.addWidget(self.button_to_right)
        vertikal_box.addWidget(self.button_to_left)
        horizontal_box.addWidget(self.list_left)
        horizontal_box.addWidget(self.list_right)
        horizontal_box.addLayout(vertikal_box)
        self.setLayout(horizontal_box)

        self.list_left.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_left.addItems(self.products)
        self.list_right.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.button_to_right.clicked.connect(self.move_item_to_right)
        self.button_to_left.clicked.connect(self.move_item_to_left)

    def move_item_to_right(self):
        print("1")
        list_for_grabing = self.list_left.selectedItems()
        for item in list_for_grabing:
            self.list_left.takeItem(self.list_left.row(item))
            self.list_right.addItem(item)

    def move_item_to_left(self):
        print("2")
        list_for_grabing = self.list_right.selectedItems()
        for item in list_for_grabing:
            self.list_right.takeItem(self.list_right.row(item))
            self.list_left.addItem(item)


if __name__ == "__main__":
    main()
