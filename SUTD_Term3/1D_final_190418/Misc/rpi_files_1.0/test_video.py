#Note - This prog is to identify the position of the edge

import time
tic = time.clock()

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (400,400)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size = (400,400))

time.sleep(0.1)

"""
Matrices are used to represent each frame by having a numerical value assigned
to every pixel of the frame. In grayscale the value would represent the
'whiteness' of the pixel. In color the matrix would represent 3 smaller matrices
inside, each representing the intensity of Blue, Green and Red.

An array would be used to express these matrices, with each row of the matrix
represented by an element in the array. In this case numpy n-dimensional arrays
are used instead of nested lists as numpy arrays allows for operations that are
much more suited for the context of matrices.

"""

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    image = frame.array
    
    #displays colored video

    cv2.rectangle(image, (10,10), (390,390), (0,255,0),1)
    cv2.imshow("Frame", image)
    

    #displays grayscale video
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    """

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
    """
    edges = cv2.Canny(gray, 75, 150)
    cv2.imshow('edges', edges)
    print(edges)
    """
    
    #stops loop when the letter 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):  
        break

    #clear the stream between captures. A way to get by the restrictions in Python 2 in error handling. Apparently uses concepts of exception chaining. Could be placed anywhere (i think?)
    rawCapture.truncate(0)
    






cv2.destroyAllWindows()  #closes all windows including the one with the video feed
toc = time.clock()
print('processing time: {0}'.format(toc-tic))
