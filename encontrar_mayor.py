# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:14:20 2024

@author: andres

Escriba una función que encuentre el mayor número en una lista de 
enteros positivos. En caso de que la lista esté vacía, se debe 
retornar-1.  

Nombre de la función: encontrar_mayor

Descripción de parámetros:

Nombre                Tipo                Descripción
entrada               list          Lista en la que se buscará.

Descripción de retorno:
Tipo                  Descripción
int            El número mayor en la lista. Si la lista
               está vacía retorna -1. 
"""

def encontrar_mayor(entrada: list) -> int:
    # Verificar si la lista está vacía
    if not entrada:
        return -1
    # Retornar el mayor número en la lista
    return max(entrada)

# Ejemplo de uso
mi_lista = [10, 80, 30, 40, 50]
mayor_numero = encontrar_mayor(mi_lista)
print(f"El mayor número en la lista es: {mayor_numero}")
