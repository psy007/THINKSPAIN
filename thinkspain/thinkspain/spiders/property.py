from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from thinkspain import items




class thinkspain(Spider):

    name = "property"
    start_urls = ['https://www.thinkspain.com/property-for-sale']

    def parse(self, response):
        basic_datas = response.xpath('//div[@class="basic-datas"]')

        for each_item in basic_datas:

            property = ItemLoader(item=items.ThinkspainItem(), selector=each_item)
            property.add_xpath('property_name', 'a/div/h4[@class="desc"]/text()')
            property.add_xpath('property_price', 'a/h4[@class="price"]/text()')
            yield property.load_item()

