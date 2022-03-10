from kivy.app import App
from kivy.uix.widget import Widget


# interface
class Interface(Widget):
    def On_Enter_Pressed(self):
        print("Enter Has Been Pressed! \n Boom You have made some progress in Logics")


# app creation
class TestApp(App):
    pass


TestApp().run()
