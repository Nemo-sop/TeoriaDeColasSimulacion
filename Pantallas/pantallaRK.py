# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantallaRK.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1867, 773)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 773))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 9999999))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(670, 10, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(28)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 70, 901, 671))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tblLlegadaAtaque = QtWidgets.QTableWidget(self.groupBox)
        self.tblLlegadaAtaque.setGeometry(QtCore.QRect(20, 90, 861, 551))
        self.tblLlegadaAtaque.setObjectName("tblLlegadaAtaque")
        self.tblLlegadaAtaque.setColumnCount(8)
        self.tblLlegadaAtaque.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblLlegadaAtaque.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblLlegadaAtaque.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblLlegadaAtaque.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblLlegadaAtaque.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblLlegadaAtaque.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblLlegadaAtaque.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblLlegadaAtaque.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblLlegadaAtaque.setHorizontalHeaderItem(7, item)
        self.txtA = QtWidgets.QLineEdit(self.groupBox)
        self.txtA.setGeometry(QtCore.QRect(20, 50, 139, 24))
        self.txtA.setText("")
        self.txtA.setReadOnly(True)
        self.txtA.setObjectName("txtA")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(940, 70, 901, 341))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tblDuracionBloqueo = QtWidgets.QTableWidget(self.groupBox_2)
        self.tblDuracionBloqueo.setGeometry(QtCore.QRect(20, 30, 861, 281))
        self.tblDuracionBloqueo.setObjectName("tblDuracionBloqueo")
        self.tblDuracionBloqueo.setColumnCount(8)
        self.tblDuracionBloqueo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionBloqueo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionBloqueo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionBloqueo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionBloqueo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionBloqueo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionBloqueo.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionBloqueo.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionBloqueo.setHorizontalHeaderItem(7, item)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(940, 420, 901, 321))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.tblDuracionAtaqueServ = QtWidgets.QTableWidget(self.groupBox_3)
        self.tblDuracionAtaqueServ.setGeometry(QtCore.QRect(20, 30, 861, 271))
        self.tblDuracionAtaqueServ.setObjectName("tblDuracionAtaqueServ")
        self.tblDuracionAtaqueServ.setColumnCount(8)
        self.tblDuracionAtaqueServ.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionAtaqueServ.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionAtaqueServ.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionAtaqueServ.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionAtaqueServ.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionAtaqueServ.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionAtaqueServ.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionAtaqueServ.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDuracionAtaqueServ.setHorizontalHeaderItem(7, item)
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.label_13.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Muestra del Runge Kutta - Simulaci??n Control de Aviones"))
        self.label_13.setText(_translate("MainWindow", "Runge Kuttas Caluculados"))
        self.groupBox.setTitle(_translate("MainWindow", "C??lculo Pr??ximo Bloqueo"))
        item = self.tblLlegadaAtaque.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "t"))
        item = self.tblLlegadaAtaque.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "A"))
        item = self.tblLlegadaAtaque.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "K1"))
        item = self.tblLlegadaAtaque.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "K2"))
        item = self.tblLlegadaAtaque.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "K3"))
        item = self.tblLlegadaAtaque.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "K4"))
        item = self.tblLlegadaAtaque.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "t(i + 1)"))
        item = self.tblLlegadaAtaque.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "A(i + 1)"))
        self.label_14.setText(_translate("MainWindow", "A (Tiempo de las primeras 30 llegadas)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "C??lculo Duraci??n Ataque Servidor"))
        item = self.tblDuracionBloqueo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "t"))
        item = self.tblDuracionBloqueo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "A"))
        item = self.tblDuracionBloqueo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "K1"))
        item = self.tblDuracionBloqueo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "K2"))
        item = self.tblDuracionBloqueo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "K3"))
        item = self.tblDuracionBloqueo.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "K4"))
        item = self.tblDuracionBloqueo.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "t(i + 1)"))
        item = self.tblDuracionBloqueo.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "A(i + 1)"))
        self.groupBox_3.setTitle(_translate("MainWindow", "C??lculo Duraci??n Ataque Llegadas"))
        item = self.tblDuracionAtaqueServ.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "t"))
        item = self.tblDuracionAtaqueServ.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "A"))
        item = self.tblDuracionAtaqueServ.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "K1"))
        item = self.tblDuracionAtaqueServ.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "K2"))
        item = self.tblDuracionAtaqueServ.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "K3"))
        item = self.tblDuracionAtaqueServ.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "K4"))
        item = self.tblDuracionAtaqueServ.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "t(i + 1)"))
        item = self.tblDuracionAtaqueServ.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "A(i + 1)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
