# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantallaResultados.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PantallaResultados(object):
    def setupUi(self, PantallaResultados):
        PantallaResultados.setObjectName("PantallaResultados")
        PantallaResultados.resize(1447, 557)
        self.centralwidget = QtWidgets.QWidget(PantallaResultados)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 30, 661, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tablaResultados = QtWidgets.QTableWidget(self.centralwidget)
        self.tablaResultados.setGeometry(QtCore.QRect(20, 140, 1421, 192))
        self.tablaResultados.setObjectName("tablaResultados")
        self.tablaResultados.setColumnCount(16)
        self.tablaResultados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(15, item)
        PantallaResultados.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PantallaResultados)
        self.statusbar.setObjectName("statusbar")
        PantallaResultados.setStatusBar(self.statusbar)

        self.retranslateUi(PantallaResultados)
        QtCore.QMetaObject.connectSlotsByName(PantallaResultados)

    def retranslateUi(self, PantallaResultados):
        _translate = QtCore.QCoreApplication.translate
        PantallaResultados.setWindowTitle(_translate("PantallaResultados", "MainWindow"))
        self.label.setText(_translate("PantallaResultados", "Resultado Simulación: Aviones"))
        item = self.tablaResultados.horizontalHeaderItem(0)
        item.setText(_translate("PantallaResultados", "Reloj"))
        item = self.tablaResultados.horizontalHeaderItem(1)
        item.setText(_translate("PantallaResultados", "Cola Tierra"))
        item = self.tablaResultados.horizontalHeaderItem(2)
        item.setText(_translate("PantallaResultados", "Avion"))
        item = self.tablaResultados.horizontalHeaderItem(3)
        item.setText(_translate("PantallaResultados", "Tiempo Hasta Prox. Llegada"))
        item = self.tablaResultados.horizontalHeaderItem(4)
        item.setText(_translate("PantallaResultados", "Prox. Llegada"))
        item = self.tablaResultados.horizontalHeaderItem(5)
        item.setText(_translate("PantallaResultados", "Proximo Avion Sale"))
        item = self.tablaResultados.horizontalHeaderItem(6)
        item.setText(_translate("PantallaResultados", "Estado Pista"))
        item = self.tablaResultados.horizontalHeaderItem(7)
        item.setText(_translate("PantallaResultados", "Usada Por"))
        item = self.tablaResultados.horizontalHeaderItem(8)
        item.setText(_translate("PantallaResultados", "Porcentaje Ocup."))
        item = self.tablaResultados.horizontalHeaderItem(9)
        item.setText(_translate("PantallaResultados", "Llegadas"))
        item = self.tablaResultados.horizontalHeaderItem(10)
        item.setText(_translate("PantallaResultados", "Aterrizajes"))
        item = self.tablaResultados.horizontalHeaderItem(11)
        item.setText(_translate("PantallaResultados", "Salidas"))
        item = self.tablaResultados.horizontalHeaderItem(12)
        item.setText(_translate("PantallaResultados", "Derivados"))
        item = self.tablaResultados.horizontalHeaderItem(13)
        item.setText(_translate("PantallaResultados", "Cola Aire"))
        item = self.tablaResultados.horizontalHeaderItem(14)
        item.setText(_translate("PantallaResultados", "Cola Tierra"))
        item = self.tablaResultados.horizontalHeaderItem(15)
        item.setText(_translate("PantallaResultados", "Aviones en Tierra"))