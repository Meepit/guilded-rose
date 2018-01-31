

class NormalItem():
    def __init__(self, item):
        self.item = item

    def __repr__(self):
        return Item.__repr__(self) + ", normal item"

    def update(self):
        if self.item.sell_in <= 0:
            self.item.quality -= 2
        else:
            self.item.quality -= 1
        self.item.sell_in -= 1
