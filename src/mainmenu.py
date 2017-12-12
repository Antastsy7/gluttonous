import cocos
from cocos.director import director
import define
from picture import Picture

class Mainmenu(cocos.layer.ColorLayer):

    def __init__(self):
        self.visible=True
        wid=director.get_window_size()[0]
        heg=director.get_window_size()[1]
        super(Mainmenu, self).__init__(255, 255, 255,200,wid,heg)
        self.position = (0,0)
        text = cocos.text.Label('GAME MODE',
                                font_name='times new roman',
                                font_size=36,
                                color=define.GRAY)
        text.position = 165,300
        self.add(text)
        text = cocos.text.Label('LEARNING MODE',
                                font_name='times new roman',
                                font_size=36,
                                color=define.GRAY)
        text.position = 125, 180
        self.add(text)




