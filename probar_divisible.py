# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:48:02 2024

@author: aepp1
Escriba una función que reciba dos números enteros n y d y determine si n es divisible por 2d, si n es divisible por d, o si n no es divisible ni por d ni por 2d.
Recuerde que ningún número es divisible por 0.
Su solución debe tener una función de acuerdo con la siguiente especificación:

    Nombre de la función: es_divisible

Si lo requiere, puede agregar funciones adicionales. Descripción de parámetros:

Nombre          Tipo         Descripción

  n             int        Un número entero.
  d             int        Un número entero.

Descripción del retorno:

Tipo        Descripción         
 int      Si el número n es divisible por 2d, retorna 2. 
          Si el número n es divisible entre d pero no entre 2d, retorna 1. 
          De lo contrario, retorna 0.
"""

def es_divisible(n, d):
    # Verificar si d es 0 para evitar la división por cero
    if d == 0:
        return "Ningún número es divisible por 0"

    # Verificar si n es divisible por 2d
    elif n % (2*d) == 0:
        return f"{n} es divisible por 2d"

    # Verificar si n es divisible por d
    elif n % d == 0:
        return f"{n} es divisible por d"

    # Si n no es divisible ni por d ni por 2d
    else:
        return f"{n} no es divisible ni por d ni por 2d"


print(es_divisible(10, 2))