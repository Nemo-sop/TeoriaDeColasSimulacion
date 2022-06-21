from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from Pantallas import LogicaPantallaResultados
from main import *


class PantallaIngreso(QMainWindow):
    """Incializar clase"""

    def __init__(self):
        super().__init__()

        """Cargar la GUI"""
        uic.loadUi("Pantallas/pantallaIngreso.ui", self)

        self.btnSimular.clicked.connect(self.metodoAuxiliar)

    def metodoAuxiliar(self):

        if self.duracion.text() != "":
            principal(self,
                      [int(self.tiempoPrimeraLlegada.text()), int(self.permanencia1.text()),
                       int(self.permanencia2.text()),
                       int(self.permanencia3.text()), int(self.permanencia4.text()), int(self.permanencia5.text())],
                      int(self.duracion.text()),
                      [float(self.media.text()), float(self.dsvStd.text())],
                      [float(self.aAterrizaje.text()), float(self.bAterrizaje.text())],
                      [float(self.aDespegue.text()), float(self.bDespegue.text())],
                      float(self.mediaExpo.text()),
                      int(self.capMax.text()),
                      int(self.txtInicioFilas.text()))

    def mostrarResultados(self, datos, estadisticas, inicio, RungeKuttas):
        self.pantallaResultados = LogicaPantallaResultados.PantallaResultados()
        self.pantallaResultados.mostrarResultados(datos, estadisticas, inicio, RungeKuttas)
        self.pantallaResultados.show()
