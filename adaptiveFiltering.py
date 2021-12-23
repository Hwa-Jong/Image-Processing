import numpy as np
import matplotlib.pyplot as plt
import cv2

import padding
import noise
import filtering

def adaptiveFiltering(img, pad_size, pad_type='zero', sigma=3, sigma_r=0.1, return_uint8=True):

    h, w = img.shape

    pad_h, pad_w = pad_size[0]//2, pad_size[1]//2

    pad = padding.padding(src=img, pad_size=( pad_h, pad_w ), pad_type=pad_type, return_uint8=return_uint8)
    dst = np.zeros((h, w))

    y, x = np.mgrid[-pad_h:pad_h+1, -pad_w:pad_w+1]

    for row in range(h):
        for col in range(w):
            k = y + row
            l = x + col

            mask = np.exp( -(((row - k)**2) / (2 * sigma**2)) -(((col-l)**2) / (2 * sigma**2)) ) * np.exp( -(((pad[row+pad_h, col+pad_w] - pad[k+pad_h, l+pad_w])**2)/(2*sigma_r**2)) )
            mask = mask/mask.sum()

            dst[row, col] = np.sum(pad[row:row + pad_size[0], col:col + pad_size[1]] * mask)


    if return_uint8:
        dst = np.clip(dst, 0, 255)
        dst = dst.astype(np.uint8)

    return dst


def showAdaptiveFilteringTest(img):
    img = noise.get_noise(img, noise_type='gausian')
    dst = adaptiveFiltering(img.copy(), pad_size=(5,5))


    mask = filtering.getFilter(ftype='gaussian2D', fsize=(5,5), sigma=3 )
    gaus = filtering.filtering(img.copy(), mask)

    plt.subplot(1,3,1)
    plt.title('Original')
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1,3,2)
    plt.title('Gaussian')
    plt.imshow(gaus, cmap='gray', vmin=0, vmax=255)


    plt.subplot(1,3,3)
    plt.title('bilateral')
    plt.imshow(dst, cmap='gray', vmin=0, vmax=255)

    plt.show()


def main():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    img = noise.get_noise(img, noise_type='gausian')
    dst = adaptiveFiltering(img.copy(), pad_size=(5,5))


    mask = filtering.getFilter(ftype='gaussian2D', fsize=(5,5), sigma=3 )
    gaus = filtering.filtering(img.copy(), mask)

    plt.subplot(1,3,1)
    plt.title('Original')
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1,3,2)
    plt.title('Gaussian')
    plt.imshow(gaus, cmap='gray', vmin=0, vmax=255)


    plt.subplot(1,3,3)
    plt.title('bilateral')
    plt.imshow(dst, cmap='gray', vmin=0, vmax=255)

    plt.show()

if __name__ =='__main__':
    main()