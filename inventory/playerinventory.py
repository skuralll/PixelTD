from inventory import Inventory


class PlayerInventory(Inventory):

    def __init__(self):
        self.size = 8
        super().__init__()
