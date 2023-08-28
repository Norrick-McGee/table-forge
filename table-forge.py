import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.label import Label

class TableForge(App):
    def build(self):
        return Label(text="Welcome Dungeon Master")


if __name__ == '__main__':
    App = TableForge()
    App.run()
