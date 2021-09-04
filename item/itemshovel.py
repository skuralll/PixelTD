from item import Item, ItemTool


class ItemShovel(ItemTool):

    NAME = "Shovel"
    TEXTURE = [136, 40]

    def __init__(self):
        super().__init__()
