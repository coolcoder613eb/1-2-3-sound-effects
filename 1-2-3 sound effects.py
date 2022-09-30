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
import kivy.core.audio.audio_sdl2
#import kivy.core.audio.audio_ffpyplayer
from kivy.core.audio import SoundLoader

img = 'img.png'

shorse   = SoundLoader.load('sounds/bbc_horses-on-_07024178.mp3')
ssiren   = SoundLoader.load('sounds/bbc_dial-999--_07045258.mp3')
sgoat    = SoundLoader.load('sounds/bbc_goats---on_2.mp3')
shonk    = SoundLoader.load('sounds/bbc_cars---bus_2.mp3')
sknock   = SoundLoader.load('sounds/bbc_ten-urgent_07037567.mp3')
srooster = SoundLoader.load('sounds/bbc_domestic-f_nhu2.mp3')
sdoor    = SoundLoader.load('sounds/bbc_wooden-doo_07037344.mp3')
ssnore   = SoundLoader.load('sounds/snore.mp3')

def shorseplay(i):
    shorse.play()

def ssirenplay(i):
    ssiren.play()

def sgoatplay(i):
    sgoat.play()

def shonkplay(i):
    shonk.play()

def sknockplay(i):
    sknock.play()

def sroosterplay(i):
    srooster.play()

def sdoorplay(i):
    sdoor.play()

def ssnoreplay(i):
    ssnore.play()

class AppLayout(GridLayout):
    
    def __init__(self, **kwargs):
        super(AppLayout, self,).__init__(**kwargs)
        #self.canvas.add(Color(0, 0, 1))
        
        self.padding = 50
        self.spacing = 30
        self.cols = 2
        self.col_default_width = 220
        self.row_default_height = 80
        self.col_force_default = True
        self.row_force_default = True
        self.bhorse = Button(text='Horse',
                      background_color=(0, 0, 1, 1),
                      on_press=shorseplay,
                      font_size=50)
        self.bsiren = Button(text='Siren',
                      background_color=(0, 0, 1, 1),
                      on_press=ssirenplay,
                      font_size=50)
        self.bgoat = Button(text='Goat',
                      background_color=(0, 0, 1, 1),
                      on_press=sgoatplay,
                      font_size=50)
        self.bhonk = Button(text='Honk',
                      background_color=(0, 0, 1, 1),
                      on_press=shonkplay,
                      font_size=50)
        self.bknock = Button(text='Knocking',
                      background_color=(0, 0, 1, 1),
                      on_press=sknockplay,
                      font_size=50)
        self.brooster = Button(text='Rooster',
                      background_color=(0, 0, 1, 1),
                      on_press=sroosterplay,
                      font_size=50)
        self.bdoor = Button(text='Door',
                      background_color=(0, 0, 1, 1),
                      on_press=sdoorplay,
                      font_size=50)
        self.bsnore = Button(text='Snore',
                      background_color=(0, 0, 1, 1),
                      on_press=ssnoreplay,
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
        g = GridLayout()
        g.cols = 1
        with g.canvas.before:
            Color(0, 0, 1, 1) # green; colors range from 0-1 instead of 0-255
            g.rect = Rectangle(source=img,size=g.size,
                               pos=g.pos)
        g.label = Label(text='1-2-3 Sound Effects',
                        height = 80,
                        size_hint = (1, None),
                        color = [1,0,0,1],
                        font_size=50)
        
        g.spacing = 0
        g.add_widget(g.label)
        g.l = AppLayout(size_hint = (1, None))
        g.bind(pos=update_rect, size=update_rect)
        g.add_widget(g.l)
        return g


if __name__ == '__main__':
    SoundEffectsAppApp().run()
