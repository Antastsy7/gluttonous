# -*- coding: utf-8 -*-
import cocos
import pyglet
from gluttonous2 import HelloWorld2
from cocos.director import director
from cocos.sprite import Sprite

class Menu(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        wid = director.get_window_size()[0]
        heg = director.get_window_size()[1]
        super(Menu, self).__init__(255,255,255,255)

        self.text1 = Sprite('Choose List.png')
        self.text1pos = self.text1.width / 2 + wid / 2 - 200, self.text1.height / 2 + heg / 2 + 150
        self.text1.position = self.text1pos
        self.add(self.text1, 1)

        self.text2 = Sprite('CEM8 1.png')
        self.text2pos = self.text2.width / 2 + wid / 2 - 180, self.text2.height / 2 + heg / 2 + 50
        self.text2.position = self.text2pos
        self.add(self.text2)

        self.text3 = Sprite('CET4 1.png')
        self.text3pos = self.text3.width / 2 + wid / 2 - 180, self.text3.height / 2 + heg / 2 - 50
        self.text3.position = self.text3pos
        self.add(self.text3)

        self.text4 = Sprite('CET6 1.png')
        self.text4pos = self.text4.width / 2 + wid / 2 - 180, self.text4.height / 2 + heg / 2 - 150
        self.text4.position = self.text4pos
        self.add(self.text4)

        self.text5 = Sprite('Easy 1.png')
        self.text5pos = self.text5.width / 2 + wid / 2 + 80, self.text5.height / 2 + heg / 2
        self.text5.position = self.text5pos
        self.add(self.text5)

        self.text6 = Sprite('Hard 1.png')
        self.text6pos = self.text6.width / 2 + wid / 2 + 80, self.text6.height / 2 + heg / 2 - 100
        self.text6.position = self.text6pos
        self.add(self.text6)

        self.listselect = None
        self.modeselect = None
        '''self.text1 = cocos.text.Label('CHOOSE A WORDLIST:',
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
        self.i = 0'''
    '''
    def on_mouse_press(self, x, y, buttons, modifiers):
        if y>50 and y<150:
            self.i=1
        if y>150 and y<250:
            self.i=2
        if y>250 and y<350:
            self.i=3
        if not self.i==0:
            '''

    def reset_list(self):
        self.text2.image = pyglet.resource.image('CEM8 1.png')
        self.text3.image = pyglet.resource.image('CET4 1.png')
        self.text4.image = pyglet.resource.image('CET6 1.png')

    def reset_mode(self):
        self.text5.image = pyglet.resource.image('Easy 1.png')
        self.text6.image = pyglet.resource.image('Hard 1.png')

    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.is_event_handler:
            if buttons == 4:
                if self.modeselect is not None and self.listselect is not None:
                    hel = HelloWorld2(self.listselect, self.modeselect)
                    self.is_event_handler = False
                    self.parent.add(hel)

                else:
                    return
            else:
                if x in range(160, 280):
                    self.reset_list()
                    if y in range(300, 330):
                        self.listselect = 'CEM-8'
                        self.text2.image = pyglet.resource.image('CEM8 2.png')
                    elif y in range(200, 230):
                        self.listselect = 'CET-4'
                        self.text3.image = pyglet.resource.image('CET4 2.png')
                    elif y in range(100, 130):
                        self.listselect = 'CET-6'
                        self.text4.image = pyglet.resource.image('CET6 2.png')
                elif x in range(420, 500):
                    self.reset_mode()
                    if y in range(250, 280):
                        self.modeselect = 'easy'
                        self.text5.image = pyglet.resource.image('Easy 2.png')
                    elif y in range(150, 180):
                        self.modeselect = 'hard'
                        self.text6.image = pyglet.resource.image('Hard 2.png')
                else:
                    return

