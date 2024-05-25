# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:45:45 2024

@author: aepp1
"""

def calcular_edad(nacimiento, actual):
    # Convertir las fechas a días totales
    nacimiento_dias = nacimiento[0]*360 + nacimiento[1]*30 + nacimiento[2]
    actual_dias = actual[0]*360 + actual[1]*30 + actual[2]

    # Calcular la diferencia en días
    diferencia_dias = actual_dias - nacimiento_dias

    # Convertir la diferencia en años, meses y días
    anos = diferencia_dias // 360
    meses = (diferencia_dias % 360) // 30
    dias = (diferencia_dias % 360) % 30

    # Retornar la edad en el formato solicitado
    return f"{anos},{meses},{dias}"

nacimiento_julieta = [1980, 6, 13]
fecha_actual = [2024, 4, 22]
print(calcular_edad(nacimiento_julieta, fecha_actual))  

