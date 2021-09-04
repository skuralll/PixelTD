from item import Item, ItemTool


class ItemAxe(ItemTool):

    NAME = "Axe"
    TEXTURE = [128, 40]

    def __init__(self):
        super().__init__()
