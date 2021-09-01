import pyxel

from inventory import Inventory


class PlayerInventory(Inventory):

    def __init__(self):
        self.size = 10
        self.holdIndex = 0
        super().__init__()

    def update(self):
        if pyxel.btnp(pyxel.KEY_1):
            self.holdIndex = 0
        if pyxel.btnp(pyxel.KEY_2):
            self.holdIndex = 1
        if pyxel.btnp(pyxel.KEY_3):
            self.holdIndex = 2
        if pyxel.btnp(pyxel.KEY_4):
            self.holdIndex = 3
        if pyxel.btnp(pyxel.KEY_5):
            self.holdIndex = 4
        if pyxel.btnp(pyxel.KEY_6):
            self.holdIndex = 5
        if pyxel.btnp(pyxel.KEY_7):
            self.holdIndex = 6
        if pyxel.btnp(pyxel.KEY_8):
            self.holdIndex = 7
        if pyxel.btnp(pyxel.KEY_9):
            self.holdIndex = 8
        if pyxel.btnp(pyxel.KEY_0):
            self.holdIndex = 9

    def getItemInHand(self):
        return self.contents[self.holdIndex]
