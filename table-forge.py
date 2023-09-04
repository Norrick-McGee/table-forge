import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

import pandas

class TableForge(App):
    def build(self):
        return MainGrid() 

class MainGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HomeScreen())
        rollscreen1 = RollScreen()
        rollscreen2 = RollScreen()

class RollTable(pandas.DataFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class RollScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        rolltable1 = RollTable()

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        grid = GridLayout(cols = 3)
        search_label = Label(text="Search for a roll table")
        search_text = TextInput()
        search_button = Button()
        grid.add_widget(search_label)
        grid.add_widget(search_text)
        grid.add_widget(search_button)
        self.add_widget(grid)

if __name__ == '__main__':

    App = TableForge()
    App.run()
