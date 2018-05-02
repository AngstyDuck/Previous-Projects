import time
import numpy as np
tic = time.clock()


#--------------------------------------Image Capture--------------------------
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, format='bgr')
image = rawCapture.array
#----------------------------------------------------------------------------



#--------------------------------------Grayscaling---------------------------

#outputImage = cv2.cvtColor(image, 'CV_BGR2GRAY')
#----------------------------------------------------------------------------



"""
    Note: The code below converts the image to output an array, where every element
    (i.e. pixel of the picture) represents the magnitude of 'blueness'. This array
    of a frame would be represented by variable name 'mask'. Every other color is
    removed from this picture.
    """
#step 1: converts BGR (color format) to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    #step 2: define range of blue color in HSV
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

    #step 3: threshold the HSVimage to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)



    #applies laplacian operator
"""
[Not used in 1D]
Laplacian operator applies to matrices, and for multivariable
functions it places a value on points on a graph, with the most
positive on the lowest 'trough' of the graph and the most negative
on the highest 'hill' of a graph.
"""
"""
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
cv2.imshow('laplacian', laplacian)
"""

    #applies sobel operators of x and y
"""
[Not used in 1D]
Sobel operators identify edges of a picture. In terms of matrix, they
place a value on the rate of change of the intensity of blue green or red
(for matrices representing color pictures), or the rate of change of
the intensity of 'whiteness' (for matrices representing grayscale images).
High values are placed for more extreme changes, and zero is placed for
areas with no change.
"""
"""
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
"""

#applies canny edge detector on pictures
"""
Canny edge detector is a step further from sobel operators, it takes the
output of sobel operators and tries to remove so-called noise by
[non-maximum suppression]
finding if a certain point is has the maximum value among nearby pixels, and
rendering non-maximum value pixels as zero. This thins out the edges of images
into a single line.
[hysteresis thresholding]
setting a certain value of the sobel operator as definitely an 'edge', and a
value that is definitely not. Edges that fall below the latter value is
immediately discarded, while the ones that are kept either has a value that
is above the former one (maximum sobel value), or is connected to the former
one and not below the latter one (minimum sobel value).

I would guess the second and third parameters of the Canny function
determines the max and min sobel value.
"""

edges = cv2.Canny(mask, 75, 150)
np.savetxt(r'/home/pi/dw1d/Datafiles/data_color_edge.txt',edges,fmt='%d')

"""
^ the imshow will now highlight the boundary of a blue object. As the array
'mask' is itself, a largely black image, we might want to lower the max and
min sobel value of our canny function to reveal more details to work with,
instead of wiping the edge of the object away as noise
"""
    





#-------------------------------------Shows the image------------------------
cv2.imshow('edges', edges)
print(edges)
cv2.waitKey(0)






toc = time.clock()
print('processing time: {0}'.format(toc-tic))
