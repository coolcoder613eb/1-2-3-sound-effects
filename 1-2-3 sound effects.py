import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.core.image import Image
from kivy.graphics import *

img = 'img.png'

class AppLayout(GridLayout):
    
    def __init__(self, **kwargs):
        super(AppLayout, self).__init__(**kwargs)
        #self.canvas.add(Color(0, 0, 1))
        with self.canvas.before:
            Color(0, 0, 1, 1) # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(source=img,size=self.size,
                               pos=self.pos)
        self.padding = [50,80]
        self.spacing = 30
        self.cols = 2
        self.col_default_width = 220
        self.row_default_height = 80
        self.col_force_default = True
        self.row_force_default = True
        self.bhorse = Button(text='Horse',
                      background_color=(0, 0, 1, 1),
                      font_size=50)
        self.bsiren = Button(text='Siren',
                      background_color=(0, 0, 1, 1),
                      font_size=50)
        self.bgoat = Button(text='Goat',
                      background_color=(0, 0, 1, 1),
                      font_size=50)
        self.bhonk = Button(text='Honk',
                      background_color=(0, 0, 1, 1),
                      font_size=50)
        self.bknock = Button(text='Knocking',
                      background_color=(0, 0, 1, 1),
                      font_size=50)
        self.brooster = Button(text='Rooster',
                      background_color=(0, 0, 1, 1),
                      font_size=50)
        self.bdoor = Button(text='Door',
                      background_color=(0, 0, 1, 1),
                      font_size=50)
        self.bsnore = Button(text='Snore',
                      background_color=(0, 0, 1, 1),
                      font_size=50)
        self.add_widget(self.bhorse)
        self.add_widget(self.bsiren)
        self.add_widget(self.bgoat)
        self.add_widget(self.bhonk)
        self.add_widget(self.bknock)
        self.add_widget(self.brooster)
        self.add_widget(self.bdoor)
        self.add_widget(self.bsnore)
        
        

    

    # listen to size and position changes
    
def update_rect(instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
        
class SoundEffectsAppApp(App):
    
    def build(self):
        l = AppLayout()
        l.bind(pos=update_rect, size=update_rect)
        return l


if __name__ == '__main__':
    SoundEffectsAppApp().run()
