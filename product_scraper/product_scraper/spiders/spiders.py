import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Price_spiders(CrawlSpider):
    name = "spiders"
    start_urls = ['https://www.perekrestok.ru/cat']
    rules = (
        Rule(LinkExtractor(restrict_css=response.css('div.Box-sc-149qidf-0.dgzgIv a::attr(href)').get())), 
        Rule(LinkExtractor(restrict_css=response.css('div.sc-kmASHI.bRmtIT a::attr(href)').get())),
        Rule(LinkExtractor(restrict_css=response.css('div.sc-JAcuL.bEPPNO a::attr(href)').get())), 
        callback='parce_price'
    )


        
        def parce_price (self, response):
            yield {
                'type':response.css('span.breadcrumb ::text')[3].get(),
                'name':response.css('h1.sc-fubCfw.cqjzZF.product__title ::text').get(),
                'price':response.css('div.price-new::text').get().split()[0],
            }