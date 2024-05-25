# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:31:30 2024

@author: andres
Escriba una función que determine si en dos números enteros aparecen los 
En matemáticas, la sucesión o serie de Fibonacci es la siguiente sucesión
infinita de números naturales: 0,1,1,2,3,5,8,13,...
La sucesión comienza con los números 0 y 1, y a partir de estos, cada término
es la suma de los dos anteriores. Cree una función que reciba un número que
indica la cantidad de números de la sucesión que se quieren encontrar y 
retorne una cadena con los números separados por coma.

Por ejemplo, el resultado de la función, si se pasa como parámetro el número 18 es el siguiente:
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597

Su solución debe tener una función de acuerdo con la siguiente especificación:
    Nombre de la función: sucesion_fibonacci

Si lo requiere, puede agregar funciones adicionales. 

 Descripción de parámetros:

Nombre                     Tipo                   Descripción
cantidad_numeros            int         Cantidad de números de la sucesión que
                                        se quieren encontrar.

Descripción del retorno:

Tipo                  Descripción
str             Cadena que contiene los números de la sucesión 
                de Fibonacci hasta la cantidad que indica el parámetro, 
                separados por coma y sin espacios intermedios.       
"""

def sucesion_fibonacci(cantidad_numeros):
    # Inicializar los dos primeros números de la sucesión
    a, b = 0, 1
    # Inicializar la lista de la sucesión con el primer número
    sucesion = [a]
    # Utilizar un bucle while para generar la sucesión
    while len(sucesion) < cantidad_numeros:
        # Agregar el siguiente número a la lista
        sucesion.append(b)
        # Actualizar los valores de a y b
        a, b = b, a + b
    # Crear una cadena de texto con los números separados por coma
    cadena_resultado = ''
    for numero in sucesion:
        cadena_resultado += str(numero) + ','
    # Eliminar la coma al final
    cadena_resultado = cadena_resultado[:-1]
    return cadena_resultado

# Ejemplo de uso de la función
resultado = sucesion_fibonacci(9)
print(resultado)
