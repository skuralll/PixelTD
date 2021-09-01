from item import Item


class ItemAir(Item):

    NAME = "Air"
    TEXTURE = [128, 32]

    def __init__(self):
        super().__init__()
