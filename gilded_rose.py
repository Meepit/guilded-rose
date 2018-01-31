# -*- coding: utf-8 -*-
import items
from items.Item import Item
from items.backstage_pass_item import BackStagePassItem
from items.legendary_item import LegendaryItem
from items.normal_item import NormalItem
from items.quality_increase_item import QualityIncreaseItem

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def create_item(self, item):
        # Returns a class that has a update() class method
        item_classes = {
            "Aged Brie": QualityIncreaseItem,
            "Sulfuras, Hand of Ragnaros": LegendaryItem,
            "Backstage passes to a TAFKAL80ETC concert": BackStagePassItem
        }

        if item.name in item_classes.keys():
            return item_classes[item.name](item)
        return NormalItem(item)

    def update_quality(self):
        for item in self.items:
            self.create_item(item).update()
