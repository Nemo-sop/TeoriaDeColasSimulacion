import numpy as np
import pandas as pd

from Clases import *
import random
import time
"""
parametros = [
    proxima_llegada,
    [(finalizacion de permanencia de los aviones q estan)],
    tiempo_total_simulacion,
    capacidad_maxima_tierra, 
    media_distribucion_llegada,
    [a_despegue, b_despegue],
    [a_aterrizaje, b_aterrizaje],
    [media_operacion, dvstd_operacion]
]
"""
def exponencialNegativa(media):
    return -media * np.log(1 - random.random())


def normal(media, desvEst):
    rnds = [random.random() for i in range(12)]
    return (np.sum(rnds)-6) * desvEst + media

def uniforme(a,b):
    return a + random.random() * (b - a)

def simular(proxima_llegada, permanencia_inicial, tiempo_total_simulacion, capacidad_maxima_tierra, media_distribucion_llegada, uniforme_despegue, uniforme_aterrizaje, normal_operacion):
    permanencia_inicial = [7, 9, 15, 17, 20]
    uniforme_despegue = [4,7]
    uniforme_aterrizaje = [3,5]
    normal_operacion = [60, 20]


    # reloj = 0
    # proximos_eventos = {"llegda":[],"salida":[]}
    # while reloj <= tiempo_total_simulacion:
    #     evento = min(proximos_eventos)
    #     actualizar(evento,)
    #

    tabla = pd.DataFrame(
        {"Evento": [],
         "Reloj": [],
         "LA_RND": [],
         "LA_tiempo_entre_llegada": [],
         "LA_proxima_llegada": [],
         "FA_RND": [],
         "FA_tiempo_aterrizaje": [],
         "FA_finalizacion_aterrizaje": [],
         "FO_RND": [],
         "FO_tiempo operacion": [],
         "FO_finalizacion_operacion": [],
         "SA_rnd":[],
         "SA_tiempo_despegue": [],
         "SA_finalizacion_despegue": [],
         "Estado pista":[],
         "cola aire": [],
         "cola tierra": [],
         "cant naves_en_tierra":[],
         "naves"
         "naves_salientes":[]
         })