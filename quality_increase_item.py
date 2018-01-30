from Item import Item

class QualityIncreaseItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def __repr__(self):
        return Item.__repr__(self) + ", quality increase item"
