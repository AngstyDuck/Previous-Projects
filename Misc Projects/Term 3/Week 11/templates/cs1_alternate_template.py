from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class AlternateApp(App):
	state = 0

	def build(self):
		b = Button(
			text='Programming is fun',
			font_size=25)
		b.bind(on_touch_down=self.alternate)
		return b


	def alternate(self,instance, touch):
		print(touch.dx)
		if self.state == 0:
			self.state = 1
			instance.text = 'It is fun to program'
		elif self.state == 1:
			self.state = 0
			instance.text = 'Programming is fun'
			pass
		else:
			return 'self.state error'


myapp=AlternateApp()
myapp.run()