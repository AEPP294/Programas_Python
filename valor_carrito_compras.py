# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:48:11 2024

@author: andres

Reto 11: Costo total de un carro de compras

Catalina necesita llevar un mejor control de sus gastos cuando hace 
mercado. Para esto, ha decidido construir una aplicación para registrar
cada producto que agregue en su carrito de compras. Estos datos son 
guardados en un diccionario cuyas llaves corresponden a los nombres 
de los productos. El valor asociado a cada llave es el precio del 
producto correspondiente.

Cree una función que retorne el valor total del carrito de compras. 
Esto es, la suma de los precios individuales de todos los productos que
están en el carrito. Su solución debe tener una función de acuerdo con
la siguiente especificación: 

    Nombre de la función: valor_carrito_compras  

Si lo requiere, puede agregar funciones adicionales

Descripción de parámetros:

Nombre                 Tipo            Descripción
carrito_compras        dict        Diccionario que contiene los nombres
                                   de los productos del carro de compras
                                   como llaves y sus respectivos precios
                                   como valores.  

Descripción de retorno:

Tipo                     Descripción
float       Valor total del carro de compras. Si el carro de compras
            está vacío, retornará el valor cero.  
"""

def valor_carrito_compras(carrito_compras: dict) -> float:
    # Sumar los precios de todos los productos en el carrito
    return sum(carrito_compras.values()) if carrito_compras else 0.0

# Ejemplo de uso
carrito_ejemplo = {
    'pan': 1500,
    'leche': 2300,
    'huevos': 3500
}

valor_total = valor_carrito_compras(carrito_ejemplo)
print(f"El valor total del carrito de compras es: {valor_total}")
