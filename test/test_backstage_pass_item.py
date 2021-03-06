import unittest
import items
from items.backstage_pass_item import BackStagePassItem
from items.Item import Item

class BackStagePassItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item("Backstage passes to a TAFKAL80ETC concert", 12, 11)
        self.backstage_item = BackStagePassItem(self.item)

    # def test_item_print(self):
    #     self.assertEqual("Backstage passes to a TAFKAL80ETC concert, 12, 11, backstage pass item", self.backstage_item.__repr__())
    #

    def test_quality_increase_more_than_10_days(self):
        self.backstage_item.update()
        self.assertEqual(12, self.item.quality)

    def test_quality_increase_10_or_less_days(self):
        self.item.sell_in = 10
        self.backstage_item.update()
        self.assertEqual(13, self.item.quality)

    def test_quality_increase_5_or_less_days(self):
        self.item.sell_in = 5
        self.backstage_item.update()
        self.assertEqual(14, self.item.quality)

    def test_quality_0_after_sell_in(self):
        self.item.sell_in = 0
        self.backstage_item.update()
        self.assertEqual(0, self.item.quality)

    def test_sell_in_decrement(self):
        self.backstage_item.update()
        self.assertEqual(11, self.item.sell_in)

    def test_quality_cannot_exceed_50(self):
        self.item.quality = 50
        self.backstage_item.update()
        self.assertEqual(50, self.item.quality)
