from math import ceil
import matplotlib.pyplot as plt

def Graph_EDA_Cat(cat, n_top_categories=10):
    # Calculamos el número de filas que necesitamos
    filas = ceil(cat.shape[1] / 2)

    # Definimos el gráfico
    f, ax = plt.subplots(nrows=filas, ncols=2, figsize=(16, filas * 6))

    # Aplanamos para iterar por el gráfico como si fuera de 1 dimensión en lugar de 2
    ax = ax.flat 

    # Creamos el bucle que va añadiendo gráficos
    for cada, variable in enumerate(cat):
        if variable in ['CUSTOMERNAME', 'CITY', 'PRODUCTCODE' , 'ORDERDATE']:
            # Graficamos solo las primeras N categorías
            cat[variable].value_counts().nlargest(n_top_categories).plot.barh(ax=ax[cada])
            ax[cada].tick_params(axis='y', labelrotation=0)  # Ajusta el ángulo de las etiquetas
        else:
            cat[variable].value_counts().plot.barh(ax=ax[cada])

        ax[cada].set_title(variable, fontsize=12, fontweight="bold")
        ax[cada].tick_params(labelsize=12)


def Graph_EDA_Num(num):
    # Calculamos el número de filas que necesitamos
    filas = ceil(num.shape[1] / 2)

    # Definimos el gráfico
    f, ax = plt.subplots(nrows=filas, ncols=2, figsize=(16, filas * 6))

    # Aplanamos para iterar por el gráfico como si fuera de 1 dimensión en lugar de 2
    ax = ax.flat 

    # Creamos el bucle que va añadiendo gráficos
    for cada, variable in enumerate(num):
        num[variable].plot.hist(ax=ax[cada], bins=20)  # Puedes ajustar el número de bins según tus necesidades
        ax[cada].set_title(variable, fontsize=12, fontweight="bold")
        ax[cada].tick_params(labelsize=12)

    # Ajuste de diseño para gráficos no utilizados
    for i in range(num.shape[1], len(ax)):
        f.delaxes(ax[i])


def Stadistic_Cont(num):
    #Calculamos describe
    estadisticos = num.describe().T
    #Añadimos la mediana
    estadisticos['median'] = num.median()
    #Reordenamos para que la mediana esté al lado de la media
    estadisticos = estadisticos.iloc[:,[0,1,8,2,3,4,5,6,7]]
    #Lo devolvemos
    return(estadisticos)

