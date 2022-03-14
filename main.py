from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout


# interface
class Inti(FloatLayout):
    pass


class stackInterface(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(30):
            b1 = Button(text=str(i+1), size_hint=(.15, .15), background_color=(i*0.1, i*0.2, i*0.3, 1))
            self.add_widget(b1)


# app creation
class TestApp(App):
    pass


TestApp().run()
