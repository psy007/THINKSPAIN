from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from thinkspain import items
from scrapy.http.request import Request
#from urllib.parse import urlparse
from urllib.parse import urljoin





class thinkspain(Spider):

    name = "property"
    start_urls = ['https://www.thinkspain.com/property-for-sale','https://www.thinkspain.com/property-for-sale?numpag=2']
    '''
    def parse(self, response):
        basic_datas = response.xpath('//div[@class="basic-datas"]')

        for each_item in basic_datas:

            property = ItemLoader(item=items.ThinkspainItem(), selector=each_item)
            property.add_xpath('property_name', 'a/div/h4[@class="desc"]/text()', re='\\n\s*\\n\s*(.*)')
            property.add_xpath('property_price', 'a/h4[@class="price"]/text()', re='\\u20ac (.*)')
            yield property.load_item()
    '''

    def parse(self, response):
        basic_datas = response.xpath('//div[@class="basic-datas"]')
        links = basic_datas.xpath('//div[@class="basic-datas"]/a/@href').extract()
        for link in links:
            yield Request(urljoin('https://www.thinkspain.com/property-for-sale#p:', link), callback=self.detail_page)



    def detail_page(self, response):



        property = ItemLoader(item=items.ThinkspainItem(), selector=response)

        property.add_xpath('property_name', '//div[@class="description"]/div/h1/text()')
        property.add_xpath('property_price','//span[@class="price pr-none mr-none"]/text()', re='\\u20ac (.*)')
        property.add_xpath('Build_Size', '//div[@class="facilities"]/ul[1]/li[1]/strong/text()')
        property.add_xpath('Plot_Size', '//div[@class="facilities"]/ul[1]/li[2]/strong/text()')
        property.add_xpath('Bed_room', '//div[@class="facilities"]/ul[2]/li[1]/strong/text()')
        property.add_xpath('Bath_room', '//div[@class="facilities"]/ul[2]/li[2]/strong/text()')
        property.add_xpath('WC', '//div[@class="facilities"]/ul[2]/li[3]/strong/text()')
        if response.xpath('//div[@class="facilities"]/ul/li/i[@class="icon-pool"]'):
            property.add_value('Pool', u'YES')
        else:
            property.add_value('Pool', u'NO')
        if response.xpath('//div[@class="facilities"]/ul/li/i[@class="icon-air-conditioning"]'):
            property.add_value('AC', u'YES')
        else:
            property.add_value('AC', u'NO')
        if response.xpath('//div[@class="facilities"]/ul/li/i[@class="icon-heating"]'):
            property.add_value('Heating', u'YES')
        else:
            property.add_value('Heating', u'NO')
        if response.xpath('//div[@class="facilities"]/ul/li/i[@class="icon-garage"]'):
            property.add_value('Garage', u'YES')
        else:
            property.add_value('Garage', u'NO')


        property.add_xpath('property_description', '//div[@class="description"]/p/text()')

        yield property.load_item()


