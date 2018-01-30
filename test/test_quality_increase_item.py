import unittest
import items
from items.quality_increase_item import QualityIncreaseItem

class NormalItemTest(unittest.TestCase):
    def setUp(self):
        self.item = QualityIncreaseItem("Aged Brie", 5, 5)

    def test_item_print(self):
        self.assertEqual("Aged Brie, 5, 5, quality increase item", self.item.__repr__())

    def test_quality_increase_over_time(self):
        self.item.update()
        self.assertEqual(6, self.item.quality)

    def test_sell_in_decrease(self):
        self.item.update()
        self.assertEqual(4, self.item.sell_in)
