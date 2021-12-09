import histogram
import cv2




def main():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    histogram.showHistEqual(img//2)
    

if __name__ =='__main__':
    main()