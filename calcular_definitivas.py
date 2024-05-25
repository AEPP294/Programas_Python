# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:08:42 2024

@author: andres

Reto 7: Aproximación de notas

Una clase de la Universidad de los Andes tiene las siguientes reglas 
con respecto a las aproximaciones de las notas finales.  

    Si la nota es mayor o igual a 4.5, la nota se aproxima a 5.0.
    Si la nota es mayor o igual a 3.5 y menor a 4.5, la nota 
       se aproxima a 4.0.
    Si la nota es mayor o igual a 2.5 y menor a 3.5, la nota se 
       aproxima a 3.0.

De lo contrario, la nota asignada será 1.5.  

Teniendo una lista de diccionarios en donde cada uno corresponde a un
estudiante y que tiene como llaves "nombre" y "nota" (sin aproximar),
retorne una lista con todos los diccionarios actualizados con sus 
notas después de aproximación.

Cada uno de los diccionarios retornados tiene las llaves "nombre" 
y "nota"(aproximada).
Se garantiza que la lista tiene al menos un diccionario.  
Su solución debe tener una función de acuerdo con la siguiente 
especificación: 

    Nombre de la función: calcular_definitivas

Si lo requiere, puede agregar funciones adicionales. 

Descripción de parámetros:

    Nombre                  Tipo              Descripción
 estudiantes                list    Lista de diccionarios que 
                                    representan a los estudiantes que 
                                    han finalizado el curso con su 
                                    nota final sin aproximar.
                                    Cada diccionario tiene las 
                                    siguientes llaves: "nombre": (str) el nombre del estudiante. 
                                    "nota": (float), un float que 
                                    representa la nota sin aproximar del estudiante  

Descripción de retorno:
Tipo                        Descripción
list            Lista de diccionarios, con la misma cantidad que en 
                la lista inicial, pero con sus notas aproximadas. 
                El orden de los diccionarios debe ser el mismo que
                en la lista de entrada. Cada uno de los diccionarios 
                retornados debe tener las llaves: "nombre" (str) y 
                "nota" (float).  
"""

def calcular_definitivas(estudiantes: list) -> list:
    # Función para aproximar la nota de un estudiante
    def aproximar_nota(nota):
        if nota >= 4.5:
            return 5.0
        elif 3.5 <= nota < 4.5:
            return 4.0
        elif 2.5 <= nota < 3.5:
            return 3.0
        else:
            return 1.5

    # Recorrer la lista de estudiantes y actualizar sus notas
    for estudiante in estudiantes:
        estudiante['nota'] = aproximar_nota(estudiante['nota'])
    
    return estudiantes

# Ejemplo de uso
estudiantes = [
    {'nombre': 'Juan', 'nota': 4.6},
    {'nombre': 'Ana', 'nota': 3.7},
    {'nombre': 'Luis', 'nota': 2.3},
    {'nombre': 'Sofía', 'nota': 4.2}
]

estudiantes_con_notas_definitivas = calcular_definitivas(estudiantes)
print(estudiantes_con_notas_definitivas)
