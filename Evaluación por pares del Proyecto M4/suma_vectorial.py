# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:49:44 2024

@author: andres

Módulo 4 

Reto 1: Sumar dos vectores (3d)

Construya una función que reciba dos vectores (con 3 componentes cada uno) y 
retorne un nuevo vector que sea la suma de los dos vectores recibidos. Cada 
vector debe recibirse como una tupla con tres valores flotantes.

Su solución debe tener una función de acuerdo con la siguiente especificación:

    Nombre de la función: suma_vectorial    

Si lo requiere, puede agregar funciones adicionales.

Descripción de parámetros:

Nombre               Tipo             Descripción
vector_1            tuple           Vector a sumar.
vector_2            tuple           Vector a sumar.

Descripción del retorno:

Tipo                    Descripción

tuple         Vector resultado de la suma como una tupla.

"""

def suma_vectorial(vector_1, vector_2):
    """
    Suma dos vectores representados como tuplas con tres componentes cada uno.
    
    Args:
        vector_1 (tuple): Primer vector.
        vector_2 (tuple): Segundo vector.
        
    Returns:
        tuple: Vector resultado de la suma.
    """
    # Desempaquetamos los valores de los vectores
    x1, y1, z1 = vector_1
    x2, y2, z2 = vector_2
    
    # Calculamos la suma de los componentes
    suma_x = x1 + x2
    suma_y = y1 + y2
    suma_z = z1 + z2
    
    # Devolvemos el resultado como una tupla
    return suma_x, suma_y, suma_z

# Ejemplo de uso
vector1 = (1.0, 2.0, 3.0)
vector2 = (4.0, 5.0, 6.0)
resultado = suma_vectorial(vector1, vector2)
print("Resultado:", resultado)  # Debería imprimir (5.0, 7.0, 9.0)
