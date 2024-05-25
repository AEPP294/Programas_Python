# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:07:50 2024

@author: andres
Escriba una función que reciba una lista y un número entero a buscar,
y que retorne un entero que indique el índice en que se encuentra 
este elemento.

En caso de que el elemento se encuentre más de una vez dentro de 
la lista, debe retornar la primera posición en que lo encuentre.

En caso de no encontrar el número, retorne -1.

   Nombre de la función: buscar_elemento
 

Descripción de parámetros:

Nombre                  Tipo              Descripción
entrada                 list    Lista en la que se buscará el número
buscado                 int 	Número entero a buscar

Descripción de retorno:

Tipo                      Descripción
int                   Número que indica el índice en el que 
                      se encuentra el elemento buscado, 
                      si no lo encuentra retorna -1.

"""

def buscar_elemento(entrada: list, buscado: int) -> int:
    try:
        # Buscar el índice del elemento en la lista
        indice = entrada.index(buscado)
        return indice
    except ValueError:
        # Si el elemento no se encuentra en la lista, retornar -1
        return -1
    
# Ejemplo de uso
mi_lista = [10, 20, 30, 40, 20, 50]
numero_buscado = 20
resultado = buscar_elemento(mi_lista, numero_buscado)
print(f"El índice del número {numero_buscado} es: {resultado}")