import items
from items.Item import Item

class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def __repr__(self):
        return Item.__repr__(self) + ", normal item"

    def update(self):
        self.quality -= 1
        self.sell_in -= 1
