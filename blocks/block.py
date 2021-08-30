from mymath import Vector
from mymath.aabb import AABB


class Block(AABB):

    TEXTURE = [0, 0]

    def __init__(self, x, y, world):
        super().__init__(x, y, 1, 1)
        self.world = world
        self.passable = True

    def getTexturePos(self):
        return self.TEXTURE

    def isPassable(self):
        return self.passable
