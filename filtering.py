import numpy as np
import matplotlib.pyplot as plt

import padding

def filtering(src, mask, pad_type='zero'):
    print('filtering start...')
    h, w = src.shape[:2] 
    mh, mw = mask.shape[:2]
    pad_img = padding.padding(src=src, pad_size=(mh//2, mw//2), pad_type=pad_type)

    dst = np.zeros((h, w))

    #filtering
    for row in range(h):
        for col in range(w):
            val = np.sum(pad_img[row:row+mh, col:col+mw] * mask)
            dst[row, col] = val

            # cliping 0 ~ 255
    dst = np.clip(dst, 0, 255)
    dst = np.round(dst)
    dst = dst.astype(np.uint8)
    print('filtering end...')
    return dst

def getFilter(ftype, fsize):
    
    if ftype == 'average':
        mask = np.ones(fsize)
        mask = mask/mask.sum()
    
    elif ftype == 'sharpening':
        base = np.zeros(fsize)
        base[fsize[0]//2,fsize[1]//2] = 2

        average = np.ones(fsize)
        average = average/average.sum()

        mask = base - average

    return mask

def showFilteringTest(img):
    # get filters
    fsize = (5,5)
    average_mask = getFilter(ftype='average', fsize=fsize)
    sharp_mask = getFilter(ftype='sharpening', fsize=fsize)

    # filtering with zero padding
    average_img_zero_pad = filtering(src=img, mask=average_mask, pad_type='zero')
    sharp_img_zero_pad = filtering(src=img, mask=sharp_mask, pad_type='zero')

    # filtering with mirror padding
    average_img_mirror_pad = filtering(src=img, mask=average_mask, pad_type='mirror')
    sharp_img_mirror_pad = filtering(src=img, mask=sharp_mask, pad_type='mirror')
    

    plt.figure(figsize=(12,8))
    plt.subplot(2,3,1)
    plt.title('5x5 average filter with zero padding')
    plt.imshow(average_img_zero_pad, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,3,2)
    plt.title('original image')
    plt.imshow(img.copy(), cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,3,3)
    plt.title('5x5 sharpening filter with zero padding')
    plt.imshow(sharp_img_zero_pad, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,3,4)
    plt.title('5x5 average filter with mirror padding')
    plt.imshow(average_img_mirror_pad, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,3,5)
    plt.title('original image')
    plt.imshow(img.copy(), cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,3,6)
    plt.title('5x5 sharpening filter with mirror padding')
    plt.imshow(sharp_img_mirror_pad, cmap='gray', vmin=0, vmax=255)

    plt.show()

