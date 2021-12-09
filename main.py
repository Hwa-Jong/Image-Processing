import cv2

import histogram
import padding
import filtering
import gaussian_filter_separability

def histogramTest():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    histogram.showHistEqual(img//2)

def paddingTest():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    padding.showPaddingTest(img)

def filteringTest():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    filtering.showFilteringTest(img)

def gausFilterSeparability():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    gaussian_filter_separability.separabilityTest(img)

def main():
    #histogramTest()
    #paddingTest()
    #filteringTest()
    gausFilterSeparability()

    

if __name__ =='__main__':
    main()