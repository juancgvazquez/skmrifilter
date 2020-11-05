# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/juancvazquez/skmrifilter).
# Copyright (c) 2020, Jeremías Fahrrer - Juan Carlos Vázquez
# License: MIT
#   Full Text: https://github.com/juancgvazquez/skmrifilter/blob/master/LICENSE
"""Module that contains the ImageFilterTransformer Class."""
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class ImageFilterTransformer(BaseEstimator, TransformerMixin):
    """Class Transformer to Use and Chain Image Filters."""

    def __init__(self, filter, **kwargs) -> None:
        self.filter = filter
        self.kwargs = kwargs

    def fit(self, X, y=None) -> 'ImageFilterTransformer':
        """Fit Transformer."""
        return self

    def __repr__(self):
        """Return representation."""
        filter_name = getattr(self.filter, "__name__")
        return (f'ImageFilterTransformer({filter_name, self.kwargs}')

    def transform(self, X: np.ndarray) -> np.ndarray:
        """Apply Filters."""
        image_filtered = self.filter(X, **self.kwargs)
        return image_filtered
