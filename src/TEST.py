import csv
import random
import unicodedata
import cocos
from cocos.scene import Scene
class Picture(Scene):
    def __init__(self, pos=None, color=None):
        super(Picture, self).__init__('scene.png')


cocos.director.director.run(cocos.scene.Scene(Picture()))