import items
from items.quality_increase_item import QualityIncreaseItem

class BackStagePassItem(QualityIncreaseItem):
    def __init__(self, name, sell_in, quality):
        QualityIncreaseItem.__init__(self, name, sell_in, quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality) + ", backstage pass item"

    def update(self):
        if self.sell_in == 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 10:
            self.quality += 2
        else:
            self.quality += 1
