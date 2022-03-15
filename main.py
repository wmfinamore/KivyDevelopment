from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout


class Relative_Practice(FloatLayout):
    pass


# interface
class Interface(FloatLayout):
    pass


class Scroller_Func():
    pass


class StackInterface(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            b1 = Button(text=str(i+1), size_hint=(None, None), size=(100, 100))
            self.add_widget(b1)


# app creation
class TestApp(App):
    pass


TestApp().run()
