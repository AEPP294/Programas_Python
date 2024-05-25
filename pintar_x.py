# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:03:31 2024

@author: andres

Reto 16: Repintar la x

Un matemático ha diseñado un juego muy sencillo para que sus hijos
practiquen operaciones aritméticas básicas. En este juego, él les da 
una matriz cuadrada de más de 3x3 y les pide que "repinten la X" usando
una operación determinada. Es decir, ellos tienen que devolver la 
matriz aplicando la operación sobre todas las casillas que hacen parte
de las diagonales de la matriz.

Las operaciones posibles son sumar, restar, multiplicar y dividir el
valor de cada casilla por él mismo. Por ejemplo, si en una casilla de
la X el número original era 5 y la operación que se debe aplicar es la
suma, el valor 5 deberá reemplazarse por 10. 

Construya una función que le sirva a los hijos del matemático para
verificar sus respuestas. La función recibe una matriz cuadrada, 
una operación y retorna la matriz modificada según las reglas 
del juego.  

Su solución debe tener una función de acuerdo con la siguiente especificación:

    Nombre de la función: pintar_x  

Si lo requiere, puede agregar funciones adicionales. 

Descripción de parámetros:

Nombre              Tipo             Descripción
matriz              list     Matriz cuadrada con números positivos.
operacion           str      Cadena con el símbolo de la operación 
                             a realizar. El símbolo puede 
                             ser '+', '-', '*' o '/'.

Descripción de retorno:

Tipo                   Descripción
list       La matriz modificada según la operación indicada.  
"""

def pintar_x(matriz, operacion):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:  # Verificar si la celda está en alguna de las diagonales
                if operacion == '+':
                    matriz[i][j] *= 2
                elif operacion == '-':
                    matriz[i][j] = 0
                elif operacion == '*':
                    matriz[i][j] **= 2
                elif operacion == '/':
                    matriz[i][j] = 1
    return matriz