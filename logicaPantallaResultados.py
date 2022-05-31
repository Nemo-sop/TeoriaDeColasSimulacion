from PyQt5 import uic
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem


class PantallaResultados(QMainWindow):
    """Inicializar Clase"""

    def __init__(self, _datosPrincipales):
        super().__init__()
        self.DatosPrincipales = _datosPrincipales

        """Cargar GUI"""
        uic.loadUi("pantallaResultados.ui", self)

        self.cargarTabla(self.DatosPrincipales)

    def cargarTabla(self, datos):
        fila = 0

        cantFilas = len(datos)
        self.tablaResultados.setRowCount(cantFilas)

        """df = pd.DataFrame({"clk": [], "tipo": []
                          , "avion": [],"tiempo hasta la prox llegada":[],"prox llegada": [],
                          "proximo avion que sale":[]  ,"estado pista":[],"usada por":[],"porcentaje ocupacion":[],
                         "llegadas": [], "aterrizajes": [], "salidas": [],"derivados":[],
                         "cola aire": [], "cola tierra": [],"aviones en tierra":[]},dtype=object)"""

        for i in range(cantFilas):
            self.tablaResultados.setItem(fila, 0, QTableWidgetItem(str(datos.at[i, "clk"])))
            self.tablaResultados.setItem(fila, 1, QTableWidgetItem(str(datos.at[i, "tipo"])))
            self.tablaResultados.setItem(fila, 2, QTableWidgetItem(str(datos.at[i, "avion"])))
            self.tablaResultados.setItem(fila, 3, QTableWidgetItem(str(datos.at[i, "tiempo hasta la prox llegada"])))
            self.tablaResultados.setItem(fila, 4, QTableWidgetItem(str(datos.at[i, "prox llegada"])))
            self.tablaResultados.setItem(fila, 5, QTableWidgetItem(str(datos.at[i, "proximo avion que sale"])))
            self.tablaResultados.setItem(fila, 6, QTableWidgetItem(str(datos.at[i, "estado pista"])))
            self.tablaResultados.setItem(fila, 7, QTableWidgetItem(str(datos.at[i, "usada por"])))
            self.tablaResultados.setItem(fila, 8, QTableWidgetItem(str(datos.at[i, "porcentaje ocupacion"])))
            self.tablaResultados.setItem(fila, 9, QTableWidgetItem(str(datos.at[i, "llegadas"])))
            self.tablaResultados.setItem(fila, 10, QTableWidgetItem(str(datos.at[i, "aterrizajes"])))
            self.tablaResultados.setItem(fila, 11, QTableWidgetItem(str(datos.at[i, "salidas"])))
            self.tablaResultados.setItem(fila, 12, QTableWidgetItem(str(datos.at[i, "derivados"])))
            self.tablaResultados.setItem(fila, 13, QTableWidgetItem(str(datos.at[i, "cola aire"])))
            self.tablaResultados.setItem(fila, 14, QTableWidgetItem(str(datos.at[i, "cola tierra"])))
            self.tablaResultados.setItem(fila, 15, QTableWidgetItem(str(datos.at[i, "aviones en tierra"])))

            fila = fila +1
