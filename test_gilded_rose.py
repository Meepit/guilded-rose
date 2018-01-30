# -*- coding: utf-8 -*-
import unittest
from unittest import mock
from unittest.mock import MagicMock
import mock

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        # Reassigning name is neccessary because name is an attribute of MagicMock..
        self.normal_item = mock.Mock(name="foo", sell_in=0, quality=1)
        self.normal_item.name = "foo"

    def test_normal_item_degradation(self):
        gilded_rose = GildedRose([self.normal_item])
        gilded_rose.update_quality()
        self.assertEqual(0, self.normal_item.quality)



if __name__ == '__main__':
    unittest.main()
