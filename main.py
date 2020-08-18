# -*- coding: utf-8 -*-
import gi
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


from UnityTweakTool.section.windowmanager import WindowManager

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.rst import RstDocument
from kivy.lang import Builder
import os
import kivy.resources
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty, BooleanProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import mainthread

import time
import threading
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.metrics import dp
from database import Database
from kivy.properties import NumericProperty
from kivy.core.window import Window
from os.path import dirname, join



kivy.resources.resource_add_path('/usr/share/fonts/')
LabelBase.register(DEFAULT_FONT, "truetype/takao-gothic/TakaoPGothic.ttf")
#LabelBase.register(DEFAULT_FONT, "opentype/noto/NotoSansCJK-Bold.ttc")


# with open('my.kv', encoding='utf8') as f:
#     Builder.load_string(f.read())


class LicensScreen(Screen):
    text = ""
    with open("assets/inFileII.txt") as fobj:
        for line in fobj:
            text += line

class MyScreen(Screen):
    pass

class Screen1(Screen):
    pass
class Screen2(Screen):
    pass
class MainScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")
sm = WindowManager()

# screens = [MainScreen(name="main_screen"), Screen1(name="screen1"), Screen2(name="screen2")]
# for screen in screens:
#     sm.add_widget(screen)


# screens = [PreScreen(name="pre"), ListScreen(name="speakers")]
# for screen in screens:
#     sm.add_widget(screen)
#
# sm.current = "pre"

class Screen1(Screen):
    pass



class MyApp(App):
    def build(self):
        self.title = 'Hello world'
        return MyScreen()
        # return LicensScreen()
        #return Controller()
        # return sm

    # def build(self): #for external kv files
    #     return sm
    #     # self.load_screen(0)

if __name__ == "__main__":
    MyApp().run()


