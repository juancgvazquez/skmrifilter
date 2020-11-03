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



def chain_2(image, sigma=2):
    """
    función que aplica el filtro bilateral, NLM, unsharp, una 2da iteración del NLM y la mediana
    """
    A = cv2.bilateralFilter(image,5,50,50)
    B = denoise_nl_means(A,patch_size=10, patch_distance=10, h=0.1,preserve_range=False)
    C = np.around(unsharp_mask(B, radius=10, amount=10),2)
    D = denoise_nl_means(C,patch_size=15, patch_distance=20, h=0.19)
    E = median(D)

    return
