from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout=BoxLayout(spacing=1)
        b1 = Button(text="Settings", on_press=self.change_to_setting, halign='center', valign='center')
        self.layout.add_widget(b1)
        b2 = Button(text='Quit', on_press=self.quit_app, halign='center', valign='center')
        self.layout.add_widget(b2)
        self.add_widget(self.layout)
        # Add your code below to add the two Buttons
    
    def change_to_setting(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
        self.manager.current='settings'

    def quit_app(self, value):
        App.get_running_app().stop()


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout=BoxLayout(spacing=1)
        l1 = Label(text='Settings Screen', halign='center', valign='center')
        self.layout.add_widget(l1)
        b1 = Button(text='Back to Menu', on_press=self.change_to_menu, halign='center', valign='center')
        self.layout.add_widget(b1)
        # Add your code below to add the label and the button
        self.add_widget(self.layout)
        pass

    def change_to_menu(self,value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
        self.manager.current='menu'



class SwitchScreenApp(App):
    def build(self):
        sm=ScreenManager()
        ms=MenuScreen(name='menu')
        st=SettingsScreen(name='settings')
        sm.add_widget(ms)
        sm.add_widget(st)
        sm.current='menu'
        return sm

if __name__=='__main__':
	SwitchScreenApp().run()
