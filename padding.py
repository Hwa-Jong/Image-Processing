import numpy as np
import matplotlib.pyplot as plt

def padding(src, pad_size, pad_type='zero'):
    h, w = src.shape[:2]
    ph, pw = pad_size
    pad_img = np.zeros((h+2*ph, w+2*pw), dtype=np.uint8)
    pad_img[ph:ph+h, pw:pw+w] = src

    if pad_type == 'zero':
        pass

    elif pad_type == 'repetition':
        #top
        pad_img[:ph, pw:pw+w] = np.tile(src[0,:], (ph,1))

        #bottom
        pad_img[ph+h:, pw:pw+w] = np.tile(src[h-1, :], (ph,1))

        #left
        pad_img[:, :pw] = np.tile(pad_img[:, pw:pw+1], (1,pw))

        #right
        pad_img[:, pw+w:] = np.tile(pad_img[:, w+pw-1:w+pw], (1,pw))

    elif pad_type == 'mirror':
        #top
        pad_img[:ph, pw:pw+w] = src[0:ph,:][::-1,...] # flip

        #bottom
        pad_img[ph+h:, pw:pw+w] = src[h-ph:h, :][::-1,...] # flip

        #left
        pad_img[:, :pw] = pad_img[:, pw:pw+pw][:,::-1] # flip

        #right
        pad_img[:, pw+w:] = pad_img[:, w:w+pw][:,::-1] # flip


    else:
        assert False, 'check pad type!'

    return pad_img

def showPaddingTest(img):
    zero_pad_img = padding(src=img, pad_size=(90,60), pad_type='zero')
    repetition_pad_img = padding(src=img, pad_size=(90,60), pad_type='repetition')
    mirror_pad_img = padding(src=img, pad_size=(90,60), pad_type='mirror')

    plt.figure(figsize=(12,5))
    plt.subplot(1,3,1)
    plt.title('zero padding')
    plt.imshow(zero_pad_img, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1,3,2)
    plt.title('repetition padding')
    plt.imshow(repetition_pad_img, cmap='gray', vmin=0, vmax=255)

    plt.subplot(1,3,3)
    plt.title('mirror padding')
    plt.imshow(mirror_pad_img, cmap='gray', vmin=0, vmax=255)

    plt.show()


def main():
    img = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=np.uint8)
    dst = padding(img, (2,2), 'mirror')
    print(dst)

if __name__ =='__main__':
    main()