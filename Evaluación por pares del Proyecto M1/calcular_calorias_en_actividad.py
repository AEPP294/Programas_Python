# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:56:06 2024

@author: andre
"""

import calculadoraindicessalud as calc

def calcular_calorias_en_actividad()->None:
    peso = float(input("Ingrese el peso en kilogramos: "))
    altura = float(input("Ingrese la altura en centimetros: "))
    edad = float(input("Ingrese la edad: "))
    valor_genero= float(input("Ingrese 5 si es hombre y -161 si es mujer: "))
    valor_actividad= float(input("Ingrese el valor de la tabla segun su actividad fisica semanal: "))
    calorias_reposo=calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print("La cantidad de calorias en reposo es de " + str(round(calorias_reposo,2)) + " cal")

def iniciar_aplicacion()->None:
    calcular_calorias_en_actividad()
    
    
print("En esta funcion se calcula la cantidad de calorias de una persona segun su actividad: ")
print("1.2: poco o ningún ejercicio")
print("1.375: ejercicio ligero (1 a 3 días a la semana)")
print("1.55: ejercicio moderado (3 a 5 días a la semana)")
print("1.725: deportista (6 -7 días a la semana)")
print("1.9: atleta (entrenamientos mañana y tarde)")
print(" \n")
iniciar_aplicacion()