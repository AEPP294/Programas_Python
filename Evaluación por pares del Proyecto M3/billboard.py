# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:42:50 2024

@author: andre
"""

import csv

"Funcion 1"
def cargar_canciones(ruta_archivo:str)->list:
    """
    Carga las canciones desde un archivo CSV y las representa como una lista de diccionarios.

    Args:
        ruta_archivo (str): Nombre del archivo CSV con la información de las canciones.

    Returns:
        Lista de diccionarios representando las canciones.
    """
    canciones = []
    with open(ruta_archivo, 'r') as file:
        next(file)  # Saltar la primera línea (encabezados)
        for linea in file:
            datos = linea.strip().split(',')
            cancion = {
                'posicion': datos[0],
                'nombre_cancion': datos[1],
                'nombre_artista': datos[2],
                'anio': datos[3],
                'letra': datos[4]
            }
            canciones.append(cancion)
    return canciones

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
"Funcion 2"
def buscar_cancion(canciones: list, nombre_cancion: str, anio: int) -> dict:
    """
    Busca una canción por su nombre y año en una lista de canciones.

    Args:
        canciones: Lista de canciones.
        nombre_cancion (str): El nombre de la canción a buscar.
        anio (int): El año del ranking al cual pertenece la canción.

    Returns:
        Diccionario con la información de la canción encontrada o None si no se encuentra.
    """
    for cancion in canciones:
        if cancion['nombre_cancion'].lower() == nombre_cancion.lower() and int(cancion['anio']) == anio:
            return cancion
    return None

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 3"

def buscar_canciones_por_anio(canciones: list, anio: int) -> list:
    """
    Consulta las canciones de un año dado.

    Args:
        canciones : Lista de canciones.
        anio (int): Año del ranking al cual pertenecen las canciones.

    Returns:
        Lista de diccionarios con la información de las canciones de ese año, exceptuando la letra.
    """
    canciones_por_anio = []
    for cancion in canciones:
        if int(cancion['anio']) == anio:
            # Crear un nuevo diccionario sin incluir la letra de la canción
            cancion_sin_letra = {llave: valor for llave, valor in cancion.items() if llave != 'letra'}
            canciones_por_anio.append(cancion_sin_letra)
    return canciones_por_anio

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
"Funcion 4"

def buscar_canciones_artista_periodo(canciones: list, nombre_artista: str, anio_inicial: int, anio_final: int) -> list:
    """
    Consulta las canciones de un artista en un rango de años.

    Args:
        canciones : Lista de canciones.
        nombre_artista (str): Nombre del artista a buscar.
        anio_inicial (int): Año inicial del rango.
        anio_final (int): Año final del rango.

    Returns:
        Lista de diccionarios con la información de las canciones del artista en el rango de años.
    """
    canciones_artista_periodo = []
    for cancion in canciones:
        if (cancion['nombre_artista'].lower() == nombre_artista.lower() and 
            anio_inicial <= int(cancion['anio']) <= anio_final):
            # Excluir la letra de la canción en la información retornada
            info_cancion = {llave: valor for llave, valor in cancion.items() if llave != 'letra'}
            canciones_artista_periodo.append(info_cancion)
    return canciones_artista_periodo
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"Funcion 5"

def buscar_canciones_por_artista(canciones: list, nombre_artista: str) -> list:
    """
    Consulta todas las canciones de un artista dado.

    Args:
        canciones : Lista de canciones.
        nombre_artista (str): Nombre del artista a buscar.

    Returns:
         Lista de diccionarios con la información de las canciones del artista, exceptuando la letra.
    """
    titulos_canciones_artista = []
    for cancion in canciones:
        if cancion['nombre_artista'].lower() == nombre_artista.lower():
            titulos_canciones_artista.append(cancion['nombre_cancion'])
    return titulos_canciones_artista


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
"Funcion 6"
def buscar_artistas_de_cancion(canciones: list, nombre_cancion: str) -> list[str]:
    """
    Consulta los artistas que han interpretado una canción dada.

    Args:
        canciones : Lista de canciones.
        nombre_cancion (str): Nombre de la canción a buscar.

    Returns:
        List[str]: Lista de nombres de artistas que han interpretado la canción.
    """
    artistas = []
    for cancion in canciones:
        if cancion['nombre_cancion'].lower() == nombre_cancion.lower():
            artistas.append(cancion['nombre_artista'])
    return list(set(artistas))  # Usar set para eliminar duplicados

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 7"

def buscar_artistas_mas_populares(canciones: list, umbral_canciones: int) -> list[str]:
    """
    Calcula los artistas más populares basados en la cantidad de canciones.

    Args:
        canciones (list): Lista de diccionarios con información de las canciones.
        umbral_canciones (int): Número mínimo de canciones para considerar a un artista popular.

    Returns:
        dict: Diccionario con los nombres de los artistas y la cantidad de canciones que han tenido.
    """
    artistas_contador = {}  # Diccionario para almacenar la cantidad de canciones por artista

    for cancion in canciones:
        artista = cancion["nombre_artista"]
        if artista in artistas_contador:
            artistas_contador[artista] += 1
        else:
            artistas_contador[artista] = 1

    # Filtrar los artistas populares (más de umbral_canciones canciones)
    artistas_populares = {artista: canciones for artista, canciones in artistas_contador.items() if canciones > umbral_canciones}
    return artistas_populares
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 8"

def buscar_artista_estrella(canciones:list) :
    """
    Encuentra el artista estrella de todos los tiempos basado en la cantidad de canciones.

    Args:
        canciones (list): Lista de diccionarios con información de las canciones.

    Returns:
        dict: Diccionario con el nombre del artista y la cantidad total de canciones.
    """
    artistas_contador = {}  # Diccionario para almacenar la cantidad de canciones por artista

    for cancion in canciones:
        artista = cancion["nombre_artista"]
        if artista in artistas_contador:
            artistas_contador[artista] += 1
        else:
            artistas_contador[artista] = 1

    # Encontrar el artista con la mayor cantidad de canciones
    artista_max_canciones = max(artistas_contador, key=artistas_contador.get)
    total_canciones_max = artistas_contador[artista_max_canciones]

    return {artista_max_canciones: total_canciones_max}

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 9"
def canciones_por_artista(canciones: list):
    """
    Crea un diccionario con los nombres de los artistas y sus listas de canciones.

    Args:
        canciones (list): Lista de diccionarios con información de las canciones.

    Returns:
        dict: Diccionario con los nombres de los artistas y sus listas de canciones.
    """
    artistas_canciones = {}  # Diccionario para almacenar las listas de canciones por artista

    for cancion in canciones:
        artista = cancion["nombre_artista"]
        cancion_actual = cancion["nombre_cancion"]

        # Agregar la canción al artista correspondiente (sin duplicados)
        if artista in artistas_canciones:
            if cancion_actual not in artistas_canciones[artista]:
                artistas_canciones[artista].append(cancion_actual)
        else:
            artistas_canciones[artista] = [cancion_actual]

    return artistas_canciones

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 10"
def canciones_promedio_por_artista(canciones:list):
    """
    Calcula el promedio de canciones por artista en la lista de canciones.
    
    Parameters:
        canciones (list): Una lista de diccionarios con los detalles de las canciones.
    
    Returns:
        float: El promedio de canciones por artista.
    """
    artistas_canciones = {}

    # Recorrer la lista de canciones
    for cancion in canciones:
        nombre_artista = cancion['nombre_artista']
        nombre_cancion = cancion['nombre_cancion']

        # Verificar si el artista ya está en el diccionario
        if nombre_artista in artistas_canciones:
            if nombre_cancion not in artistas_canciones[nombre_artista]:
                artistas_canciones[nombre_artista].append(nombre_cancion)
        else:
            artistas_canciones[nombre_artista] = [nombre_cancion]
    
    # Calcular la cantidad total de canciones
    total_canciones = 0
    for canciones in artistas_canciones.values():
        total_canciones += len(canciones)

    # Calcular la cantidad total de artistas
    total_artistas = len(artistas_canciones)

    # Calcular la cantidad promedio de canciones por artista
    if total_artistas > 0:
        promedio = total_canciones / total_artistas
    else:
        promedio = 0
    
    return promedio
    
    


#*****************************************************************************************
