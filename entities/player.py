import math

import pyxel

from entities import Entity


class Player(Entity):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.direction = 2
        self.maxHealth = 100
        self.health = 100
        self.maxFood = 100
        self.food = 100

    def update(self):
        # 歩行
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.direction = 3
            if self.x > 0:
                self.motionX -= 0.25
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.direction = 1
            if self.x < self.world.WIDTH - 1:
                self.motionX += 0.25
        if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
            self.direction = 2
            if self.y < self.world.HEIGHT - 1:
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

        # UI
        base_x = 0
        base_y = 0 if self.y > self.world.HEIGHT / 2 else 224
        pyxel.rect(base_x, base_y, 256, 32, pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 1, base_y + 1, 254, 30, pyxel.COLOR_BLACK)
        # HP
        health_ratio = self.health / self.maxHealth
        pyxel.text(base_x + 4, base_y + 4, "VIT:", pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 20, base_y + 4, 30, 5, pyxel.COLOR_NAVY)
        pyxel.rect(base_x + 20, base_y + 4, math.ceil(30 * health_ratio), 5, pyxel.COLOR_ORANGE)
        # FOOD
        food_ratio = self.food / self.maxFood
        pyxel.text(base_x + 4, base_y + 12, "FOD:", pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 20, base_y + 12, 30, 5, pyxel.COLOR_NAVY)
        pyxel.rect(base_x + 20, base_y + 12, math.ceil(30 * health_ratio), 5, pyxel.COLOR_YELLOW)
