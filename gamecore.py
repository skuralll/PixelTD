from ui import InGameUI, UIManager
from world import World


class GameCore:

    def __init__(self):
        self.world = World()
        UIManager.addUI(InGameUI(self))

    def update(self):
        self.world.update()

    def draw(self):
        self.world.draw()

    def getPlayer(self):
        return self.world.entities[0]
