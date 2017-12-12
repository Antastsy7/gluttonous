# -*- coding: utf-8 -*-
import random
from cocos.actions import MoveTo, CallFuncS
from cocos.sprite import Sprite
import unicodedata
import define


def kill(spr):
    spr.unschedule(spr.update)
    arena = spr.parent.parent
    if not spr.is_big:
        spr.killer.add_score()
    else:
        spr.killer.add_score(2)
    arena.batch.remove(spr)
    arena.batch.add(Dot2())
    del spr

class Dot2(Sprite):
    def __init__(self, pos=None, color=None,num=None):
        if num is None:
            self.num = random.randint(1, 26)
        else:
            self.num=num
        switcher = {
            1: 'A.png',
            2: 'B.png',
            3: 'C.png',
            4: 'D.png',
            5: 'E.png',
            6: 'F.png',
            7: 'G.png',
            8: 'H.png',
            9: 'I.png',
            10: 'J.png',
            11: 'K.png',
            12: 'L.png',
            13: 'M.png',
            14: 'N.png',
            15: 'O.png',
            16: 'P.png',
            17: 'Q.png',
            18: 'R.png',
            19: 'S.png',
            20: 'T.png',
            21: 'U.png',
            22: 'V.png',
            23: 'W.png',
            24: 'X.png',
            25: 'Y.png',
            26: 'Z.png',
        }
        ss=switcher[self.num]
        super(Dot2, self).__init__(ss)
        self.killed = False
        if pos is None:
            self.position = (random.randint(40, define.WIDTH - 40),
                             random.randint(40, define.HEIGHT - 40))
            self.is_big = False
            self.scale = 0.8
        else:
            self.position = (pos[0] + random.random() * 32 - 16,
                             pos[1] + random.random() * 32 - 16)
            self.is_big = True

        self.schedule_interval(self.update, random.random() * 0.2 + 0.1)


    def update(self, dt):
        arena = self.parent.parent
        snake = arena.snake
        self.check_kill(snake)

    def check_kill(self, snake):
        if (not self.killed and not snake.is_dead) and (
            abs(snake.x - self.x) < 32 and abs(snake.y - self.y) < 32
        ):
            self.killed = True
            self.killer = snake
            if not self.killer.is_enemy:
                are=self.parent.parent.parent
                s=chr(self.num+96)                         # 判断当前吃掉的字母
                if are.word[are.order]==s:                 # 如果和当前要吃的字母相同 则指针右移继续判断下一个字母
                    are.order+=1
                    are.score.element.text += s
                    if are.order==are.length:               #已经吃完当前单词 吃下一个
                        are.i=random.randint(0,are.num)
                        are.j+=1
                        are.order=0
                        are.word=are.wordlist[are.i][0]
                        ss=unicode(are.wordlist[are.i][1],'utf-8')
                        are.chinese.element.text=ss
                        are.length=len(are.word)
                        are.score.element.text=''
                        for c in are.word:
                            s=ord(c)-96
                            print(s)
                            arena = self.parent.parent
                            arena.batch.add(Dot2(s))
                else:
                    if are.chance>0:
                        are.chance-=1
                        are.life.element.text=str(are.chance)
                    else:
                        self.killer.crash()


            self.do(MoveTo(snake.position, 0.1) + CallFuncS(kill))