# -*- coding: utf-8 -*-
import cocos
import define
from arena2 import Arena2
from gameover2 import Gameover2
from dot2 import Dot2
import csv
import random
import os

class HelloWorld2(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self,listselect, modeselect):
        super(HelloWorld2, self).__init__()
        # 新建一个游戏
        self.arena = Arena2()
        self.add(self.arena)
        # 新建显示当前已经吃掉的字母的层
        self.score = cocos.text.Label('',
                                          font_name='SimHei',
                                          font_size=24,
                                          color=define.GOLD)

        self.score.position= 40,440
        self.add(self.score,99999)
        # 打开数据库文件
        path = os.getcwd()[0:-4]

        with open(path + '/Wordlists/'+listselect+'.csv', 'r', encoding='utf8') as fin:
            cin=csv.reader(fin)
            self.wordlist=[row for row in cin]
        self.num=len(self.wordlist)-1
        # i是当前读取的单词序号 legnth是当前单词的长度 order表示当前要吃的字母在单词中的序号
        # j表示已经背的单词数
        self.i=random.randint(0,self.num)
        self.j=0
        self.word = self.wordlist[self.i][0]
        self.length=len(self.word)
        for c in self.word:
            s = ord(c) - 96
            if s>0:
                self.arena.batch.add(Dot2(None,None,s))
        self.order=0
        # chance表示剩余的机会 如果<0则结束
        if modeselect == 'easy':
            self.chance = 50
        else:
            self.chance = 20
        # 新建显示chance的层
        self.life = cocos.text.Label(str(self.chance),
                                      font_name='SimHei',
                                      font_size=24,
                                      color=define.GOLD)

        self.life.position = 560, 440
        self.add(self.life, 99999)
        # 显示当前单词的中文释义
        ss = self.wordlist[self.i][1]
        self.chinese = cocos.text.Label(ss,
                                     font_name='SimHei',
                                     font_size=16,
                                     color=define.GOLD)
        self.chinese.position = 40, 40
        self.add(self.chinese, 99999)
        # 新建gameover的面板 初始是不可见的
        self.gameover = Gameover2()
        self.add(self.gameover, 100000)
        self.hint = cocos.text.Label(self.word[0]+self.word[1],
                                      font_name='SimHei',
                                      font_size=24,
                                      color=define.GOLD)

        self.hint.position = 40, 80
        self.add(self.hint, 99999)

    def update_score(self):
        self.score.element.text = str(self.arena.snake.score)

    def end_game(self):
        self.gameover.visible = True
        self.arena.is_event_handler = False
        self.gameover.score.element.text = str(self.j)

    def on_mouse_press(self, x, y, buttons, modifiers):
        if buttons == 1 and self.gameover.visible:
            self.gameover.visible = False
            self.remove(self.arena)
            self.parent.i = 2
            self.parent.remove(self)
            del self



