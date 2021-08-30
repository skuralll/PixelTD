from mymath import Vector
from mymath.aabb import AABB


class Entity(AABB):

    def __init__(self, x, y, world):
        super().__init__(x, y, 1, 1)
        self.livedTick = 0
        self.world = world
        self.lastX = x
        self.lastY = y
        self.motionX = 0.0
        self.motionY = 0.0

    def update(self):
        self.livedTick += 1
        # 移動
        while abs(self.motionX) + abs(self.motionY) != 0:
            sign_x = self.motionX / abs(self.motionX) if self.motionX != 0 else 0
            sign_y = self.motionY / abs(self.motionY) if self.motionY != 0 else 0
            self.lastX = self.x
            self.lastY = self.y
            self.x += 0.125 * sign_x
            self.motionX -= 0.125 * sign_x
            self.y += 0.125 * sign_y
            self.motionY -= 0.125 * sign_y
            collision_flag = False
            for block in self.getAroundBlocks():  # ブロックと衝突しているか
                if block.isPassable():
                    continue
                if self.isCollision(block):
                    collision_flag = True
                    break
            for entity in self.world.getEntities():
                if entity == self:
                    continue
                if self.isCollision(entity):
                    collision_flag = True
                    break
            if collision_flag:
                self.motionX = 0
                self.motionY = 0
                self.x = self.lastX
                self.y = self.lastY
                break

    def draw(self):
        pass

    def getAroundBlocks(self):
        return self.world.getAroundBlocks(self.x, self.y)
