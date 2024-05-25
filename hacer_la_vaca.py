# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:46:54 2024

@author: andres

Reto 14: La vaca de cumpleaños

Una clase de estudiantes ejemplares ha decidido hacer una vaca para 
el cumpleaños de su profesor favorito. Para esto, un estudiante 
recorrerá todo el salón recogiendo el dinero que cada estudiante va 
a aportar. Tienen dos opciones de regalo: una botella de licor que
cuesta 120.000 o un pastel que cuesta 35.000. Además, el estudiante 
que más dinero ponga, será el que tenga el honor de darle el regalo 
al profesor. Recree este caso en una función que reciba una matriz
que representa al salón y una cadena que indica el regalo. 
Debe retornar una lista cuya primera posición es un mensaje que 
indica si el dinero alcanzó para la vaca y las siguientes dos 
posiciones son las coordenadas del puesto del estudiante que más 
aportó.  

Su solución debe tener una función de acuerdo con la siguiente 
especificación: 

    Nombre de la función: hacer_la_vaca 

Si lo requiere, puede agregar funciones adicionales.

Descripción de parámetros:

Nombre                Tipo              Descripción
salon                 list     Matriz que representa el salón de 
                               estudiantes, los valores son enteros
                               que representan cuánto dinero aportarán.

vaca                  str      Cadena que indica qué vaca se está 
                               realizando, esta puede ser 'botella' 
                               o 'pastel .

Descripción de retorno:

Tipo                   Descripción
list            Lista cuya primera posición es un str de la forma 
               'Hay Vaca' si se alcanzó la vaca, y 'No Alcanza' 
                de lo contrario. Las siguientes dos posiciones,  
                son las coordenadas del estudiante qué más dinero 
                aportó.  
"""

def hacer_la_vaca(salon: list, vaca: str) -> list:
    # Precios de los regalos
    precios = {'botella': 120000, 'pastel': 35000}
    # Inicializar la suma total y el mayor aporte
    suma_total = 0
    mayor_aporte = 0
    coordenadas_mayor_aporte = (0, 0)

    # Recorrer la matriz para sumar aportes y encontrar el mayor aporte
    for i, fila in enumerate(salon):
        for j, aporte in enumerate(fila):
            suma_total += aporte
            if aporte > mayor_aporte:
                mayor_aporte = aporte
                coordenadas_mayor_aporte = (i, j)

    # Verificar si el dinero alcanza para el regalo seleccionado
    mensaje = 'Hay Vaca' if suma_total >= precios[vaca] else 'No Alcanza'

    return [mensaje, coordenadas_mayor_aporte[0], coordenadas_mayor_aporte[1]]

# Ejemplo de uso
salon_ejemplo = [
    [5000, 10000, 15000],
    [20000, 5000, 25000],
    [30000, 20000, 10000]
]
vaca_ejemplo = 'botella'
resultado = hacer_la_vaca(salon_ejemplo, vaca_ejemplo)
print(resultado)

