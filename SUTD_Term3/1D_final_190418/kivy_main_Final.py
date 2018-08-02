from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.clock import Clock

from firebase import firebase
import numpy as np

import time

url = "https://dmini-1ac59.firebaseio.com/" # URL to Firebase database
token = "NKLCd1EWC9buuxN9tJw3Oe6djsZQVTjePSdbiZK1" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)


class DW1D_app(App):
    update_time_period = 1  # This time period is the interval the label.text updates it's timing once button is pressed
    schedule = None

    def build(self):
        """
        Has 2 buttons and one label.
        Buttons:
        Quit - quits program
        Start Program! - Puts data on firebase, changing the state of the camera; displays time as label

        Label:
        Either displays 'Awaiting instructions!' or a timer that runs down to zero.

        """

        layout = GridLayout(cols=1)
        self.l1 = Label(text='Awaiting instructions!', halign='center', valign='center')
        layout.add_widget(self.l1)
        b1 = Button(text='Start Program!', on_press=self.press_start, halign='center', valign='center')
        layout.add_widget(b1)
        b1 = Button(text='Quit', on_press=self.quit_app, halign='center', valign='center')
        layout.add_widget(b1)
        return layout

    def press_start(self, value):
        """
        Pressing start will trigger a few events:
        1. In firebase, the node 'cam' will be changed to 1
        2. Program will wait when the value of the node 'coord' in firebase is 0
        3. When the value of the node 'coord' != 0, we will set value of node
        '/command' = 1 (thymio will start scanning for coordinates and move)
        4. Estimated time before robot reaches destination will be calculated
        5. self.l1.text will regularly show that time slowly counting down to
        zero, then display 'Time's up'

        Functions:
        self.update,

        Values to edit:
        time_error_margin - the inherent time delay between the display of the
        time on self.l1.text, and the time where the thymio starts moving.

        """

        time_error_margin = 3  # <----------------------------Change this-----------------------------

        def calculating_time(x,y):
            """
            The function here calculates the time required for the thymio to travel to destination.
            Note, we will be experimenting and setting a value of v in this function (as well as
            the value w), which represents the pixel/s of the thymio, and the rotational speed of
            the thymio itself.

            Input:
            x,y - x and y of the coordinates updated to firebase.

            Output:
            Time required for thymio to rotate and move straight

            Module:
            Numpy

            Values to be changed:
            v, w
            """
            v = 73.47  # <----------------------------Change value of v here------------------------------------------
            magnitude = np.sqrt(x ** 2 + y ** 2)
            mv_time = magnitude/v
            w = 21.18/180 * 3.14159  # <--------------value changed: 21.18--------------------------------------------
            rv_time = np.arctan2(y, x)/w     # time required to rotate and face target
            return mv_time, rv_time

        # Step 1
        firebase.put('/', '/cam', 1)
        self.l1.text = 'Camera is reading...'

        # Step 2
        while firebase.get('/coord') == 0:
            print('ok')
        x, y = firebase.get('/coord')

        # Step 3
        firebase.put('/', '/command', 1)
        self.l1.text = 'Robot is moving...'

        # Step 4
        mv_time, rv_time = calculating_time(x, y)
        self.total_time = mv_time + rv_time + time_error_margin
        self.start_time = time.time()

        # Step 5
        self.schedule = Clock.schedule_interval(self.update, self.update_time_period)  # Used to call function regularly

    def update(self, *args):
        """
        This function will be called regularly to change the time displayed on
        self.l2.text once the start button is pressed.
        """
        thymio_travel_duration = self.total_time
        display_time = round(thymio_travel_duration + self.start_time - time.time(),2)

        if display_time >= 0:
            self.l1.text = 'estimated time left to reach object: {0} seconds'.format(display_time)
        elif display_time < 0:
            Clock.unschedule(self.schedule)  # Stops the regular calling of function update
            time.sleep(1)
            self.l1.text = "Awaiting instructions!"
        else:
            print('error')

    def quit_app(self, value):
        App.get_running_app().stop()


if __name__ == '__main__':
    DW1D_app().run()
