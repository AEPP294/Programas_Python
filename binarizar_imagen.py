# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:06:15 2024

@author: andres

Reto 3: Binarizar

Este ejercicio consiste en llevar los valores de una matriz que  representa 
una imagen a dos colores: negro y blanco. En cada posición de  la matriz que 
representa la imagen, hay una tupla de 3 flotantes entre 0 y 1 que representan
los valores R, G y B del píxel. 

Para ello, se establece un umbral (valor entre 0 y 1) y los  píxeles con 
promedio de color que  son iguales o mayores al  umbral se cambian a blanco 
(todos los valores de la tupla en 1) y los que están por  debajo se cambian a
negro (todos los valores de la tupla en 0).

Su solución debe tener una función de acuerdo con la siguiente especificación: 

    Nombre de la función: binarizar_imagen

Si lo requiere, puede agregar funciones adicionales.

Descripción de argumentos:

Nombre              Tipo                 Descripción
imagen              list        Matriz que representa la imagen
umbral             float        Umbral de binarización

Descripción del retorno:

Tipo                          Descripción
list            Matriz que representa la imagen binarizada
"""


def binarizar_imagen(imagen, umbral):
    """
    Binariza una imagen representada como una matriz de tuplas RGB.

    Args:
        imagen (list): Matriz que representa la imagen (cada elemento es una tupla RGB).
        umbral (float): Umbral de binarización (valor entre 0 y 1).

    Returns:
        list: Matriz que representa la imagen binarizada (cada elemento es una tupla RGB).
    """
    # Inicializamos la matriz binarizada
    imagen_binarizada = []

    # Recorremos cada fila de la imagen
    for fila in imagen:
        fila_binarizada = []
        # Recorremos cada píxel en la fila
        for pixel in fila:
            # Calculamos el promedio de los valores R, G y B
            promedio_color = sum(pixel) / 3.0

            # Si el promedio es mayor o igual al umbral, asignamos blanco (1, 1, 1)
            if promedio_color >= umbral:
                fila_binarizada.append((1.0, 1.0, 1.0))
            else:
                # Si es menor, asignamos negro (0, 0, 0)
                fila_binarizada.append((0.0, 0.0, 0.0))

        # Agregamos la fila binarizada a la matriz resultante
        imagen_binarizada.append(fila_binarizada)

    return imagen_binarizada

# Ejemplo de uso
imagen_ejemplo = [
    [(0.2, 0.4, 0.6), (0.8, 0.9, 0.7)],
    [(0.1, 0.3, 0.5), (0.6, 0.7, 0.8)]
]
umbral_ejemplo = 0.5
resultado_ejemplo = binarizar_imagen(imagen_ejemplo, umbral_ejemplo)
print("Resultado:", resultado_ejemplo)

