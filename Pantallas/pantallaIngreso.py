# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantallaIngreso.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1324, 400)
        MainWindow.setMinimumSize(QtCore.QSize(1324, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1324, 400))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 222, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 245, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 244, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 222, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 245, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 244, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 222, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 221, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 117, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 245, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 245, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(380, 10, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(28)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 1261, 301))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tiempoPrimeraLlegada = QtWidgets.QLineEdit(self.groupBox)
        self.tiempoPrimeraLlegada.setGeometry(QtCore.QRect(250, 42, 81, 21))
        self.tiempoPrimeraLlegada.setObjectName("tiempoPrimeraLlegada")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(18, 36, 231, 21))
        self.label.setObjectName("label")
        self.permanencia1 = QtWidgets.QLineEdit(self.groupBox)
        self.permanencia1.setGeometry(QtCore.QRect(250, 71, 81, 21))
        self.permanencia1.setObjectName("permanencia1")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(18, 196, 231, 17))
        self.label_6.setObjectName("label_6")
        self.permanencia2 = QtWidgets.QLineEdit(self.groupBox)
        self.permanencia2.setGeometry(QtCore.QRect(250, 100, 81, 21))
        self.permanencia2.setObjectName("permanencia2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 231, 29))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 231, 16))
        self.label_4.setObjectName("label_4")
        self.permanencia5 = QtWidgets.QLineEdit(self.groupBox)
        self.permanencia5.setGeometry(QtCore.QRect(249, 193, 81, 21))
        self.permanencia5.setObjectName("permanencia5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(18, 156, 231, 31))
        self.label_5.setObjectName("label_5")
        self.permanencia4 = QtWidgets.QLineEdit(self.groupBox)
        self.permanencia4.setGeometry(QtCore.QRect(250, 158, 81, 21))
        self.permanencia4.setObjectName("permanencia4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(18, 126, 231, 21))
        self.label_3.setObjectName("label_3")
        self.permanencia3 = QtWidgets.QLineEdit(self.groupBox)
        self.permanencia3.setGeometry(QtCore.QRect(250, 129, 81, 21))
        self.permanencia3.setObjectName("permanencia3")
        self.btnSimular = QtWidgets.QPushButton(self.groupBox)
        self.btnSimular.setGeometry(QtCore.QRect(1100, 250, 111, 41))
        self.btnSimular.setObjectName("btnSimular")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 30, 831, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.dsvStd = QtWidgets.QLineEdit(self.groupBox_2)
        self.dsvStd.setGeometry(QtCore.QRect(680, 60, 81, 24))
        self.dsvStd.setObjectName("dsvStd")
        self.media = QtWidgets.QLineEdit(self.groupBox_2)
        self.media.setGeometry(QtCore.QRect(390, 62, 71, 21))
        self.media.setObjectName("media")
        self.aDespegue = QtWidgets.QLineEdit(self.groupBox_2)
        self.aDespegue.setGeometry(QtCore.QRect(390, 140, 71, 21))
        self.aDespegue.setObjectName("aDespegue")
        self.bDespegue = QtWidgets.QLineEdit(self.groupBox_2)
        self.bDespegue.setGeometry(QtCore.QRect(680, 140, 81, 24))
        self.bDespegue.setObjectName("bDespegue")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(30, 100, 281, 31))
        self.label_9.setObjectName("label_9")
        self.aAterrizaje = QtWidgets.QLineEdit(self.groupBox_2)
        self.aAterrizaje.setGeometry(QtCore.QRect(390, 100, 71, 21))
        self.aAterrizaje.setObjectName("aAterrizaje")
        self.bAterrizaje = QtWidgets.QLineEdit(self.groupBox_2)
        self.bAterrizaje.setGeometry(QtCore.QRect(680, 100, 81, 24))
        self.bAterrizaje.setObjectName("bAterrizaje")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 57, 251, 31))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 30, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(30, 130, 281, 31))
        self.label_11.setObjectName("label_11")
        self.mediaExpo = QtWidgets.QLineEdit(self.groupBox_2)
        self.mediaExpo.setGeometry(QtCore.QRect(520, 180, 81, 21))
        self.mediaExpo.setObjectName("mediaExpo")
        self.duracion = QtWidgets.QLineEdit(self.groupBox_2)
        self.duracion.setGeometry(QtCore.QRect(140, 30, 81, 20))
        self.duracion.setObjectName("duracion")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(30, 180, 261, 20))
        self.label_10.setObjectName("label_10")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(270, 60, 81, 21))
        self.label_22.setObjectName("label_22")
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setGeometry(QtCore.QRect(10, 90, 751, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(20, 120, 751, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(20, 160, 751, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(510, 60, 111, 21))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(340, 100, 51, 21))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(520, 100, 101, 21))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(520, 140, 101, 21))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(340, 140, 51, 21))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(400, 180, 121, 21))
        self.label_28.setObjectName("label_28")
        self.capMax = QtWidgets.QLineEdit(self.groupBox)
        self.capMax.setGeometry(QtCore.QRect(260, 242, 91, 24))
        self.capMax.setObjectName("capMax")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(70, 250, 171, 16))
        self.label_12.setObjectName("label_12")
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setGeometry(QtCore.QRect(430, 260, 181, 21))
        self.label_31.setObjectName("label_31")
        self.txtInicioFilas = QtWidgets.QLineEdit(self.groupBox)
        self.txtInicioFilas.setGeometry(QtCore.QRect(610, 260, 71, 21))
        self.txtInicioFilas.setObjectName("txtInicioFilas")
        self.label_32 = QtWidgets.QLabel(self.groupBox)
        self.label_32.setGeometry(QtCore.QRect(720, 260, 311, 21))
        self.label_32.setObjectName("label_32")
        self.groupBox_2.raise_()
        self.tiempoPrimeraLlegada.raise_()
        self.label.raise_()
        self.permanencia1.raise_()
        self.label_6.raise_()
        self.permanencia2.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.permanencia5.raise_()
        self.label_5.raise_()
        self.permanencia4.raise_()
        self.label_3.raise_()
        self.permanencia3.raise_()
        self.btnSimular.raise_()
        self.capMax.raise_()
        self.label_12.raise_()
        self.label_31.raise_()
        self.txtInicioFilas.raise_()
        self.label_32.raise_()
        self.groupBox.raise_()
        self.label_13.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tiempoPrimeraLlegada, self.permanencia1)
        MainWindow.setTabOrder(self.permanencia1, self.permanencia2)
        MainWindow.setTabOrder(self.permanencia2, self.permanencia3)
        MainWindow.setTabOrder(self.permanencia3, self.permanencia4)
        MainWindow.setTabOrder(self.permanencia4, self.permanencia5)
        MainWindow.setTabOrder(self.permanencia5, self.capMax)
        MainWindow.setTabOrder(self.capMax, self.duracion)
        MainWindow.setTabOrder(self.duracion, self.media)
        MainWindow.setTabOrder(self.media, self.dsvStd)
        MainWindow.setTabOrder(self.dsvStd, self.aAterrizaje)
        MainWindow.setTabOrder(self.aAterrizaje, self.bAterrizaje)
        MainWindow.setTabOrder(self.bAterrizaje, self.aDespegue)
        MainWindow.setTabOrder(self.aDespegue, self.bDespegue)
        MainWindow.setTabOrder(self.bDespegue, self.mediaExpo)
        MainWindow.setTabOrder(self.mediaExpo, self.txtInicioFilas)
        MainWindow.setTabOrder(self.txtInicioFilas, self.btnSimular)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ingreso Datos - Simulaci??n Control de Aviones"))
        self.label_13.setText(_translate("MainWindow", "Simulaci??n Control de Aviones"))
        self.groupBox.setTitle(_translate("MainWindow", "Ingreso Datos"))
        self.tiempoPrimeraLlegada.setText(_translate("MainWindow", "22"))
        self.label.setText(_translate("MainWindow", "Tiempo inicial de llegada: "))
        self.permanencia1.setText(_translate("MainWindow", "7"))
        self.label_6.setText(_translate("MainWindow", "Finalizacion de permanencia 5:"))
        self.permanencia2.setText(_translate("MainWindow", "9"))
        self.label_2.setText(_translate("MainWindow", "Finalizacion de permanencia 1:"))
        self.label_4.setText(_translate("MainWindow", "Finalizacion de permanencia 3:"))
        self.permanencia5.setText(_translate("MainWindow", "20"))
        self.label_5.setText(_translate("MainWindow", "Finalizacion de permanencia 4:"))
        self.permanencia4.setText(_translate("MainWindow", "17"))
        self.label_3.setText(_translate("MainWindow", "Finalizacion de permanencia 2:"))
        self.permanencia3.setText(_translate("MainWindow", "15"))
        self.btnSimular.setText(_translate("MainWindow", "Simular!"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Distribuciones"))
        self.dsvStd.setText(_translate("MainWindow", "20"))
        self.media.setText(_translate("MainWindow", "60"))
        self.aDespegue.setText(_translate("MainWindow", "4"))
        self.bDespegue.setText(_translate("MainWindow", "7"))
        self.label_9.setText(_translate("MainWindow", "Distribucion uniforme de Aterrizajes:"))
        self.aAterrizaje.setText(_translate("MainWindow", "3"))
        self.bAterrizaje.setText(_translate("MainWindow", "5"))
        self.label_8.setText(_translate("MainWindow", "Distribucion normal de estadia:"))
        self.label_7.setText(_translate("MainWindow", "Duracion:"))
        self.label_11.setText(_translate("MainWindow", "Distribucion uniforme de Despegues:"))
        self.mediaExpo.setText(_translate("MainWindow", "10"))
        self.duracion.setText(_translate("MainWindow", "1000"))
        self.label_10.setText(_translate("MainWindow", "Distribucion exponencial negativa de llegadas:"))
        self.label_22.setText(_translate("MainWindow", "Media:"))
        self.label_23.setText(_translate("MainWindow", "Desviaci??n:"))
        self.label_24.setText(_translate("MainWindow", "a:"))
        self.label_25.setText(_translate("MainWindow", "b:"))
        self.label_26.setText(_translate("MainWindow", "b:"))
        self.label_27.setText(_translate("MainWindow", "a:"))
        self.label_28.setText(_translate("MainWindow", "Media:"))
        self.capMax.setText(_translate("MainWindow", "20"))
        self.label_12.setText(_translate("MainWindow", "Capacidad Maxima:"))
        self.label_31.setText(_translate("MainWindow", "Mostrar desde la fila..."))
        self.txtInicioFilas.setText(_translate("MainWindow", "0"))
        self.label_32.setText(_translate("MainWindow", "Las 400 l??neas despu??s"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
