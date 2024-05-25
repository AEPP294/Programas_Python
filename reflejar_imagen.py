# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:11:03 2024

@author: andres

Reto 4: Reflejar Verticalmente

En este ejercicio se debe reflejar la imagen verticalmente sobre una  línea 
imaginaria en el centro de la figura, creando una imagen espejo de  la figura
original. En cada posición de la matriz que representa la  imagen hay una 
tupla de 3 flotantes entre 0 y 1 que representan los  valores R, G y B 
del píxel.

Después de reflejar una figura, la distancia  entre la línea de reflexión y 
cada punto en la figura original es la  misma que la distancia entre la línea
de reflexión y el punto  correspondiente en la imagen de espejo. Para hacer 
esta transformación,  se intercambian las columnas de píxeles de la imagen:
La primera con la  última, la segunda con penúltima, etc.

Su solución debe tener una función de acuerdo con la siguiente especificación: 

    Nombre de la función: reflejar_imagen

Si lo requiere, puede agregar funciones adicionales.

Descripción de argumentos:

Nombre                  Tipo                    Descripción
imagen                  list        Matriz que representa la imagen.

Descripción del retorno:
Tipo                      Descripción
list          Matriz que representa la imagen reflejada.
"""

def reflejar_imagen(imagen):
    """
    Refleja una imagen verticalmente sobre una línea imaginaria en el centro de la figura.

    Args:
        imagen (list): Matriz que representa la imagen (cada elemento es una tupla RGB).

    Returns:
        list: Matriz que representa la imagen reflejada (cada elemento es una tupla RGB).
    """
    # Obtenemos el número de columnas de la imagen
    num_columnas = len(imagen[0])

    # Inicializamos la matriz reflejada
    imagen_reflejada = []

    # Recorremos cada fila de la imagen
    for fila in imagen:
        # Creamos una fila reflejada invirtiendo el orden de las columnas
        fila_reflejada = fila[::-1]
        # Agregamos la fila reflejada a la matriz resultante
        imagen_reflejada.append(fila_reflejada)

    return imagen_reflejada

# Ejemplo de uso
imagen_ejemplo = [
    [(0.2, 0.4, 0.6), (0.8, 0.9, 0.7)],
    [(0.1, 0.3, 0.5), (0.6, 0.7, 0.8)]
]
resultado_ejemplo = reflejar_imagen(imagen_ejemplo)
print("Resultado:", resultado_ejemplo)
