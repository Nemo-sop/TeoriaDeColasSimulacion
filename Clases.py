class Avion():
    def __init__(self, estado, tiempo_llegada, tiempo_espera_aire, tiempo_espera_tierra):
        self.__estado = estado
        self.__tiempo_llegada = tiempo_llegada
        self.__tiempo_espera_aire = tiempo_espera_aire
        self.__tiempo_espera_tierra = tiempo_espera_tierra

class Pista():
    def __init__(self, estado, cola_aire, cola_tierra):
        self.__estado = estado
        self.__cola_aire = cola_aire
        self.__cola_tierra = cola_tierra
        