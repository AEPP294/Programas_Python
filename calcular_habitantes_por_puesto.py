# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:21:36 2024

@author: andres

Reto 7: Calcular capacidad en universidades

Construya la función calcular_habitantes_por_puesto que calcule la cantidad de
habitantes que hay en un país, por cada estudiante inscrito en una universidad
de ese país y clasificada en el ranking TIMES.

La función recibe dos DataFrames. El primero tiene la información sobre la 
población de cada país organizada en tres columnas: 'Pais', 'Poblacion' y
'Edad_mediana'. El segundo tiene la información sobre universidades organizada 
en tres columnas: 'country', con el nombre del país; 'university_name', con el nombre de una universidad del ranking; y 'num_students', con el número de estudiantes inscritos en esa universidad.

Su función debe retornar un DataFrame con las siguientes condiciones:

    Una columna llamada 'Pais' con el nombre de los países.

    Una columna llamada 'habitantes_por_puesto'. 

En esta última columna aparecerá la cantidad de habitantes de cada país, 
dividida por la cantidad total de estudiantes que hay en las universidades del 
país que aparecen en el ranking TIMES. Por ejemplo, si la población de 
Australia es de 25 millones de personas y hay 31 universidades que en total
atienden a 740.000 estudiantes, entonces la cantidad de 'habitantes_por_puesto'
será 33.8 (el número debe redondearse a 1 cifra decimal). Además, el DataFrame
resultante debe estar ordenado de menor a mayor de acuerdo con la cantidad de
'habitantes_por_puesto'.

Nota: para ordenar los resultados no tenga en cuenta las aproximaciones.
Su solución debe tener una función de acuerdo con la siguiente especificación: 

    Nombre de la función: calcular_habitantes_por_puesto

Si lo requiere, puede agregar funciones adicionales.

Descripción de parámetros:

Nombre                       Tipo                 Descripción
poblacion                  DataFrame      DataFrame con las columnas 'Pais', 
                                          'Poblacion' y 'Edad_mediana'. Este 
                                          DataFrame está desordenado.      

universidades              DataFrame   	  DataFrame con las columnas 'country',
                                          'num_students' y 'university_name'. 
                                          Este DataFrame está desordenado.

Descripción del retorno:
 
Tipo                      	 Descripción

DataFrame             DataFrame con las columnas 'Pais' y 
                      'habitantes_por_puesto', ordenado de menor a mayor de 
                      acuerdo con la columna 'habitantes_por_puesto'.      
"""

import pandas as pd

def calcular_habitantes_por_puesto(poblacion, universidades):
    """
    Calcula la cantidad de habitantes por puesto de estudiantes en universidades del ranking TIMES.

    Args:
        poblacion (DataFrame): DataFrame con las columnas 'Pais', 'Poblacion' y 'Edad_mediana'.
        universidades (DataFrame): DataFrame con las columnas 'country', 'num_students' y 'university_name'.

    Returns:
        DataFrame: DataFrame con las columnas 'Pais' y 'habitantes_por_puesto', ordenado de menor a mayor.
    """
    # Agrupamos las universidades por país y sumamos el número de estudiantes
    estudiantes_por_pais = universidades.groupby('country')['num_students'].sum().reset_index()
    
    # Unimos la información de población y estudiantes por país
    datos_completos = pd.merge(poblacion, estudiantes_por_pais, left_on='Pais', right_on='country')
    
    # Calculamos la cantidad de habitantes por puesto de estudiantes (redondeado a 1 decimal)
    datos_completos['habitantes_por_puesto'] = datos_completos['Poblacion'] / datos_completos['num_students']
    datos_completos['habitantes_por_puesto'] = datos_completos['habitantes_por_puesto'].round(1)
    
    # Seleccionamos las columnas relevantes y ordenamos por habitantes_por_puesto
    resultado = datos_completos[['Pais', 'habitantes_por_puesto']].sort_values(by='habitantes_por_puesto')
    
    return resultado

# Ejemplo de uso
data_poblacion = {
    'Pais': ['Australia', 'Canadá', 'Estados Unidos', 'Brunei'],
    'Poblacion': [25000000, 38000000, 330000000, 400000],
    'Edad_mediana': [38, 41, 38, 31]
}

data_universidades = {
    'country': ['Australia', 'Canadá', 'Estados Unidos', 'Brunei'],
    'num_students': [740000, 900000, 800000, 333333],
    'university_name': ['UniA', 'UniB', 'UniC', 'UniD']
}

df_poblacion = pd.DataFrame(data_poblacion)
df_universidades = pd.DataFrame(data_universidades)

resultado_ejemplo = calcular_habitantes_por_puesto(df_poblacion, df_universidades)
print("Resultado:")
print(resultado_ejemplo)
