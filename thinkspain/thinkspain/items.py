# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import  TakeFirst, MapCompose
from w3lib.html import remove_tags


'''
class Yelp(Item):
    handyman_name = Field()
    handyman_address = Field()
    handyman_contact = Field()
'''


class ThinkspainItem(Item):
    property_name = Field(output_processor=TakeFirst())
    property_price = Field(output_processor=TakeFirst())
    property_description = Field(input_processor = MapCompose(remove_tags), output_processor=TakeFirst())
    Build_Size = Field(output_processor=TakeFirst())
    Plot_Size = Field(output_processor=TakeFirst())
    Bed_room = Field(output_processor=TakeFirst())
    Bath_room = Field(output_processor=TakeFirst())
    Pool = Field(output_processor=TakeFirst())
    Heating = Field(output_processor=TakeFirst())
    AC = Field(output_processor=TakeFirst())
    Garage = Field(output_processor=TakeFirst())
    WC = Field(output_processor=TakeFirst())
    D_from_city = Field(output_processor=TakeFirst())
    D_from_Airport = Field(output_processor=TakeFirst())
    D_from_Marin = Field(output_processor=TakeFirst())
    D_from_beach = Field(output_processor=TakeFirst())
    D_from_countryside = Field(output_processor=TakeFirst())
    D_golfcourse = Field(output_processor=TakeFirst())
