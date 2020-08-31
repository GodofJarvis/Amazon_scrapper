import scrapy
from ..items import AmazonScrapperItem

class MobilesReviewSpiderSpider(scrapy.Spider):
    name = 'mobiles_review_spider'
    start_urls = ['https://www.amazon.in/s?k=samsung+smartphones&ref=nb_sb_noss_1']

    def parse(self, response):
        mobileItems = AmazonScrapperItem()

        mobile_name = response.css('.a-size-medium::text').extract()
        price = response.css('.a-price-whole::text').extract()

        mobileItems['mobile_name'] = mobile_name
        mobileItems['price'] = price
        yield mobileItems
