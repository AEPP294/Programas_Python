# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x1=int(input("Ingrese el valor de x1: "))
x2=int(input("Ingrese el valor de x2: "))
x3=int(input("Ingrese el valor de x3: "))

temporal=x1
x1=x3
x3=x2
x2=temporal
print(str(x1)+","+str(x2)+","+str(x3))