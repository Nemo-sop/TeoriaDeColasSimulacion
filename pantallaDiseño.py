# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantalla.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 280, 178, 16))
        self.label_7.setObjectName("label_7")
        self.duracion = QtWidgets.QLineEdit(self.centralwidget)
        self.duracion.setGeometry(QtCore.QRect(110, 280, 149, 20))
        self.duracion.setObjectName("duracion")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 320, 201, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 350, 221, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(0, 410, 261, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 380, 211, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 470, 121, 16))
        self.label_12.setObjectName("label_12")
        self.bAterrizaje = QtWidgets.QLineEdit(self.centralwidget)
        self.bAterrizaje.setGeometry(QtCore.QRect(420, 339, 139, 24))
        self.bAterrizaje.setObjectName("bAterrizaje")
        self.dsvStd = QtWidgets.QLineEdit(self.centralwidget)
        self.dsvStd.setGeometry(QtCore.QRect(420, 308, 139, 24))
        self.dsvStd.setObjectName("dsvStd")
        self.bDespegue = QtWidgets.QLineEdit(self.centralwidget)
        self.bDespegue.setGeometry(QtCore.QRect(420, 370, 139, 24))
        self.bDespegue.setObjectName("bDespegue")
        self.capMax = QtWidgets.QLineEdit(self.centralwidget)
        self.capMax.setGeometry(QtCore.QRect(170, 470, 139, 24))
        self.capMax.setObjectName("capMax")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(630, 520, 161, 51))
        self.start.setObjectName("start")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 180, 133))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(270, 310, 141, 119))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.media = QtWidgets.QLineEdit(self.layoutWidget1)
        self.media.setObjectName("media")
        self.verticalLayout_3.addWidget(self.media)
        self.aAterrizaje = QtWidgets.QLineEdit(self.layoutWidget1)
        self.aAterrizaje.setObjectName("aAterrizaje")
        self.verticalLayout_3.addWidget(self.aAterrizaje)
        self.aDespegue = QtWidgets.QLineEdit(self.layoutWidget1)
        self.aDespegue.setObjectName("aDespegue")
        self.verticalLayout_3.addWidget(self.aDespegue)
        self.mediaExpo = QtWidgets.QLineEdit(self.layoutWidget1)
        self.mediaExpo.setObjectName("mediaExpo")
        self.verticalLayout_3.addWidget(self.mediaExpo)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(200, 30, 161, 177))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tiempoPrimeraLlegada = QtWidgets.QLineEdit(self.layoutWidget2)
        self.tiempoPrimeraLlegada.setObjectName("tiempoPrimeraLlegada")
        self.verticalLayout_2.addWidget(self.tiempoPrimeraLlegada)
        self.permanencia1 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.permanencia1.setObjectName("permanencia1")
        self.verticalLayout_2.addWidget(self.permanencia1)
        self.permanencia2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.permanencia2.setObjectName("permanencia2")
        self.verticalLayout_2.addWidget(self.permanencia2)
        self.permanencia3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.permanencia3.setObjectName("permanencia3")
        self.verticalLayout_2.addWidget(self.permanencia3)
        self.permanencia4 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.permanencia4.setObjectName("permanencia4")
        self.verticalLayout_2.addWidget(self.permanencia4)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.permanencia5 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.permanencia5.setObjectName("permanencia5")
        self.verticalLayout_4.addWidget(self.permanencia5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Duracion:"))
        self.duracion.setText(_translate("MainWindow", "2000"))
        self.label_8.setText(_translate("MainWindow", "Distribucion normal de estadia:"))
        self.label_9.setText(_translate("MainWindow", "Distribucion uniforme de Aterrizajes:"))
        self.label_10.setText(_translate("MainWindow", "Distribucion exponencial negativa de llegadas:"))
        self.label_11.setText(_translate("MainWindow", "Distribucion uniforme de Despegues:"))
        self.label_12.setText(_translate("MainWindow", "Capacidad Maxima:"))
        self.bAterrizaje.setText(_translate("MainWindow", "5"))
        self.dsvStd.setText(_translate("MainWindow", "20"))
        self.bDespegue.setText(_translate("MainWindow", "7"))
        self.capMax.setText(_translate("MainWindow", "20"))
        self.start.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Tiempo inicial de llegada: "))
        self.label_2.setText(_translate("MainWindow", "Finalizacion de permanencia 1:"))
        self.label_3.setText(_translate("MainWindow", "Finalizacion de permanencia 2:"))
        self.label_4.setText(_translate("MainWindow", "Finalizacion de permanencia 3:"))
        self.label_5.setText(_translate("MainWindow", "Finalizacion de permanencia 4:"))
        self.label_6.setText(_translate("MainWindow", "Finalizacion de permanencia 5:"))
        self.media.setText(_translate("MainWindow", "60"))
        self.aAterrizaje.setText(_translate("MainWindow", "3"))
        self.aDespegue.setText(_translate("MainWindow", "4"))
        self.mediaExpo.setText(_translate("MainWindow", "10"))
        self.tiempoPrimeraLlegada.setText(_translate("MainWindow", "22"))
        self.permanencia1.setText(_translate("MainWindow", "7"))
        self.permanencia2.setText(_translate("MainWindow", "9"))
        self.permanencia3.setText(_translate("MainWindow", "15"))
        self.permanencia4.setText(_translate("MainWindow", "17"))
        self.permanencia5.setText(_translate("MainWindow", "20"))
