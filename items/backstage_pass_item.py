

class BackStagePassItem():
    def __init__(self, item):
        self.item = item

    # def __repr__(self):
    #     return "%s, %s, %s" % (self.name, self.sell_in, self.quality) + ", backstage pass item"

    def update(self):
        self.update_quality()
        self.item.sell_in -= 1

    def update_quality(self):
        if self.item.sell_in == 0:
            self.item.quality = 0
        elif self.item.sell_in <= 5:
            self.item.quality += 3
        elif self.item.sell_in <= 10:
            self.item.quality += 2
        else:
            self.item.quality += 1
        if self.item.quality > 50:
            self.item.quality = 50
