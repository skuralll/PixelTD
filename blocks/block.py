from mymath import Vector
from mymath.aabb import AABB


class Block(Vector):

    TEXTURE = [0, 0]

    def __init__(self, x, y, world):
        super().__init__(x, y)
        self.world = world
        self.passable = True
        self.width = 1
        self.height = 1
        self.aabb = AABB(x, y, self.width, self.height)

    def getTexturePos(self):
        return self.TEXTURE

    def isPassable(self):
        return self.passable
