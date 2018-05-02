from libdw import sm
from firebase import firebase
import numpy as np
import time
import cv2

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
        if state == 0:
            camera.capture('image.jpg')
            img = cv2.imread('image.jpg',0)
            ret,thresh = cv2.threshold(img,127,255,0)
            #cv2.imshow('abc', img)   ################ @ Junde: do you want to display image on kivy + draw contours?
            #cv2.waitKey(0)

            im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) < 2:
                return state, state ## returns to state = 0
            cnt = contours[1]
            M = cv2.moments(cnt)

            c_x = int(M['m10']/M['m00'])
            c_y = int(M['m01']/M['m00'])
            firebase.put('/','coord', (c_x,c_y))
            firebase.put('/','cam','1')
            state = 1
            return state,state
        elif state == 1:
            if self.firebase.get('/cam') == '0':
                state = 0
            return state,state




'''
### VALUES FOR pixels/ s IS STILL NEEDED --> v --------> @ junde u can use this for ETA for thymio to reach target.
### as discussed, self.start = time.time() + mv_time() + rv_time()
### time_ETA = int(self.start - time.time())
### use kivy.clock function! --> Clock.schedule_interval(time_ETA, 1) # in kivy, it reads this function every 1 second
    def mv_time(self):
        magnitude = np.sqrt(self.c_x ** 2 + self.c_y ** 2)
        return magnitude/v

    def rv_time(self):
        w = 57.1429/180 * 3.14159 # change deg to rad
        return np.arctan2(y,x)/w
'''



'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def build(App): ### here here @ jun de FOR KIVY

        l1 = ToggleButton(text='Run', on_press = self.update_status, state = 'normal')
        label.add_widget(l1)

    def update＿status(self,instance):
        if instance.state == 'normal':
            instance.state == 'down'
            state = 1
            self.now = time.time()
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'''


MySM=MySMClass()
MySM.start()
