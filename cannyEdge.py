import cv2
import numpy as np
import matplotlib.pyplot as plt

import filtering

def cannyEdgeFiltering(img, fsize=3, sigma=1):
    DoG_x, DoG_y = filtering.getFilter(ftype='DoG', fsize=fsize, sigma=sigma)
    Ix = filtering.filtering(img, DoG_x, return_uint8=False)
    Iy = filtering.filtering(img, DoG_y, return_uint8=False)
    return Ix, Iy

def calcMagnitude(Ix, Iy):
    magnitude = np.sqrt(Ix ** 2 + Iy ** 2)
    return magnitude
    
def calcAngle(Ix, Iy, eps=1E-6):
    angle = np.rad2deg(np.arctan(Iy / (Ix+eps)))
    return angle

def nonMaximumSupression(magnitude, angle):
    (h, w) = magnitude.shape
    largest_magnitude = np.zeros((h, w))
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            degree = angle[row, col]

            if 0 <= degree and degree < 45:
                rate = np.tan(np.deg2rad(degree))
                left_magnitude = (rate) * magnitude[row - 1, col - 1] + (1 - rate) * magnitude[row, col - 1]
                right_magnitude = (rate) * magnitude[row + 1, col + 1] + (1 - rate) * magnitude[row, col + 1]
                if magnitude[row, col] == max(left_magnitude, magnitude[row, col], right_magnitude):
                    largest_magnitude[row, col] = magnitude[row, col]

            elif 45 <= degree and degree <= 90:
                rate = 1 / np.tan(np.deg2rad(degree))
                up_magnitude = (1 - rate) * magnitude[row - 1, col] + rate * magnitude[row - 1, col - 1]
                down_magnitude = (1 - rate) * magnitude[row + 1, col] + rate * magnitude[row + 1, col + 1]
                if magnitude[row, col] == max(up_magnitude, magnitude[row, col], down_magnitude):
                    largest_magnitude[row, col] = magnitude[row, col]

            elif -45 <= degree and degree < 0:
                rate = -np.tan(np.deg2rad(degree))
                left_magnitude = (1 - rate) * magnitude[row, col - 1] + rate * magnitude[row + 1, col - 1]
                right_magnitude = (1 - rate) * magnitude[row, col + 1] + rate * magnitude[row - 1, col + 1]
                if magnitude[row, col] == max(left_magnitude, magnitude[row, col], right_magnitude):
                    largest_magnitude[row, col] = magnitude[row, col]

            elif -90 <= degree and degree < -45:
                rate = -1 / np.tan(np.deg2rad(degree))
                up_magnitude = (1 - rate) * magnitude[row - 1, col] + rate * magnitude[row - 1, col + 1]
                down_magnitude = (1 - rate) * magnitude[row + 1, col] + rate * magnitude[row + 1, col - 1]
                if magnitude[row, col] == max(up_magnitude, magnitude[row, col], down_magnitude):
                    largest_magnitude[row, col] = magnitude[row, col]

            else:
                print(row, col, 'error!  degree :', degree)

    return largest_magnitude

def doubleThresholding(src, high_threshold=None, low_threshold=None):
    dst = np.zeros((src.shape[0]+2, src.shape[1]+2))
    dst[1:-1, 1:-1] = src
    (h, w) = dst.shape

    high_threshold_value = high_threshold
    low_threshold_value = low_threshold
    if high_threshold is None:
        high_threshold_value, _ = cv2.threshold(dst.astype(np.uint8), 0, 255, cv2.THRESH_OTSU)
    if low_threshold is None:
        low_threshold_value = high_threshold_value * 0.4

    for row in range(h):
        for col in range(w):
            if dst[row, col] >= high_threshold_value:
                dst[row, col] = 255
            elif dst[row, col] < low_threshold_value:
                dst[row, col] = 0
            else:
                weak_edge = []
                weak_edge.append((row, col))
                search_weak_edge(dst, weak_edge, high_threshold_value, low_threshold_value)
                if calssify_edge(dst, weak_edge, high_threshold_value):
                    for idx in range(len(weak_edge)):
                        (r, c) = weak_edge[idx]
                        dst[r, c] = 255
                else:
                    for idx in range(len(weak_edge)):
                        (r, c) = weak_edge[idx]
                        dst[r, c] = 0

    return dst[1:-1, 1:-1]

def search_weak_edge(dst, edges, high_threshold_value, low_threshold_value):
    (row, col) = edges[-1]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if dst[row+i, col+j] < high_threshold_value and dst[row+i, col+j] >= low_threshold_value:
                if edges.count((row+i, col+j)) < 1:
                    edges.append((row+i, col+j))
                    search_weak_edge(dst, edges, high_threshold_value, low_threshold_value)


def calssify_edge(dst, weak_edge, high_threshold_value):
    for idx in range(len(weak_edge)):
        (row, col) = weak_edge[idx]
        value = np.max(dst[row-1:row+2, col-1:col+2])
        if value >= high_threshold_value:
            return True

def cannyEdgeDetection(img):
    img = img.astype(np.float64)
    Ix, Iy = cannyEdgeFiltering(img, fsize=3, sigma=1)
    
    magnitude = calcMagnitude(Ix, Iy)
    angle = calcAngle(Ix, Iy)

    NMS = nonMaximumSupression(magnitude, angle)

    dst = doubleThresholding(NMS)

    dst = np.clip(dst, 0, 255)
    dst = dst.astype(np.uint8)
    return dst


def showCannyEdgeTest(img):
    dst = cannyEdgeDetection(img)

    plt.subplot(1,2,1)
    plt.title('Original')
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1,2,2)
    plt.title('Canny Edge Detection')
    plt.imshow(dst, cmap='gray', vmin=0, vmax=255)

    plt.show()

    return


def main():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    dst = cannyEdgeDetection(img)


if __name__ == '__main__':
    main()