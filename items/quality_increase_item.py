

class QualityIncreaseItem():
    def __init__(self, item):
        self.item = item

    # def __repr__(self):
    #     return Item.__repr__(self) + ", quality increase item"

    def update(self):
        if self.item.sell_in <= 0:
            if self.item.quality + 2 > 50: self.item.quality = 50
            else: self.item.quality += 2
        elif self.item.quality != 50: self.item.quality += 1
        self.item.sell_in -= 1
