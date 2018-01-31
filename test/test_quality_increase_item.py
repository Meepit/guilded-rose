import unittest
import items
from items.quality_increase_item import QualityIncreaseItem
from items.Item import Item

class QualityIncreaseItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item("Aged Brie", 5, 5)
        self.quality_increase_item = QualityIncreaseItem(self.item)

    def test_quality_increase_over_time(self):
        self.quality_increase_item.update()
        self.assertEqual(6, self.item.quality)

    def test_double_increase_after_sell_in(self):
        self.item.sell_in = 0
        self.quality_increase_item.update()
        self.assertEqual(7, self.item.quality)

    def test_sell_in_decrease(self):
        self.quality_increase_item.update()
        self.assertEqual(4, self.item.sell_in)

    def test_max_quality_50(self):
        self.item.quality = 50
        self.quality_increase_item.update()
        self.assertEqual(50, self.item.quality)

    def test_max_quality_50_passed_sell_in(self):
        self.item.quality = 49
        self.item.sell_in = 0
        self.quality_increase_item.update()
        self.assertEqual(50, self.item.quality)
