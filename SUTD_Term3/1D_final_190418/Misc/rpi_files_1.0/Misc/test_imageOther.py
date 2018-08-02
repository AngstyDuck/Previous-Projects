import time
tic = time.clock()

from picamera import PiCamera
import cv2

camera = PiCamera()
while True:
    print('Taking Picture...')
    camera.capture('image1.jpg')
    image = 'image1.jpg'
    images = cv2.imread(image)
    (h, w)=images.shape[:2]
    img = cv2.resize(images,(300,300))







toc = time.clock()
print('processing time: {0}'.format(toc-tic))
