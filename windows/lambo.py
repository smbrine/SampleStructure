from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import json


class LamboWindow(QWidget):
    def __init__(self):
        super().__init__()

        with open('./data/cars.json', 'r') as file:
            cars = json.load(file)

        self.setWindowTitle('./windows/lambo.py')
        self.setFixedSize(400, 300)

        # Обращение к словарю по принципу словарь[ключ][ключ]
        self.image_label = QLabel(self)
        pixmap = QPixmap(cars['lambo']['image']).scaled(self.width(), self.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)

        self.speed_label = QLabel('Speed: ' + cars['lambo']['speed'], self)
        self.accel_label = QLabel('Acceleration: ' + cars['lambo']['accel'], self)

        self.back_button = QPushButton('Back', self)
        self.back_button.clicked.connect(self.show_menu)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.accel_label)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

    def show_menu(self):
        from windows.menu import MenuWindow
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.hide()