# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/juancgvazquez/skmrifilter).
# Copyright (c) 2020, Jeremías Farrher - Juan Carlos Vázquez
# License: MIT
#   Full Text:
#   https://github.com/juancgvazquez/skmrifilter/blob/master/LICENSE

import numpy.testing as npt

from skimage.restoration import (
    denoise_bilateral,
    denoise_tv_chambolle,
    denoise_wavelet,
)

from sklearn.pipeline import Pipeline

from skmrifilter.transformer import ImageFilterTransformer


def test_simple_transformer(noisy_image, noisy_wavelet):
    t_wavelet = ImageFilterTransformer(denoise_wavelet)
    transformed_image = t_wavelet.transform(noisy_image)
    npt.assert_array_almost_equal(transformed_image, noisy_wavelet, decimal=15)


def test_pipe_no_kwargs(noisy_image, noisy_pipeline):
    t_tv_chambelle = ImageFilterTransformer(denoise_tv_chambolle)
    t_wavelet = ImageFilterTransformer(denoise_wavelet)
    pipeline = Pipeline(
        steps=[
            (t_tv_chambelle.__repr__(), t_tv_chambelle),
            (t_wavelet.__repr__(), t_wavelet),
        ]
    )
    transformed_image = pipeline.transform(noisy_image)
    npt.assert_array_almost_equal(
        noisy_pipeline, transformed_image, decimal=15
    )


def test_pipeline_kwargs(noisy_image, noisy_pipeline_kwargs):
    t_tv_chambelle = ImageFilterTransformer(denoise_tv_chambolle)
    t_bilateral = ImageFilterTransformer(denoise_bilateral, multichannel=True)
    t_wavelet = ImageFilterTransformer(denoise_wavelet)
    pipe = Pipeline(
        steps=[
            (t_tv_chambelle.__repr__(), t_tv_chambelle),
            (t_bilateral.__repr__(), t_bilateral),
            (t_wavelet.__repr__(), t_wavelet),
        ]
    )
    pipe_transformed = pipe.transform(noisy_image)
    npt.assert_array_almost_equal(
        pipe_transformed, noisy_pipeline_kwargs, decimal=15
    )
