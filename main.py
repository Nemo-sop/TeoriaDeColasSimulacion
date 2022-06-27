import sys

from PyQt5.QtWidgets import QApplication

import distribuciones
from Pantallas.LogicaPantallaIngreso import *
import clases
import bisect
import numpy as np
from RungeKutta import *
import random


def simular(clkRK, hayUnAtaque, RungeKuttas, pista, colas, eventos, llegadas, aterrizajes, salidas, derivados, nuevo,
            normal, uniAterrizaje,
            uniSalidas, expNegLlegadas, capMax, probAtaqueLlegadas, ataqueLlegadas, estabaOcupadaLaPista):
    RKControlador = Controlador(clkRK)
    df = pd.DataFrame({"clk": [], "tipo": []
                          , "avion": [], "tiempo hasta la prox llegada": [], "prox llegada": [], "proximo ataque": [],
                       "objetivo del ataque": [],
                       "proximo avion que sale": [], "estado pista": [], "usada por": [], "porcentaje ocupacion": [],
                       "llegadas": [], "aterrizajes": [], "salidas": [], "derivados": [],
                       "cola aire": [], "cola tierra": [], "aviones en tierra": []}, dtype=object)
    df2 = pd.DataFrame({
        "avion": [], "tiempo espera en tierra": [], "tiempo espera en aire": [], "demora aterrizaje": []
        , "demora despegue": [], "tiempo espera aire total": [], "tiempo espera tierra total": []
    }, dtype=object)

    avionNulo = clases.Avion(None, 0, 0, 0, (1, 1), (1, 1), (1, 1))
    avionNulo.set_nombre("n/a")

    tipo_evento = eventos[0].get_tipo()
    clk = eventos[0].get_tiempo()

    if tipo_evento == "llegada":

        llegadas += 1

        nuevo = clases.Avion("llegada", round(distribuciones.exponencialNegativa(expNegLlegadas), 2) + clk,
                             normal=normal, aterrizaje=uniAterrizaje, despegue=uniSalidas)
        event = clases.Evento("llegada", nuevo, round(nuevo.get_tiempo_llegada()))
        bisect.insort_left(eventos, event)

        if capMax > (aterrizajes - salidas) + len(colas["llegada"]):

            if pista.get_estado() == "ocupada":
                eventos[0].get_avion().set_estado("en aire")
                eventos[0].get_avion().agregar_aire(pista.get_tmp_ocup())

                event = clases.Evento("insistencia", eventos[0].get_avion(), pista.get_tmp_ocup())
                bisect.insort_right(eventos, event)

                if not (eventos[0].get_avion() in colas["llegada"]):
                    colas["llegada"].append(eventos[0].get_avion())

            elif pista.get_estado() == "atacada":
                eventos[0].get_avion().set_estado("en aire")
                eventos[0].get_avion().agregar_aire(pista.get_tiempo_ataque())

                event = clases.Evento("insistencia", eventos[0].get_avion(), pista.get_tiempo_ataque() + clk)
                bisect.insort_right(eventos, event)

                if not (eventos[0].get_avion() in colas["llegada"]):
                    colas["llegada"].append(eventos[0].get_avion())

            elif ataqueLlegadas:
                eventos[0].get_avion().set_estado("en aire")
                eventos[0].get_avion().agregar_aire(pista.get_tiempo_ataque())

                event = clases.Evento("insistencia", eventos[0].get_avion(),
                                      pista.get_Auxiliar_tiempo_ataque_llegadas() + clk)
                bisect.insort_right(eventos, event)

                if not (eventos[0].get_avion() in colas["llegada"]):
                    colas["llegada"].append(eventos[0].get_avion())

            else:
                eventos[0].get_avion().set_estado("aterrizando")
                pista.ocupar(eventos[0].get_avion(), eventos[0].get_avion().get_demora_aterrizar() + clk, clk)
                event = clases.Evento("fin aterrizaje", eventos[0].get_avion(),
                                      clk + eventos[0].get_avion().get_demora_aterrizar())
                bisect.insort_left(eventos, event)

        else:

            if eventos[0].get_avion() in colas["llegada"]:
                colas["llegada"].remove(eventos[0].get_avion())
            derivados += 1
            llegadas -= 1

    elif tipo_evento == "insistencia":

        if ataqueLlegadas:

            event = clases.Evento("insistencia", eventos[0].get_avion(),
                                  pista.get_Auxiliar_tiempo_ataque_llegadas() + clk)
            bisect.insort_right(eventos, event)

        elif pista.get_estado() == "libre":
            eventos[0].get_avion().set_estado("aterrizando")
            pista.ocupar(eventos[0].get_avion(), eventos[0].get_avion().get_demora_aterrizar() + clk, clk)
            event = clases.Evento("fin aterrizaje", eventos[0].get_avion(),
                                  clk + eventos[0].get_avion().get_demora_aterrizar())
            bisect.insort_right(eventos, event)

        elif pista.get_estado() == "atacada":

            event = clases.Evento("insistencia", eventos[0].get_avion(), pista.get_tiempo_ataque() + clk)
            bisect.insort_right(eventos, event)

        else:
            event = clases.Evento("insistencia", eventos[0].get_avion(), pista.get_tmp_ocup())
            bisect.insort_right(eventos, event)

    elif tipo_evento == "fin estacion":

        if pista.get_estado() == "libre":

            if len(colas["llegada"]) == 0:
                event = clases.Evento("fin despegue", eventos[0].get_avion(),
                                      clk + eventos[0].get_avion().get_demora_despegue())
                pista.ocupar(eventos[0].get_avion(), eventos[0].get_avion().get_demora_despegue() + clk, clk)
                bisect.insort_left(eventos, event)

            else:

                event = clases.Evento("fin estacion", eventos[0].get_avion(),
                                      colas["llegada"][0].get_demora_aterrizar() + clk)

                eventos[0].get_avion().agregar_tierra(colas["llegada"][0].get_demora_aterrizar())

                bisect.insort_right(eventos, event)

                if not (eventos[0].get_avion() in colas["salida"]):
                    colas["salida"].append(eventos[0].get_avion())

        elif pista.get_estado() == "atacada":
            event = clases.Evento("fin estacion", eventos[0].get_avion(), clk + pista.get_tiempo_ataque())

            bisect.insort_left(eventos, event)
            eventos[0].get_avion().agregar_tierra(pista.get_tiempo_ataque() - clk)

            if not (eventos[0].get_avion() in colas["salida"]):
                colas["salida"].append(eventos[0].get_avion())

        else:
            event = clases.Evento("fin estacion", eventos[0].get_avion(), pista.get_tmp_ocup())

            bisect.insort_right(eventos, event)
            eventos[0].get_avion().agregar_tierra(pista.get_tmp_ocup() - clk)

            if not (eventos[0].get_avion() in colas["salida"]):
                colas["salida"].append(eventos[0].get_avion())

    elif tipo_evento == "fin aterrizaje":
        aterrizajes += 1
        event = clases.Evento("fin estacion", eventos[0].get_avion(),
                              clk + eventos[0].get_avion().get_demora_estacion())
        bisect.insort_right(eventos, event)

        if len(colas["llegada"]):
            colas["llegada"].pop(0)

        pista.liberar()

    elif tipo_evento == "fin despegue":
        df2 = pd.DataFrame({
            "avion": [], "tiempo espera en tierra": [], "tiempo espera en aire": [], "demora aterrizaje": []
            , "demora despegue": [], "tiempo espera aire total": [], "tiempo espera tierra total": [],
            "tiempo de permanencia en el sistema": []
        })
        df2.at[0, "avion"] = eventos[0].get_avion().get_nombre()
        df2.at[0, "tiempo espera en tierra"] = eventos[0].get_avion().get_tierra()
        df2.at[0, "tiempo espera en aire"] = eventos[0].get_avion().get_aire()
        df2.at[0, "demora aterrizaje"] = eventos[0].get_avion().get_demora_aterrizar()
        df2.at[0, "demora despegue"] = eventos[0].get_avion().get_demora_despegue()
        df2.at[0, "tiempo espera aire total"] += eventos[0].get_avion().get_aire()
        df2.at[0, "tiempo espera tierra total"] += eventos[0].get_avion().get_tierra()
        df2.at[0, "tiempo de permanencia en el sistema"] = clk - eventos[0].get_avion().get_tiempo_llegada()

        pista.liberar()

        salidas += 1
        if len(colas["salida"]) != 0:
            if eventos[0].get_avion() in colas["salida"]:
                colas["salida"].remove(eventos[0].get_avion())

    elif tipo_evento == "llegada ataque":

        if eventos[0].get_objetivo() == "servidor":

            print("Para buscar: " + str(clk))
            tiempo, dfDuracionServidor = RKControlador.calcularRKDuracionAtaqueServidores(clk)

            RungeKuttas[1].append(dfDuracionServidor)

            finAtaque = clases.Evento("fin ataque servidor", avionNulo, clk + tiempo)
            bisect.insort_right(eventos, finAtaque)

            if pista.get_estado() == "ocupada":

                avion = pista.get_avion()

                for i in eventos:
                    if i.get_avion() == avion:
                        eventoARegenerar = i
                        break

                eventos.remove(eventoARegenerar)
                eventoARegenerar.set_tiempo(eventoARegenerar.get_tiempo() + tiempo)
                bisect.insort_left(eventos, eventoARegenerar)
                estabaOcupadaLaPista = True


            else:
                estabaOcupadaLaPista = False

            pista.set_estado("atacada")
            pista.set_tiempo_ataque(tiempo)

            print(pista.get_estado())

        else:
            ataqueLlegadas = True
            tiempo, dfDuracionLlegadas = RKControlador.calcularRKDuracionBloqueo(clk)

            RungeKuttas[2].append(dfDuracionLlegadas)

            finAtaque = clases.Evento("fin ataque llegadas", avionNulo, tiempo + clk)
            bisect.insort_left(eventos, finAtaque)
            pista.set_Auxiliar_tiempo_ataque_llegadas(tiempo)

    elif tipo_evento == "fin ataque servidor":
        tiempo, dfMomentoAtaque = RKControlador.calcularRKMomentoAtaque()
        RungeKuttas[0].append(dfMomentoAtaque)
        rnd = random.random()
        if rnd < probAtaqueLlegadas:
            objetivo = "llegadas"
        else:
            objetivo = "servidor"

        proxAtaque = clases.Evento("llegada ataque", avionNulo, tiempo + clk, objetivo=objetivo)
        bisect.insort_left(eventos, proxAtaque)

        if estabaOcupadaLaPista:
            pista.set_estado("ocupada")
        else:
            pista.set_estado("libre")

    elif tipo_evento == "fin ataque llegadas":

        tiempo, dfMomentoAtaque = RKControlador.calcularRKMomentoAtaque()
        RungeKuttas[0].append(dfMomentoAtaque)

        rnd = random.random()
        if (rnd) < probAtaqueLlegadas:
            objetivo = "llegadas"
        else:
            objetivo = "servidor"

        proxAtaque = clases.Evento("llegada ataque", avionNulo, tiempo + clk, objetivo=objetivo)
        bisect.insort_left(eventos, proxAtaque)

        ataqueLlegadas = False

    else:
        print("aca hiciste un estado mal")

    extra = " "
    # para mostrar el tiempo q va a demorar el avion en llegar al nuevo evento
    if tipo_evento == "llegada":
        extra += " (tiempo que demora en aterrizar: " + str(
            round(eventos[0].get_avion().get_demora_aterrizar(), 4)) + ")"
    elif tipo_evento == "insistencia":
        extra += " (tiempo que demora en aterrizar: " + str(
            round(eventos[0].get_avion().get_demora_aterrizar(), 4)) + ")"
    elif tipo_evento == "fin estacion":
        extra += " (tiempo que demora en despegar: " + str(round(eventos[0].get_avion().get_demora_despegue(), 4)) + ")"
    elif tipo_evento == "fin aterrizaje":
        extra += " (tiempo que demora en terminar el mantenimiento: " + str(
            round(eventos[0].get_avion().get_demora_estacion(), 4)) + ")"
    elif tipo_evento == "fin despegue":
        extra += ""

    if llegadas == 30 and not hayUnAtaque:
        hayUnAtaque = True
        clkRK = clk

        RKControlador.set_tiempo30llegada(clkRK)
        avionNulo = clases.Avion(None, 0, 0, 0, (1, 1), (1, 1), (1, 1))
        avionNulo.set_nombre("n/a")
        tiempoRKMomentoAtaque, dfMomentoAtaque = RKControlador.calcularRKMomentoAtaque()
        RungeKuttas[0].append(dfMomentoAtaque)
        primerAtaque = clases.Evento("llegada ataque", avionNulo, clk + tiempoRKMomentoAtaque)

        rnd = random.random()
        if rnd < probAtaqueLlegadas:
            objetivo = "llegadas"
        else:
            objetivo = "servidor"

        primerAtaque.set_objetivo(objetivo)
        bisect.insort_right(eventos, primerAtaque)


    if tipo_evento == "fin estacion":

        if len(colas["salida"]) != 0:
            if eventos[0].get_avion() == colas["salida"][0]:
                df.at[0, "clk"] = clk
                df.at[0, "tipo"] = tipo_evento + extra
                df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
                df.at[0, "tiempo hasta la prox llegada"] = nuevo.get_tiempo_llegada() - clk
                df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())

                varATK = ["no calc", "n/a"]
                if hayUnAtaque:
                    for i in eventos:
                        if i.get_tipo() == "llegada ataque":
                            varATK[0] = round(i.get_tiempo(), 4)
                        if i.get_tipo() == "fin ataque llegadas" or i.get_tipo() == "fin ataque servidor":
                            varATK[1] = round(i.get_tiempo() - clk, 4)
                else:
                    varATK[0] = "no se calculo el primer ataque"

                df.at[0, "proximo ataque"] = varATK[0]
                df.at[0, "objetivo del ataque"] = eventos[0].get_objetivo()
                df.at[0, "duracion del ataque"] = varATK[1]

                if len(colas["salida"]) == 0:
                    df.at[0, "proximo avion que sale"] = "n/a"
                else:
                    df.at[0, "proximo avion que sale"] = colas["salida"][0].get_nombre()
                df.at[0, "estado pista"] = pista.get_estado()
                if pista.get_estado() != "ocupada":
                    df.at[0, "usada por"] = "n/a"
                else:

                    df.at[0, "usada por"] = pista.get_avion().get_nombre()
                df.at[0, "porcentaje ocupacion"] = pista.acum_tmp_ocup() / clk * 100
                df.at[0, "llegadas"] = llegadas
                df.at[0, "aterrizajes"] = aterrizajes
                df.at[0, "salidas"] = salidas
                df.at[0, "derivados"] = derivados
                df.at[0, "cola aire"] = (
                    "Longitud: " + str(len(colas['llegada'])), [i.get_nombre() for i in colas['llegada']])
                df.at[0, "cola tierra"] = (
                    "Longitud: " + str(len(colas['salida'])), [i.get_nombre() for i in colas['salida']])
                df.at[0, "aviones en tierra"] = aterrizajes - salidas
        else:
            df.at[0, "clk"] = clk
            df.at[0, "tipo"] = tipo_evento + extra
            df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
            df.at[0, "tiempo hasta la prox llegada"] = nuevo.get_tiempo_llegada() - clk
            df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())

            varATK = ["no calc", "n/a"]
            if hayUnAtaque:
                for i in eventos:
                    if i.get_tipo() == "llegada ataque":
                        varATK[0] = round(i.get_tiempo(),4)
                    if i.get_tipo() == "fin ataque llegadas" or i.get_tipo() == "fin ataque servidor":
                        varATK[1] = round(i.get_tiempo() - clk, 4)
            else:
                varATK[0] = "no se calculo el primer ataque"

            df.at[0, "proximo ataque"] = varATK[0]
            df.at[0, "objetivo del ataque"] = eventos[0].get_objetivo()
            df.at[0, "duracion del ataque"] = varATK[1]

            if len(colas["salida"]) == 0:
                df.at[0, "proximo avion que sale"] = "n/a"
            else:
                df.at[0, "proximo avion que sale"] = colas["salida"][0].get_nombre()

            df.at[0, "estado pista"] = pista.get_estado()
            if pista.get_estado() != "ocupada":
                df.at[0, "usada por"] = "n/a"
            else:

                df.at[0, "usada por"] = pista.get_avion().get_nombre()
            df.at[0, "porcentaje ocupacion"] = pista.acum_tmp_ocup() / clk * 100
            df.at[0, "llegadas"] = llegadas
            df.at[0, "aterrizajes"] = aterrizajes
            df.at[0, "salidas"] = salidas
            df.at[0, "derivados"] = derivados
            df.at[0, "cola aire"] = (
                "Longitud: " + str(len(colas['llegada'])), [i.get_nombre() for i in colas['llegada']])
            df.at[0, "cola tierra"] = (
                "Longitud: " + str(len(colas['salida'])), [i.get_nombre() for i in colas['salida']])
            df.at[0, "aviones en tierra"] = aterrizajes - salidas
    else:
        if tipo_evento == "insistencia":
            df.at[0, "clk"] = clk
            df.at[0, "tipo"] = "cambiarACA" + extra
            df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
            df.at[0, "tiempo hasta la prox llegada"] = nuevo.get_tiempo_llegada() - clk
            df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())

            varATK = ["no calc", "n/a"]
            if hayUnAtaque:
                for i in eventos:
                    if i.get_tipo() == "llegada ataque":
                        varATK[0] = round(i.get_tiempo(),4)
                    if i.get_tipo() == "fin ataque llegadas" or i.get_tipo() == "fin ataque servidor":
                        varATK[1] = round(i.get_tiempo() - clk, 4)
            else:
                varATK[0] = "no se calculo el primer ataque"

            df.at[0, "proximo ataque"] = varATK[0]
            df.at[0, "objetivo del ataque"] = eventos[0].get_objetivo()
            df.at[0, "duracion del ataque"] = varATK[1]

            if len(colas["salida"]) == 0:
                df.at[0, "proximo avion que sale"] = "n/a"
            else:
                df.at[0, "proximo avion que sale"] = colas["salida"][0].get_nombre()

            df.at[0, "estado pista"] = pista.get_estado()
            if pista.get_estado() != "ocupada":
                df.at[0, "usada por"] = "n/a"
            else:

                df.at[0, "usada por"] = pista.get_avion().get_nombre()
            df.at[0, "porcentaje ocupacion"] = pista.acum_tmp_ocup() / clk * 100
            df.at[0, "llegadas"] = llegadas
            df.at[0, "aterrizajes"] = aterrizajes
            df.at[0, "salidas"] = salidas
            df.at[0, "derivados"] = derivados
            df.at[0, "cola aire"] = (
                "Longitud: " + str(len(colas['llegada'])), [i.get_nombre() for i in colas['llegada']])
            df.at[0, "cola tierra"] = (
                "Longitud: " + str(len(colas['salida'])), [i.get_nombre() for i in colas['salida']])
            df.at[0, "aviones en tierra"] = aterrizajes - salidas
        else:
            df.at[0, "clk"] = clk
            df.at[0, "tipo"] = tipo_evento + extra
            df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
            df.at[0, "tiempo hasta la prox llegada"] = nuevo.get_tiempo_llegada() - clk
            df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())

            varATK = ["no calc", "n/a"]
            if hayUnAtaque:
                for i in eventos:
                    if i.get_tipo() == "llegada ataque":
                        varATK[0] = round(i.get_tiempo(),4)
                    if i.get_tipo() == "fin ataque llegadas" or i.get_tipo() == "fin ataque servidor":
                        varATK[1] = round(i.get_tiempo() - clk, 4)
            else:
                varATK[0] = "no se calculo el primer ataque"

            df.at[0, "proximo ataque"] = varATK[0]
            df.at[0, "objetivo del ataque"] = eventos[0].get_objetivo()
            df.at[0, "duracion del ataque"] = varATK[1]

            if len(colas["salida"]) == 0:
                df.at[0, "proximo avion que sale"] = "n/a"
            else:
                df.at[0, "proximo avion que sale"] = colas["salida"][0].get_nombre()

            df.at[0, "estado pista"] = pista.get_estado()
            if pista.get_estado() != "ocupada":
                df.at[0, "usada por"] = "n/a"
            else:

                df.at[0, "usada por"] = pista.get_avion().get_nombre()
            df.at[0, "porcentaje ocupacion"] = pista.acum_tmp_ocup() / clk * 100
            df.at[0, "llegadas"] = llegadas
            df.at[0, "aterrizajes"] = aterrizajes
            df.at[0, "salidas"] = salidas
            df.at[0, "derivados"] = derivados
            df.at[0, "cola aire"] = (
                "Longitud: " + str(len(colas['llegada'])), [i.get_nombre() for i in colas['llegada']])
            df.at[0, "cola tierra"] = (
                "Longitud: " + str(len(colas['salida'])), [i.get_nombre() for i in colas['salida']])
            df.at[0, "aviones en tierra"] = aterrizajes - salidas

    eventos.remove(eventos[0])


    return clkRK, hayUnAtaque, clk, llegadas, aterrizajes, salidas, derivados, nuevo, df, df2, ataqueLlegadas, \
           estabaOcupadaLaPista, RungeKuttas


def principal(pantallaIngreso, tiempos=(22, 7, 9, 15, 17, 20), duracion=2000, normal=(60, 20),
              uniAterrizaje=(3, 5), uniSalidas=(4, 7), expNegLlegadas=10, capMax=200, inicio=0, probAtaqueLlegadas=1):
    tiempo_total = duracion

    probAtaqueLlegadas = 0.3

    actual = clases.Avion("en aire", tiempos[0], normal=normal, aterrizaje=uniAterrizaje, despegue=uniSalidas)

    eventos = [clases.Evento("llegada", actual, actual.get_tiempo_llegada())]

    # avionNulo = clases.Avion(None, 0, 0, 0, (1,1), (1,1), (1,1))
    # avionNulo.set_nombre("n/a")
    # primerAtaque =  clases.Evento("llegada ataque", avionNulo, calculo_RK())
    #
    # rnd = random.random()
    # if rnd*10 < probAtaqueLlegadas:
    #     objetivo = "llegadas"
    # else:
    #     objetivo = "servidor"
    #
    # primerAtaque.set_objetivo(objetivo)
    # bisect.insort_right(eventos, primerAtaque)

    tiemposSalidas = [tiempos[1], tiempos[2], tiempos[3], tiempos[4], tiempos[5]]
    for i in tiemposSalidas:
        a = clases.Avion("fin estacion", 0, normal=normal, aterrizaje=uniAterrizaje, despegue=uniSalidas)
        event = clases.Evento("fin estacion", a, i)
        bisect.insort_left(eventos, event)

    colas = {"llegada": [], "salida": []}
    RungeKuttas = [[], [], []]

    clk = actual.get_tiempo_llegada()  # aca por esto no simula a no ser q pongas mas de 21 min de simulacion
    # clk = 0
    pista = clases.Pista("libre")

    aterrizajes = 5
    llegadas = 0
    salidas = 0
    derivados = 0

    prueba = 0
    anterior = 0

    nuevo = actual
    data = pd.DataFrame({"clk": [], "tipo": [],
                            "avion": [], "tiempo hasta la prox llegada": [], "prox llegada": [], "proximo ataque": [],
                         "objetivo del ataque": [],
                         "proximo avion que sale": [], "estado pista": [], "usada por": [], "porcentaje ocupacion": [],
                         "llegadas": [], "aterrizajes": [], "salidas": [], "derivados": [],
                         "cola aire": [], "cola tierra": [], "aviones en tierra": []}, dtype=object)
    data2 = pd.DataFrame({
        "avion": [], "tiempo espera en tierra": [], "tiempo espera en aire": [], "demora aterrizaje": []
        , "demora despegue": [], "tiempo espera aire total": [], "tiempo espera tierra total": [],
        "tiempo de permanencia en el sistema": []
    })
    data2.at[0, "tiempo espera aire total"] = 0
    data2.at[0, "tiempo espera tierra total"] = 0
    hayUnAtaque = False
    clkRK = 0
    ataqueLlegadas = False
    while tiempo_total >= clk:

        """
        Rungekuttas tiene arrays con todos los rungekuttas q se fueron utilizando en el programa de fomra cronologica
        array 0 llegada ataque - > Separo por fila en blanco.
        array 1 duracion servidor
        array 2 duracion llegadas
        """

        print(ataqueLlegadas, llegadas, clk, eventos[0].get_tipo(), pista.get_tiempo_ataque(), pista.get_estado(),
              len(colas["llegada"]), eventos[0].get_avion())

        clkRK, hayUnAtaque, clk, llegadas, aterrizajes, salidas, derivados, nuevo, fila, fila2, ataqueLlegadas, estabaOcupadaLaPista, RungeKuttas = simular(
            clkRK, hayUnAtaque, RungeKuttas, pista, colas, eventos, llegadas,
            aterrizajes, salidas, derivados,
            nuevo
            , normal, uniAterrizaje,
            uniSalidas, expNegLlegadas, capMax, probAtaqueLlegadas, ataqueLlegadas, estabaOcupadaLaPista=None)
        data = pd.concat([data, fila], ignore_index=True)
        data2 = pd.concat([data2, fila2], ignore_index=True)

        # print(clk, anterior, prueba)

        if clk == anterior:
            prueba += 1
        else:
            prueba = 0
        anterior = clk

        if prueba >= 100:
            resultado = "Reiniciar..."

    resultado = "Completado..."

    for i in RungeKuttas:
        print(i)
        print("-" * 20)

    if resultado == "Reiniciar...":
        principal(tiempos, duracion, normal, uniAterrizaje,
                  uniSalidas, expNegLlegadas, capMax, probAtaqueLlegadas, ataqueLlegadas, estabaOcupadaLaPista=None)

    # Cálculo de Estadísticos...

    # ACLARACIÓN! -> En caso de tocar, recordar que el estadístico[2] es el último que calculamos de todos.

    estadisticos = np.zeros(9)

    # tiempo promedio permanencia -> Servidor

    promedioPermanencia = data2["tiempo de permanencia en el sistema"].mean()
    estadisticos[0] = promedioPermanencia

    '''
        # porcentaje permanencia en tierra -> Cola
        tiemposEsperaTierra = data2["tiempo espera en tierra"]

        sumaTiempos = 0

        for i in range(1, len(tiemposEsperaTierra)):
            sumaTiempos += tiemposEsperaTierra[i]

        cantAviones = len(data2["avion"]) - 1

        if sumaTiempos == 0:
            sumaTiempos = 1

        porcentajePermanencia = (cantAviones / sumaTiempos) * 100

        estadisticos[1] = porcentajePermanencia
    '''

    # cantidad promedio de clientes en cola en aire -> Cola

    # porcentaje de ocupacion de la pista -> Servidor
    if data.empty:
        estadisticos[2] = 0
        estadisticos[3] = 0
        estadisticos[4] = 0
        estadisticos[6] = 0
        estadisticos[7] = 0
        estadisticos[8] = 0
    else:
        porcentajeOcupacionPista = data.loc[data.index[-1], "porcentaje ocupacion"]

        estadisticos[2] = porcentajeOcupacionPista

        # tiempo de la pista libre -> Servidor
        tiempoOcupacionTotal = pista.acum_tmp_ocup()
        tiempoPistaLibre = duracion - tiempoOcupacionTotal

        estadisticos[3] = tiempoPistaLibre

        # caudal de salida -> Servidor
        caudalSalida = data.loc[data.index[-1], "salidas"]

        estadisticos[4] = caudalSalida

        # cantidad aviones derivados -> Cliente
        cantDerivados = data.loc[data.index[-1], "derivados"]

        estadisticos[6] = cantDerivados

        # cantidad aviones que llegaron -> Cliente
        cantLlegados = data.loc[data.index[-1], "llegadas"]

        estadisticos[7] = cantLlegados

        # cantidad aviones aterizados -> Cliente
        cantAterrizados = data.loc[data.index[-1], "aterrizajes"]

        estadisticos[8] = cantAterrizados

    # muestra solo 400 y la ultima
    # if data.shape[0]<400:
    #
    #     dataMuestra = data.iloc[inicio:(data.shape[0]-inicio)]
    #
    # else:
    #     dataMuestra = data.iloc[inicio:(inicio+400)]

    # print(dataMuestra)
    print("--" * 20)
    print(data)
    # # if not data.empty:
    # #     dataMuestra.loc[len(dataMuestra.index)] = data.iloc[-1]

    pantallaIngreso.mostrarResultados(data, estadisticos, inicio, RungeKuttas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = PantallaIngreso()
    GUI.show()
    sys.exit(app.exec_())

    # principal()
