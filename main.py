from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(text="Я"))
		
        self.add_widget(Label(text="Люблю"))
		
        self.add_widget(Label(text="Лисичку"))
		
class SimpleKivy(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    SimpleKivy().run()
