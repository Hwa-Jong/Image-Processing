import cv2

import histogram
import padding
import filtering
import gaussian_filter_separability
import interpolation
import cannyEdge
import morphology
import restoration
import adaptiveFiltering

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

def cannyEdgeDetectionTest():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    cannyEdge.showCannyEdgeTest(img)

def morphologyTest():
    morphology.showMorphologyTest()

def restorationTest():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    restoration.GaussianNoiseRemoval(img)

def adaptiveFilteringTest():
    img = cv2.imread( 'image/lenna.png' , cv2.IMREAD_GRAYSCALE)
    adaptiveFiltering.showAdaptiveFilteringTest(img)



def main():
    #histogramTest()
    #paddingTest()
    #filteringTest()
    #gausFilterSeparability()
    #interpolationTest()
    #cannyEdgeDetectionTest()
    #morphologyTest()
    #restorationTest()
    adaptiveFilteringTest()


    

if __name__ =='__main__':
    main()