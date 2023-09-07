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
        rollscreen1 = RollScreen('random-potions')
        rollscreen2 = RollScreen('loot-drow')

class RollTable(pandas.DataFrame):
    def __init__(self, description, **kwargs):
        super().__init__(**kwargs)
        self.description = description


class RollScreen(Screen):
    def __init__(self, _dev_rollscreen_str, **kwargs):
        '''
        _dev_rollscreen_str: 
            string for initializing a RollTable for a RollScreen
        '''
        super().__init__( **kwargs)
        


        ### Dev -- Generating RandomTable ###
        if _dev_rollscreen_str == 'random-potions':
            table = {
                      'roll': [1, 2],
                      'potion': ['healing potion', 'mana potion'],
                      'description': ['heals 2d10 damage', 'restores 1d8 mana']
                    } 
                    
            self.roll_table = RollTable('Random Potions')
        elif _dev_rollscreen_str == '':
            self.roll_table = RollTable('Drow Loot')
        else:
            self.roll_table = RollTable('A New Roll Table')


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
