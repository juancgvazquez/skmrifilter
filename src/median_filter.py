import numpy as np


def median_filter(image, kernel_size):
    temp = []
    indexer = kernel_size // 2
    data_final = []
    data_final = np.zeros((len(image), len(image[0])))
    for i in range(len(image)):

        for j in range(len(image[0])):

            for z in range(kernel_size):
                if i + z - indexer < 0 or i + z - indexer > len(image) - 1:
                    for c in range(kernel_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(image[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(kernel_size):
                            temp.append(image[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final