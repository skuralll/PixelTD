import random
import sys

import pyxel

from blocks import Grass, Bedrock
from blocks.air import Air
from entities import Player


class World:

    def __init__(self):
        # ワールド生成
        self.blocks = []
        for x in range(32):
            row = []
            for y in range(32):
                row.append(Air(x, y, self))
            self.blocks.append(row)
        # デバッグ
        self.blocks[5][5] = Bedrock(5, 5, self)
        self.blocks[5][6] = Bedrock(5, 6, self)
        self.blocks[6][5] = Bedrock(6, 5, self)
        self.blocks[6][6] = Bedrock(6, 6, self)
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

    def getBlock(self, x:int, y:int):
        if x < 0 or y < 0 or 31 < x or 31 < y:
            print('Error: position is out of range (pls 0~31)', file=sys.stderr)
        return self.blocks[x][y]

    def getAroundBlocks(self, x, y):
        x = int(x)
        y = int(y)
        aroundBlocks = []
        for ix in range(3):
            for iy in range(3):
                posX = x + ix - 1
                posY = y + iy - 1
                if 0 <= posX <= 31 and 0 <= posY <= 31:
                    aroundBlocks.append(self.blocks[posX][posY])
        return aroundBlocks
