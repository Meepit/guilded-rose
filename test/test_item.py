import unittest
import items
from items.Item import Item

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item = Item("foo", 5, 1)

    def test_item_name(self):
        self.assertEqual("foo", self.item.name)

    def test_item_sell_in(self):
        self.assertEqual(5, self.item.sell_in)

    def test_item_quality(self):
        self.assertEqual(1, self.item.quality)

    def test_item_print(self):
        self.assertEqual("foo, 5, 1", self.item.__repr__())

if __name__ == '__main__':
    unittest.main()
