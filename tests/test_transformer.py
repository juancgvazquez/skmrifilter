# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/juancgvazquez/skmrifilter).
# Copyright (c) 2020, Jeremías Farrher - Juan Carlos Vázquez
# License: MIT
#   Full Text:
#   https://github.com/juancgvazquez/skmrifilter/blob/master/LICENSE


from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet)
from skmrifilter.transformer import ImageFilterTransformer
from sklearn.pipeline import Pipeline
import pickle
import numpy.testing as npt


def test_simple_transformer():
    with open('tests/noisy_image.pkl', 'rb') as f:
        noisy = pickle.load(f)
    t_tv_chambelle = ImageFilterTransformer(denoise_tv_chambolle)
    t_wavelet = ImageFilterTransformer(denoise_wavelet)
    pipeline = Pipeline(steps=[(t_tv_chambelle.__repr__(), t_tv_chambelle),
                        (t_wavelet.__repr__(), t_wavelet)])
    transformed_image = pipeline.transform(noisy)
    with open('tests/test_output1.pkl', 'rb') as f:
        test_transformer = pickle.load(f)
    npt.assert_array_almost_equal(test_transformer, transformed_image,
                                  decimal=15)


def test_pipeline_transformer():
    with open('tests/noisy_image.pkl', 'rb') as f:
        noisy = pickle.load(f)
    t_tv_chambelle = ImageFilterTransformer(denoise_tv_chambolle)
    t_bilateral = ImageFilterTransformer(denoise_bilateral, multichannel=True)
    t_wavelet = ImageFilterTransformer(denoise_wavelet)
    pipe = Pipeline(steps=[(t_tv_chambelle.__repr__(), t_tv_chambelle),
                    (t_bilateral.__repr__(), t_bilateral),
                    (t_wavelet.__repr__(), t_wavelet)])
    pipe_transformed = pipe.transform(noisy)
    with open('tests/test_output_pipeline.pkl', 'rb') as f:
        pipe_test_output = pickle.load(f)
    npt.assert_array_almost_equal(pipe_transformed, pipe_test_output,
                                  decimal=15)
