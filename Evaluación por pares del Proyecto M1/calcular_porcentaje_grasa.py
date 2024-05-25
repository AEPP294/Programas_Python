# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:29:28 2024

@author: andres
"""

import calculadoraindicessalud as calc

def calcular_porcentaje_grasa()->None:
    peso = float(input("Ingrese el peso en kilogramos: "))
    altura = float(input("Ingrese la altura en metros: "))
    edad = float(input("Ingrese la edad: "))
    valor_genero= float(input("Ingrese 10.8 si es hombre y 0 si es mujer: "))
    porcentaje_grasa=calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print(porcentaje_grasa)
    print("El porcentaje de grasa es del " + str(round(porcentaje_grasa,2)) + "%")

def iniciar_aplicacion()->None:
    calcular_porcentaje_grasa()
    
    
print("En esta funcion se calcula el porcetaje de grasa de una persona ")
iniciar_aplicacion()