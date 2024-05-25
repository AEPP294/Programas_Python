# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:44:22 2024

@author: aepp1
En el taller de regalos de Santa Claus, el CTE (Chief Technology Elf) ha 
decidido implementar un nuevo sistema de clasificación de regalos, para 
facilitar su organización. Cada paquete tiene ahora un identificador numérico
único. El identificador es un número entero entre 100 y 999 y sirve para
clasificar los regalos de la siguiente manera.

    Si el número es palíndromo e impar, el regalo corresponde a una niña.

    Si el número es palíndromo y par, el regalo corresponde a un niño.

    Si el número es par pero no es palíndromo, el regalo corresponde a un hombre.

    Si el número es impar pero no es palíndromo, el regalo corresponde a una mujer.

Escriba una función que ayude al CTE a calcular, dado un identificador único 
de regalo, a qué tipo de persona corresponde dicho regalo.

Su solución debe tener una función de acuerdo con la siguiente especificación:

    Nombre de la función: clasificar_regalo

Si lo requiere, puede agregar funciones adicionales.

Descripción de parámetros:

Nombre    Tipo       Descripción
 id       int    El identificador del regalo cuyo tipo de persona se quiere calcular.

Descripción del retorno:

Tipo    Descripción   
str   Si el número es palíndromo e impar, el regalo corresponde a una niña, 
      y se retorna "girl". Si el número es palíndromo y par, el regalo 
      corresponde a un niño, y se retorna "boy". Si el número es par, pero
      no palíndromo, el regalo corresponde a un hombre, y se retorna "man". 
      Si el número es impar, pero no palíndromo, el regalo corresponde 
      a una mujer, y se retorna "woman"
"""


def clasificar_regalo(n):
    # Verificar si n es un palíndromo
    if es_palindromo(n):
        # Si n es impar, el regalo corresponde a una niña
        if n % 2 != 0:
            return "girl"
        # Si n es par, el regalo corresponde a un niño
        else:
            return "boy"
    else:
        # Si n es par pero no es palíndromo, el regalo corresponde a un hombre
        if n % 2 == 0:
            return "man"
        # Si n es impar pero no es palíndromo, el regalo corresponde a una mujer
        else:
            return "woman"
        
def es_palindromo(n):
    # Convertir el número a string
    n_str = str(n)
    # Verificar si el string es igual a su reverso
    return n_str == n_str[::-1]

