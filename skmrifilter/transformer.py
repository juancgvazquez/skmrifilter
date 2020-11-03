# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/jerefarrher/skmrifilter).
# Copyright (c) 2020, Jeremías Fahrrer - Juan Carlos Vázquez
# License: MIT
#   Full Text: https://github.com/jerefarrher/skmrifilter/blob/master/LICENSE

from skimage.restoration import (denoise_tv_chambolle, denoise_wavelet)
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class ImageFilterTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, methods={denoise_tv_chambolle: None,
                                denoise_wavelet: None}) -> None:
        self.methods = methods

    def fit(self, X, y=None) -> 'ImageFilterTransformer':
        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        image_filtered = x
        for filt in self.methods:
            filt_name = next(iter(filt))
            print(f"Applying {filt_name}")
            print(filt)
            if filt[filt_name] is None:
                image_filtered = filt_name(image_filtered)
            else:
                image_filtered = filt_name(image_filtered, **filt[filt_name])
        return image_filtered
