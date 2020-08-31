import scrapy


class MobilesReviewSpiderSpider(scrapy.Spider):
    name = 'mobiles_review_spider'
    allowed_domains = ['amazon.in']
    start_urls = ['http://amazon.in/']

    def parse(self, response):
        pass
