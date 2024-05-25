# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:51:27 2024

@author: aepp1

Usted quiere anticipar el movimiento del nuevo robot que recibió como regalo 
de cumpleaños. El robot tiene una brújula interna que le permite saber 
hacia qué punto cardinal está mirando actualmente: Norte, Sur, Este, u Oeste. 
Además, el robot tiene un control remoto que permite girarlo hacia la 
izquierda o la derecha, y también pedirle que dé media vuelta. Usted debe 
escribir una función que, dados 3 comandos que se envíen usando el control 
remoto, calcule la orientación final del robot.

Nota: La representación de los puntos cardinales que llegan por parámetro 
es la siguiente:

    "N", para Norte.

    "S", para Sur.

    "E", para Este.

    "W", para Oeste.

Las representaciones de los comandos del control remoto que llegan por 
parámetro son las siguientes:

    "L", para girar a la izquierda.

    "R", para girar a la derecha.

    "H", para dar media vuelta.

    ".", para mantener la orientación actual.   

Su solución debe tener una función de acuerdo con la siguiente especificación:

    Nombre de la función: movimiento_robot

Si lo requiere, puede agregar funciones adicionales.

Descripción de parámetros:

Nombre                   Tipo             Descripción
orientacion_actual       str    La orientación actual del robot.
giro_1                   str    La acción por ejecutar a partir de la 
                                orientación inicial del robot. 
                                Debe ser un valor de los siguientes: 
                                {"L","H","R","."}.   
giro_2                   str    La acción por ejecutar a partir de la 
                                orientación posterior al giro_1 del robot. 
                                Debe ser un valor de los siguientes:
                                {"L","H","R","."}.   
giro_3                   str    La acción por ejecutar a partir de la 
                                orientación posterior al giro_2 del robot. 
                                Debe ser un valor de los siguientes: 
                                {"L","H","R","."}.   

Descripción del retorno:

Tipo                Descripción
str        La orientación final del robot. Debe ser uno de los siguientes 
           valores: {"W","N","S","E"}.   


"""
def movimiento_robot(orientacion_actual, giro_1, giro_2, giro_3):
    # Diccionario para los giros a la izquierda
    giros_izquierda = {"N": "W", "W": "S", "S": "E", "E": "N"}
    # Diccionario para los giros a la derecha
    giros_derecha = {"N": "E", "E": "S", "S": "W", "W": "N"}
    # Diccionario para los giros de media vuelta
    giros_media_vuelta = {"N": "S", "S": "N", "E": "W", "W": "E"}

    # Lista con los giros a realizar
    giros = [giro_1, giro_2, giro_3]

    # Realizar cada giro
    for giro in giros:
        if giro == "L":
            orientacion_actual = giros_izquierda[orientacion_actual]
        elif giro == "R":
            orientacion_actual = giros_derecha[orientacion_actual]
        elif giro == "H":
            orientacion_actual = giros_media_vuelta[orientacion_actual]

    # Retornar la orientación final del robot
    return orientacion_actual

