from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from firebase import firebase
import numpy as np
import time

url = "https://dmini-1ac59.firebaseio.com/" # URL to Firebase database
token = "NKLCd1EWC9buuxN9tJw3Oe6djsZQVTjePSdbiZK1" # unique token used for authentication

firebase=firebase.FirebaseApplication(url,token)



class MySMClass(sm.SM):
    start_state = 0
    def get_next_values(self, state, inp):

        if inp.button_backward:
            return 'halt', self.halt

############################### STATE ###################################
        if self.state == 0: # thymio is not moving at this state (o/p = halt)
            if firebase.get('/coord') == '0':
                self.state = 0
            else:
                self.c_x, self.c_y = firebase.get('/coord')
                self.state = 1
    '''
                magnitude = np.sqrt(self.c_x ** 2 + self.c_y ** 2)
                mv_time = magnitude/v          # let v = (pixels/ s) --> v is a fixed value that we have calculated from our own experiments
                w = 57.1429/180 * 3.14159
                rv_time = np.arctan2(y,x)/w     # time required to rotate and face target
    '''
            output = self.halt

        elif self.state == 1: # coord received, but 'run' not pressed
            output = self.halt
            if self.firebase.get('/command') == '1':
                self.state = 2
                self.now = time.time()
'''
::::::::::::::::::::::::::: THIS IS the 2nd STATE!!!! :::::::::::::::::::::::::::::::::
'''
        elif self.state == 2: # 'run' button has been pressed, rotate to face target
            output = self.rv
            if (time.time() - self.now) >= rv_time: #this is stopwatch, finished rotating
                self.state = 3
                output = self.halt
                self.now = time.time()
        elif self.state == 3: # finished rotating, now moving straight to target
            output = self.forward
            if (time.time() - self.now) >= mv_time: #this is stopwatch, finished moving
                self.state = 4
                output = self.halt
                self.now = time.time()



'''
::::::::::::::::::::::::::: THIS IS the 3rd STATE!!!! :::::::::::::::::::::::::::::::::
'''

        elif self.state == 4:
            output = self.reverse
            if (time.time() - self.now) >= mv_time: #this is stopwatch, finished moving
                self.state = 5
                output = self.halt
                self.now = time.time()

        elif self.state == 5:
            output = self.inv_rv
            if (time.time() - self.now) >= rv_time: #this is stopwatch, finished rotating
                self.state = 0
                output = self.halt
                self.now = time.time()
                firebase.put('/','cam','0') # tell camera to return to state 0
                firebase.put('/','coord','0')
                firebase.put('/','command','0')



        return self.state, output

    '''WE HAVE NOT DONE THIS TO GET THE VALUE OF V!!!!
    #mv_time is time required to reach target when thymio is moving straight.
    def mv_time(self):
        magnitude = np.sqrt(self.c_x ** 2 + self.c_y ** 2)
        return magnitude/v

    def rv_time(self):
        w = 57.1429/180 * 3.14159
        return np.arctan2(y,x)/w
    '''


    def halt(self): # thymio brake
        return io.Action(0,0)

    def forward(self): # speed tested on = 250 --> 7.82895(cm/ s)
        return io.Action(250,0)

    def reverse(self): # speed tested on = 250 --> 7.82895(cm/ s)
        return io.Action(-250,0)

    def rv(self): # speed tested on = 150 --> 57.1429(deg/ s)
        return io.Action(0,150)

    def inv_rv(self):
        return io.Action(0,-150)
'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'''
    def build(App): ### here here @ jun de FOR KIVY

        l1 = ToggleButton(text='Run', on_press = self.update_status, state = 'normal')
        label.add_widget(l1)

    def update＿status(self,instance):
        if instance.state == 'normal':
            instance.state == 'down'
            self.state = 1
            self.now = time.time()
'''
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'''
    #########################################
    # Don't modify the code below.
    # this is to stop the state machine using
    # inputs from the robot
    #########################################
    def done(self,state):
        if state=='halt':
            return True
        else:
            return False

MySM=MySMClass()

############################

m=ThymioSMReal(MySM)
try:
    m.start()
except KeyboardInterrupt:
    m.stop()
