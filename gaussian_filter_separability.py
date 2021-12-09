import numpy as np
import time

import filtering
import padding

def originalFiltering(src, mask, pad_type='zero'):
    h, w = src.shape[:2] 
    mh, mw = mask.shape[:2]
    pad_img = padding.padding(src=src, pad_size=(mh//2, mw//2), pad_type=pad_type, return_uint8=False)

    dst = np.zeros((h, w))

    # filtering without numpy to get clear results.
    for row in range(h):
        for col in range(w):
            
            val = 0
            for mrow in range(mh):
                for mcol in range(mw):
                    val += pad_img[row+mrow, col+mcol] * mask[mrow, mcol]
                    
            dst[row, col] = val

    return dst

def separabilityTest(img):
    gaus1d = filtering.getFilter(ftype='gaussian1D', fsize=(5,))
    gaus2d = filtering.getFilter(ftype='gaussian2D', fsize=(5,5))

    tmr = time.time()
    print('using 2D gaussian filter')
    dst_2D = originalFiltering(src=img, mask=gaus2d)    
    print('2D gaussian filter time : %f sec'%(time.time()-tmr))
    
    tmr = time.time()
    print('using 1D gaussian filter')
    dst_1D = originalFiltering(src=img, mask=gaus1d)
    dst_1D = originalFiltering(src=dst_1D, mask=gaus1d.T)
    print('1D gaussian filter time : %f sec'%(time.time()-tmr))

    print('< results check >')
    print('dst_2D-dst_1D : ', np.round((dst_2D-dst_1D).sum(), 5))

if __name__=='__main__':
    import cv2
    img = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.uint8)
    separabilityTest(img)