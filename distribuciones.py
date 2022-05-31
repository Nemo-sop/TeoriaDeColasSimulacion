import random
import numpy as np


def exponencialNegativa(media):
    return round(-media * np.log(1 - random.random()),2)


def normal(media, desvEst):
    rnds = [random.random() for i in range(12)]
    return (np.sum(rnds)-6) * desvEst + media

def uniforme(a,b):
    return a + random.random() * (b - a)