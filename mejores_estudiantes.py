# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:16:02 2024

@author: andres

Reto 5: Buscar los mejores estudiantes

Construya una función que reciba un DataFrame con información sobre el 
desempeño de un conjunto de estudiantes en 5 materias y retorne un DataFrame 
con información sobre los mejores estudiantes.

El DataFrame que recibe la función tiene 6 columnas: 'nombre', donde aparecen 
los nombres de los estudiantes, 'matematicas', 'ingles', 'ciencias', 
'literatura' y 'arte', en las cuales aparecen las calificaciones de los estudiantes en cada una de esas materias. Las calificaciones son números decimales entre 0 y 5.0.

La función debe retornar un DataFrame con dos columnas: 'nombre', donde 
aparecen los nombres de los estudiantes; y 'promedio', donde aparecen los 
promedios de sus calificaciones redondeados a dos decimales. El DataFrame 
resultante, debe estar ordenado de mayor a menor promedio y solo deben aparecer los estudiantes cuyo promedio haga parte del mejor 25%.

Nota: para ordenar los resultados y seleccionar el mejor 25%, no tenga en 
cuenta las aproximaciones.

Su solución debe tener una función de acuerdo con la siguiente especificación: 

    Nombre de la función: mejores_estudiantes

Si lo requiere, puede agregar funciones adicionales.

Descripción de parámetros:

Nombre                Tipo                    Descripción
estudiantes         DataFrame     DataFrame con las columnas 'nombre', 
                                 'matematicas', 'ingles', 'ciencias',  
                                 'literatura' y 'arte'.    

Descripción del retorno:

Tipo                              Descripción
DataFrame        DataFrame con las columnas 'nombre' y 'promedio', ordenado de
                 forma descendente con respecto al promedio. En este 
                 DataFrame, aparecerá el 25% de los estudiantes del DataFrame
                 original. Por ejemplo, si el DataFrame tenía las 
                 calificaciones de 19 estudiantes, en el resultado aparecerán
                 los 4 mejores estudiantes.
"""

import pandas as pd

def mejores_estudiantes(estudiantes):
    """
    Retorna un DataFrame con los mejores estudiantes basados en sus promedios.

    Args:
        estudiantes (DataFrame): DataFrame con las columnas 'nombre', 'matematicas', 'ingles',
                                 'ciencias', 'literatura' y 'arte'.

    Returns:
        DataFrame: DataFrame con las columnas 'nombre' y 'promedio', ordenado de mayor a menor promedio.
    """
    # Calculamos el promedio de calificaciones para cada estudiante
    estudiantes['promedio'] = estudiantes[['matematicas', 'ingles', 'ciencias', 'literatura', 'arte']].mean(axis=1)
    
    # Ordenamos el DataFrame por promedio de forma descendente
    estudiantes_ordenados = estudiantes.sort_values(by='promedio', ascending=False)
    
    # Calculamos el número de estudiantes que deben aparecer en el resultado (25%)
    num_estudiantes_resultado = int(len(estudiantes) * 0.25)
    
    # Seleccionamos los mejores estudiantes (primer 25%)
    mejores_estudiantes = estudiantes_ordenados.head(num_estudiantes_resultado)
    
    # Retornamos el DataFrame con las columnas 'nombre' y 'promedio'
    return mejores_estudiantes[['nombre', 'promedio']]

# Ejemplo de uso
data = {
    'nombre': ['Ana', 'Carlos', 'Elena', 'David', 'Fernando'],
    'matematicas': [4.5, 3.8, 4.2, 4.9, 4.0],
    'ingles': [4.8, 4.0, 4.5, 4.7, 3.9],
    'ciencias': [4.3, 4.1, 4.6, 4.8, 4.2],
    'literatura': [4.7, 4.2, 4.4, 4.9, 4.1],
    'arte': [4.6, 4.3, 4.5, 4.8, 4.0]
}

df_estudiantes = pd.DataFrame(data)
resultado_ejemplo = mejores_estudiantes(df_estudiantes)
print("Resultado:")
print(resultado_ejemplo)
