import sys

import numpy as np
from PyQt5.QtWidgets import QApplication

from pantallaLogica import *
import clases
import distribuciones
import bisect
import pandas as pd

def simular(pista, colas,eventos,llegadas,aterrizajes,salidas,derivados,nuevo,normal,uniAterrizaje,uniSalidas,expNegLlegadas,capMax):


    df = pd.DataFrame({"clk": [], "tipo": []
                          , "avion": [],"tiempo hasta la prox llegada":[],"prox llegada": [],
                          "proximo avion que sale":[]  ,"estado pista":[],"usada por":[],"porcentaje ocupacion":[],
                         "llegadas": [], "aterrizajes": [], "salidas": [],"derivados":[],
                         "cola aire": [], "cola tierra": [],"aviones en tierra":[]},dtype=object)
    df2 = pd.DataFrame({
        "avion":[],"tiempo espera en tierra":[],"tiempo espera en aire":[],"demora aterrizaje":[]
        ,"demora despegue":[],"tiempo espera aire total":[],"tiempo espera tierra total":[]
    },dtype=object)

    tipo_evento = eventos[0].get_tipo()
    clk = eventos[0].get_tiempo()

    if tipo_evento == "llegada":

        llegadas +=  1

        nuevo = clases.Avion("llegada", round(distribuciones.exponencialNegativa(expNegLlegadas), 2) + clk,
                             normal=normal, aterrizaje=uniAterrizaje, despegue=uniSalidas)
        event = clases.Evento("llegada", nuevo, nuevo.get_tiempo_llegada())
        bisect.insort_left(eventos, event)


        if capMax > (aterrizajes - salidas) + len(colas["llegada"]):


            if pista.get_estado() == "ocupada":
                eventos[0].get_avion().set_estado("en aire")
                eventos[0].get_avion().agregar_aire(pista.get_tmp_ocup())

                event = clases.Evento("insistencia", eventos[0].get_avion(), pista.get_tmp_ocup())
                bisect.insort_right(eventos, event)

                # if len(colas["llegada"]) == 0 :
                #     event = clases.Evento("insistencia", eventos[0].get_avion(), pista.get_tmp_ocup())
                #     bisect.insort_right(eventos, event)
                # else:
                #     if colas["llegada"][0] == eventos[0].get_avion():
                #         event = clases.Evento("insistencia", eventos[0].get_avion(), pista.get_tmp_ocup())
                #         bisect.insort_right(eventos, event)


                if not (eventos[0].get_avion() in colas["llegada"]):
                    colas["llegada"].append(eventos[0].get_avion())


            else:
                eventos[0].get_avion().set_estado("aterrizando")
                pista.ocupar(  eventos[0].get_avion()  , eventos[0].get_avion().get_demora_aterrizar() + clk,clk )
                #colas["llegada"].append(eventos[0].get_avion())
                event = clases.Evento("fin aterrizaje",eventos[0].get_avion() , clk + eventos[0].get_avion().get_demora_aterrizar())
                bisect.insort_left(eventos, event)

        else:



            if eventos[0].get_avion() in colas["llegada"]:
                colas["llegada"].remove(eventos[0].get_avion())
            derivados +=1
            llegadas -= 1

    elif tipo_evento == "insistencia":

        if pista.get_estado() == "libre":
            # if capMax > (aterrizajes - salidas):
            eventos[0].get_avion().set_estado("aterrizando")
            pista.ocupar(eventos[0].get_avion(), eventos[0].get_avion().get_demora_aterrizar() + clk, clk)
            # colas["llegada"].append(eventos[0].get_avion())
            event = clases.Evento("fin aterrizaje", eventos[0].get_avion(),
                                  clk + eventos[0].get_avion().get_demora_aterrizar())
            bisect.insort_right(eventos, event)
        else:
            event = clases.Evento("insistencia", eventos[0].get_avion(), pista.get_tmp_ocup())
            bisect.insort_right(eventos, event)


    elif tipo_evento == "fin estacion":

        if pista.get_estado() == "libre":

            if len(colas["llegada"]) == 0:
                event = clases.Evento("fin despegue", eventos[0].get_avion() , clk +eventos[0].get_avion().get_demora_despegue())
                pista.ocupar( eventos[0].get_avion(), eventos[0].get_avion().get_demora_despegue() + clk,clk )
                bisect.insort_left(eventos, event)

            else:

                event = clases.Evento("fin estacion", eventos[0].get_avion(), colas["llegada"][0].get_demora_aterrizar() + clk)

                eventos[0].get_avion().agregar_tierra(colas["llegada"][0].get_demora_aterrizar())

                bisect.insort_right(eventos,event)


                if not(eventos[0].get_avion() in colas["salida"]):
                    colas["salida"].append(eventos[0].get_avion())

        else:
            #print("BBBBBBBBBBB" )
            event = clases.Evento("fin estacion",eventos[0].get_avion(), pista.get_tmp_ocup())

            bisect.insort_right(eventos, event)
            eventos[0].get_avion().agregar_tierra(pista.get_tmp_ocup() - clk )

            if not (eventos[0].get_avion() in colas["salida"]):
                colas["salida"].append(eventos[0].get_avion())

    elif tipo_evento == "fin aterrizaje":
        aterrizajes +=1
        event = clases.Evento("fin estacion",eventos[0].get_avion(),clk + eventos[0].get_avion().get_demora_estacion())
        bisect.insort_left(eventos, event)
        pista.liberar()

        if len(colas["llegada"]):
            colas["llegada"].pop(0)
        pista.liberar()

    elif tipo_evento == "fin despegue":
        df2 = pd.DataFrame({
            "avion": [], "tiempo espera en tierra": [], "tiempo espera en aire": [], "demora aterrizaje": []
            , "demora despegue": [], "tiempo espera aire total": [], "tiempo espera tierra total": [], "tiempo de permanencia en el sistema":[]
        })
        df2.at[0,"avion"] = eventos[0].get_avion().get_nombre()
        df2.at[0,"tiempo espera en tierra"] = eventos[0].get_avion().get_tierra()
        df2.at[0,"tiempo espera en aire"] = eventos[0].get_avion().get_aire()
        df2.at[0,"demora aterrizaje"] = eventos[0].get_avion().get_demora_aterrizar()
        df2.at[0,"demora despegue"] = eventos[0].get_avion().get_demora_despegue()
        df2.at[0, "tiempo espera aire total"] +=  eventos[0].get_avion().get_aire()
        df2.at[0, "tiempo espera tierra total"] += eventos[0].get_avion().get_tierra()
        df2.at[0, "tiempo de permanencia en el sistema"] = clk - eventos[0].get_avion().get_tiempo_llegada()



        pista.liberar()

        salidas += 1
        if len(colas["salida"]) != 0:
            if eventos[0].get_avion() in colas["salida"]:
                colas["salida"].remove(eventos[0].get_avion())


    else:
        print("aca hiciste un estado mal")


    if tipo_evento == "fin estacion":

        if len(colas["salida"]) != 0:
            if eventos[0].get_avion() == colas["salida"][0]:
                df.at[0, "clk"] = clk
                df.at[0, "tipo"] = tipo_evento
                df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
                df.at[0, "tiempo hasta la prox llegada"] =  nuevo.get_tiempo_llegada() - clk
                df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())
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
                df.at[0, "cola aire"] = [i.get_nombre() for i in colas['llegada']]
                df.at[0, "cola tierra"] = [i.get_nombre() for i in colas['salida']]
                df.at[0, "aviones en tierra"] = aterrizajes - salidas
        else:
            df.at[0, "clk"] = clk
            df.at[0, "tipo"] = tipo_evento
            df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
            df.at[0, "tiempo hasta la prox llegada"] =  nuevo.get_tiempo_llegada() -clk
            df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())
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
            df.at[0, "cola aire"] = len(colas['llegada'])
            df.at[0, "cola tierra"] = len(colas['salida'])
            df.at[0, "aviones en tierra"] = aterrizajes - salidas

    #elif tipo_evento == "llegada":
        # if len(colas["llegada"]) != 0:
        #     if eventos[0].get_avion() == colas["llegada"][0]:
        #         df.at[0, "clk"] = clk
        #         df.at[0, "tipo"] = tipo_evento
        #         df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
        #         df.at[0, "tiempo hasta la prox llegada"] = clk - eventos[0].get_avion().get_tiempo_llegada()
        #         df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())
        #         if len(colas["salida"]) == 0:
        #             df.at[0, "proximo avion que sale"] = "n/a"
        #         else:
        #             df.at[0, "proximo avion que sale"] = colas["salida"][0].get_nombre()
        #         df.at[0, "estado pista"] = pista.get_estado()
        #         if pista.get_estado() != "ocupada":
        #             df.at[0, "usada por"] = "n/a"
        #         else:
        #
        #             df.at[0, "usada por"] = pista.get_avion().get_nombre()
        #         df.at[0, "porcentaje ocupacion"] = pista.acum_tmp_ocup() / clk * 100
        #         df.at[0, "llegadas"] = llegadas
        #         df.at[0, "aterrizajes"] = aterrizajes
        #         df.at[0, "salidas"] = salidas
        #         df.at[0, "derivados"] = derivados
        #         df.at[0, "cola aire"] = len(colas['llegada'])
        #         df.at[0, "cola tierra"] = len(colas['salida'])
        #         df.at[0, "aviones en tierra"] = aterrizajes - salidas
        # else:
        #     df.at[0, "clk"] = clk
        #     df.at[0, "tipo"] = tipo_evento
        #     df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
        #     df.at[0, "tiempo hasta la prox llegada"] = clk - eventos[0].get_avion().get_tiempo_llegada()
        #     df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())
        #     if len(colas["salida"]) == 0:
        #         df.at[0, "proximo avion que sale"] = "n/a"
        #     else:
        #         df.at[0, "proximo avion que sale"] = colas["salida"][0].get_nombre()
        #
        #     df.at[0, "estado pista"] = pista.get_estado()
        #     if pista.get_estado() != "ocupada":
        #         df.at[0, "usada por"] = "n/a"
        #     else:
        #
        #         df.at[0, "usada por"] = pista.get_avion().get_nombre()
        #     df.at[0, "porcentaje ocupacion"] = pista.acum_tmp_ocup() / clk * 100
        #     df.at[0, "llegadas"] = llegadas
        #     df.at[0, "aterrizajes"] = aterrizajes
        #     df.at[0, "salidas"] = salidas
        #     df.at[0, "derivados"] = derivados
        #     df.at[0, "cola aire"] = len(colas['llegada'])
        #     df.at[0, "cola tierra"] = len(colas['salida'])
        #     df.at[0, "aviones en tierra"] = aterrizajes - salidas
    else:
        if tipo_evento == "insistencia":
            df.at[0, "clk"] = clk
            df.at[0, "tipo"] = "llegada"
            df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
            df.at[0, "tiempo hasta la prox llegada"] =  nuevo.get_tiempo_llegada() -clk
            df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())
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
            df.at[0, "cola aire"] = [i.get_nombre() for i in colas['llegada']]
            df.at[0, "cola tierra"] = [i.get_nombre() for i in colas['salida']]
            df.at[0, "aviones en tierra"] = aterrizajes - salidas
        else:
            df.at[0, "clk"] = clk
            df.at[0, "tipo"] = tipo_evento
            df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
            df.at[0, "tiempo hasta la prox llegada"] = nuevo.get_tiempo_llegada() - clk
            df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())
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
            df.at[0, "cola aire"] = [i.get_nombre() for i in colas['llegada']]
            df.at[0, "cola tierra"] = [i.get_nombre() for i in colas['salida']]
            df.at[0, "aviones en tierra"] = aterrizajes - salidas
    """
    df.at[0, "clk"] = clk
    df.at[0, "tipo"] = tipo_evento
    df.at[0, "avion"] = eventos[0].get_avion().get_nombre()
    df.at[0, "tiempo hasta la prox llegada"] = clk - eventos[0].get_avion().get_tiempo_llegada()
    df.at[0, "prox llegada"] = (nuevo.get_nombre(), nuevo.get_tiempo_llegada())
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
    df.at[0, "cola aire"] = len(colas['llegada'])
    df.at[0, "cola tierra"] = len(colas['salida'])
    df.at[0, "aviones en tierra"] = aterrizajes - salidas
    """

    eventos.remove(eventos[0])

    return clk,llegadas,aterrizajes,salidas,derivados,nuevo,df,df2


def principal(tiempos = (22,7,9,15,17,20),duracion = 2000,normal=(60,20),uniAterrizaje=(3,5),uniSalidas=(4,7),expNegLlegadas = 10,capMax = 200):
    tiempo_total = duracion

    actual = clases.Avion("en aire", tiempos[0],normal = normal, aterrizaje = uniAterrizaje,despegue = uniSalidas)
    eventos = [clases.Evento("llegada", actual, actual.get_tiempo_llegada())]

    tiemposSalidas = [tiempos[1],tiempos[2],tiempos[3],tiempos[4],tiempos[5]]
    for i in tiemposSalidas:
        a = clases.Avion("fin estacion",0, normal = normal, aterrizaje = uniAterrizaje,despegue = uniSalidas)
        event = clases.Evento("fin estacion",a,i )
        bisect.insort_left(eventos,event)


    colas = {"llegada": [], "salida": []}

    clk = actual.get_tiempo_llegada()

    pista = clases.Pista("libre")


    aterrizajes = 5
    llegadas = 0
    salidas = 0
    derivados = 0

    prueba = 0
    anterior = 0

    resultado = ""

    nuevo = actual
    data = pd.DataFrame({"clk": [], "tipo": []
                          , "avion": [], "tiempo hasta la prox llegada": [], "prox llegada": [],
                       "proximo avion que sale": [], "estado pista": [], "usada por": [], "porcentaje ocupacion": [],
                       "llegadas": [], "aterrizajes": [], "salidas": [], "derivados": [],
                       "cola aire": [], "cola tierra": [], "aviones en tierra": []}, dtype=object)
    data2 = pd.DataFrame({
        "avion":[],"tiempo espera en tierra":[],"tiempo espera en aire":[],"demora aterrizaje":[]
        ,"demora despegue":[],"tiempo espera aire total":[],"tiempo espera tierra total":[], "tiempo de permanencia en el sistema":[]
    })
    data2.at[0, "tiempo espera aire total"] = 0
    data2.at[0, "tiempo espera tierra total"] = 0

    while tiempo_total >= clk:

        clk,llegadas,aterrizajes,salidas,derivados,nuevo,fila,fila2 = simular(pista,colas,eventos,llegadas,aterrizajes,salidas,derivados,nuevo
                                                              ,normal,uniAterrizaje,uniSalidas,expNegLlegadas,capMax)
        data = pd.concat([data,fila],ignore_index=True)
        data2 = pd.concat([data2, fila2], ignore_index=True)
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #     print(data)
        print(clk, anterior, prueba)

        if clk == anterior:
            prueba += 1
        else:
            prueba =0
        anterior = clk

        if prueba == 200:

            resultado = "Reiniciar..."
    resultado = "Completado..."

    if resultado == "Reiniciar...":
        principal(tiempos, duracion, normal, uniAterrizaje,
                  uniSalidas, expNegLlegadas, capMax)


    print("Termine")




    with open("C:\\Users\\ignac\\PycharmProjects\\muestra a los chicos\\001.txt", 'w') as f:
        dfAsString = data.to_string(header=True, index=True)
        f.write(dfAsString)

    with open("C:\\Users\\ignac\\PycharmProjects\\muestra a los chicos\\002.txt", 'w') as f:
        dfAsString = data2.to_string(header=True, index=True)
        f.write(dfAsString)



    # print(derivados)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = PantallaIngreso()
    GUI.show()
    sys.exit(app.exec_())

    # principal()

