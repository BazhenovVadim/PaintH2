import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMainWindow, QCheckBox
from paint_design import Ui_MainWindow


class Paint(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Paint()
    ex.show()
    sys.exit(app.exec())