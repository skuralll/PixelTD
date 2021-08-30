from mymath import Vector


class AABB(Vector):

    def __init__(self, minX, minY, width, height):
        self.x = minX
        self.y = minY
        self.width = width
        self.height = height

    def isCollision(self, aabb):
        return (self.x + self.width > aabb.x) and \
               (self.x < aabb.x + aabb.width) and \
               (self.y + self.height > aabb.y) and \
               (self.y < aabb.y + aabb.height)
