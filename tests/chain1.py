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

import matplotlib.pyplot as plt
from src.transformer import ImageFilterTransformer
from sklearn.pipeline import Pipeline

img = cv2.imread('./42original.png')
pipe = Pipeline(steps=[
    ('image_filters', 
     ImageFilterTransformer(methods={gaussian: {"sigma": 2},
                                     median: None,
                                     unsharp_mask: {"radius": 5, "amount": 7},
                                     np.around: {"decimals": 2},
                                     denoise_nl_means: {"patch_size": 15, "patch_distance": 20, "h": 0.16, "preserve_range": False},
                                     denoise_nl_means: {"patch_size": 15, "patch_distance": 20, "h": 0.16, "preserve_range": False}
                                     })),
])
final_image = pipe.transform(img)


