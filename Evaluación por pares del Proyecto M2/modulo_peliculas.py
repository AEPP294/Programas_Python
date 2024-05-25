"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    dic_pelicula={ "nombre": nombre,
                   "genero": genero,
                   "duracion": duracion,
                   "anio": anio,
                   "clasificacion": clasificacion,
                   "hora": hora,
                   "dia": dia} 
    return dic_pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    busqueda = [None]
    if p1['nombre'] == nombre_pelicula:
        busqueda = p1
    if p2['nombre'] == nombre_pelicula:
        busqueda = p2
    if p3['nombre'] == nombre_pelicula:
        busqueda = p3
    if p4['nombre'] == nombre_pelicula:
        busqueda = p4
    if p5['nombre'] == nombre_pelicula:
        busqueda = p5

    return busqueda 
    

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    mayor_duracion=p1
    if p2["duracion"]>mayor_duracion["duracion"]:
        mayor_duracion= p2
        
    if p3["duracion"]>mayor_duracion["duracion"]:
        mayor_duracion= p3
        
    if p4["duracion"]>mayor_duracion["duracion"]:
        mayor_duracion= p4
        
    if p5["duracion"]>mayor_duracion["duracion"]:
        mayor_duracion= p5
        
    return mayor_duracion

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    promedio_tiempo= (p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"])/5
    horas = int(promedio_tiempo // 60)
    minutos = int(promedio_tiempo % 60)
    tiempo_horas = str(str(horas)+":"+str(minutos))
    return tiempo_horas

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    
    resultado= p1["anio"]-anio
    diferencia1=abs(resultado)
    resultado= p2["anio"]-anio
    diferencia2=abs(resultado)
    resultado= p3["anio"]-anio
    diferencia3=abs(resultado)
    resultado= p4["anio"]-anio
    diferencia4=abs(resultado)
    resultado= p5["anio"]-anio
    diferencia5=abs(resultado)
    
    menor=diferencia1
    estreno=p1
    
    if diferencia2<menor:
        menor= diferencia2
        estreno=p2
        
    if diferencia3<menor:
        menor= diferencia3
        estreno=p3
        
    if diferencia4<menor:
        menor= diferencia4
        estreno=p4
        
    if diferencia5<menor:
        menor= diferencia5
        estreno=p5
        
    return estreno
    

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    conteo=0
    
    if p1["clasificacion"]=="18+":
        conteo+=1
    if p2["clasificacion"]=="18+":
        conteo+=1
    if p3["clasificacion"]=="18+":
        conteo+=1
    if p4["clasificacion"]=="18+":
        conteo+=1
    if p5["clasificacion"]=="18+":
        conteo+=1
        
    return conteo

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    reagendar = True
    if p1 is not None and p1 != peli:    
        if p1['hora'] == nueva_hora or p1['dia'] == nuevo_dia:
            reagendar= False
            
    if p2 is not None and p2 != peli:
        if p2['hora'] == nueva_hora or p1['dia'] == nuevo_dia:
            reagendar= False
            
    if p3 is not None and p3 != peli:
        if p3['hora'] == nueva_hora or p1['dia'] == nuevo_dia:
            reagendar= False 
    if p4 is not None and p4 != peli:
        if p4['hora'] == nueva_hora or p1['dia'] == nuevo_dia:
            reagendar= False
    if p5 is not None and p5 != peli:
        if p5['hora'] == nueva_hora or p1['dia'] == nuevo_dia:
            reagendar= False
            
    if control_horario:
        if nueva_hora < 1000 or nueva_hora > 2200:
            reagendar = False
            
    return reagendar
    
def decidir_invitar(pelicula: dict, edad_invitado: int, autorizacion: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    invitacion = False
        
    if pelicula['clasificacion'] == '18+' and edad_invitado >= 18 and autorizacion:
        invitacion = True
    elif pelicula['clasificacion'] == '7+' and edad_invitado >= 7 and autorizacion:
        invitacion = True
    elif pelicula['clasificacion'] == '13+' and edad_invitado >= 13 and autorizacion:
        invitacion = True
    elif pelicula['clasificacion'] == '16+' and edad_invitado >= 16 and autorizacion:
        invitacion = True
    else:
        invitacion = False
    return invitacion









