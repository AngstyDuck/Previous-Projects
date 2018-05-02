from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.app import App
import time
from kivy.core.window import Window

Window.size = (1000, 400)
Clock.max_iteration = 20

class Timer(Label):
    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.font_size = 26
        self.halign = 'left'
        self.valign = 'middle'
    def update(self, dt):
        time_passed = time.time()-self.start
        if self.id == 'pred' and time_passed >= 25:
            time_passed = 25
        self.text = str(int(time_passed)) + ' seconds'

class Text(Label):
    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.font_size = 26
        self.halign = 'left'
        self.valign = 'middle'
    """
    def sensor():
        for i in os.listdir('/sys/bus/w1/devices'):
            if i != 'w1_bus_master1':
                ds18b20 = i
        return ds18b20
    
    def read(ds18b20):
        location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
        tfile = open(location)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        celsius = temperature / 1000
        farenheit = (celsius * 1.8) + 32
        return celsius, farenheit
    """
    def change_text(self, dt):
        #temp = self.read(self.sensor())[0]
        temp = 3
        if self.id == 'sen':
            self.text = str(temp)
        else:
            self.text = str(round(1.28784342*temp-6.50409405,2))

class TempPredict(App):
    
    def build(self):
        
        layout = GridLayout(cols=4)
        l1 = Text(text="Time Elapsed:")
        l2 = Text(text="Prediction Time:")
        l3 = Text(text="Sensor Reading:")
        l4 = Text(text="Temperature Predicted:")
        
        elapsed = Timer(id='elsp')
        predict = Timer(id='pred')
        sensor = Text(text="sense_temp", id='sen')
        result = Text(text="Predicting...", id='res')
        
        layout.add_widget(l1)
        layout.add_widget(elapsed)
        layout.add_widget(l2)
        layout.add_widget(predict)
        layout.add_widget(l3)
        layout.add_widget(sensor)
        layout.add_widget(l4)
        layout.add_widget(result)
        
        elapsed.start = time.time()
        predict.start = time.time()
        Clock.schedule_interval(elapsed.update, 1)
        Clock.schedule_interval(predict.update, 1)
        Clock.schedule_interval(sensor.change_text, 2)
        Clock.schedule_once(result.change_text, 26)
        
        return layout

if __name__=='__main__':
    TempPredict().run()
