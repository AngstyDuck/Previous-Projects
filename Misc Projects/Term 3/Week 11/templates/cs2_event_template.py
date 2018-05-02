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
		print('instance: {0}, touch: {1}'.format(instance,touch.dx))
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
