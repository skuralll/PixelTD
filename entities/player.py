import math

import pyxel

from entities import Entity


class Player(Entity):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.direction = 2

    def update(self):
        # 歩行
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.direction = 3
            if self.x > 0:
                self.motionX -= 0.25
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.direction = 1
            if self.x < 31:
                self.motionX += 0.25
        if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
            self.direction = 2
            if self.y < 31:
                self.motionY += 0.25
        if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
            self.direction = 0
            if self.y > 0:
                self.motionY -= 0.25
        super().update()

    def draw(self):
        super().draw()
        # 歩行
        anim = 8 if self.livedTick % 20 > 9 else 0  # アニメーション(10f毎に切り替え)
        if self.direction == 0:  # up
            pyxel.blt(self.x * 8, self.y * 8, 0, 16 + anim, 0, 8, 8, 0)
        if self.direction == 1:  # right
            pyxel.blt(self.x * 8, self.y * 8, 0, 32 + anim, 0, 8, 8, 0)
        if self.direction == 2:  # down
            pyxel.blt(self.x * 8, self.y * 8, 0, 0 + anim, 0, 8, 8, 0)
        if self.direction == 3:  # left
            pyxel.blt(self.x * 8, self.y * 8, 0, 32 + anim, 0, -8, 8, 0)
