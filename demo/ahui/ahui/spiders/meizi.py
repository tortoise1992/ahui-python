# -*- coding: utf-8 -*-
import scrapy


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['meizutu.com']
    start_urls = ['http://meizutu.com/']

    def parse(self, response):
        pass
