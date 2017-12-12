from cocos.sprite import Sprite
import define
class Picture(Sprite):
    def __init__(self, pos=None, color=None):

        super(Picture, self).__init__('scene.png',self)
        self.position = (define.WIDTH ,
                          define.HEIGHT )
        self.scheduled_interval_calls()