import numpy as np
from skmrifilter.metrics import dice_coefficient


def test_dice_coeff():
    pred = np.expand_dims(np.expand_dims(np.eye(2), 0), -1)
    label = np.expand_dims(
        np.expand_dims(np.array([[1.0, 1.0], [0.0, 0.0]]), 0), -1
    )
    dc = dice_coefficient(pred, label)
    np.testing.assert_almost_equal(dc, 0.5000012499968751, decimal=10)
