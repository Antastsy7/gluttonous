import cocos
from cocos.director import director
import define
from cocos.sprite import Sprite
import pyglet

class Mainmenu(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        self.visible=True
        super(Mainmenu, self).__init__()
        self.position = (0,0)
        '''text = cocos.text.Label('GAME MODE',
                                font_name='times new roman',
                                font_size=36,
                                color=define.GRAY)
        text.position = 165,300
        self.add(text)'''
        x0, y0 = director.get_window_size()
        self.gm = Sprite(image='Game Mode1.png', scale=1.5)
        self.gmpos = self.gm.width/2 + x0/2 - 180, self.gm.height/2+y0/2 +50
        self.gm.position = self.gmpos
        self.add(self.gm)
        self.rm = Sprite(image='Learning Mode 1.png', scale=1.5)
        self.rmpos = self.rm.width/2 + x0/2 - 240, self.rm.height/2+y0/2 -80
        self.rm.position = self.rmpos
        self.add(self.rm)
        self.x0 = x0
        self.y0 = y0
        self.chosen = 'none'


    def on_mouse_motion(self, x, y, buttons, modifiers):
        if x in range(160, 480) and y in range(300, 400):
            self.gm.image = pyglet.resource.image('Game Mode2.png')
            self.chosen = 'game'
        else:
            self.gm.image = pyglet.resource.image('Game Mode1.png')
            self.chosen = 'none'
            if x in range(160, 480) and y in range(170, 270):
                self.rm.image = pyglet.resource.image('Learning Mode 2.png')
                self.chosen = 'learn'
            else:
                self.rm.image = pyglet.resource.image('Learning Mode 1.png')
                self.chosen = 'none'

