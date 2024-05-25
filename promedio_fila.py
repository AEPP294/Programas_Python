# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:52:35 2024

@author: andres

Reto 15: La fila juiciosa

Andrés es un profesor que tiene la teoría de que hay filas del salón 
que tienen mejor promedio que otras. Para comprobarlo, ha decidido 
crear una función que calcule el promedio de la nota de una fila. 
La función recibe como parámetros una matriz, un número de fila y 
retorna el promedio de la fila redondeado a dos decimales.

Cuidado: un 0 en la matriz no significa que el estudiante haya sacado 
0, sino que no hay ningún estudiante en dicha silla.

Tenga muy en cuenta que para Andrés la primera fila es la número 1. 
Si se pide un número de fila que no tenga sentido,
su función debe retornar -1. Si la fila no tiene estudiantes, 
su función debe retornar 0.  

Su solución debe tener una función de acuerdo con la siguiente especificación:

    Nombre de la función: promedio_fila

Si lo requiere, puede agregar funciones adicionales. 

Descripción de parámetros:

Nombre         Tipo                Descripción
matriz         list     Matriz que representa el salón de clases.
fila           int      Fila a la cual se le va a calcular el promedio.


Descripción de retorno:

Tipo                   Descripción
float       Promedio de la fila que el profesor solicitó. 
"""

def promedio_fila(matriz: list, fila: int) -> float:
    # Verificar si el número de fila es válido
    if fila < 1 or fila > len(matriz):
        return -1
    
    # Ajustar el índice de la fila para que coincida con la indexación de Python
    fila -= 1
    suma_notas = 0
    cantidad_estudiantes = 0
    
    # Calcular la suma de notas y la cantidad de estudiantes en la fila
    for nota in matriz[fila]:
        if nota != 0:  # Ignorar los asientos vacíos
            suma_notas += nota
            cantidad_estudiantes += 1
    
    # Calcular el promedio si hay estudiantes en la fila
    if cantidad_estudiantes > 0:
        promedio = suma_notas / cantidad_estudiantes
        return round(promedio, 2)
    else:
        return 0.0

# Ejemplo de uso
matriz_ejemplo = [
    [80, 90, 0],  # Fila 1
    [70, 85, 0],  # Fila 2
    # ... más filas ...
]
fila_ejemplo = 1
promedio = promedio_fila(matriz_ejemplo, fila_ejemplo)
print(f"El promedio de la fila {fila_ejemplo} es: {promedio}")
