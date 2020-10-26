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
        for filt in self.methods.keys():
            if self.methods[filt] == None:
                image_filtered = filt(image_filtered)
            else:
                image_filtered = filt(image_filtered, **self.methods[filt])
        return image_filtered
