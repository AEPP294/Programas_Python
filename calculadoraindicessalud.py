# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:42:21 2024

@author: andres
"""

def calcular_IMC(peso: float, altura: float)->float:
    imc=peso/(altura**2)
    return imc

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: int)->float:
    gc=1.2*calcular_IMC(peso,altura)+0.23*edad-5.4-valor_genero
    return gc

def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: float)->float:
    TMB = ((10*peso) + (6.25*altura) - (5*edad)) + valor_genero
    return TMB

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero:int, valor_actividad:float)->float:
    
    TMB = (10*peso) + (6.25*altura) - (5*edad) + valor_genero
    calorias_actividad =  TMB * valor_actividad
    return calorias_actividad

def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int, valor_genero:int)->str:
    
    TMB = (10*peso) + (6.25*altura) - (5*edad) + valor_genero
    rango1 = TMB * 0.8
    rango2 = TMB * 0.85
    
    return "Para adelgazar es recomendado que consumas entre: "+ str(round(rango1,2)) + " y " + str(round(rango2,2))+ " calorías al día. Siendo "+ str(round(rango1,2))+ "el rango inferior y" + str(round(rango2,2)) "el rango superior"                                     


    