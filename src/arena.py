import cocos
from cocos.director import director

import define
from snake import Snake
from dot import Dot
import math

class Arena(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        super(Arena, self).__init__(250, 255, 255, 255, define.WIDTH, define.HEIGHT)
        self.center = (director.get_window_size()[0] / 2, director.get_window_size()[1] / 2)
        self.batch = cocos.batch.BatchNode()
        self.add(self.batch)
        self.x0 = self.center[0]
        self.y0 = self.center[1]
        self.snake = Snake()
        self.add(self.snake, 10000)
        self.snake.init_body()
        self.x0, self.y0 = self.center
        self.enemies = []
        for i in range(7):
            self.add_enemy()

        self.keys_pressed = set()

        for i in range(50):
            self.batch.add(Dot())

        self.schedule(self.update)

    def add_enemy(self):
        enemy = Snake(True)
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
        x = 1 if x - self.x0 > 0 else -1 if x-self.x0 < 0 else 0
        y = 1 if y - self.y0 > 0 else -1 if y-self.y0 < 0 else 0
        directs = ((225, 180, 135), (270, None, 90), (315, 0, 45))
        direct = directs[x + 1][y + 1]
        if direct is None:
            self.snake.angle_dest = self.snake.angle
        else:
            self.snake.angle_dest = direct
