# -*- coding: utf-8 -*-
import cocos
import define
from menu import Menu
from mainmenu import Mainmenu
from gluttonous import HelloWorld
from cocos.director import director
import pyglet

class Hello(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        pyglet.resource.path = ['../img']
        pyglet.resource.reindex()
        super(Hello, self).__init__()
        self.main = Mainmenu()
        self.add(self.main)
        self.i=0
        # 0 初始态 已经有Main 需要建立新的游戏
        # 1 过渡态 不可响应任何操作
        # 2 终结态 重新响应操作

    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.i is 0:
            self.i=1
            self.main.visible=False
            if y>250:
                self.hel = HelloWorld()
                self.add(self.hel)
            else:
                self.hel=Menu()
                self.add(self.hel)
        else:
            if self.i is 2:
                self.main.visible=True
                self.i=0

cocos.director.director.init(caption="Gluttonous Python")
cocos.director.director.run(cocos.scene.Scene(Hello()))