# -*- coding: utf-8 -*-
import unittest
from unittest import mock
from unittest.mock import MagicMock
import mock

import items
from items.Item import Item
from items.quality_increase_item import QualityIncreaseItem
from items.legendary_item import LegendaryItem
from items.backstage_pass_item import BackStagePassItem
from items.normal_item import NormalItem
from gilded_rose import GildedRose

#python3 -m unittest to run all tests in directory
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

    def test_returns_qualityincreaseitem(self):
        gilded_rose = GildedRose([self.aged_brie])
        self.assertEqual(QualityIncreaseItem, type(gilded_rose.create_item(self.aged_brie)))

    def test_returns_qualityincreaseitem(self):
        gilded_rose = GildedRose([self.legendary_item])
        self.assertEqual(LegendaryItem, type(gilded_rose.create_item(self.legendary_item)))

    def test_returns_backstagepassitem(self):
        gilded_rose = GildedRose([self.backstage_pass])
        self.assertEqual(BackStagePassItem, type(gilded_rose.create_item(self.backstage_pass)))

    def test_returns_normalitem(self):
        gilded_rose = GildedRose([self.normal_item])
        self.assertEqual(NormalItem, type(gilded_rose.create_item(self.normal_item)))


    #
    # def test_normal_item_update(self):
    #     gilded_rose = GildedRose([self.normal_item])
    #     gilded_rose.update_quality()
    #     self.normal_item.update.assert_called()
    #
    # def test_aged_brie_update(self):
    #     gilded_rose = GildedRose([self.aged_brie])
    #     gilded_rose.update_quality()
    #     self.aged_brie.update.assert_called()
    #
    # def test_legendary_item_update(self):
    #     gilded_rose = GildedRose([self.legendary_item])
    #     gilded_rose.update_quality()
    #     self.legendary_item.update.assert_called()
    #
    # def test_backstage_pass_item_update(self):
    #     gilded_rose = GildedRose([self.backstage_pass])
    #     gilded_rose.update_quality()
    #     self.backstage_pass.update.assert_called()


if __name__ == '__main__':
    unittest.main()
