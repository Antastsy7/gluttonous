# -*- coding: utf-8 -*-
import cocos
from cocos.director import director

import define
from snake2 import Snake2
from dot2 import Dot2
import pyglet
class Arena2(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Arena2, self).__init__(250, 255, 255, 255, define.WIDTH, define.HEIGHT)
        self.center = (director.get_window_size()[0] / 2, director.get_window_size()[1] / 2)
        self.batch = cocos.batch.BatchNode()
        self.add(self.batch)

        self.snake = Snake2()
        self.add(self.snake, 10000)
        self.snake.init_body()
        self.x0, self.y0 = self.center
        self.enemies = []

        self.keys_pressed = set()

        for i in range(50):
            self.batch.add(Dot2())

        self.schedule(self.update)
        self.paused = False

    def add_enemy(self):
        enemy = Snake2(True)
        self.add(enemy, 10000)
        enemy.init_body()
        self.enemies.append(enemy)

    def update(self, dt):
        self.x = self.center[0] - self.snake.x
        self.y = self.center[1] - self.snake.y

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.snake.update_angle(self.keys_pressed)

    def on_key_release (self, key, modifiers):
        self.keys_pressed.remove(key)
        self.snake.update_angle(self.keys_pressed)

    def on_mouse_motion(self, x, y, buttons, modifiers):
        if self.paused:
            if x in range(270, 360) and y in range(285, 325):
                self.paus.image = pyglet.resource.image('暂停3.png')
            elif x in range(190, 450) and y in range(160, 200):
                self.paus.image = pyglet.resource.image('暂停2.png')
            else:
                self.paus.image = pyglet.resource.image('暂停1.png')
        else:

            x = 1 if x - self.x0 > 0 else -1 if x-self.x0 < 0 else 0
            y = 1 if y - self.y0 > 0 else -1 if y-self.y0 < 0 else 0
            directs = ((225, 180, 135), (270, None, 90), (315, 0, 45))
            direct = directs[x + 1][y + 1]
            if direct is None:
                self.snake.angle_dest = self.snake.angle
            else:
                self.snake.angle_dest = direct

    def on_mouse_press(self, x, y, buttons, modifiers):

        if buttons == 4:
            if self.paused:
                self.remove(self.paus)
                del self.paus
                self.resume_scheduler()
                self.snake.resume_scheduler()
                for snake in self.enemies:
                    snake.resume_scheduler()
                self.paused = False
            else:
                self.pause_scheduler()
                self.snake.pause_scheduler()
                for snake in self.enemies:
                    snake.pause_scheduler()
                self.paus = cocos.sprite.Sprite(
                    image='暂停1.png',
                    position=self.point_to_local(self.center)
                )
                self.add(self.paus)
                self.paused = True

        elif buttons == 1:
            if x in range(270, 360) and y in range(285, 325):
                self.remove(self.paus)
                del self.paus
                self.resume_scheduler()
                self.snake.resume_scheduler()
                for snake in self.enemies:
                    snake.resume_scheduler()
                self.paused = False
            elif x in range(190, 450) and y in range(160, 200):
                self.parent.end_game()

