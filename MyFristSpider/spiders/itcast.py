 #-*- coding: utf-8 -*-
import scrapy

class ItcastSpider(scrapy.Spider):
    name = 'xsy'
    allowed_domains = ['jsjxy.xsyu.edu.cn']
    start_urls = [
        'http://jsjxy.xsyu.edu.cn/dsfc/index.html',
        'http://jsjxy.xsyu.edu.cn/dsfc/index_2.html',
        'http://jsjxy.xsyu.edu.cn/dsfc/index_3.html',
    ]

    def parse(self, response):
            yield {
                'names': response.xpath('//td[@class="jctw1"]/ul[@class="jctw1"]/li/span/a/text()').getall(),
            }