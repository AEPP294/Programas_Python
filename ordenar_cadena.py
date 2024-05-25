# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:38:25 2024

@author: andres
Escriba una función que reciba una cadena de caracteres (str) por parámetro y
retorne dicha cadena ordenada alfabéticamente. Por ejemplo, si se recibe 
la palabra "bca", el retorno correcto sería "abc".

Suponga que las palabras que su función deberá ordenar están compuestas
únicamente del alfabeto inglés en minúsculas. La cadena no tiene espacios.

Su solución debe tener una función de acuerdo con la siguiente especificación:

    Nombre de la función: ordenar_cadena

Si lo requiere, puede agregar funciones adicionales.

Descripción de parámetros:

Nombre              Tipo             Descripción
cadena              str        La cadena de texto por ordenar

Descripción de retorno:

Tipo               Descripción
str           La cadena que se recibió por parámetro 
              ordenada alfabéticamente
"""

def ordenar_cadena(cadena: str) -> str:
    # Convertir la cadena en una lista de caracteres y ordenarla
    cadena_ordenada = sorted(cadena)
    # Unir la lista ordenada de caracteres en una cadena y retornarla
    return ''.join(cadena_ordenada)

# Ejemplo de uso
cadena_ejemplo = "bca"
cadena_ordenada = ordenar_cadena(cadena_ejemplo)
print(f"La cadena ordenada es: {cadena_ordenada}")


