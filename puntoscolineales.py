# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:21:47 2024

@author: aepp1
"""

def son_colineales(x1:int,y1:int,x2:int,y2:int,x3:int,y3:int)->int:
    pendiente_1=(y2-y1)/(x2-x1)
    pendiente_2=(y3-y2)/(x3-x2)
    
    return pendiente_1 == pendiente_2