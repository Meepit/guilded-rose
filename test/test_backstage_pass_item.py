import unittest
import items
from items.backstage_pass_item import BackStagePassItem

class BackStagePassItemTest(unittest.TestCase):
    def setUp(self):
        self.item = BackStagePassItem("Backstage passes to a TAFKAL80ETC concert", 0, 5)

    def test_item_print(self):
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert, 0, 5, backstage pass item", self.item.__repr__())
