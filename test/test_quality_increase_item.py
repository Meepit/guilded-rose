import unittest
import items
from items.quality_increase_item import QualityIncreaseItem

class NormalItemTest(unittest.TestCase):
    def setUp(self):
        self.item = QualityIncreaseItem("Aged Brie", 0, 5)

    def test_item_print(self):
        self.assertEqual("Aged Brie, 0, 5, quality increase item", self.item.__repr__())
