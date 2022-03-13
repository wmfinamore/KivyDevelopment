from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


# interface
class Inti(FloatLayout):
    layout = BoxLayout()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Hello", size_hint=(.25, .25), pos=(200, 100))
        self.layout.add_widget(b1)
        self.add_widget(self.layout)


# app creation
class TestApp(App):
    pass


TestApp().run()
