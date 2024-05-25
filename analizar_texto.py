# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:56:33 2024

@author: andres

Módulo 4

Reto 2: Analizador léxico

Construya una función que reciba como parámetros un texto (cadena de 
caracteres) y una lista de caracteres permitidos (lista de cadenas de 
caracteres), y que retorne un diccionario con información sobre las palabras 
contenidas en el texto. 

La función debe construir un diccionario en el que las llaves son todas 
las palabras que aparecen en el texto, ignorando si en el texto aparecen en 
mayúsculas o minúsculas. Sin embargo, las llaves del diccionario deben ser 
sólo cadenas en minúscula.

Cada una de las llaves, debe tener asociada una tupla con tres valores de tipo
entero: el primero indica la cantidad de veces que aparece la palabra en el 
texto, el segundo indica la primera posición en la que aparece la palabra, y 
el tercero indica la última posición en la que aparece. Si la palabra aparece 
una sola vez en el texto, el segundo y el tercer valor serán iguales.

La lista de caracteres permitidos indica qué caracteres pueden hacer parte de 
las palabras, cualquier carácter que no haga parte de esta lista debe tratarse
como si fuera un espacio o un signo de puntuación.

Nota: las posiciones hacen referencia a las posiciones en el texto original 
que la función recibe como parámetro, contadas desde 0.

Veamos un ejemplo en el que los caracteres permitidos son todos los caracteres
del español, incluyendo las vocales acentuadas. Suponga que el texto que se 
va a analizar es el siguiente: "Muchos años después, frente al pelotón de 
fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde 
remota en que su padre lo llevó a conocer el hielo."

En el diccionario resultante deben aparecer las siguientes palabras, de las 
cuales sólo dos se repiten: 'a', 'al', 'aquella', 'aureliano','años', 
'buendía', 'conocer', 'coronel', 'de', 'después', 'el', 'en','frente', 
'fusilamiento', 'había', 'hielo', 'llevó', 'lo', 'muchos', 'padre', 'pelotón',
'que', 'recordar', 'remota', 'su', 'tarde'.

La palabra 'el' aparece dos veces en el texto, la primera a partir de la 
posición 56 y la segunda a partir de la posición 159. Tenga cuidado, la 
aparición de la cadena 'el' dentro de la palabra 'hielo' no se tiene en cuenta
porque no es una palabra completa.

La otra palabra que se repite en este texto es la palabra 'de', que aparece 
a partir de las posiciones 39 y 91. Tenga cuidado de no contar la aparición de
la sílaba 'de' en la palabra 'después'.

Su solución debe tener una función de acuerdo con la siguiente especificación: 

    Nombre de la función: analizar_texto

Si lo requiere, puede agregar funciones adicionales.

Descripción de parámetros:

Nombre                 Tipo               Descripción
texto                   str     La cadena de caracteres que se va a analizar.    
caracteres_permitidos  list     Lista de caracteres que pueden hacer parte de 
                                las palabras que se van a analizar.  

Descripción del retorno:

Tipo                    Descripción
dict           Diccionario donde las llaves son todas las palabras que 
               aparecen en el texto y los valores son tuplas con tres
               números enteros.      
"""

def analizar_texto(texto, caracteres_permitidos):
    """
    Analiza un texto y devuelve un diccionario con información sobre las palabras contenidas en él.
    
    Args:
        texto (str): El texto a analizar.
        caracteres_permitidos (list): Lista de caracteres permitidos en las palabras.
        
    Returns:
        dict: Diccionario con información sobre las palabras.
    """
    # Convertimos el texto a minúsculas para que las palabras sean tratadas de manera uniforme
    texto = texto.lower()
    
    # Inicializamos el diccionario para almacenar la información
    resultado = {}
    
    # Dividimos el texto en palabras
    palabras = texto.split()
    
    # Recorremos cada palabra
    for palabra in palabras:
        # Filtramos los caracteres no permitidos
        palabra_filtrada = ''.join(c for c in palabra if c in caracteres_permitidos)
        
        # Si la palabra filtrada no está vacía, la procesamos
        if palabra_filtrada:
            # Si la palabra ya está en el diccionario, actualizamos sus valores
            if palabra_filtrada in resultado:
                cantidad, primera_posicion, _ = resultado[palabra_filtrada]
                cantidad += 1
            else:
                # Si es la primera vez que encontramos la palabra, inicializamos sus valores
                cantidad = 1
                primera_posicion = texto.find(palabra_filtrada)
            
            # Actualizamos la última posición
            ultima_posicion = texto.rfind(palabra_filtrada)
            
            # Guardamos la información en el diccionario
            resultado[palabra_filtrada] = (cantidad, primera_posicion, ultima_posicion)
    
    return resultado

# Ejemplo de uso
texto_ejemplo = "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo."
caracteres_permitidos_ejemplo = "abcdefghijklmnopqrstuvwxyzáéíóúüñ"
resultado_ejemplo = analizar_texto(texto_ejemplo, caracteres_permitidos_ejemplo)
print("Resultado:", resultado_ejemplo)


