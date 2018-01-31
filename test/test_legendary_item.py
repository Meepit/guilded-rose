import unittest
import items
from items.legendary_item import LegendaryItem
from items.Item import Item

class LegendaryItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        self.legendary_item = LegendaryItem(self.item)

    # def test_item_print(self):
    #     self.assertEqual("Sulfuras, Hand of Ragnaros, 0, 80, legendary item", self.legendary_item.__repr__())

    def test_no_quality_decrement(self):
        self.legendary_item.update()
        self.assertEqual(80, self.item.quality)

    def test_no_sell_in_decrement(self):
        self.legendary_item.update()
        self.assertEqual(0, self.item.sell_in)
