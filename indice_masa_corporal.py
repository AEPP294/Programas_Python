# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:51:37 2024

@author: aepp1
"""
def convertir_peso(peso: float)->float:
    peso_kg = peso*0.45
    return peso_kg

def convertir_altura(altura: float)->float:
    altura_metros = altura*0.025
    return altura_metros
    
def calcular_BMI(peso_kg: float,altura_m: float)->float:
   BMI = peso_kg/(altura_m**2)
   return BMI

peso = float(input("Teclee el valor del peso en libras: "))
altura = float(input("Teclee el valor de la altura en pulgadas: "))
peso_kg = convertir_peso(peso)
altura_m = convertir_altura(altura)

print("El indice de masa corporal es: ", str(calcular_BMI(peso_kg,altura_m)))
