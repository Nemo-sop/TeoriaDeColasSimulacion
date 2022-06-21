import random

import pandas as pd


def calculo_RK():
    return 24

class Controlador():
    def __init__(self, tiempo):
        super().__init__()
        self.__tiempo30llegada = tiempo

    def get_tiempo30llegada(self):
        return self.__tiempo30llegada

    def set_tiempo30llegada(self, tiempo):
        self.__tiempo30llegada = tiempo

    def calcularRKMomentoAtaque(self):
        " Ecuación diferencial: DA/dt = B * A"
        tiempo30llegada = self.get_tiempo30llegada()
        #valorBeta = distribuciones.uniforme(0, 1)
        ecDif = lambda t, A: random.random() * A
        valor, dfDuracionMomentoAtque = self.rungeKuttaMomentoAtaque(ecDif, 0, tiempo30llegada, tiempo30llegada)
        valorReal = valor * 9
        return valorReal, dfDuracionMomentoAtque


    def rungeKuttaMomentoAtaque(self, fun, xi, yi, tiempo30Llegadas):
        dfDuracionMomentoAtque = pd.DataFrame({"xi":[], "yi":[], "k1":[], "k2":[], "k3":[], "k4":[], "xi+1":[], "yi+1":[]})
        h = 0.01
        while yi < (tiempo30Llegadas*2):
            fila = pd.DataFrame({"xi": [], "yi": [], "k1": [], "k2": [], "k3": [], "k4": [], "xi+1": [], "yi+1": []})

            k1 = fun(xi, yi)
            k2 = fun(xi + h / 2, yi + h / 2 * k1)
            k3 = fun(xi + h / 2, yi + h / 2 * k2)
            k4 = fun(xi + h, yi + h * k3)

            fila.at[0, "xi"] = xi
            fila.at[0, "yi"] = yi

            yi = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            xi += h

            fila.at[0, "k1"] = k1
            fila.at[0, "k2"] = k2
            fila.at[0, "k3"] = k3
            fila.at[0, "k4"] = k4
            fila.at[0, "xi+1"] = xi
            fila.at[0, "yi+1"] = yi

            dfDuracionMomentoAtque = pd.concat([dfDuracionMomentoAtque, fila], ignore_index=True)

        return xi, dfDuracionMomentoAtque


    def calcularRKDuracionBloqueo(self, reloj):
        # lambda x,y:
        ecDif = lambda t, L: -(L / 0.8) * (t**2) - L
        valor, dfDuracionBloqueo = self.rungeKuttaDuracionBloqueo(ecDif, 0, reloj)
        valorReal = valor * 5

        return valorReal, dfDuracionBloqueo

    def rungeKuttaDuracionBloqueo(self, fun, xi, yi):

        dfDuracionBloqueo = pd.DataFrame({"xi":[], "yi":[], "k1":[], "k2":[], "k3":[], "k4":[], "xi+1":[], "yi+1":[]})

        h = 0.1

        yAnterior = yi
        unaMasFlaco = False

        while True:#abs(yAnterior - yi) < 1:
            yAnterior = yi
            fila = pd.DataFrame({"xi": [], "yi": [], "k1": [], "k2": [], "k3": [], "k4": [], "xi+1": [], "yi+1": []})

            k1 = fun(xi, yi)
            k2 = fun(xi + h / 2, yi + h / 2 * k1)
            k3 = fun(xi + h / 2, yi + h / 2 * k2)
            k4 = fun(xi + h, yi + h * k3)


            yi = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

            fila.at[0, "xi"] = xi
            fila.at[0, "yi"] = yAnterior
            #print(xi, yi, yAnterior)
            xi += h

            fila.at[0, "k1"] = k1
            fila.at[0, "k2"] = k2
            fila.at[0, "k3"] = k3
            fila.at[0, "k4"] = k4
            fila.at[0, "xi+1"] = xi
            fila.at[0, "yi+1"] = yi

            dfDuracionBloqueo = pd.concat([dfDuracionBloqueo, fila], ignore_index=True)


            if unaMasFlaco:
                return xi, dfDuracionBloqueo

            if abs(yAnterior - yi) < 1:
                unaMasFlaco = True



        #print("terminado")
        return xi, dfDuracionBloqueo


    def calcularRKDuracionAtaqueServidores(self, reloj):
        # lambda x,y:
        ecDif = lambda t, S: (0.2 * S) + 3 - t
        valor, dfDuracionAtaqueServidores = self.rungeKuttaDuracionAtaqueServidores(ecDif, 0, reloj, reloj)
        valorReal = valor * 2
        return valorReal, dfDuracionAtaqueServidores

    def rungeKuttaDuracionAtaqueServidores(self, fun, xi, yi, reloj):
        dfDuracionAtaqueServidores = pd.DataFrame({"xi":[], "yi":[], "k1":[], "k2":[], "k3":[], "k4":[], "xi+1":[], "yi+1":[]})

        h = 0.01
        reloj = yi
        objetivoEncontrado = False
        unaMasFlaco = False
        while True:#yi < (reloj * 1.35):
            fila = pd.DataFrame({"xi": [], "yi": [], "k1": [], "k2": [], "k3": [], "k4": [], "xi+1": [], "yi+1": []})

            k1 = fun(xi, yi)
            k2 = fun(xi + h / 2, yi + h / 2 * k1)
            k3 = fun(xi + h / 2, yi + h / 2 * k2)
            k4 = fun(xi + h, yi + h * k3)

            fila.at[0, "xi"] = xi
            fila.at[0, "yi"] = yi

            yi = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            xi += h

            fila.at[0, "k1"] = k1
            fila.at[0, "k2"] = k2
            fila.at[0, "k3"] = k3
            fila.at[0, "k4"] = k4
            fila.at[0, "xi+1"] = xi
            fila.at[0, "yi+1"] = yi
            #print(xi, yi, reloj)

            if yi >= reloj*1.35 and not objetivoEncontrado:
                objetivo = yi*1.35
                objetivoEncontrado = True



            dfDuracionAtaqueServidores = pd.concat([dfDuracionAtaqueServidores, fila], ignore_index=True)

            if unaMasFlaco:
                return round(xi, 4), dfDuracionAtaqueServidores

            if objetivoEncontrado and yi >= objetivo:
                unaMasFlaco = True




# prueba = Controlador()
# prueba.set_tiempo30llegada(250)
#
# for i in range(22, 23):
#     tiempo, df =prueba.calcularRKDuracionAtaqueServidores(86)
#     print(tiempo)
#     print(df)
#     tiempo, df = prueba.calcularRKDuracionBloqueo(86)
#     print(tiempo)




