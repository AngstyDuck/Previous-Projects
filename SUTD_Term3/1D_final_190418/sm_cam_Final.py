from libdw import sm
from firebase import firebase
import numpy as np
import time
import cv2
from picamera import PiCamera
camera = PiCamera()

'''
take note: we have 3 folders in firebase:
1. 'cam' --> put '1' when camera has sent coordinates to 'coord' --> receive '0' when thymio has returned
2. 'command' --> sends '1' when ToggleButton(text = 'Run') is pressed --> receives '0' when thymio has returned
3. 'coord' --> sends coordinates when camera has finished scanning and len(contour) > 1
'''

url = "https://dmini-1ac59.firebaseio.com/" # URL to Firebase database
token = "NKLCd1EWC9buuxN9tJw3Oe6djsZQVTjePSdbiZK1" # unique token used for authentication

firebase=firebase.FirebaseApplication(url,token)

class MySMClass(sm.SM):
    start_state = 0

    def get_next_values(self, state, inp):
        # Checks value of node '/cam' in firebase, if value is 1, state of camera changed to 1, if value is 0, state of
        # camera is 0
        if inp == 1:
            state = 1
        elif inp == 0:
            state = 0

        # State machine, if state=0, continue checking value of node '/cam' in firebase, if state=1, take photo of
        # ground, apply Canny edge detector to outline just the edge of the object in the picture. Then apply
        # cv2.findContours to find the estimated middle point of the object, and put the coordinates as values of the
        # node '/coord' in firebase.
        # After that, put value of node '/cam' as 0 in firebase, state of camera change to 0; process repeats.
        if state == 0:
            print('0')
            if firebase.get('/cam') == '1':
                state = 1
            return state, state
        elif state == 1:
            print('1')
            camera.capture('image.jpg', resize = (400, 400))
            img = cv2.imread('image.jpg', 0)

            #Image processing
            edges = cv2.Canny(img, 75, 150)
            ret, thresh = cv2.threshold(edges, 127, 255, 0)
            im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) < 2:
                return state, state  # returns to state = 0
            cnt = contours[1]

            #creation and putting of coordinates
            M = cv2.moments(cnt)
            c_y = int(M['m10']/M['m00'])
            c_x = int(M['m01']/M['m00'])
            firebase.put('/', 'coord', (c_x,c_y))
            firebase.put('/', 'cam', '0')
            state = 0
            return state, state


MySM=MySMClass()
MySM.start()
while True:
    MySM.step(firebase.get('/cam'))
