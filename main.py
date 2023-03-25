import sys
from PyQt5.QtWidgets import QApplication
# Импорт главного окна из папки windows по следующему принципу:
# from папка.файл import класс/функция/переменная/почтичтоугодно
from windows.menu import MenuWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu_window = MenuWindow()
    sys.exit(app.exec_())