# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:42:11 2024

@author: aepp1
"""

import math

def velocidad_en_caida_libre(altura):
    # Velocidad inicial
    v0 = 0
    # Aceleración debido a la gravedad
    a = 9.8
    # Distancia al suelo
    d = altura
    # Calcular la velocidad final
    vf = math.sqrt(v0**2 + 2*a*d)
    # Redondear el resultado a dos decimales
    vf_rounded = round(vf, 2)
    return vf_rounded

altura_objeto = float(input("Ingrese la altura desde la que se soltó el objeto (en metros): "))
velocidad_final = velocidad_en_caida_libre(altura_objeto)
print("La velocidad final del objeto al tocar el suelo es:", velocidad_final, "m/s")
