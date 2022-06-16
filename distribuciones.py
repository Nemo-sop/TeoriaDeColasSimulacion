import random
import numpy as np


def exponencialNegativa(media):
    return round(-media * np.log(1 - random.random()), 2)


def normal(media, desvEst):
    rnds = [random.random() for i in range(12)]
    return (np.sum(rnds) - 6) * desvEst + media


def uniforme(a, b):
    return a + random.random() * (b - a)


def truncate(values, decs=0):
    """funcion utilizada para truncar nuevaDistr y no trabajar con todos los decimales de python """
    return np.trunc(values * 10 ** decs) / (10 ** decs)

