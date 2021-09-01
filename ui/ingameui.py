import math

import pyxel

from ui import UI


class InGameUI(UI):

    UI_ID = "ingameui"

    def __init__(self, gamecore):
        self.gamecore = gamecore

    def draw(self):
        player = self.gamecore.getPlayer()
        base_x = 0
        base_y = 224
        pyxel.rect(base_x, base_y, 256, 32, pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 1, base_y + 1, 254, 30, pyxel.COLOR_BLACK)
        # HP
        health_ratio = player.health / player.maxHealth
        pyxel.text(base_x + 4, base_y + 4, "VIT:", pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 20, base_y + 4, 30, 5, pyxel.COLOR_NAVY)
        pyxel.rect(base_x + 20, base_y + 4, math.ceil(30 * health_ratio), 5, pyxel.COLOR_ORANGE)
        # Calorie
        calorie = player.calorie / player.maxCalorie
        pyxel.text(base_x + 4, base_y + 12, "CAL:", pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 20, base_y + 12, 30, 5, pyxel.COLOR_NAVY)
        pyxel.rect(base_x + 20, base_y + 12, math.ceil(30 * calorie), 5, pyxel.COLOR_YELLOW)
        # 未実装
        pyxel.text(base_x + 4, base_y + 20, "___:", pyxel.COLOR_WHITE)
        pyxel.rect(base_x + 20, base_y + 20, 30, 5, pyxel.COLOR_NAVY)
        # 線
        pyxel.line(base_x + 54, base_y + 4, base_x + 54, base_y + 24, pyxel.COLOR_WHITE)
        # Inventory
        inv_base_x = base_x + 59
        inv_base_y = base_y + 4
        for i in range(int(player.inventory.size / 2)):
            for j in range(2):
                pyxel.blt(inv_base_x + i*11, inv_base_y + j*11, 0, 128, 0, 10, 10, 0)
                pyxel.blt(inv_base_x + i*11 + 1, inv_base_y + j*11 + 1, 0, player.inventory.contents[i * 2 + j].TEXTURE[0], player.inventory.contents[i * 2 + j].TEXTURE[1], 8, 8, 0)
        pyxel.blt(inv_base_x + int(player.inventory.holdIndex / 2) * 11, inv_base_y + int(player.inventory.holdIndex % 2) * 11, 0, 128, 16, 10, 10, 0)
        pyxel.line(base_x + 116, base_y + 14, base_x + 180, base_y + 14, pyxel.COLOR_WHITE)
        pyxel.text(base_x + 117, inv_base_y + 2, player.inventory.getItemInHand().getName(), pyxel.COLOR_WHITE)
        # 線
        pyxel.line(base_x + 184, base_y + 4, base_x + 184, base_y + 24, pyxel.COLOR_WHITE)
