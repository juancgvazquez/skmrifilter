# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/juancvazquez/skmrifilter).
# Copyright (c) 2020, Jeremías Fahrrer - Juan Carlos Vázquez
# License: MIT
#   Full Text: https://github.com/juancgvazquez/skmrifilter/blob/master/LICENSE
""" This module contains the ImageFilterTransformer Class """
from skimage.restoration import (denoise_tv_chambolle, denoise_wavelet)
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class ImageFilterTransformer(BaseEstimator, TransformerMixin):
    """Class Transformer to Use and Chain Image Filters"""
    def __init__(self, methods={denoise_tv_chambolle: None,
                                denoise_wavelet: None}) -> None:
        self.methods = methods

    def fit(self, X, y=None) -> 'ImageFilterTransformer':
        """ Necessary method to Fit Transformer """
        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        """ Method to actually apply the filters """
        image_filtered = x
        for filt in self.methods.items():
            print(f"Applying {filt[0].__name__}")
            if filt[1] is None:
                image_filtered = filt[0](image_filtered)
            else:
                image_filtered = filt[0](image_filtered, **filt[1])
        return image_filtered
