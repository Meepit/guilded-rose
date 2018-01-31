import unittest
import items
from items.normal_item import NormalItem
from items.Item import Item

class NormalItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item("Bread", 5, 5)
        self.normal_item = NormalItem(self.item)

    # def test_item_print(self):
    #     self.assertEqual("Bread, 5, 5, normal item", self.normal_item.__repr__())

    def test_quality_degradation(self):
        self.normal_item.update()
        self.assertEqual(4, self.item.quality)

    def test_double_degradation_after_sell_in(self):
        self.item.sell_in = 0
        self.normal_item.update()
        self.assertEqual(3, self.item.quality)

    def test_sell_in_degradation(self):
        self.normal_item.update()
        self.assertEqual(4, self.item.sell_in)
