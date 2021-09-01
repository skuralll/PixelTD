from item import ItemAir


class Inventory:

    def __init__(self):
        try:
            self.size
        except AttributeError:
            self.size = 0
        self.contents = []
        for i in range(self.size):
            self.contents.append(ItemAir)

    def setItem(self, item, index):
        self.contents[index] = item
