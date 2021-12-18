# Image-Processing
Image Processing Study

----------
## histogram & histogram equalization
![results](https://github.com/Hwa-Jong/Image-Processing/blob/main/Fig/histogram.png)

----------
## padding
![results](https://github.com/Hwa-Jong/Image-Processing/blob/main/Fig/padding.png)

----------
## filtering
![results](https://github.com/Hwa-Jong/Image-Processing/blob/main/Fig/filtering.png)

----------
## Gaussian Filter Separability Test
using 2D gaussian filter  
2D gaussian filter time : 3.483424 sec  
using 1D gaussian filter  
1D gaussian filter time : 1.777921 sec  
< results check >  
dst_2D - dst_1D :  -0.0  

----------
## interpolation
![results](https://github.com/Hwa-Jong/Image-Processing/blob/main/Fig/interpolation.png)

###### forward img[:7, :7]
[[158   0 158   0 162   0 158]<br />
 [  0   0   0   0   0   0   0]<br />
 [158   0 158   0 162   0 158]<br />
 [  0   0   0   0   0   0   0]<br />
 [158   0 158   0 162   0 158]<br />
 [  0   0   0   0   0   0   0]<br />
 [158   0 158   0 162   0 158]]<br />
 
 ###### in this case, you can find holes

###### backward img[:7, :7] 
[[158 158 158 160 162 160 158]<br />
 [158 158 158 160 162 160 158]<br />
 [158 158 158 160 162 160 158]<br />
 [158 158 158 160 162 160 158]<br />
 [158 158 158 160 162 160 158]<br />
 [158 158 158 160 162 160 158]<br />
 [158 158 158 160 162 160 158]]<br />