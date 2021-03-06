from kivy.animation import Animation
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.stacklayout import StackLayout
import random

from kivy.uix.widget import Widget


class CustomWidget(Widget):
    pass


class CustomWidget_2(Widget):
    pass


class MainInterface_2(Widget):
    cw = CustomWidget_2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.music = SoundLoader.load("House_Lannister.mp3")
        if self.music:
            self.music.play()
            print(self.music.length)
            self.music.volume = 0.2
        else:
            pass
        self.cw()
        circle_1 = self.cw(pos=(200, 300), size=(85, 85), hex_code="#50A3A4")
        self.add_widget(circle_1)
        circle_2 = self.cw(pos=(300, 300), size=(85, 85), hex_code="#FCAF38")
        self.add_widget(circle_2)
        self.circle_3 = self.cw(pos=(400, 300), size=(85, 85), hex_code="#F93553")
        self.add_widget(self.circle_3)
        # animations
        anim1 = Animation(x=400, duration=1.8)
        anim1.start(circle_1)
        anim2 = Animation(pos=(300, 400), duration=.3)
        anim2 += Animation(pos=(200, 400), duration=.3)
        anim2 += Animation(pos=(200, 300), duration=.3)
        anim2.start(circle_2)
        anim2.bind(on_complete=self.motions3)

    def motions3(self, *args):
        anim3 = Animation(pos=(400, 400), duration=.3)
        anim3 += Animation(pos=(300, 400), duration=.3)
        anim3 += Animation(pos=(300, 300), duration=.3)
        anim3.start(self.circle_3)


class MainInterfaceAnimation(Widget):
    cw = ObjectProperty(CustomWidget)
    pert_val = StringProperty("0%")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cw()
        Clock.schedule_interval(self.looper, 0.1)
        custom_wid = self.cw(pos=(300, 300), wid=8)
        self.add_widget(custom_wid)
        self.custom_wid2 = self.cw(pos=(300, 300), angle=0, wid=5,
                                   cr=.9)
        self.add_widget(self.custom_wid2)
        self.pert_val = str(self.custom_wid2.angle)
        anim = Animation(angle=360, duration=3)
        anim.start(self.custom_wid2)
        sg_anim = self.cw(pos=(300, 500), wid=7, segments=10)
        self.add_widget(sg_anim)
        sg_animation = Animation(segments=3, duration=3)
        sg_animation.start(sg_anim)

    def looper(self, dt):
        self.pert_val = str(int(self.custom_wid2.angle/360 * 100))+'%'


class My_ScreenManager(BoxLayout):

    def firstBtn(self, SM):
        SM.current = "second"
        SM.transition.direction = "left"

    def secondBtn(self, SM):
        SM.current = "first"
        SM.transition.direction = "right"


class Image_Viewer(BoxLayout):
    pass


Builder.load_string("""
<ExternalKivy>:
    Button:
        text: "Hello"
        background_color: 1,0,0,1
""")


class Canvas_tuts(BoxLayout):
    pass


class ExternalKivy(BoxLayout):
    pass


class Variables(BoxLayout):
    _text_ = StringProperty("Hello World")

    def pressing(self, btn):
        btn.text = "We have changed this text with help of self"


class LogicalInterface(BoxLayout):
    def OnPressing(self, ID, input):  # ID From Test.kv
        print("Hello World!")
        cal = eval(input.text)
        ID.text = str(cal)

    def OnReleasing(self, ID, input):  # ID From Test.kv
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
            b1 = Button(text=str(i + 1), size_hint=(None, None), size=(100, 100))
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


class Game(BoxLayout):
    btn_list = []
    i = 0

    def create_btn(self):
        r = random.randint(1, 10)
        g = random.randint(1, 10)
        b = random.randint(1, 10)
        R = r / 10
        G = g / 10
        B = b / 10
        btn = Button(text="Button {}".format(self.i), size_hint=(None, None), size=(100, 100),
                     background_color=(R, G, B), background_normal="", font_size=20)
        self.btn_list.append(btn)
        # ids is a collection of all ids
        self.ids.stacker.add_widget(self.btn_list[self.i])
        print("Button {} Created".format(self.i))
        self.i += 1

    def remove_btn(self):
        if self.i > 0:
            self.ids.stacker.remove_widget(self.btn_list[self.i - 1])
            print("Button {} Removed".format(self.i - 1))
            if self.i - 1 >= 0:
                self.i -= 1


# app creation
class TestApp(App):
    pass


TestApp().run()
