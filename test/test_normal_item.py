import unittest
import items
from items.normal_item import NormalItem

class NormalItemTest(unittest.TestCase):
    def setUp(self):
        self.item = NormalItem("Bread", 0, 5)

    def test_item_print(self):
        self.assertEqual("Bread, 0, 5, normal item", self.item.__repr__())
