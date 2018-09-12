# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class AllSpider(scrapy.Spider):
    name = 'all'
    allowed_domains = ['sanet.st']
    start_urls = ['https://sanet.st/full/']

    def parse(self, response):
        records = response.xpath('//section/ul[2]/li')
        for record in records:
            title = record.xpath('header/div/h2/a/span/text()').extract()
            category = record.xpath('header/div/ul/li[3]/a[@class="cat"][1]/span/text()').extract()
            subcategory = record.xpath('header/div/ul/li[3]/a[@class="cat"][2]/span/text()').extract()
            info = record.xpath('div/div[@class="release-info"]/text()').extract()

            print(title)
            print(category)
            print(subcategory)
            print(info)

            yield{
                'Title':title,
                'Category':category,
                'SubCategory':subcategory,
                'Info':info
            }
        
        next_page = response.xpath('//*[@class="next_page"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page)
        yield scrapy.Request(absolute_next_page_url)
