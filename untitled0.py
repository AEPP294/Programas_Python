# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:14:52 2024

@author: andres

Reto 12: La mejor aerolínea

Recopilamos los registros de los vuelos que ocurrieron durante
un día entre aeropuertos ubicados en Estados Unidos y los organizamos 
en un diccionario de diccionarios. Ahora queremos que usted nos ayude 
a averiguar cuál es la mejor aerolínea con base en la puntualidad. 
Es decir, queremos saber cuál es la aerolínea que acumuló el menor
retraso promedio en los vuelos que recopilamos.

El parámetro vuelos de la función, es un diccionario de diccionarios 
con la información de los vuelos. Las llaves en este diccionario son 
el código de cada vuelo. 

Los valores en este diccionario son diccionarios con la información 
de un vuelo organizado de acuerdo con las siguientes llaves:

    aerolinea, corresponde al nombre de la aerolínea.

    origen, corresponde al código de aeropuerto de origen.

    destino, corresponde al código de aeropuerto destino del vuelo.

    distancia, corresponde a la distancia entre el origen y el destino.

    retraso, corresponde a la cantidad de minutos de retraso que tuvo el vuelo.

    duracion, corresponde a la duración planeada del vuelo en minutos.

    salida, corresponde a un entero que representa la hora de salida.

La hora de salida, se representa usando la hora en formato 24 horas
multiplicada por 100 más la cantidad de minutos (por ejemplo, las 2007
indica que el vuelo salió a las 8:07 pm).  

Su solución debe tener una función de acuerdo con la 
siguiente especificación: 

    Nombre de la función: mejor_aerolinea 

Si lo requiere, puede agregar funciones adicionales.    

Descripción de parámetros:

Nombre             Tipo                    Descripción
vuelos             dict         Diccionario de diccionarios con la 
                                información de los vuelos.

Descripción de retorno:

Tipo
	
Descripción                str
	

El nombre de la mejor aerolínea (la que tenga menor retraso promedio).
"""

def mejor_aerolinea(vuelos: dict) -> str:
    # Crear un diccionario para almacenar el total de retrasos y la cantidad de vuelos por aerolínea
    retrasos_por_aerolinea = {}
    vuelos_por_aerolinea = {}

    # Calcular el total de retrasos y la cantidad de vuelos para cada aerolínea
    for vuelo in vuelos.values():
        aerolinea = vuelo['aerolinea']
        retraso = vuelo['retraso']
        if aerolinea not in retrasos_por_aerolinea:
            retrasos_por_aerolinea[aerolinea] = retraso
            vuelos_por_aerolinea[aerolinea] = 1
        else:
            retrasos_por_aerolinea[aerolinea] += retraso
            vuelos_por_aerolinea[aerolinea] += 1

    # Calcular el retraso promedio para cada aerolínea
    retraso_promedio_por_aerolinea = {}
    for aerolinea, total_retrasos in retrasos_por_aerolinea.items():
        vuelos_totales = vuelos_por_aerolinea[aerolinea]
        retraso_promedio = total_retrasos / vuelos_totales
        retraso_promedio_por_aerolinea[aerolinea] = retraso_promedio

    # Encontrar la aerolínea con el menor retraso promedio
    mejor_aerolinea = min(retraso_promedio_por_aerolinea, key=retraso_promedio_por_aerolinea.get)

    return mejor_aerolinea

# Ejemplo de uso
vuelos_ejemplo = {
    'DL101': {'aerolinea': 'Delta', 'retraso': 10, 'duracion': 180, 'salida': 800},
    'AA202': {'aerolinea': 'American Airlines', 'retraso': 5, 'duracion': 150, 'salida': 1000},
    # ... más vuelos ...
}

mejor_aerolinea_ejemplo = mejor_aerolinea(vuelos_ejemplo)
print(f"La mejor aerolínea es: {mejor_aerolinea_ejemplo}")
