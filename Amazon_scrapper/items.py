# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AmazonScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mobile_name = scrapy.Field()
    price = scrapy.Field()
    pass
