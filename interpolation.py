import numpy as np
import cv2
import matplotlib.pyplot as plt

def resizeImg(img, scale=None, size=None):
    if scale is None and size is None:
        assert False, 'You need to set the scale or size'


    h, w = img.shape[:2]

    if scale is not None:
        pass

    elif size is not None:
        dst = np.zeros(size)

    else:
        assert False, 'scale or size error'


def interpolation(img, reshape, inter_type='bilinear', mapping_type='backward'):

    if inter_type == 'nearest':
        inter = nearest

    elif inter_type == 'bilinear':
        inter = bilinear

    else:
        assert False, 'interpolation type error!'

    re_img = inter(img, reshape, mapping_type)
    return re_img
        
def nearest(img, reshape, mapping_type):
    h, w = img.shape[:2]
    rh, rw = reshape

    h_rate, w_rate = rh/h, rw/w

    dst = np.zeros((rh, rw))

    if mapping_type =='forward':
        counter = np.zeros_like(dst)

        for row in range(h):
            for col in range(w):
                r_pos = row*h_rate
                c_pos = col*w_rate
                
                r, c = int(min(np.round(r_pos), rh-1)), int(min(np.round(c_pos), rw-1))

                dst[r, c] += img[row, col]
                counter[r, c] += 1

        dst = dst / (counter + 1E-8)
    
    elif  mapping_type =='backward':
        r_pos, c_pos = np.arange(rh), np.arange(rw)
        r_pos, c_pos = r_pos/h_rate, c_pos/w_rate
        r_pos, c_pos = np.round(r_pos), np.round(c_pos)
        r_pos, c_pos = np.clip(r_pos, 0, h-1), np.clip(c_pos, 0, w-1)
        r_pos, c_pos = r_pos.astype(np.int32), c_pos.astype(np.int32)

        for row in range(rh):
            for col in range(rw):
                r, c = r_pos[row], c_pos[col]
                dst[row, col] = img[r, c]

    else:
        assert False, 'mapping type error!'

    dst = np.round(dst).astype(np.uint8)
    return dst


def bilinear(img, reshape, mapping_type):
    h, w = img.shape[:2]
    rh, rw = reshape

    h_rate, w_rate = rh/h, rw/w

    dst = np.zeros((rh, rw))

    if mapping_type =='forward':
        counter = np.zeros_like(dst)

        for row in range(h):
            for col in range(w):
                h_pos = row*h_rate
                w_pos = col*w_rate

                pos = []
                pos.append((int(np.floor(h_pos)), int(np.floor(w_pos))))
                pos.append((int(np.floor(h_pos)), min(int(np.ceil(w_pos)), rw-1)))
                pos.append((min(int(np.ceil(h_pos)), rh-1), int(np.floor(w_pos))))
                pos.append((min(int(np.ceil(h_pos)), rh-1), min(int(np.ceil(w_pos)), rw-1)))
                pos = list(set(pos))

                for p in pos:
                    dst[p[0], p[1]] += img[row, col]
                    counter[p[0], p[1]] += 1

        dst = dst / (counter + 1E-8)
    
    elif  mapping_type =='backward':

        for row in range(rh):
            for col in range(rw):

                r_pos, c_pos = row/h_rate, col/w_rate
                r_top, r_bottom = min(int(np.ceil(r_pos)), h-1), int(np.floor(r_pos))                
                c_top, c_bottom = min(int(np.ceil(c_pos)), w-1), int(np.floor(c_pos))

                u, v = r_pos%1, c_pos%1

                intensity = img[r_top, c_top]*(u*v) + img[r_top, c_bottom]*(u*(1-v)) + img[r_bottom, c_top]*((1-u)*v) + img[r_bottom, c_bottom]*((1-u)*(1-v))
                dst[row, col] = intensity

    else:
        assert False, 'mapping type error!'

    dst = np.round(dst).astype(np.uint8)
    return dst


def showInterpolationTest(img):
    re_shape = (1024,1024)
    nearest_for = interpolation(img, reshape=re_shape, inter_type='nearest', mapping_type='forward')
    nearest_back = interpolation(img, reshape=re_shape, inter_type='nearest', mapping_type='backward')
    bilinear_for = interpolation(img, reshape=re_shape, inter_type='bilinear', mapping_type='forward')
    bilinear_back = interpolation(img, reshape=re_shape, inter_type='bilinear', mapping_type='backward')

    plt.figure(figsize=(10,10))
    plt.subplot(2,2,1)
    plt.title('nearest interpolation(forward)')
    plt.imshow(nearest_for, cmap='gray', vmin=0, vmax=255)


    plt.subplot(2,2,2)
    plt.title('nearest interpolation(backward)')
    plt.imshow(nearest_back, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,2,3)
    plt.title('bilinear interpolation(forward)')
    plt.imshow(bilinear_for, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2,2,4)
    plt.title('bilinear interpolation(backward)')
    plt.imshow(bilinear_back, cmap='gray', vmin=0, vmax=255)

    plt.show()

    print(bilinear_for[:7, :7])
    print(bilinear_back[:7, :7])





def main():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    #re_img = interpolation(img, reshape=(1024, 1024), inter_type='bilinear', mapping_type='forward')
    #print(re_img[:6, :6])

    showInterpolationTest(img)


    

if __name__ =='__main__':
    main()