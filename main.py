import cv2

import histogram
import padding
import filtering

def histogramTest():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    histogram.showHistEqual(img//2)

def paddingTest():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    padding.showPaddingTest(img)

def filteringTest():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    filtering.showFilteringTest(img)

def main():
    #histogramTest()
    #paddingTest()
    filteringTest()
    

if __name__ =='__main__':
    main()