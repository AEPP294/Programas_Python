# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:42:10 2024

@author: andres

Reto 10: Producto más caro de un carro de compras

Catalina necesita llevar un mejor control de sus gastos cuando 
hace mercado. Para esto, ha decidido construir una aplicación para 
registrar cada producto que agregue en su carrito de compras. Estos 
datos son guardados en un diccionario cuyas llaves corresponden a 
los nombres de los productos. El valor asociado a cada llave es 
el precio del producto correspondiente.

Cree una función que retorne el nombre del producto más costoso del
carrito de compras. Si se encuentran dos productos igual de costosos
(siendo los más costosos del carro), la función retorna el menor 
alfabéticamente. Por ejemplo, si los 'bananos' que compra Catalina 
costaran los mismo que las 'chocolatinas', la función retornaría 
'bananos'  

Su solución debe tener una función de acuerdo con la siguiente especificación: 

    Nombre de la función: producto_mas_costoso

Si lo requiere, puede agregar funciones adicionales.

Descripción de parámetros:

    Nombre             Tipo        Descripción
carrito_compras        dict     Diccionario que contiene los nombres de
                                los productos del carrito de compras 
                                como llaves y sus respectivos precios
                                como valores. Todas las llaves están 
                                escritas únicamente con letras 
                                minúsculas.  

Descripción de retorno:

Tipo                      Descripción
str            El nombre del artículo más costoso en el carrito de 
               compras. Si el carrito de compras está vacío, retornará
               la cadena "No hay productos en el carrito".
"""

def producto_mas_costoso(carrito_compras: dict) -> str:
    # Verificar si el carrito de compras está vacío
    if not carrito_compras:
        return "No hay productos en el carrito"
    
    # Encontrar el precio máximo en el carrito de compras
    precio_maximo = float('-inf')
    for producto, precio in carrito_compras.items():
        if precio > precio_maximo:
            precio_maximo = precio
    
    # Encontrar el nombre del artículo más costoso
    articulo_mas_costoso = None
    for producto, precio in carrito_compras.items():
        if precio == precio_maximo:
            if articulo_mas_costoso is None or producto < articulo_mas_costoso:
                articulo_mas_costoso = producto
    
    return articulo_mas_costoso

# Ejemplo de uso
carrito_ejemplo = {
    'manzanas': 5000,
    'bananos': 4500,
    'chocolatinas': 5500,
    'uvas': 5500
}

resultado = producto_mas_costoso(carrito_ejemplo)
print(f"El artículo más costoso en el carrito es: {resultado}")
