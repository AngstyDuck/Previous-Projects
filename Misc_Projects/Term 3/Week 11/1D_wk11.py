from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton





class laptop_side(App):
    def build(self):
        """
        #state 0: currently off; state 1: currently on
        self.state_yellow_button = 0
        self.state_red_button = 0
        """

        layout = GridLayout(cols=2)

        l1 = Label(text='Yellow LED')
        b1 = ToggleButton(text='off', on_press=self.press, id='yellow123')
        layout.add_widget(l1)
        layout.add_widget(b1)

        l2 = Label(text='Red LED')
        b2 = ToggleButton(text='off', on_press=self.press, id='red123')
        layout.add_widget(l2)
        layout.add_widget(b2)

        return layout


    def press(self, instance):
        print(instance.id)


myapp=laptop_side()
myapp.run()


