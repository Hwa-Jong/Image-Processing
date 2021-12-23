import numpy as np
import cv2
import matplotlib.pyplot as plt


def get_noise(img, noise_type, prob=0.05, mean=0, sigma=0.1):
    h, w = img.shape

    # Salt and Pepper noise
    if noise_type == 'snp':
        noise_prob = np.random.rand(h, w)
        dst = np.zeros((h, w), dtype=np.uint8)
        for row in range(h):
            for col in range(w):
                if noise_prob[row, col] < prob:
                    # pepper noise
                    dst[row, col] = 0
                elif noise_prob[row, col] > 1 - prob:
                    # salt noise
                    dst[row, col] = 255
                else:
                    dst[row, col] = img[row, col]

    elif noise_type == 'gausian':
        noise = np.random.normal(mean, sigma, size=(h, w))
        
        dst = img/255
        dst = dst + noise
        dst = np.clip(dst*255, 0, 255)
        dst = dst.astype(np.uint8)


    return dst




def main():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    dst = get_noise(img, noise_type='gausian')
    plt.imshow(dst, cmap='gray', vmin=0, vmax=255)

    plt.show()

if __name__=='__main__':
    main()