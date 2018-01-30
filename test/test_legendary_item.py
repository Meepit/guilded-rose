import unittest
import items
from items.legendary_item import LegendaryItem

class LegendaryItemTest(unittest.TestCase):
    def setUp(self):
        self.item = LegendaryItem("Sulfuras, Hand of Ragnaros", 0, 80)

    def test_item_print(self):
        self.assertEqual("Sulfuras, Hand of Ragnaros, 0, 80, legendary item", self.item.__repr__())

    def test_no_quality_decrement(self):
        self.item.update()
        self.assertEqual(80, self.item.quality)

    def test_no_sell_in_decrement(self):
        self.item.update()
        self.assertEqual(0, self.item.sell_in)
