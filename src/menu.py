# -*- coding: utf-8 -*-
import cocos
import define
from gluttonous2 import HelloWorld2
from cocos.director import director

class Menu(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        wid = director.get_window_size()[0]
        heg = director.get_window_size()[1]
        super(Menu, self).__init__(255, 255, 255, 200, wid, heg)
        self.text1 = cocos.text.Label('CHOOSE A WORDLIST:',
                                      font_name='times new roman',
                                      font_size=32,
                                      color=define.GRAY)

        self.text1.position = 100, 400
        self.add(self.text1, 99999)
        self.text2 = cocos.text.Label('CET-4',
                                      font_name='times new roman',
                                      font_size=30,
                                      color=define.GRAY)

        self.text2.position = 280, 300
        self.add(self.text2, 99999)
        self.text3 = cocos.text.Label('CET-6',
                                      font_name='times new roman',
                                      font_size=30,
                                      color=define.GRAY)

        self.text3.position = 280, 200
        self.add(self.text3, 99999)
        self.text4 = cocos.text.Label('CEM-8',
                                      font_name='times new roman',
                                      font_size=30,
                                      color=define.GRAY)

        self.text4.position = 273, 100
        self.add(self.text4, 99999)
        self.i = 0

    def on_mouse_press(self, x, y, buttons, modifiers):
        if y>50 and y<150:
            self.i=1
        if y>150 and y<250:
            self.i=2
        if y>250 and y<350:
            self.i=3
        if not self.i==0:
            self.hel = HelloWorld2(self.i)
            self.add(self.hel)
            self.remove(self.text1)
            self.remove(self.text4)
            self.remove(self.text3)
            self.remove(self.text2)
            self.color=(0,0,0)