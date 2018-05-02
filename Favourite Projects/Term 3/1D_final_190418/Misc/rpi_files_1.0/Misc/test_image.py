import time
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

outputImage = cv2.cvtColor(image, 'CV_BGR2GRAY')
#----------------------------------------------------------------------------









#-------------------------------------Shows the image------------------------
cv2.imshow('Image',outputImage)
cv2.waitKey(0)






toc = time.clock()
print('processing time: {0}'.format(toc-tic))
