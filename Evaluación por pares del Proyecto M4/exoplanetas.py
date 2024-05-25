import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np
import seaborn as sns

plt.rcParams.update({'font.size': 12})
#***************************************************************************************
"Requerimiento 0"

def cargar_datos(nombre_archivo:str)->pd.DataFrame:
    """ Carga los datos de un archivo csv y retorna el DataFrame con la informacion.
    Parametros:
        nombre_archivo (str): El nombre del archivo CSV que se debe cargar
    Retorno:
        (DataFrame) : El DataFrame con todos los datos contenidos en el archivo
    """
    try:
        # Cargar el archivo CSV en un DataFrame
        df = pd.read_csv(nombre_archivo)
        return df
    except FileNotFoundError:
        return None
    pass
#***************************************************************************************
"Requerimiento 1"

def histograma_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un histograma con 30 grupos (bins) en el que debe
        aparecer la cantidad de planetas descubiertos por anho.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    
    # Crear el histograma
    plt.figure(figsize=(8, 8))
    plt.hist(datos["DESCUBRIMIENTO"], bins=30, edgecolor="black", alpha=0.7)
    plt.xlabel("Año de descubrimiento")
    plt.ylabel("Cantidad de exoplanetas")
    plt.title("Número de descubrimientos de exoplanetas por año (1998-2018)")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()

    pass
#***************************************************************************************
"Requerimiento 2"

def estado_publicacion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de publicacion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    # Crear el boxplot con textos verticales
    plt.figure(figsize=(8, 8))
    sns.boxplot(x="ESTADO_PUBLICACION", y="DESCUBRIMIENTO", data=datos)
    plt.xlabel("Estado de publicación")
    plt.ylabel("Año de descubrimiento")
    plt.title("Relación entre el año de descubrimiento y el estado de publicación")

    # Rotar los textos de los tipos de publicación
    plt.xticks(rotation=90)

    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()


#*****************************************************************************************
"Requerimiento 3"

def deteccion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de deteccion
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    # Crear el boxplot con textos verticales para los tipos de detección
    plt.figure(figsize=(8, 8))
    sns.boxplot(x="TIPO_DETECCION", y="DESCUBRIMIENTO", data=datos)
    plt.xlabel("Tipo de detección")
    plt.ylabel("Año de descubrimiento")
    plt.title("Relación entre el año de descubrimiento y el tipo de detección")
    plt.xticks(rotation=90)  # Rotar los textos de los tipos de detección
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()
    pass

#****************************************************************************************
"Requerimiento 4"
def deteccion_y_descubrimiento(datos:pd.DataFrame,anho:int)->None:
    """ Calcula y despliega un diagrama de pie donde aparecen la cantidad de
        planetas descubiertos en un anho particular, clasificados de acuerdo
        con el tipo de publicacion.
        Si el anho es 0, se muestra la información para todos los planetas.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
        anho (int): el anho para el que se quieren analizar los planetas descubiertos
                    o 0 para indicar que deben ser todos los planetas.
    """
    if anho != 0:
        df_filtered = datos[datos["DESCUBRIMIENTO"] == anho]
    else:
        df_filtered = datos

    tipos_deteccion_counts = df_filtered["TIPO_DETECCION"].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(tipos_deteccion_counts, labels=tipos_deteccion_counts.index, autopct="%1.1f%%", startangle=90)
    plt.title(f"Tipos de detección {'(Todos los años)' if anho == 0 else f'(Año {anho})'}")
    plt.show()

    pass
#*****************************************************************************************
"Requerimiento 5"
def cantidad_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de deteccion y se muestra la cantidad de planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    # Agrupar los datos por tipo de detección y año de descubrimiento
    grouped = datos.groupby(["TIPO_DETECCION", "DESCUBRIMIENTO"]).size()

    # Crear un diccionario con las cantidades por tipo de detección y año
    data_dict = {}
    for (tipo_deteccion, year), count in grouped.items():
        if tipo_deteccion not in data_dict:
            data_dict[tipo_deteccion] = {}
        data_dict[tipo_deteccion][year] = count

    # Crear un DataFrame a partir del diccionario
    df_descubrimientos_por_tipo = pd.DataFrame(data_dict)

    # Graficar los datos
    plt.figure(figsize=(10, 6))
    for tipo_deteccion in df_descubrimientos_por_tipo.columns:
        plt.plot(df_descubrimientos_por_tipo.index, df_descubrimientos_por_tipo[tipo_deteccion], label=tipo_deteccion)

    plt.xlabel("Año de descubrimiento")
    plt.ylabel("Cantidad de planetas")
    plt.title("Cantidad de planetas descubiertos por tipo de detección")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()

    pass

#**************************************************************************************
"Requerimiento 6"

def masa_promedio_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de detección y se muestra la masa promedio de los planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    
    # Agrupar por año de descubrimiento y tipo de detección, calculando la masa promedio
    grupo_masas = datos.groupby(['DESCUBRIMIENTO', 'TIPO_DETECCION'])['MASA'].mean().reset_index()

    # Crear un gráfico de líneas
    plt.figure(figsize=(10, 6))
    for tipo in grupo_masas['TIPO_DETECCION'].unique():
        datos_tipo = grupo_masas[grupo_masas['TIPO_DETECCION'] == tipo]
        plt.plot(datos_tipo['DESCUBRIMIENTO'], datos_tipo['MASA'], label=tipo)

    # Personalizar el gráfico
    plt.xlabel('Año de descubrimiento')
    plt.ylabel('Masa promedio')
    plt.title('Masa promedio de planetas por año y tipo de detección')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

    pass

#****************************************************************************************

"Requerimiento 7"
def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de dispersión donde en el eje x se
        encuentra la masa de los planetas y en el eje y se encuentra el logaritmo
        de la masa de las estrellas. Cada punto en el diagrama correspondera
        a un planeta y estara ubicado de acuerdo con su masa y la masa de la
        estrella más cercana.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
     # Calcular la masa de la estrella en escala logarítmica
    datos['MASA_ESTRELLA_LOG'] = np.log10(datos['MASA_ESTRELLA'])

    # Crear el gráfico de dispersión
    plt.figure(figsize=(8, 6))
    plt.scatter(datos['MASA'], datos['MASA_ESTRELLA_LOG'], alpha=0.5)
    plt.xlabel('Masa de los planetas')
    plt.ylabel('Log(Masa de la estrella)')
    plt.title('Masa de los planetas vs. Masa de la estrella (escala logarítmica)')
    plt.grid(True)

    # Mostrar el gráfico
    plt.show()


    pass
#***************************************************************************************
"Requerimiento 8"

def graficar_cielo(datos:pd.DataFrame)->list:
    """ Calcula y despliega una imagen donde aparece un pixel por cada planeta,
        usando colores diferentes que dependen del tipo de detección utilizado
        para descubirlo.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    Retorno:
        Una matriz de pixeles con la representacion del cielo
    """
    # Crear una matriz en blanco (imagen) con dimensiones 1008x1008 (puedes ajustar el tamaño)
    img = np.zeros((100, 100, 3))  # 3 canales para RGB

    # Mapeo de tipos de detección a valores RGB
    detection_colors = {
        "Microlensing": [0.94, 0.10, 0.10],  # Rojo
        "Radial Velocity": [0.1, 0.5, 0.94],  # Azul
        "Imaging": [0.34, 0.94, 0.10],  # Verde
        "Primary Transit": [0.10, 0.94, 0.85],  # Turquesa
        "Other": [0.94, 0.10, 0.85],  # Magenta
        "Astrometry": [0.94, 0.65, 0.10],  # Naranja
        "TTV": [1.0, 1.0, 1.0]  # Blanco
    }

    for planet in datos:
        ra = (int(planet['ra']) * (1008 / 360))  # Escalar RA para que quepa en la imagen
        dec = int((int(planet['dec']) + 90) * (1008 / 180))  # Escalar DEC y desplazar hacia arriba
        color = detection_colors.get(planet['TIPO_DETECCION'], [1.0, 1.0, 1.0])  # Blanco por defecto
        img[dec][ra] = color

    plt.imshow(img)
    plt.axis('off')  # Ocultar ejes
    plt.show()
     
    pass


def filtrar_imagen_cielo(imagen:list)->None:
    """ Le aplica a la imagen un filtro de convolucion basado en la matriz
        [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    Parametros:
        imagen (list): una matriz con la imagen del cielo
    """
    pass



