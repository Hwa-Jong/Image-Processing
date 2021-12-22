import cv2

import histogram
import padding
import filtering
import gaussian_filter_separability
import interpolation
import cannyEdge

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

def interpolationTest():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    interpolation.showInterpolationTest(img)

def cannyEdgeDetection():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    cannyEdge.showCannyEdgeTest(img)

def main():
    #histogramTest()
    #paddingTest()
    #filteringTest()
    #gausFilterSeparability()
    #interpolationTest()
    cannyEdgeDetection()

    

if __name__ =='__main__':
    main()