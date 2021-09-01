import pyxel

from gamecore import GameCore
from ui import UIManager


class App:

    def __init__(self):
        self.game = None
        pyxel.init(256, 256, caption="SurvivalGame")
        # リソース読み込み
        pyxel.load("my_resource.pyxres")

    def run(self):
        self.game = GameCore()
        pyxel.run(self.update, self.draw)

    def update(self):
        if not (self.game is None):
            self.game.update()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        UIManager.update()

    def draw(self):
        if not (self.game is None):
            self.game.draw()
        UIManager.draw()
