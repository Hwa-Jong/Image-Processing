import cv2
import numpy as np
import matplotlib.pyplot as plt

import padding


def dilation(B, S):
    (b_h, b_w) = B.shape
    (s_h, s_w) = S.shape
    pad_size_h = s_h // 2
    pad_size_w = s_w // 2

    dst = padding.padding(B, (pad_size_h, pad_size_w), pad_type='zero')

    for row in range(b_h):
        for col in range(b_w):
            if B[row, col] == 1:
                dst[row:row+s_h, col:col+s_w] = S
    dst = dst[pad_size_h:b_h + pad_size_h, pad_size_w:b_w + pad_size_w]
    return dst

def erosion(B, S):
    (b_h, b_w) = B.shape
    (s_h, s_w) = S.shape
    pad_size_h = s_h // 2
    pad_size_w = s_w // 2

    dst = np.zeros(B.shape)

    for row in range(pad_size_h, b_h-pad_size_h):
        for col in range(pad_size_w, b_w-pad_size_w):
            if np.array_equal(B[row-pad_size_h:row+pad_size_h+1, col-pad_size_w:col+pad_size_w+1], S):
                dst[row, col] = 1

    return dst

def opening(B, S):
    dst = dilation(erosion(B, S), S)
    return dst

def closing(B, S):
    dst = erosion(dilation(B, S), S)
    return dst

def showMorphologyTest():
    B = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]])

    S = np.array(
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]])


    img_dilation = dilation(B, S)
    img_dilation = (img_dilation*255).astype(np.uint8)

    img_erosion = erosion(B, S)
    img_erosion = (img_erosion * 255).astype(np.uint8)

    img_opening = opening(B, S)
    img_opening = (img_opening * 255).astype(np.uint8)

    img_closing = closing(B, S)
    img_closing = (img_closing * 255).astype(np.uint8)

    plt.subplot(2,3,1)
    plt.title('Original')
    plt.imshow((B*255).astype(np.uint8), cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,3,2)
    plt.title('Dilation')
    plt.imshow(img_dilation, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,3,3)
    plt.title('Erosion')
    plt.imshow(img_erosion, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,3,5)
    plt.title('Opening')
    plt.imshow(img_opening, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,3,6)
    plt.title('Closing')
    plt.imshow(img_closing, cmap='gray', vmin=0, vmax=255)

    plt.show()


def main():
    B = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]])

    S = np.array(
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]])


    img_dilation = dilation(B, S)
    img_dilation = (img_dilation*255).astype(np.uint8)
    print(img_dilation)
    #cv2.imwrite('morphology_dilation.png', img_dilation)

    img_erosion = erosion(B, S)
    img_erosion = (img_erosion * 255).astype(np.uint8)
    print(img_erosion)
    #cv2.imwrite('morphology_erosion.png', img_erosion)

    img_opening = opening(B, S)
    img_opening = (img_opening * 255).astype(np.uint8)
    print(img_opening)
    #cv2.imwrite('morphology_opening.png', img_opening)

    img_closing = closing(B, S)
    img_closing = (img_closing * 255).astype(np.uint8)
    print(img_closing)
    #cv2.imwrite('morphology_closing.png', img_closing)



if __name__ == '__main__':
    main()