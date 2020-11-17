"""Métricas para usar en procesos con imagenes de MRI."""
import numpy as np


def dice_coefficient(y_true, y_pred, axis=(1, 2, 3), epsilon=0.00001):
    """Compute mean dice coefficient over all classes.

    Parameters
    ----------
    y_true: Tensor
        tensor of ground truth values for all classes.
        shape (num_classes, x_dim, y_dim, z_dim)
    y_pred: Tensor
        tensor of predictions for all classes.
        shape (num_classes, x_dim, y_dim, z_dim)
    axis: Tuple
        spatial axes to sum over when computing numerator and
        denominator of dice coefficient.
    epsilon: Float
        constant to avoid dividing by 0.

    Returns
    -------
    dice_coefficient: Float
        computed value of dice coefficient.
    """
    dice_numerator = 2.0 * np.sum(y_true * y_pred, axis=axis) + epsilon
    dice_denominator = (
        np.sum(y_true, axis=axis) + np.sum(y_pred, axis=axis) + epsilon
    )
    dice_coefficient = np.mean((dice_numerator) / (dice_denominator))

    return dice_coefficient


def dice_loss(y_true, y_pred):
    """Compute dice_loss for all classes.

    Parameters
    ----------
    y_true: Tensor
        tensor of ground truth values for all classes.
        shape (num_classes, x_dim, y_dim, z_dim)
    y_pred: Tensor
        tensor of predictions for all classes.
        shape (num_classes, x_dim, y_dim, z_dim).
    """
    return 1 - dice_coefficient(y_true, y_pred)
