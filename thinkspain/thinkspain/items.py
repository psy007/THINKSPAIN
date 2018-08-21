# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

'''
class Yelp(Item):
    handyman_name = Field()
    handyman_address = Field()
    handyman_contact = Field()
'''


class ThinkspainItem(Item):
    property_name = Field()
    property_price = Field()
    property_description = Field()
    Build_Size = Field()
    Plot_Size = Field()
    Bed_room = Field()
    Bath_room = Field()
    Pool = Field()
    Heating = Field()
    AC = Field()
    Garage = Field()
    WC = Field()
