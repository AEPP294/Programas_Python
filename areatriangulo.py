# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:45:31 2024

@author: aepp1
"""
import math

def area_triangulo(s1: float,s2: float,s3_float)->float:
   s=(s1+s2+s3)/2
   area= math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
   return area

s1 = float(input("Teclee el valor del lado 1: "))
s2 = float(input("Teclee el valor del lado 2: "))
s3 = float(input("Teclee el valor del lado 3: "))
print("El área del triangulo es: ", str(area_triangulo(s1,s2,s3)))

