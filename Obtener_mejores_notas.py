# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:39:28 2024

@author: andre
"""

def obtener_mejores_notas(*estudiantes):
    # Inicializar el diccionario de mejores notas
    mejores_notas = {
        'matematicas': ('', 0),
        'español': ('', 0),
        'ciencias': ('', 0),
        'literatura': ('', 0),
        'arte': ('', 0)
    }
    
    # Iterar sobre cada estudiante y sus notas
    for estudiante in estudiantes:
        for materia in mejores_notas:
            # Comprobar si la nota actual es mayor o si es igual y el nombre es alfabéticamente menor
            if (estudiante[materia] > mejores_notas[materia][1] or
               (estudiante[materia] == mejores_notas[materia][1] and estudiante['nombre'].lower() < mejores_notas[materia][0].lower())):
                mejores_notas[materia] = (estudiante['nombre'], estudiante[materia])
    
    # Convertir las tuplas en solo nombres para el resultado final
    resultado_final = {materia: nombre for materia, (nombre, _) in mejores_notas.items()}
    
    return resultado_final

# Ejemplo de uso de la función
estudiantes = [
    {'nombre': 'Ana', 'matematicas': 4.5, 'español': 4.0, 'ciencias': 4.2, 'literatura': 4.8, 'arte': 5.0},
    {'nombre': 'Luis', 'matematicas': 4.6, 'español': 4.1, 'ciencias': 4.3, 'literatura': 4.9, 'arte': 4.9},
    # ... Añadir el resto de los estudiantes aquí
]

mejores_estudiantes = obtener_mejores_notas(*estudiantes)
print(mejores_estudiantes)
