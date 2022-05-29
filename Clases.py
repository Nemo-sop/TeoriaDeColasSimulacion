
# todo usamos un archivo por clase?

class Avion:
    def __init__(self, estado, tiempo_llegada, tiempo_espera_aire, tiempo_espera_tierra):
        self.estado = estado
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_espera_aire = tiempo_espera_aire
        self.tiempo_espera_tierra = tiempo_espera_tierra


class Pista:
    def __init__(self, estado, cola_aire, cola_tierra):
        self.estado = estado
        self.cola_aire = cola_aire
        self.cola_tierra = cola_tierra
        