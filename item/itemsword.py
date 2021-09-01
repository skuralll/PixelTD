from item import Item, ItemTool


class ItemSword(ItemTool):

    NAME = "Sword"
    TEXTURE = [136, 32]

    def __init__(self):
        super().__init__()
