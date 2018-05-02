from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

from firebase import firebase

import time


url = "https://dmini-1ac59.firebaseio.com/" # URL to Firebase database
token = "NKLCd1EWC9buuxN9tJw3Oe6djsZQVTjePSdbiZK1" # unique token used for authentication
firebase=firebase.FirebaseApplication(url,token)

class MenuScreen(Screen):

    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout=GridLayout(cols=1)

        #Button that brings us to Begin
        button_begin = Button(text='BEGINZ!?!?!?!', on_press=self.change_to_Begin, font_size=20, halign='center', valign='center')
        self.layout.add_widget(button_begin)

        # Button that brings us to Instructions
        button_instruc = Button(text='Instructionzszsz', on_press=self.change_to_Instruc, halign='center', valign='center')
        self.layout.add_widget(button_instruc)

        #Button that quits
        button_quit = Button(text='Quit', on_press=self.quit_app, halign='center', valign='center')
        self.layout.add_widget(button_quit)

        self.add_widget(self.layout)

    def change_to_Begin(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
        self.manager.current = 'Begin'

    def change_to_Instruc(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
        self.manager.current = 'Instruc'

    def quit_app(self, value):
        App.get_running_app().stop()

class BeginScreen(Screen):
    update_time_period = 0.1
    schedule = None

    def __init__(self, **kwargs):
        """
        Has 2 buttons and one label.
        Buttons:
        Back - brings user to menu
        Start - Puts data on firebase, displays time as label

        Label:
        Either displays 'None' or a timer that runs down to zero.

        """

        Screen.__init__(self, **kwargs)
        self.layout = GridLayout(cols=1)
        b1 = Button(text='Back to Menu', on_press=self.change_to_menu, halign='center', valign='center')
        self.layout.add_widget(b1)
        self.l1 = Label(text='Lets Begin!', halign='center', valign='center')
        self.layout.add_widget(self.l1)
        b1 = Button(text='STARTZ', on_press=self.press_start, halign='center', valign='center')
        self.layout.add_widget(b1)
        self.add_widget(self.layout)
        pass

    def press_start(self, value):
        #changes state of cam to 1
        firebase.put('/', '/cam', 1)
        #note down start_time, used in function update
        self.start_time = time.time()
        #to change the text in the label to most updated time
        self.l1.text = 'time: {0}'.format(firebase.get('/time'))
        #Referenced with self. to enable Clock.unschedule to access it from another function
        self.schedule = Clock.schedule_interval(self.update, self.update_time_period)

    def update(self, *args):
        firebase_time = int(firebase.get('/time'))
        display_time = round(firebase_time + self.start_time - time.time(),2)

        if display_time > 0:
            self.l1.text = 'time: {0}'.format(display_time)
        elif display_time < 0:
            self.l1.text = "Time's Up!"
            firebase.put('/', 'time', None)
            Clock.unschedule(self.schedule)
        else:
            print('error')

    def change_to_menu(self, value):
        Clock.unschedule(self.schedule)
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
        self.manager.current = 'Menu'

class IntrucScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = GridLayout(cols=1)
        l1 = Label(text='Instructions', halign='center', valign='center')
        self.layout.add_widget(l1)
        b1 = Button(text='Back to Menu', on_press=self.change_to_menu, halign='center', valign='center')
        self.layout.add_widget(b1)
        # Add your code below to add the label and the button
        self.add_widget(self.layout)
        pass

    def change_to_menu(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
        self.manager.current = 'Menu'

class SwitchScreenApp(App):
    def build(self):
        sm = ScreenManager()
        ms = MenuScreen(name='Menu')
        bs = BeginScreen(name='Begin')
        it = IntrucScreen(name='Instruc')
        sm.add_widget(ms)
        sm.add_widget(bs)
        sm.add_widget(it)
        sm.current = 'Menu'
        return sm

if __name__ == '__main__':
    SwitchScreenApp().run()
