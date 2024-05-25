# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:49:32 2024

@author: andres
"""

import calculadoraindicessalud as calc

def calcular_calorias_en_reposo()->None:
    peso = float(input("Ingrese el peso en kilogramos: "))
    altura = float(input("Ingrese la altura en centimetros: "))
    edad = float(input("Ingrese la edad: "))
    valor_genero= float(input("Ingrese 5 si es hombre y -161 si es mujer: "))
    calorias_reposo=calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print("La cantidad de calorias en reposo es de " + str(round(calorias_reposo,2)) + " cal")

def iniciar_aplicacion()->None:
    calcular_calorias_en_reposo()
    
    
print("En esta funcion se calcula la cantidad de calorias de una persona en reposo ")
iniciar_aplicacion()