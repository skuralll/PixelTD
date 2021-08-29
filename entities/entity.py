from mymath import Vector
from mymath.aabb import AABB


class Entity(Vector):

    def __init__(self, x, y, world):
        super().__init__(x, y)
        self.livedTick = 0
        self.world = world
        self.lastX = x
        self.lastY = y
        self.motionX = 0.0
        self.motionY = 0.0
        self.width = 1
        self.height = 1
        self.aabb = AABB(x, y, self.width, self.height)

    def update(self):
        self.livedTick += 1
        self.lastX = self.x
        self.lastY = self.y

    def draw(self):
        pass
