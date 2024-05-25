# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:20:47 2024

@author: andres

Reto 13: Estadísticas de las tareas

Como parte de una iniciativa de analítica sobre el desempeño de 
los estudiantes para identificar las dificultades que tienen en un 
curso, se recopilaron las notas que obtuvieron en diferentes tareas.
Ahora, queremos analizarlas con un pequeño programa que usted tendrá 
que construir.

La información obtenida está organizada en un diccionario donde las
llaves son los nombres de los estudiantes (cadenas de caracteres) y 
los valores son diccionarios.

En estos diccionarios "internos", las llaves son los nombres de las
tareas y los valores son las notas obtenidas por el estudiante para 
esa tarea (un número entero entre 0 y 100).

Es decir, si el único estudiante en la muestra se llama "Roberto" y 
ha realizado dos tareas ("Tarea 1" y "Tarea 2" con notas de 80 y 90 
respectivamente), el diccionario de diccionarios con esta información
se vería en Python de la siguiente forma:
    {"Roberto": {"Tarea 1": 80, "Tarea 2" : 90}}.

Tenga cuidado: no todos los estudiantes resolvieron todas las tareas.
Usted debe construir una función que, dados los resultados de los 
estudiantes, calcule las siguientes estadísticas para una tarea dada
su nombre: la mayor nota obtenida, el nombre del estudiante que obtuvo
la mejor nota, la menor nota obtenida, el nombre del estudiante que 
obtuvo la peor nota, el promedio de las notas de los estudiantes, 
la cantidad de estudiantes que recibieron una nota y la suma de las 
notas obtenidas por los estudiantes.

La función debe retornar un diccionario con las siguientes llaves:
    "mayor", "mejor", "menor", "peor", "promedio", "cantidad" y "total".

Su solución debe tener una función de acuerdo con la siguiente 
especificación: 

    Nombre de la función: calcular_estadisticas_tarea   

Si lo requiere, puede agregar funciones adicionales. 

Descripción de parámetros:

Nombre                      Tipo              Descripción
estudiantes_tareas          dict      Un diccionario de diccionarios 
                                     con la información de los 
                                     estudiantes y sus tareas.  

nombre_tarea                str      El nombre de la tarea para la que
                                     se quiere calcular las estadísticas  

Descripción de retorno:

Tipo                   Descripción
dict           Un diccionario con las llaves "mayor", "mejor", 
              "menor", "peor", "promedio", "cantidad" y 
              "total" que representan: la mayor nota, el nombre del 
              estudiante con la mejor nota, la peor nota, el nombre
              del estudiante con la peor nota, el promedio, la 
              cantidad de estudiantes que hicieron la tarea y el valor
              total que resulta de sumar todas las notas obtenidas en
              esa tarea.  
"""

def calcular_estadisticas_tarea(estudiantes_tareas: dict, nombre_tarea: str) -> dict:
    # Inicializar variables para las estadísticas
    mayor_nota = float('-inf')
    mejor_estudiante = None
    menor_nota = float('inf')
    peor_estudiante = None
    suma_notas = 0
    cantidad_estudiantes = 0

    # Recorrer los estudiantes y sus notas para la tarea dada
    for estudiante, tareas in estudiantes_tareas.items():
        if nombre_tarea in tareas:
            nota = tareas[nombre_tarea]
            suma_notas += nota
            cantidad_estudiantes += 1

            # Actualizar la mayor y menor nota
            if nota > mayor_nota:
                mayor_nota = nota
                mejor_estudiante = estudiante
            if nota < menor_nota:
                menor_nota = nota
                peor_estudiante = estudiante

    # Calcular el promedio y el valor total
    promedio = suma_notas / cantidad_estudiantes
    valor_total = suma_notas

    # Crear el diccionario con las estadísticas
    estadisticas = {
        "mayor": mayor_nota,
        "mejor": mejor_estudiante,
        "menor": menor_nota,
        "peor": peor_estudiante,
        "promedio": promedio,
        "cantidad": cantidad_estudiantes,
        "total": valor_total
    }

    return estadisticas

# Ejemplo de uso
estudiantes_tareas_ejemplo = {
    "Roberto": {"Tarea 1": 80, "Tarea 2": 90},
    "Ana": {"Tarea 1": 70, "Tarea 3": 85},
    # ... más estudiantes ...
}

nombre_tarea_ejemplo = "Tarea 1"
resultados = calcular_estadisticas_tarea(estudiantes_tareas_ejemplo, nombre_tarea_ejemplo)
print(resultados)
