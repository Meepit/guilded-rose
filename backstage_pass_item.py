from quality_increase_item import QualityIncreaseItem

class NormalItem(QualityIncreaseItem):
    def __init__(self, name, sell_in, quality):
        QualityIncreaseItem.__init__(self, name, sell_in, quality)

    def __repr__(self):
        return Item.__repr__(self) + ", backstage pass item"
