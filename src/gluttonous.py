# -*- coding: utf-8 -*-
import cocos
import define
from arena import Arena
from gameover import Gameover

class HelloWorld(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(HelloWorld, self).__init__()
        self.arena = Arena()
        self.add(self.arena)
        self.score = cocos.text.Label('30',
                                      font_name='Times New Roman',
                                      font_size=24,
                                      color=define.GOLD)
        self.score.position = 20, 440
        self.add(self.score, 99999)

        self.gameover = Gameover()
        self.add(self.gameover, 100000)

    def update_score(self):
        self.score.element.text = str(self.arena.snake.score)

    def end_game(self):
        self.gameover.visible = True
        self.gameover.score.element.text = str(self.arena.snake.score)

    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.gameover.visible:                           # 如果当前gameover面板可见 则结束游戏 通过parent删除当前游戏回到主菜单
            self.gameover.visible = False
            self.remove(self.arena)
            self.parent.i=2
            del self



