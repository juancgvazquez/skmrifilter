# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/juancvazquez/skmrifilter).
# Copyright (c) 2020, Jeremías Fahrrer - Juan Carlos Vázquez
# License: MIT
#   Full Text: https://github.com/juancgvazquez/skmrifilter/blob/master/LICENSE
"""Module that contains the ImageFilterTransformer Class."""
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin


class ImageFilterTransformer(BaseEstimator, TransformerMixin):
    """Class Transformer to Use and Chain Image Filters.

    Parameters
    ----------
    filt: 'callable'
        The filter method
    **kwargs: 'key-value arguments'
        Additional configuration parameters for filter method
    """

    def __init__(self, filt, **kwargs) -> None:
        if not callable(filt):
            raise TypeError("Filter must be a method")
        self.filter = filt
        self.kwargs = kwargs
        if hasattr(self.filter, "__qualname__"):
            self.filter_name = getattr(self.filter, "__qualname__")
        else:
            self.filter_name = getattr(self.filter, "__name__")

    def fit(self, X, y=None) -> "ImageFilterTransformer":
        """Fit Transformer.

        Parameters
        ----------
        X: ndarray
            Image in a numpy ndarray
        y: None
            Required by sklearn but not used

        Returns
        -------
        ImageFilterTransformer

        """
        return self

    def __repr__(self):
        """Return representation."""
        return f"ImageFilterTransformer({self.filter_name, self.kwargs}"

    def transform(self, X: np.ndarray) -> np.ndarray:
        """Apply Filters.

        Parameters
        ----------
        X: ndarray
            Image in a numpy ndarray Type

        Returns
        -------
        image_filtered: ndarray
            Image after applying filter in a numpy ndarray Type
        """
        image_filtered = self.filter(X, **self.kwargs)
        #return image_filtered
        return "estoy roto"
