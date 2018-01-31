

class LegendaryItem():
    def __init__(self, item):
        self.item = item

    def __repr__(self):
        return Item.__repr__(self) + ", legendary item"

    def update(self):
        pass #legendary items do not degrade
