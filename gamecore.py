from world import World


class GameCore:

    def __init__(self):
        self.world = World()

    def update(self):
        self.world.update()

    def draw(self):
        self.world.draw()
