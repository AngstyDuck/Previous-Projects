
"""
#Cohort Question 1
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
		print(touch.is_double_tap)
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


"""

"""
#-------------------------Question 2----------------------------
from kivy.app import App
from kivy.uix.label import Label

class SlideDetectApp(App):
	def build(self):
		b = Label(
			text = 'Slide Me'
		)
		b.bind(on_touch_move=self.detect)
		return b

	def detect(self, instance, touch):
		#if not instance.collide_point(touch.x, touch.y):
		#	return False
		print(touch.dx)
		if touch.dx<-40:
			instance.text = 'Slide Left'
		if touch.dx>40:
			instance.text = 'Slide Right'
		if touch.dy<-40:
			instance.text = 'Slide Down'
		if touch.dy>40:
			instance.text = 'Slide Up'
		return True

if __name__=='__main__':
	SlideDetectApp().run()
"""


























