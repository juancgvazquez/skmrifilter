# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/jerefarrher/skmrifilter).
# Copyright (c) 2020, Jeremías Fahrrer - Juan Carlos Vázquez
# License: MIT
#   Full Text: https://github.com/jerefarrher/skmrifilter/blob/master/LICENSE

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

