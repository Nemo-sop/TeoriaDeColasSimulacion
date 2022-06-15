import math
from random import random

import distribuciones


class Controlador():
    def __init__(self):
        super().__init__()

    def calcularRKMomentoAtaque(self, tiempo80Llegadas):
        " Ecuación diferencial: DA/dt = B * A"
        valorBeta = distribuciones.uniforme(0, 1)
        ecDif = lambda t, A: valorBeta * A
        valor = self.rungeKuttaMomentoAtaque(ecDif, 0, tiempo80Llegadas, tiempo80Llegadas)
        valorReal = valor * 9
        return valorReal

    def tomarA(self, tiempo80Llegadas):
        self.calcularRKMomentoAtaque(tiempo80Llegadas)

    def calcularRKDuracionBloqueo(self, reloj):
        # lambda x,y:
        ecDif = lambda t, L: - (L / (0.8 * (t**2))) - L
        valor = self.rungeKuttaDuracionBloqueo(ecDif, 0, reloj)
        valorReal = valor * 5
        return valorReal

    def calcularRKDuracionAtaqueServidores(self, reloj):
        # lambda x,y:
        ecDif = lambda t, S: (0.2 * S) + 3 - t
        valor = self.rungeKuttaDuracionAtaqueServidores(ecDif, 0, reloj)
        valorReal = valor * 2
        return valorReal

    def rungeKuttaDuracionAtaqueServidores(self, fun, xi, yi, ):
        h = 0.01
        reloj = yi
        while yi > (reloj * 1.35):
            k1 = fun(xi, yi)
            k2 = fun(xi + h / 2, yi + h / 2 * k1)
            k3 = fun(xi + h / 2, yi + h / 2 * k2)
            k4 = fun(xi + h, yi + h * k3)

            yi = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            xi += h

        return xi

    def rungeKuttaDuracionBloqueo(self, fun, xi, yi):
        h = 0.01
        yj = 1
        while (yj - yi) < 1:
            k1 = fun(xi, yi)
            k2 = fun(xi + h / 2, yi + h / 2 * k1)
            k3 = fun(xi + h / 2, yi + h / 2 * k2)
            k4 = fun(xi + h, yi + h * k3)

            yj = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            xi += h

        return xi

    def rungeKuttaMomentoAtaque(self, fun, xi, yi, tiempo80Llegadas):
        h = 0.01
        while yi < (tiempo80Llegadas*2):
            k1 = fun(xi, yi)
            k2 = fun(xi + h / 2, yi + h / 2 * k1)
            k3 = fun(xi + h / 2, yi + h / 2 * k2)
            k4 = fun(xi + h, yi + h * k3)

            yi = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            xi += h

        return xi
