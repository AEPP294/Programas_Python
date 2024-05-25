# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:36:16 2024

@author: andres

Reto 9: El novio tacaño

Nicolás es un novio muy amoroso, pero tiene fama de ser tacaño. Para 
el cumpleaños de su novia ha pedido un catálogo de artículos para 
escoger el regalo más barato disponible. El catálogo es un diccionario
que tiene varias llaves que corresponden al nombre de los productos. 
El valor asociado a cada llave es el precio del producto.

Cree una función que retorne el nombre del artículo más barato en el
catálogo. Si Nicolás encuentra dos artículos igual de baratos, 
comprará el que tenga el nombre alfabéticamente menor 
(el que aparecería antes en el diccionario ignorando las mayúsculas 
y minúsculas).

Si el artículo más barato vale más de 10.000 pesos, Nicolás no 
comprará nada e invitará a su novia a ver una película en su casa.  
Su solución debe tener una función de acuerdo con la siguiente 
especificación:

    Nombre de la función: producto_mas_barato  

Si lo requiere, puede agregar funciones adicionales. 

Descripción de parámetros:

Nombre             Tipo             Descripción
catalogo           dict    Diccionario que contiene los nombres de los
                           productos como llaves y sus respectivos
                           precios como valores.  

Descripción de retorno:

Tipo               Descripción
str        El nombre del artículo más barato en el catálogo. Si no hay
           ningún artículo que valga menos de 10.000, retornará None. 
           Si el catálogo está vacío, retornará la cadena 
           "No hay productos para escoger".  
"""

def producto_mas_barato(catalogo: dict) -> str:
    # Verificar si el catálogo está vacío
    if not catalogo:
        return "No hay productos para escoger"
    
    # Encontrar el precio mínimo en el catálogo
    precio_minimo = float('inf')
    for producto, precio in catalogo.items():
        if precio < precio_minimo:
            precio_minimo = precio
    
    # Encontrar el nombre del artículo más barato
    articulo_mas_barato = None
    for producto, precio in catalogo.items():
        if precio == precio_minimo:
            if articulo_mas_barato is None or producto.lower() < articulo_mas_barato.lower():
                articulo_mas_barato = producto
    
    # Verificar si el artículo más barato vale menos de 10.000 pesos
    if precio_minimo <= 10000:
        return articulo_mas_barato
    else:
        return None

# Ejemplo de uso
catalogo_ejemplo = {
    'Camiseta': 8000,
    'Zapatos': 12000,
    'Gafas de sol': 9500,
    'Bufanda': 7500
}

resultado = producto_mas_barato(catalogo_ejemplo)
print(f"El artículo más barato es: {resultado}")

