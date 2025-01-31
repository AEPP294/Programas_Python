#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio nivel 3: Billboard.
Interfaz basada en consola para la interacción con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos

@author: Cupi2
"""

import billboard as bb

"Funcion 1"
def ejecutar_cargar_canciones() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    las canciones y las carga.
    Retorno: list
        La lista de canciones con la información del archivo.
    """
    canciones = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con las canciones: ")
    canciones = bb.cargar_canciones(archivo)
    if len(canciones) == 0:
        print("El archivo seleccionado no es válido. No se pudieron cargar las canciones del Ranking")
    else:
        print("Se cargaron", len(canciones), "canciones a partir del archivo.")
        print("Imprime las primeras 2 canciones_cargadas")
        print(canciones[:10])  # Imprimir las primeras 2 canciones para verificar
    return canciones

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 2"
def ejecutar_buscar_cancion(canciones:list)->None:
    """ Ejecuta la opción de buscar una canción dado el nombre y el año del 
    ranking al cual pertenece 
    """
    cancion = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    anio = int(input("Por favor ingrese el año de la canción que desea buscar: "))
    
    resultado_busqueda = bb.buscar_cancion(canciones, cancion, anio)
    
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    if cancion:
        print(f"Canción encontrada: {resultado_busqueda}")
    else:
        print("Canción no encontrada.")
        
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"Funcion 3"

def ejecutar_canciones_anio(canciones:list)->None:
    """ Ejecuta la opción de consultar las canciones de un año dado 
    """
    anio = int(input("Por favor ingrese el año que desea consultar: "))

    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    anio_canciones = bb.buscar_canciones_por_anio(canciones, anio)
    
    if len(anio_canciones) > 0:
        for cancion in anio_canciones:
           print(cancion)
    else:
        print('No hay canciones con el año dado. Por favor, intenta con otro año.')

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
"Funcion 4"
def ejecutar_canciones_artista_periodo(canciones:list)->None:
    """ Ejecuta la opción de consultar las canciones de un artista dado en 
    un periodo de tiempo definido 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    anio_inic = int(input("Por favor ingrese el año inicial que desea buscar: "))
    anio_fin = int(input("Por favor ingrese el año final que desea buscar: "))
    
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    artista_canciones = bb.buscar_canciones_artista_periodo(canciones, artista, anio_inic, anio_fin)
    if len(artista_canciones) > 0:
        for cancion in artista_canciones:
           print(cancion)
    else:
        print('No hay canciones con el año dado. Por favor, intenta con otro año.')
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"Funcion 5"    
def ejecutar_todas_canciones_artista(canciones:list)->None:
    """ Ejecuta la opción de consultar todas las canciones de un artista dado 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    

    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    todas_las_canciones = bb.buscar_canciones_por_artista(canciones, artista)
    
    if len(todas_las_canciones) > 0:
        for cancion in todas_las_canciones:
           print(cancion)
    else:
        print('No hay canciones del artista.')
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 6"

def ejecutar_todos_artistas_cancion(canciones:list)->None:
    """ Ejecuta la opción de consultar todos los artistas que han interpretado 
    una canción dada 
    """
    nom_cancion = input("Por favor ingrese el nombre de la canción que desea buscar: ")

    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    todos_los_artistas = bb.buscar_artistas_de_cancion(canciones, nom_cancion)
    
    if len(todos_los_artistas) > 0:
        for cancion in todos_los_artistas:
           print(cancion)
    else:
        print('No hay canciones del artista.')
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 7"
def ejecutar_artistas_mas_populares(canciones:list)->None:
    """ Ejecuta la opción de consultar los artistas más populares 
    """
    min = int(input("Por favor ingrese la cantidad mínima de canciones que desea buscar: "))

    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    artistas_mas_populares = bb.buscar_artistas_mas_populares(canciones, min)
    
    if len(artistas_mas_populares) > 0:
           print(artistas_mas_populares)
    else:
        print('Error en la busqueda.')

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 8"
def ejecutar_artista_estrella(canciones:list)->None:
    """ Ejecuta la opción de consultar el artista estrella de todos los tiempos 
    """
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    artista = bb.buscar_artista_estrella(canciones)
    if len(artista) > 0:
        print(artista)
    else:
        print('Ocurrio un error encontrando el artista.')

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 9"
def ejecutar_artistas_y_sus_canciones(canciones:list):
    """ Ejecuta la opción de consultar la lista completa de artistas del Billboard 
    junto con sus canciones 
    """
    #TODO: complete el código haciendo el llamado a la función del módulo que
    #implementa este requrimiento e imprimiendo por pantalla el resultado
    lista_artistas = bb.canciones_por_artista(canciones)
    if len(lista_artistas) > 0:
        print(lista_artistas)
    else:
        print('Ocurrio un error en la busqueda.')

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
"Funcion 10"
def ejecutar_promedio_canciones_por_artista(canciones: list) -> None:
    promedio = bb.canciones_promedio_por_artista(canciones)
    print(f'El promedio de canciones por artista es: {promedio}')

 
#----------------------------------------------------------------------------------------    
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de canciones")
    print("2. Buscar una canción")
    print("3. Consultar las canciones de un año")
    print("4. Consultar las canciones de un artista en un periodo")
    print("5. Consultar todas las canciones de un artista")
    print("6. Consultar todos los artistas que han interpretado una canción")
    print("7. Consultar los artistas más populares")
    print("8. Consultar el artista estrella de todos los tiempos")
    print("9. Consultar los artistas y sus canciones")    
    print("10. Consultar la cantidad promedio de canciones por artista")
    print("11. Salir.")

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    canciones = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            canciones=ejecutar_cargar_canciones()
        elif opcion_seleccionada == 2:
            ejecutar_buscar_cancion(canciones)
        elif opcion_seleccionada == 3:
            ejecutar_canciones_anio(canciones)
        elif opcion_seleccionada == 4:
            ejecutar_canciones_artista_periodo(canciones)
        elif opcion_seleccionada == 5:
            ejecutar_todas_canciones_artista(canciones)
        elif opcion_seleccionada == 6:
            ejecutar_todos_artistas_cancion(canciones)
        elif opcion_seleccionada == 7:
            ejecutar_artistas_mas_populares(canciones)
        elif opcion_seleccionada == 8:
            ejecutar_artista_estrella(canciones)
        elif opcion_seleccionada == 9:
            ejecutar_artistas_y_sus_canciones(canciones)
        elif opcion_seleccionada == 10:
            ejecutar_promedio_canciones_por_artista(canciones)            
        elif opcion_seleccionada == 11:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

