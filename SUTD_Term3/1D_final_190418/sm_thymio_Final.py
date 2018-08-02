from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from firebase import firebase
import numpy as np
import time

url = "https://dmini-1ac59.firebaseio.com/" # URL to Firebase database
token = "NKLCd1EWC9buuxN9tJw3Oe6djsZQVTjePSdbiZK1" # unique token used for authentication

firebase = firebase.FirebaseApplication(url, token)
# print('done')


class MySMClass(sm.SM):
    """
    This one is a state machine. Involves 6 states that could be grouped into 3
    phases
    Phase 1 - Thymio is stationary
    state 0 : thymio constantly scans value of 'command' node in firebase. If value is 0,
    thymio stays stagnant, if value is 1, state = 1. output = self.brake()
    state 1 : thymio is not moving, awaits coordinates from 'coord' node in firebase. Once
    received, returns state changes = 2, output is self.rv_(). self.mv_time and
    self.rv_time is defined

    Phase 2 - Thymio is on the move
    state 2 : thymio will be rotating. When the duration of rotating has not
    exceeded the duration specified by formula, state = 2, output = self.rv_()
    When duration has exceeded, state = 3, output = self.forward()
    state 3 : thymio will be moving forward. When the duration of rotating has not
    exceeded the duration specified by formula, state = 3, output = self.forward()
    Wehn duration has exceeded, state = 4, output = self.reverse()

    Phase 3 - Thymio is reversing
    state 4 : same as state 2 and 3, except now the thymio is in reverse. When
    duration exceeds, state = 5, output = self.inv_rv()
    state 5 : same as 4, except now the thymio is in inverse rotate. When duration
    exceeds, state = 0, output = self.brake(). We will reset the values of node
    '/command' and '/coord' to the default value 0, and reset global variables
    self.mv_time and self-rv_time as None


    Overall note: value v has yet been confirmed, please change it at
    function get_next_values > if state=1 > function calculating_time > v
    [edit: value has been updated, tgt with the function w found in function
    calculating_time]

    """
    start_state = 0

    def get_next_values(self, state, inp):

        if inp.button_backward:
            return 'brake', self.brake()

        # State 0
        if state == 0:
            output = self.brake()
            print('o')
            if firebase.get('/command') == 1:
                state = 1

        # State 1
        elif state == 1:
            print('1')
            output = self.brake()
            if firebase.get('/coord') == 0:
                state = 0
            else:
                def calculating_time(x,y):
                    """
                    The function here calculates the time required for the thymio to travel to destination.
                    Note, we will be experimenting and setting a value of v in this function (as well as
                    the value w), which represents the pixel/s of the thymio itself.

                    Input:
                    x,y - x and y of the coordinates updated to firebase.

                    Output:
                    Time required for thymio to rotate and move straight

                    Module:
                    Numpy

                    Values to be changed:
                    v, w
                    """
                    v = 73.47  # <----------------------------------Change value of v here------------------------------
                    magnitude = np.sqrt(x ** 2 + y ** 2)
                    mv_time = magnitude/v
                    w = 21.18/180 * 3.14159  # <---------------------value changed: 21.18-------------------------------
                    rv_time = np.arctan2(y,x)/w  # time required to rotate and face target
                    return mv_time, rv_time

                self.c_x, self.c_y = firebase.get('/coord')
                self.mv_time,self.rv_time = calculating_time(self.c_x,self.c_y)
                state = 2
                self.now = time.time()

        # State 2
        elif state == 2:
            output = self.rv_()
            print('2')
            # print('phase 2: {0}'.format(time.time() - self.now))
            if (time.time() - self.now) >= self.rv_time:  # this is stopwatch, finished rotating
                output = self.forward()
                state = 3
                self.now = time.time()

        # State 3
        elif state == 3:
            print('3')
            # print('phase 3: {0}'.format(time.time() - self.now))
            output = self.forward()
            if (time.time() - self.now) >= self.mv_time:  # this is stopwatch, finished moving
                state = 4
                output = self.reverse()
                self.now = time.time()

        # State 4
        elif state == 4:
            print('4')
            # print('phase 4: {0}'.format(time.time() - self.now))
            output = self.reverse()
            if (time.time() - self.now) >= self.mv_time:  # this is stopwatch, finished moving
                state = 5
                output = self.inv_rv()
                self.now = time.time()

        # State 5
        elif state == 5:
            print('5')
            # print('phase 5: {0}'.format(time.time() - self.now))
            output = self.inv_rv()
            if (time.time() - self.now) >= self.rv_time:  # this is stopwatch, finished rotating
                state = 0
                output = self.brake()
                self.now = time.time()

                # Resetting firebase values to 0 and clearing unused nonlocal variables
                firebase.put('/','coord',0)
                firebase.put('/','command',0)
                self.mv_time = None
                self.rv_time = None

        next_state = state
        return next_state, output

    def brake(self):  # thymio brake
        return io.Action(0,0)

    def forward(self):  # speed tested on = 250 --> 7.82895(cm/ s)
        return io.Action(1,0)

    def reverse(self):  # speed tested on = 250 --> 7.82895(cm/ s)
        return io.Action(-1,0)

    def rv_(self):  # speed tested on = 150 --> 57.1429(deg/ s)
        return io.Action(0,0.5)

    def inv_rv(self):
        return io.Action(0,-0.5)

    #########################################
    # Don't modify the code below.
    # this is to stop the state machine using
    # inputs from the robot
    #########################################
    def done(self,state):
        if state == 'brake':
            return True
        else:
            return False


MySM = MySMClass()

############################

m = ThymioSMReal(MySM)
try:
    m.start()
except KeyboardInterrupt:
    m.stop()
