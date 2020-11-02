# This file is part of the
#   Scikit-Learn MRI-Filter Project
#   (https://github.com/jerefarrher/skmrifilter).
# Copyright (c) 2020, Jeremías Fahrrer - Juan Carlos Vázquez
# License: MIT
#   Full Text:
#   https://github.com/jerefarrher/skmrifilter/blob/master/LICENSE


from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from skimage import data, img_as_float
from skimage.util import random_noise
import matplotlib.pyplot as plt
from src.transformer import ImageFilterTransformer
from sklearn.pipeline import Pipeline


original = img_as_float(data.chelsea()[100:250, 50:300])

sigma = 0.155
noisy = random_noise(original, var=sigma**2)

fig, ax = plt.subplots(nrows=2, ncols=4, figsize=(8, 5),
                       sharex=True, sharey=True)

plt.gray()

# Estimate the average noise standard deviation across color channels.
sigma_est = estimate_sigma(noisy, multichannel=True, average_sigmas=True)
# Due to clipping in random_noise, the estimate will be a bit smaller than the
# specified sigma.
print(f"Estimated Gaussian noise standard deviation = {sigma_est}")
ax[0, 0].imshow(noisy)
ax[0, 0].axis('off')
ax[0, 0].set_title('Noisy')

transformer = ImageFilterTransformer()
new_image = transformer.transform(noisy)
ax[0, 1].imshow(new_image)
ax[0, 1].axis('off')
ax[0, 1].set_title('denoise tv')

pipe = Pipeline(steps=[
    ('image_filters',
     ImageFilterTransformer(methods={denoise_tv_chambolle: None,
                                     denoise_bilateral: {"multichannel": True},
                                     denoise_wavelet: None})),
])
two_process = pipe.transform(noisy)
ax[0, 2].imshow(two_process)
ax[0, 2].axis('off')
ax[0, 2].set_title('denoise tv + wavelet')


fig.tight_layout()

plt.savefig('./fig.png')
