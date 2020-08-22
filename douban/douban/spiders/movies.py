# -*- coding: utf-8 -*-
import scrapy


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['https://www.douban.com/']
    start_urls = ['http://https://www.douban.com//']

    def parse(self, response):
        pass
