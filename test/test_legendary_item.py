import unittest
import items
from items.legendary_item import LegendaryItem

class LegendaryItemTest(unittest.TestCase):
    def setUp(self):
        self.item = LegendaryItem("Sulfuras, Hand of Ragnaros", 0, 80)

    def test_item_print(self):
        self.assertEqual("Sulfuras, Hand of Ragnaros, 0, 80, legendary item", self.item.__repr__())
