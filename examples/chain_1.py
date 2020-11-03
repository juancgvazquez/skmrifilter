# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/juancgvazquez/skmrifilter).
# Copyright (c) 2020, Jeremías Fahrrer - Juan Carlos Vázquez
# License: MIT
#   Full Text: https://github.com/juancgvazquez/skmrifilter/blob/master/LICENSE

import cv2
from skimage.filters import apply_hysteresis_threshold
from skimage.filters import frangi, hessian,prewitt, roberts, sobel, prewitt_h, prewitt_v
from skimage.filters import gabor, gaussian, laplace, median, meijering
from skimage.filters import rank_order,threshold_local,threshold_niblack
from skimage.filters import threshold_otsu,threshold_sauvola,threshold_triangle
from skimage.filters import threshold_yen, unsharp_mask, wiener
from skimage.restoration import denoise_nl_means, denoise_bilateral
from skimage import filters
import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import disk
from skimage import exposure


def chain_1(image, sigma=2):
    """
    esta función toma una imagen en escala de grises y aplica el filtro gaussiano, el mediano, 		unsharp para resaltar bordes y 2 iteraciones de NLM
    """
    A = gaussian(image, sigma)
    B = median(A, disk(3))
    C = np.around(unsharp_mask(B, radius=5, amount=7),2)
    D = denoise_nl_means(C,patch_size=15, patch_distance=20, h=0.19,preserve_range=False)
    E = denoise_nl_means(D,patch_size=15, patch_distance=20, h=0.19,preserve_range=False)

    return E
