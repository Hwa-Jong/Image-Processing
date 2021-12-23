import cv2
import numpy as np
import matplotlib.pyplot as plt

import noise
import filtering

def GaussianNoiseRemoval(img):
    h, w = img.shape

    noiseImg = noise.get_noise(img, noise_type='gausian')
    # Average 100 noisy images
    num = 100
    imgs = np.zeros((h, w))
    for i in range(num):
        imgs += noise.get_noise(img, noise_type='gausian')

    imgs = imgs/num
    imgs = np.clip(imgs, 0, 255)
    imgs = imgs.astype(np.uint8)

    mask = filtering.getFilter(ftype='gaussian2D', fsize=(3,3))
    img_filtering = filtering.filtering(noiseImg, mask)


    plt.subplot(2,2,1)
    plt.title('Original')
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,2,2)
    plt.title('Gaussian noise')
    plt.imshow(noiseImg, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,2,3)
    plt.title('gaussian filtering')
    plt.imshow(img_filtering, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,2,4)
    plt.title('Noise removal')
    plt.imshow(imgs, cmap='gray', vmin=0, vmax=255)

    plt.show()


def main():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    GaussianNoiseRemoval(img)
    

if __name__=='__main__':
    main()