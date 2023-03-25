from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

# Импорт окон для машин из папки windows и соответствующих им файлов
from windows.lambo import LamboWindow
from windows.volks import volksWindow

# Основное окно
class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Заголовок и размер окна
        self.setWindowTitle('./windows/menu.py')
        self.setFixedSize(400, 200)

        self.lambo_button = QPushButton('Lamborghini', self)
        self.lambo_button.clicked.connect(self.show_lambo)

        self.volks_button = QPushButton('Volkswagen', self)
        self.volks_button.clicked.connect(self.show_volks)

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.lambo_button)
        layout.addWidget(self.volks_button)
        layout.addWidget(self.exit_button)
        self.setLayout(layout)

        self.show()

    # Функция открытия окна с Ламборгини
    def show_lambo(self):
        
        self.lambo_window = LamboWindow()
        self.lambo_window.show()
        self.hide()

    # Функция открытия окна с Фольксваген
    def show_volks(self):
        self.volks_window = volksWindow()
        self.volks_window.show()
        self.hide()