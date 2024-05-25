# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:34:34 2024

@author: andres

Escriba una función que cuente la cantidad de caracteres diferentes que 
aparecen más de una vez en una cadena. Suponga que todas las cadenas se 
componen únicamente de letras minúsculas del alfabeto en inglés.

Su solución debe tener una función de acuerdo con la siguiente especificación:

    Nombre de la función: contar_caracteres_repetidos

Si lo requiere, puede agregar funciones adicionales.

Descripción de parámetros:

Nombre                 Tipo             Descripción
cadena                 str          La cadena por revisar.

Descripción del retorno:

Tipo                 Descripción
int          La cantidad de caracteres diferentes que aparecen
             repetidos en la cadena.        
"""

def contar_caracteres_repetidos(cadena: str) -> int:
    # Crear un diccionario para almacenar la frecuencia de cada caracter
    frecuencia = {}
    
    # Contar la frecuencia de cada caracter en la cadena
    for char in cadena:
        if char in frecuencia:
            frecuencia[char] += 1
        else:
            frecuencia[char] = 1
    
    # Contar la cantidad de caracteres que aparecen más de una vez
    count = 0
    for char, freq in frecuencia.items():
        if freq > 1:
            count += 1
    
    return count

# Ejemplo de uso
cadena_ejemplo = "abracadabra"
resultado = contar_caracteres_repetidos(cadena_ejemplo)
print(f"La cantidad de caracteres diferentes que aparecen repetidos en la cadena es: {resultado}")

