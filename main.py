from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.stacklayout import StackLayout


Builder.load_string("""
<ExternalKivy>:
    Button:
        text: "Hello"
        background_color: 1,0,0,1
""")


class ExternalKivy(BoxLayout):
    pass


class Variables(BoxLayout):
    _text_ = StringProperty("Hello World")

    def pressing(self, btn):
        btn.text = "We have changed this text with help of self"


class LogicalInterface(BoxLayout):
    def OnPressing(self, ID, input): # ID From Test.kv
        print("Hello World!")
        cal = eval(input.text)
        ID.text = str(cal)

    def OnReleasing(self, ID, input): # ID From Test.kv
        print("Don't Go!")



class Page_Layout(PageLayout):
    pass


class Page_1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Hello", background_color=(.3, .4, .5, 1))
        b2 = Button(text="World!", background_color=(.3, .4, .5, 1))
        self.add_widget(b1)
        self.add_widget(b2)


class Page_2(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Hello", background_color=(.6, .7, .8, 1))
        b2 = Button(text="World!", background_color=(.6, .7, .8, 1))
        self.add_widget(b1)
        self.add_widget(b2)


class Page_3(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Hello", background_color=(.2, .3, .4, 1))
        b2 = Button(text="World!", background_color=(.2, .3, .4, 1))
        self.add_widget(b1)
        self.add_widget(b2)


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


class Binding(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Hello")
        b1.bind(on_press=self.callback_funt)
        self.add_widget(b1)

    def callback_funt(self, event):
        print("Hello World")


class Buttons(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            b1=Button(text=str(i+1), size_hint=(None, None), size=(100,100))
            self.add_widget(b1)


class Game(BoxLayout):
    pass


# app creation
class TestApp(App):
    pass


TestApp().run()
