# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:17:21 2024

@author: andres

Reto 8: Ash y la liga Kalos

Ash Ketchum, el personaje principal del anime Pokémon, está a punto de
luchar en la final de la liga Kalos. En estos eventos compiten los 
mejores entrenadores del mundo en batallas donde cada entrenador puede
tener 3, 4, 5 o 6 criaturas. Ash quiere saber, para una cantidad de 
criaturas específica, si él podrá formar un equipo únicamente con 
Pokémon seudolegendarios para competir en la final. Un pokemon 
seudolegendario es aquel que en la suma de sus estadísticas de combate
tiene 600 puntos o más.

Las estadísticas de combate de cada pokemon son 6:  
    "ataque"
    "defensa"
    "ataque_especial"
    "defensa_especial"
    "velocidad"
    "vida"  

Escriba una función que, dada una lista de diccionarios (cada uno 
representando un pokémon) con las anteriores estadísticas, determine 
si Ash podrá formar un equipo de pokémon seudolegendarios para afrontar
la final de la liga. En caso que Ash pueda formar un equipo, 
retorne una lista con los nombres de las criaturas que Ash utilizaría
en la batalla. Si es imposible generar un equipo que cumpla con las
condiciones, retorne None.

Se garantiza que en caso de poder formar un equipo válido, solamente 
habrá una configuración posible.  

La lista de retorno debe componerse únicamente de cadenas de caracteres
y debe tener el mismo orden de la lista que llega por parámetro. Su 
solución debe tener una función de acuerdo con la siguiente 
especificación: 

   Nombre de la función: construir_equipo_pokemon

Si lo requiere, puede agregar funciones adicionales. 

Descripción de parámetros:
Nombre              Tipo           Descripción
Cantidad            int     La cantidad de pokémones que usará cada 
                            entrenador en la batalla final. 
                            Es un entero entre 3 y 6.  

Lista_pkmn         list     Una lista compuesta de diccionarios. 
                            Los diccionarios representan cada uno de
                            los pokémon elegibles por Ash. 
                            Cada diccionario tiene las siguientes 
                            llaves: "nombre": (str) el nombre del 
                            pokemon, se garantiza que no hay nombres
                            repetidos en los diccionarios de la lista;
                            "vida": (int), "ataque":(int), "defensa": 
                            (int),"ataque_especial": (int),
                            "defensa_especial": (int),"velocidad": (int). Cada uno de estos valores enteros representa la estadística de combate respectiva del pokémon.  

Descripción de retorno:

Tipo               Descripción
list	     None si es imposible generar un equipo de pokémon 
             seudolegendarios para la batalla. De lo contrario,
             retorna una lista con los nombres de los pokémon a
             utilizar en la batalla.


"""
def construir_equipo_pokemon(cantidad: int, lista_pkmn: list) -> list:
    # Función para calcular la suma de las estadísticas de combate de un Pokémon
    def suma_estadisticas(pokemon):
        return sum(pokemon[stat] for stat in ['vida', 'ataque', 'defensa', 'ataque_especial', 'defensa_especial', 'velocidad'])

    # Filtrar la lista para obtener solo Pokémon seudolegendarios
    seudolegendarios = [pkmn for pkmn in lista_pkmn if suma_estadisticas(pkmn) >= 600]

    # Verificar si hay suficientes Pokémon seudolegendarios para formar el equipo
    if len(seudolegendarios) >= cantidad:
        # Retornar los nombres de los primeros 'cantidad' Pokémon seudolegendarios
        return [pkmn['nombre'] for pkmn in seudolegendarios[:cantidad]]
    else:
        # Retornar None si no es posible formar el equipo
        return None

# Ejemplo de uso
lista_pkmn = [
    {'nombre': 'Dragonite', 'vida': 91, 'ataque': 134, 'defensa': 95, 'ataque_especial': 100, 'defensa_especial': 100, 'velocidad': 80},
    {'nombre': 'Tyranitar', 'vida': 100, 'ataque': 134, 'defensa': 110, 'ataque_especial': 95, 'defensa_especial': 100, 'velocidad': 61},
    # ... más Pokémon ...
]

cantidad = 1  # Cantidad de Pokémon que Ash quiere usar en la batalla
equipo = construir_equipo_pokemon(cantidad, lista_pkmn)
print(equipo)

