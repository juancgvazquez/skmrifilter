from src.img_transforms import add_gaussian_noise, rgb2gray
from src.median_filter import median_filter
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load image and convert it to gray scale
    img = rgb2gray(plt.imread("./lena.png"))

    # Add Gaussian noise
    noisy_img = add_gaussian_noise(img, 0.05)

    # Apply Median Filter
    removed_noise_3 = median_filter(noisy_img, 3)
    removed_noise_5 = median_filter(noisy_img, 5)

    # Display results
    fig = plt.figure(figsize=(12, 10))
    display = [img, noisy_img, removed_noise_3, removed_noise_5]
    title = [
        "Original Image",
        "Gaussian Noise Added",
        "3x3 Median Filter",
        "5x5 Median Filter",
    ]

    for i in range(len(display)):
        fig.add_subplot(2, 2, i + 1)
        plt.imshow(display[i], cmap="gray")
        plt.title(title[i])

    plt.savefig("./lena_out.png")
