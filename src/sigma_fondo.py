#funcion sigma
import numpy as np
#recordar de deben instalar la dependencia skimage
from skimage.filters import threshold_otsu

def SigmaFondo(imagen):

"""
calcula la desviación estandar de los píxeles de la imagen que se ingresa
"""

    sqImagen = imagen**2
    umbral = threshold_otsu(sqImagen) 
    fondo = (sqImagen < umbral)*sqImagen 
    sigma = np.std(fondo) 
    return sigma

