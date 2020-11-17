import nibabel
import glob
import numpy as np


def load_hdr_folder(path, x_size, y_size, slices):
    """Load data in hdr format from a folder, and builds an array of images.

    Parameters
    ----------
    path: str
        path to the folder with the hdr files
    x_size: int
        horizontal size of images.
    y_size: int
        vertical size of images.
    slices: int
        number of slices in which image was cut.

    Returns
    -------
    data_array: list
        array containing all images.
    """
    data_array = []
    for file in glob.glob(path + "*.hdr"):
        img_data = nibabel.load(file).get_data()
        data_array.append(img_data.reshape(x_size, y_size, slices))
    return data_array


def load_hdr_image(path, rotate=True):
    """Load data from an hdr image for MRI.
    Parameters
    ----------
    path: str
        path to the image file.
    rotate: boolean
        option to rotate 90 degrees the image.
    """
    image = nibabel.load(path).get_data()
    image = image.squeeze()
    if rotate == True:
        image = np.rot90(image, 1)
    return image


if __name__ == "__main__":
    path = str(input("Enter path to images files: "))
    x_size = int(input("Enter x_size of images: "))
    y_size = int(input("Enter y_size of images: "))
    slices = int(input("Enter number of slices per MRI: "))
    load_hdr_folder(path, x_size, y_size, slices)
