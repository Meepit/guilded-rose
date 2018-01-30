# -*- coding: utf-8 -*-
import unittest
from unittest import mock
from unittest.mock import MagicMock
import mock

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        # Reassigning name is neccessary because name is an attribute of MagicMock..
        self.normal_item = mock.Mock(name="foo", sell_in=1, quality=1)
        self.normal_item.name = "foo"

        self.aged_brie = mock.Mock(name="Aged Brie", sell_in=1, quality=1)
        self.aged_brie.name = "Aged Brie"

        self.legendary_item = mock.Mock(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        self.legendary_item.name = "Sulfuras, Hand of Ragnaros"

        self.backstage_pass = mock.Mock(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=1)
        self.backstage_pass.name = "Backstage passes to a TAFKAL80ETC concert"

    def test_normal_item_degradation(self):
        gilded_rose = GildedRose([self.normal_item])
        gilded_rose.update_quality()
        self.assertEqual(0, self.normal_item.quality)

    def test_double_degradation_after_sell_in_date(self):
        self.normal_item.sell_in = 0
        self.normal_item.quality = 2
        gilded_rose = GildedRose([self.normal_item])
        gilded_rose.update_quality()
        self.assertEqual(0, self.normal_item.quality)


    def test_normal_item_sell_in_date_decrementation(self):
        gilded_rose = GildedRose([self.normal_item])
        gilded_rose.update_quality()
        self.assertEqual(0, self.normal_item.sell_in)

    def test_aged_brie_item_no_degradation(self):
        gilded_rose = GildedRose([self.aged_brie])
        gilded_rose.update_quality()
        self.assertEqual(2, self.aged_brie.quality)

    def test_aged_brie_double_increase_after_sell_in(self):
        gilded_rose = GildedRose([self.aged_brie])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(4, self.aged_brie.quality)

    def test_legendary_items_no_quality_decreae(self):
        gilded_rose = GildedRose([self.legendary_item])
        gilded_rose.update_quality()
        self.assertEqual(80, self.legendary_item.quality)

    def test_backstage_pass_quality_increase(self):
        gilded_rose = GildedRose([self.backstage_pass])
        gilded_rose.update_quality()
        self.assertEqual(2, self.backstage_pass.quality)

    def test_backstage_double_increase_10_days_before_sell_in(self):
        self.backstage_pass.sell_in = 10
        gilded_rose = GildedRose([self.backstage_pass])
        gilded_rose.update_quality()
        self.assertEqual(3, self.backstage_pass.quality)

if __name__ == '__main__':
    unittest.main()
