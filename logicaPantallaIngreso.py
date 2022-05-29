import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class PantallaIngreso(QMainWindow):
    """Incializar clase"""

    def __init__(self):
        super().__init__()

        """Cargar la GUI"""
        uic.loadUi("pantallaIngreso.ui", self)
