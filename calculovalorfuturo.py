# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:51:43 2024

@author: aepp1
"""

capital=float(input("Capital inicial: "))
tasa=float(input("Ingrese tasa anual: "))
tiempo=float(input("Ingrese el tiempo: "))

valor_futuro = capital* (1+(tasa/100))**tiempo

print("El valor futuro del monto inicial es de "+str(valor_futuro)+", trancurridos "+str(tiempo)+ "años y a una tasa del "+str(tasa)+"% anual")
