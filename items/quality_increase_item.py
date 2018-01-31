import items
from items.Item import Item

class QualityIncreaseItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def __repr__(self):
        return Item.__repr__(self) + ", quality increase item"

    def update(self):
        if self.sell_in <= 0:
            if self.quality + 2 > 50: self.quality = 50
            else: self.quality += 2
        elif self.quality != 50: self.quality += 1
        self.sell_in -= 1
