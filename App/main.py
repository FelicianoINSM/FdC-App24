
from connection import Connect

import kivy
kivy.require('2.3.0')

from kivy.config import Config
Config.set('graphics', 'width', '600')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class Home(Screen):
    def on_switch_active(self, switch, value):
        if value:
            Connect().bomb_test(1)
        else:
            Connect().bomb_test(0)


class Menu(Screen):
    pass
        
class TabManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class Riego(App):

    def build(self):
        return kv

if __name__ == '__main__':
    riegoApp = Riego()
    riegoApp.run()