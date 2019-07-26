from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

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

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}

if __name__ == '__main__':
   reset()
   SimpleKivy().run()
