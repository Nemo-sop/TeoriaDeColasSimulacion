import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from main import *
import distribuciones as d


class PantallaIngreso(QMainWindow):
    """Incializar clase"""

    def __init__(self):
        super().__init__()

        """Cargar la GUI"""
        uic.loadUi("pantalla.ui", self)

        self.start.clicked.connect(self.metodoAuxiliar)

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
                      int(self.txInicioFilas.text()))

    def cargarResultados(self, datos, estadisticas):
        self.cargarTabla(datos)
        self.cargarEstadisticas(estadisticas)

    def cargarTabla(self, datos):
        fila = 0
        inicio = int(self.txInicioFilas.text())

        cantFilas = len(datos)
        self.tablaResultados.setRowCount(401)

        if cantFilas < 400:
            final = cantFilas
        else:
            final = 400+inicio

        for i in range(inicio, final):
            self.tablaResultados.setItem(fila, 0, QTableWidgetItem(str(distribuciones.truncate(datos.at[i, "clk"], 4))))
            self.tablaResultados.setItem(fila, 1, QTableWidgetItem(str(datos.at[i, "tipo"])))
            self.tablaResultados.setItem(fila, 2, QTableWidgetItem(str(datos.at[i, "avion"])))
            self.tablaResultados.setItem(fila, 3, QTableWidgetItem(str(distribuciones.truncate(
                datos.at[i, "tiempo hasta la prox llegada"], 4))))
            self.tablaResultados.setItem(fila, 4, QTableWidgetItem(str(datos.at[i, "prox llegada"])))
            self.tablaResultados.setItem(fila, 5, QTableWidgetItem(str(datos.at[i, "proximo avion que sale"])))
            self.tablaResultados.setItem(fila, 6, QTableWidgetItem(str(datos.at[i, "estado pista"])))
            self.tablaResultados.setItem(fila, 7, QTableWidgetItem(str(datos.at[i, "usada por"])))
            self.tablaResultados.setItem(fila, 8, QTableWidgetItem(str(distribuciones.truncate(
                datos.at[i, "porcentaje ocupacion"], 4))))
            self.tablaResultados.setItem(fila, 9, QTableWidgetItem(str(datos.at[i, "llegadas"])))
            self.tablaResultados.setItem(fila, 10, QTableWidgetItem(str(datos.at[i, "aterrizajes"])))
            self.tablaResultados.setItem(fila, 11, QTableWidgetItem(str(datos.at[i, "salidas"])))
            self.tablaResultados.setItem(fila, 12, QTableWidgetItem(str(datos.at[i, "derivados"])))
            self.tablaResultados.setItem(fila, 13, QTableWidgetItem(str(datos.at[i, "cola aire"])))
            self.tablaResultados.setItem(fila, 14, QTableWidgetItem(str(datos.at[i, "cola tierra"])))
            self.tablaResultados.setItem(fila, 15, QTableWidgetItem(str(datos.at[i, "aviones en tierra"])))

            fila = fila + 1

        if not (cantFilas < 400):

            self.tablaResultados.setItem(fila, 0, QTableWidgetItem(str(distribuciones.truncate(datos.at[(cantFilas-1), "clk"], 4))))
            self.tablaResultados.setItem(fila, 1, QTableWidgetItem(str(datos.at[(cantFilas-1), "tipo"])))
            self.tablaResultados.setItem(fila, 2, QTableWidgetItem(str(datos.at[(cantFilas-1), "avion"])))
            self.tablaResultados.setItem(fila, 3, QTableWidgetItem(str(distribuciones.truncate(
                datos.at[(cantFilas-1), "tiempo hasta la prox llegada"], 4))))
            self.tablaResultados.setItem(fila, 4, QTableWidgetItem(str(datos.at[(cantFilas-1), "prox llegada"])))
            self.tablaResultados.setItem(fila, 5, QTableWidgetItem(str(datos.at[(cantFilas-1), "proximo avion que sale"])))
            self.tablaResultados.setItem(fila, 6, QTableWidgetItem(str(datos.at[(cantFilas-1), "estado pista"])))
            self.tablaResultados.setItem(fila, 7, QTableWidgetItem(str(datos.at[(cantFilas-1), "usada por"])))
            self.tablaResultados.setItem(fila, 8, QTableWidgetItem(str(distribuciones.truncate(
                datos.at[(cantFilas-1), "porcentaje ocupacion"], 4))))
            self.tablaResultados.setItem(fila, 9, QTableWidgetItem(str(datos.at[(cantFilas-1), "llegadas"])))
            self.tablaResultados.setItem(fila, 10, QTableWidgetItem(str(datos.at[(cantFilas-1), "aterrizajes"])))
            self.tablaResultados.setItem(fila, 11, QTableWidgetItem(str(datos.at[(cantFilas-1), "salidas"])))
            self.tablaResultados.setItem(fila, 12, QTableWidgetItem(str(datos.at[(cantFilas-1), "derivados"])))
            self.tablaResultados.setItem(fila, 13, QTableWidgetItem(str(datos.at[(cantFilas-1), "cola aire"])))
            self.tablaResultados.setItem(fila, 14, QTableWidgetItem(str(datos.at[(cantFilas-1), "cola tierra"])))
            self.tablaResultados.setItem(fila, 15, QTableWidgetItem(str(datos.at[(cantFilas-1), "aviones en tierra"])))

    def cargarEstadisticas(self, estadisticas):
        self.txtTiempoPromedioPermSistema.setText(str(d.truncate(estadisticas[0], 4)))
        self.txtPorcPromedioPermTierra.setText(str(d.truncate(estadisticas[1], 4)))
        self.txtPorcOcupacionPista.setText(str(d.truncate(estadisticas[2], 4)))

        self.txtTiempoPistaLibre.setText(str(d.truncate(estadisticas[3], 4)))
        self.txtCaudalSalida.setText(str(d.truncate(estadisticas[4], 4)))

        self.txtCantAvionesDerivados.setText(str(d.truncate(estadisticas[6], 4)))
        self.txtCantAvionesLlegaron.setText(str(d.truncate(estadisticas[7], 4)))
        self.txtCantAvionesAterriz.setText(str(d.truncate(estadisticas[8], 4)))
