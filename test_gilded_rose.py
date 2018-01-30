# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        pass
        #self.gilded_rose = GildedRose()

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        self.gilded_rose = GildedRose(items)
        self.gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 1, 0)]
        self.gilded_rose = GildedRose(items)
        self.gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

if __name__ == '__main__':
    unittest.main()
