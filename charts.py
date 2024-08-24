from interface import Ui_MainWindow
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCharts

class ChartyApp(QMainWindow, Ui_MainWindow):
    def ___init__(self):
        super().__init__()
        