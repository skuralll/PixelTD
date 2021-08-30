import random
import sys

import pyxel

from blocks import Grass, Bedrock, Tree
from blocks.air import Air
from entities import Player


class World:
    WIDTH = 32
    HEIGHT = 28

    def __init__(self):
        # ワールド生成
        self.blocks = []
        for x in range(self.WIDTH):
            row = []
            for y in range(self.HEIGHT):
                row.append(Air(x, y, self))
            self.blocks.append(row)
        # デバッグ
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                self.setBlock(Grass(x, y, self))
                if random.randint(0, 20) == 1:
                    self.setBlock(Tree(x, y, self))
        # エンティティ生成
        self.entities = []
        self.entities.append(Player(0, 0, self))  # プレイヤー生成

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self):
        # ブロック描画
        for row in self.blocks:
            for block in row:
                texturePos = block.getTexturePos()
                pyxel.blt(block.x * 8, block.y * 8, 0, texturePos[0], texturePos[1], 8, 8)
        # エンティティ描画
        for entity in self.entities:
            entity.draw()

    def getBlock(self, x: int, y: int):
        if x < 0 or y < 0 or self.WIDTH <= x or self.HEIGHT <= y:
            print('Error: position is out of range (pls 0~31)', file=sys.stderr)
        return self.blocks[x][y]

    def setBlock(self, block, x=None, y=None):
        if x is None or y is None:
            self.blocks[block.x][block.y] = block
        else:
            self.blocks[x][y] = block

    def getAroundBlocks(self, x, y):
        x = int(x)
        y = int(y)
        aroundBlocks = []
        for ix in range(3):
            for iy in range(3):
                posX = x + ix - 1
                posY = y + iy - 1
                if 0 <= posX < self.WIDTH and 0 <= posY < self.HEIGHT:
                    aroundBlocks.append(self.blocks[posX][posY])
        return aroundBlocks

    def getEntities(self):
        return self.entities
