# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:44:06 2024

@author: andre
"""

import calculadoraindicessalud as calc

def calcular_IMC()->None:
    peso = float(input("Ingrese el peso en kilogramos: "))
    altura = float(input("Ingrese la altura en metros: "))
    imc= calc.calcular_IMC(peso, altura)
    print("El indice de masa corporal es:" + str(round(imc,2)))

def iniciar_aplicacion()->None:
    calcular_IMC()
    
    
print("En esta funcion se calcula el índice de masa corporal de una persona ")
iniciar_aplicacion()