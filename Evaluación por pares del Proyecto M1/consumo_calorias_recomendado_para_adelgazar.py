# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:02:23 2024

@author: andres
"""

import calculadoraindicessalud as calc

def consumo_calorias_recomendado_para_adelgazar()->None:
    peso = float(input("Ingrese el peso en kilogramos: "))
    altura = float(input("Ingrese la altura en centimetros: "))
    edad = float(input("Ingrese la edad: "))
    valor_genero= float(input("Ingrese 5 si es hombre y -161 si es mujer: "))
    print(calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero))
    

def iniciar_aplicacion()->None:
    consumo_calorias_recomendado_para_adelgazar()
    
    
print("En esta funcion se calcula el consumo de calorias para adelgazar: ")
print(" \n")
iniciar_aplicacion() 