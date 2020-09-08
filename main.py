#kivy.require("1.8.0")

from random import randint
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

#Word List

words = [
    "dog",
    "cloud",
    "cat",
    "tree",
    "river",
    "tired guy",
    "angry guy",
    "sleepy guy",
    "hat",
    "angel",
    "eyeball",
    "pizza",
    "giraffe",
    "castle",
    "rabbit",
    "baby",
    "giraffe",
    "tiny dog",
    "pencil",
    "potato",
    "snowflake",
    "cake"
]

#Drawing Widget

class Painter(Widget):
    def on_touch_down(self, touch):
        #Set color to blue
        color = (.7, 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]


#Image Button

class ImageButton(ButtonBehavior, Image):
    pass


#Screen Manager

class ScreenManagement(ScreenManager):
    pass

#Screens

class MainScreen(Screen):
    pass

class ReadyScreen(Screen):
    pass

class WordScreen(Screen):
    def random_word(self):
        end = len(words) - 1
        randomword = words[randint(0, end)].lower() + "."
        return randomword

class DrawingScreen(WordScreen, Screen):
    pass

#GUI Builder & Run

presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()