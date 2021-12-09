import numpy as np
import cv2
import matplotlib.pyplot as plt


MAX_VALUE = 255

def calcHist(src):
    h, w = src.shape[:2]
    hist = np.zeros((256,))
    for row in range(h):
        for col in range(w):
            intensity = src[row, col]
            hist[intensity] += 1
    return hist

def normalizedHist(hist, pixel_num):
    return hist/pixel_num

def transformPDF2CDF(pdf):
    length = pdf.shape[0]
    cdf = np.zeros((length, ))
    cdf[0] = pdf[0]
    for i in range(1, length):
        cdf[i] = pdf[i] + cdf[i-1]

    return cdf

def denormalizeHist(normalized, gray_level):
    return normalized * gray_level

def calcHistEqualization(denormalized, hist):
    hist_equal = np.zeros(denormalized.shape, dtype=np.int64)
    for i in range(len(hist_equal)):
        hist_equal[denormalized[i]] += hist[i]
    return hist_equal

def equalizationImg(src, output_gray_level):
    h, w = src.shape[:2]
    dst = np.zeros((h, w), dtype=np.uint8)
    for row in range(h):
        for col in range(w):
            dst[row, col] = output_gray_level[src[row, col]]
    return dst

def histogramEqualization(src):
    h, w = src.shape[:2]
    histogram = calcHist(src)
    normalized_histogram = normalizedHist(histogram, h*w)
    normalized_output = transformPDF2CDF(normalized_histogram)
    denormalized_output = denormalizeHist(normalized_output, MAX_VALUE)
    output_gray_level = denormalized_output.astype(np.int64)
    hist_equal = calcHistEqualization(output_gray_level, histogram)

    dst = equalizationImg(src, output_gray_level)

    return dst, hist_equal
    
def showHistEqual(img):
    histogram = calcHist(img)

    dst, equal_hist = histogramEqualization(img)

    plt.figure(figsize=(8,5))
    plt.subplot(2,2,1)
    binX = np.arange(len(histogram))
    plt.bar(binX, histogram, width=0.5, color='g')
    plt.title('histogram')

    plt.subplot(2,2,3)
    plt.imshow(img, cmap='gray', vmin=0, vmax=MAX_VALUE)


    plt.subplot(2,2,2)
    plt.bar(binX, equal_hist, width=0.5, color='g')
    plt.title('histogram equalization')

    plt.subplot(2,2,4)
    plt.imshow(dst, cmap='gray', vmin=0, vmax=MAX_VALUE)

    plt.show()




def main():    
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)

    histogram = calcHist(img)

    dst, equal_hist = histogramEqualization(img.copy())

    plt.figure(figsize=(14,7))
    plt.subplot(2,2,1)
    binX = np.arange(len(histogram))
    plt.bar(binX, histogram, width=0.5, color='g')
    plt.title('histogram')

    plt.subplot(2,2,3)
    plt.imshow(img, cmap='gray', vmin=0, vmax=MAX_VALUE)


    plt.subplot(2,2,2)
    plt.bar(binX, equal_hist, width=0.5, color='g')
    plt.title('histogram equalization')

    plt.subplot(2,2,4)
    plt.imshow(dst, cmap='gray', vmin=0, vmax=MAX_VALUE)

    plt.show()




if __name__ =='__main__':
    main()