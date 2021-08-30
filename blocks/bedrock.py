from blocks import Block


class Bedrock(Block):

    TEXTURE = [0, 128]

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.passable = False
