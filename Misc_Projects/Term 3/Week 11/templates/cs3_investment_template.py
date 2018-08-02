from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyLabel(Label):
    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.bind(size=self.setter('text_size'))
        print(self.setter('text_size'))
        self.padding = (20, 20)


class Investment(App):
    def build(self):
        layout = GridLayout(cols=2)

        l1 = MyLabel(text="Investment Amount", font_size=24, halign='center', valign='center')
        layout.add_widget(l1)
        self.invest_input_box = TextInput()
        layout.add_widget(self.invest_input_box)

        l2 = MyLabel(text="Years", font_size=24, halign='center', valign='center')
        layout.add_widget(l2)
        self.years_input_box = TextInput()
        layout.add_widget(self.years_input_box)

        l3 = MyLabel(text="Annual Interest Rate", font_size=24, halign='center', valign='center')
        layout.add_widget(l3)
        self.mth_int_input_box = TextInput()
        layout.add_widget(self.mth_int_input_box)

        # future invest amount label
        future_label = Label(text='Future Value', font_size=24, halign='center', valign='center')
        layout.add_widget(future_label)
        self.txt_future_val = Label(font_size=24)
        layout.add_widget(self.txt_future_val)

        btn = Button(text="Calculate", on_press=self.calculate, font_size=24)
        layout.add_widget(btn)

        return layout

    def calculate(self, instance):
        print('invest: {0}, years: {1}, mth: {2}'.format(self.invest_input_box.text,self.years_input_box.text,self.mth_int_input_box.text))
        inv_amt = float(self.invest_input_box.text)
        years = float(self.years_input_box.text)
        mth_int_rate = float(self.mth_int_input_box.text)
        self.txt_future_val.text = str(round(inv_amt * (1 + (mth_int_rate/1200)) ** (years * 12),2))


Investment().run()
