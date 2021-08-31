import math

import pyxel

from blocks.air import Air
from entities import Entity
from inventory import Inventory
from inventory.playerinventory import PlayerInventory
from mymath import Direction


class Player(Entity):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.direction = 2
        self.maxHealth = 1000
        self.health = 1000
        self.maxCalorie = 1000
        self.calorie = 1000
        self.inTask = False
        self.inventory = PlayerInventory()

    def update(self):
        # 歩行
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.direction = Direction.WEST
            if self.x > 0:
                self.motionX -= 0.125
                self.calorie -= 1
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.direction = Direction.EAST
            if self.x < self.world.WIDTH - 1:
                self.motionX += 0.125
                self.calorie -= 1
        if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
            self.direction = Direction.SOUTH
            if self.y < self.world.HEIGHT - 1:
                self.motionY += 0.125
                self.calorie -= 1
        if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
            self.direction = Direction.NORTH
            if self.y > 0:
                self.motionY -= 0.125
                self.calorie -= 1
        # Interact
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.world.setBlock(Air(int(self.x + 0.5 + Direction.VECTOR[self.direction][0]), int(self.y + 0.5 + Direction.VECTOR[self.direction][1]), self.world))
        super().update()

    def draw(self):
        super().draw()

        # 歩行
        anim = 8 if self.livedTick % 20 > 9 else 0  # アニメーション(10f毎に切り替え)
        if self.direction == Direction.NORTH:  # up
            pyxel.blt(self.x * 8, self.y * 8, 0, 16 + anim, 0, 8, 8, 0)
        if self.direction == Direction.EAST:  # right
            pyxel.blt(self.x * 8, self.y * 8, 0, 32 + anim, 0, 8, 8, 0)
        if self.direction == Direction.SOUTH:  # down
            pyxel.blt(self.x * 8, self.y * 8, 0, 0 + anim, 0, 8, 8, 0)
        if self.direction == Direction.WEST:  # left
            pyxel.blt(self.x * 8, self.y * 8, 0, 32 + anim, 0, -8, 8, 0)

        # UI
        base_x = 0
        # base_y = 0 if self.y > self.world.HEIGHT / 2 else 224
        base_y = 224
        pyxel.rect(base_x, base_y, 256, 32, pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 1, base_y + 1, 254, 30, pyxel.COLOR_BLACK)
        # HP
        health_ratio = self.health / self.maxHealth
        pyxel.text(base_x + 4, base_y + 4, "VIT:", pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 20, base_y + 4, 30, 5, pyxel.COLOR_NAVY)
        pyxel.rect(base_x + 20, base_y + 4, math.ceil(30 * health_ratio), 5, pyxel.COLOR_ORANGE)
        # Calorie
        calorie = self.calorie / self.maxCalorie
        pyxel.text(base_x + 4, base_y + 12, "CAL:", pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 20, base_y + 12, 30, 5, pyxel.COLOR_NAVY)
        pyxel.rect(base_x + 20, base_y + 12, math.ceil(30 * calorie), 5, pyxel.COLOR_YELLOW)
        # 未実装
        pyxel.text(base_x + 4, base_y + 20, "___:", pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 20, base_y + 20, 30, 5, pyxel.COLOR_NAVY)
        # 線
        pyxel.line(base_x + 54, base_y + 4, base_x + 54, base_y + 24, pyxel.COLOR_WHITE)
        # Inventory
        pyxel.blt(base_x + 59, base_y + 4, 0, 128, 0, 10, 10, 0)
        pyxel.blt(base_x + 59, base_y + 15, 0, 128, 0, 10, 10, 0)
        pyxel.blt(base_x + 70, base_y + 4, 0, 128, 0, 10, 10, 0)
        pyxel.blt(base_x + 70, base_y + 15, 0, 128, 0, 10, 10, 0)
        pyxel.blt(base_x + 81, base_y + 4, 0, 128, 0, 10, 10, 0)
        pyxel.blt(base_x + 81, base_y + 15, 0, 128, 0, 10, 10, 0)
        pyxel.blt(base_x + 92, base_y + 4, 0, 128, 0, 10, 10, 0)
        pyxel.blt(base_x + 92, base_y + 15, 0, 128, 0, 10, 10, 0)

    def burnCalories(self, amount):
        self.calorie -= amount
        if self.calorie < 0:
            self.calorie = 0
