import random
import distribuciones
import string

class Avion():


    def __init__(self, estado, tiempo_llegada,tiempo_espera_aire=0, tiempo_espera_tierra=0,normal = (60,20), despegue = (4,7)
                 ,aterrizaje = (3,5)):
        self.__nombre = random.choice(string.ascii_letters) + str(random.randint(1, 100)) \
                        + random.choice(string.ascii_letters)
        self.__estado = estado
        self.__tiempo_llegada = tiempo_llegada
        self.__tiempo_espera_aire = tiempo_espera_aire
        self.__tiempo_espera_tierra = tiempo_espera_tierra
        self.__demora_aterrizar = round(distribuciones.uniforme(aterrizaje[0], aterrizaje[1]), 4)
        self.__demora_despegar = round(distribuciones.uniforme(despegue[0], despegue[1]), 4)
        demoraEstacion = round(distribuciones.normal(normal[0], normal[1]), 4)
        while demoraEstacion < 0:
            demoraEstacion = round(distribuciones.normal(normal[0], normal[1]), 4)
        self.__demora_estacion = demoraEstacion

        self.__tiempo_en_estacion = tiempo_llegada + tiempo_espera_aire + self.__demora_aterrizar

    def __str__(self):
        return f"{self.__nombre.ljust(5)},t_llegada:{str(self.__tiempo_llegada).ljust(15)},t_aterrizaje:{str(self.__demora_aterrizar).ljust(15)}," \
               f"t_estacion:{str(self.__demora_estacion).ljust(15)},t_despegue:{str(self.__demora_despegar).ljust(15)}"

    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_tiempo_estacion(self):
        return self.__tiempo_en_estacion

    def get_nombre(self):
        return self.__nombre

    def get_demora_aterrizar(self):
        return self.__demora_aterrizar

    def get_tiempo_llegada(self):
        return self.__tiempo_llegada

    def get_demora_estacion(self):
        return self.__demora_estacion

    def get_demora_despegue(self):
        return  self.__demora_despegar

    def set_estado(self, estado):
        self.__estado = estado

    def get_estado(self):
        return self.__estado

    def agregar_tierra(self, tmp):
        self.__tiempo_espera_tierra += tmp

    def get_tierra(self):
        return self.__tiempo_espera_tierra

    def agregar_aire(self, tmp):
        self.__tiempo_espera_aire += tmp

    def get_aire(self):
        return self.__tiempo_espera_aire


class Pista():
    def __init__(self, estado, avion = None,tmp = 0, tiempoAtaque = 0):
        self.__estado = estado
        self.__avion = avion
        self.__tiempo_ocup = tmp
        self.__suma_ocup = tmp
        self.__tiempo_atacada = tiempoAtaque

    def set_tiempo_ataque(self, tiempo):
        self.__tiempo_atacada = tiempo

    def get_tiempo_ataque(self):
        return self.__tiempo_atacada

    def acum_tmp_ocup(self):
        return self.__suma_ocup

    def get_tmp_ocup(self):
        return self.__tiempo_ocup


    def get_estado(self):
        return self.__estado
    def set_estado(self,estado):
        self.__estado=estado

    def get_avion(self):
        return self.__avion
    def set_avion(self,avion):
        self.__avion=avion

    def ocupar(self,avion,tmp,clk):
        self.__estado = "ocupada"
        self.__avion = avion
        self.__tiempo_ocup = tmp
        self.__suma_ocup += (tmp-clk)

    def liberar(self):
        self.__estado = "libre"
        self.__avion = None
        self.__tiempo_ocup = 0

    def atacar(self):
        self.__estado = "atacada"
        self.__avion = None



class Evento():
    def __init__(self, tipo,avion,tiempo, objetivo="n/a"):
        self.__tiempo = tiempo
        self.__avion = avion
        self.__tipo = tipo
        self.__objetivo = objetivo

    def __lt__(self, other):
        return self.__tiempo < other.get_tiempo()
    def __gt__(self, other):
        return self.__tiempo > other.get_tiempo()

    def get_objetivo(self):
        return self.__objetivo

    def set_objetivo(self, objetivo):
        self.__objetivo = objetivo

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self,tipo):
        self.__tipo = tipo

    def get_tiempo(self):
        return self.__tiempo

    def set_tiempo(self, tiempo):
        self.__tiempo = tiempo

    def get_avion(self):
        return self.__avion

    def set_avion(self, avion):
        self.__avion = avion
        
        
        