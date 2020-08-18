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
from kivy.properties import ObjectProperty
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

class myJobEntry(BoxLayout):
    def __init__(self):
        super(myJobEntry, self).__init__()

    def addStuff(self,runindex,program):
        b1 = Button(text=runindex,size_hint=(None,1.0),width=100)
        vbox1 = BoxLayout(orientation='vertical')
        for ind in range(int(runindex), 0, -1):
            vbox1.add_widget(Button(text='{}'.format(ind)))
        self.add_widget(vbox1)

class Controller(TabbedPanel):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from the kv lang file.
    '''
    layout_content = ObjectProperty()
    # tab1_refresh_btn = ObjectProperty()
    text_input = ObjectProperty()
    i = 3
    h = NumericProperty(0)

    def on_pre_enter(self, *args):
        self.refresh()


    def addSeveralObjects(self, *args):
        self.layout_content.enabled=False
        myObj = myJobEntry()


        myObj.addStuff('{}'.format(self.i), '{}'.format(self.i))
        self.layout_content.add_widget(myObj)

    def refresh(self):
        # self.tab1_refresh_btn.enabled = False
        self.addSeveralObjects()
        # self.resetRefreshButton()


    def resetRefreshButton(self):
        pass
        # self.tab1_refresh_btn.text = 'Last Refresh: {}'.format(time.ctime())
        # self.tab1_refresh_btn.enabled = True

class MyScreen(Screen):
    pass

# class MyApp(MDApp):
#     def build(self):
#         return MyScreen()
#

db = Database("speakers.txt")

class ListScreen(Screen):
    def __init__(self, **kwargs):
        super(ListScreen, self).__init__(**kwargs)
        self.printSpeakersNum()
        self.floatLayout = FloatLayout()
        self.scrollView = ScrollView(do_scroll_x=False, do_scroll_y=True)

        self.gridLayout = GridLayout() #cols=1, size_hint_y=None, row_default_height=100 )#, height= self.gridLayout.minimum_height)
        self.gridLayout.cols = 1
        self.gridLayout.size_hint_y = None
        self.gridLayout.row_default_height = 100
        #self.gridLayout.height = 1000  #self.gridLayout.minimum_height
        #self.gridLayout.height = 1000  #self.gridLayout.minimum_height
        num = len(db.speakers) #/5
        self.gridLayout.size_hint_y =  round(num/5, 0)  #self.gridLayout.minimum_height

        self.scrollView.add_widget(self.gridLayout)
        self.floatLayout.add_widget(self.scrollView)
        self.add_widget(self.floatLayout)

        for i in range(num, 0, -1):
            self.gridLayout.add_widget(Button(text=str(i)))


    def printSpeakersNum(self):
        print( len(db.speakers) )


class PreScreen(Screen):
    def loadList(self):
        print("Loading speakers' list")
        sm.current = "speakers"

class WindowManager(ScreenManager):
    pass

sm = WindowManager()
kv = Builder.load_file("my-speakers.kv")

screens = [PreScreen(name="pre"), ListScreen(name="speakers")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "pre"



class MyApp(App):
    def build(self):
        #return MyScreen()
        #return LicensScreen()
        #return Controller()
        return sm


if __name__ == "__main__":
    MyApp().run()


