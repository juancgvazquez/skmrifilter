# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/jerefarrher/skmrifilter).
# Copyright (c) 2020, Jeremías Fahrrer - Juan Carlos Vázquez
# License: MIT
#   Full Text: https://github.com/jerefarrher/skmrifilter/blob/master/LICENSE

import cv2
from skimage.filters import gaussian, median, unsharp_mask
from skimage.restoration import denoise_nl_means
import numpy as np
from src.transformer import ImageFilterTransformer
from sklearn.pipeline import Pipeline

img = cv2.imread('./42original.png')
pipe = Pipeline(steps=[
    ('image_filters',
     ImageFilterTransformer(methods=[{gaussian: {"sigma": 2}},
                                     {median: None},
                                     {unsharp_mask: {"radius": 5, "amount": 7}},
                                     {np.around: {"decimals": 2}},
                                     {denoise_nl_means: {"patch_size": 15, "patch_distance": 20, "h": 0.16, "preserve_range": False}},
                                     {denoise_nl_means: {"patch_size": 15, "patch_distance": 20, "h": 0.16, "preserve_range": False}}
                                     ])),
])
final_image = pipe.transform(img)


