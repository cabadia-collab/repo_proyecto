# -*- coding: utf-8 -*-
"""carga_datos
"""


# Funciones para carga de datos

def cargar_datos(ruta):
    '''
    lee un archivo y transforma su contenido en una lista de diccionarios

    Parameters
    ----------
    ruta : str
        ruta del archivo que contiene los datos

    Returns
    -------
    list
        lista con los registros agrupados por participante
    '''
    datos = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    participantes = {}

    for linea in lineas[1:]:
        if linea.strip() != "":
            partes = parsear_linea(linea)

            id_participante = partes[0]
            tiempo = partes[1]
            valor = partes[2]
            fase = partes[3]
            condicion_experimental = partes[4]
            hit = partes[5]

            if id_participante not in participantes:
                participantes[id_participante] = {
                    "id_participante": id_participante,
                    "tiempo": [],
                    "valor": [],
                    "fase": [],
                    "condicion_experimental": [],
                    "hit": []
                }

            participantes[id_participante]["tiempo"].append(tiempo)
            participantes[id_participante]["valor"].append(valor)
            participantes[id_participante]["fase"].append(fase)
            participantes[id_participante]["condicion_experimental"].append(condicion_experimental)
            participantes[id_participante]["hit"].append(hit)

    for participante in participantes:
        datos.append(participantes[participante])

    return datos


def parsear_linea(linea):
    '''
    transforma una línea del archivo en una estructura de datos

    Parameters
    ----------
    linea : str
        línea del archivo con los datos de una medición

    Returns
    -------
    list
        lista con los valores de la línea
    '''
    return linea.strip().split(",")