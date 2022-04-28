# import scrapy
# from douban.items import Movies
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
#
#
# class TeSpider(CrawlSpider):
#     name = 'te'
#     allowed_domains = ['tencent.com']
#     start_urls = ['https://careers.tencent.com/search.html']
#
#     rules = (
#         # 详情页链接规律
#         Rule(LinkExtractor(allow=r'position_detail\.php\id=\d+&keywords=&tid=0&lid=0'), callback='parse_item'),
#         # 在列表页查找翻页链接规律
#         Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'), follow=True)
#     )
#
#     def parse_item(self, response):
#         print(123)
#         item = Movies()
#         item['sharetitle'] = response.xpath('//td[@id="sharetitle"]/text()').extract_first()
#         item['category'] = response.xpath('//span[text()="职位类别："]/../text()').extract_first()
#         item['location'] = response.xpath('//span[text()="工作地点："]/../text()').extract_first()
#         item['num'] = response.xpath('//span[text()="招聘人数："]/../text()').extract_first()
#         item['duty'] = response.xpath('//div[text()="工作职责："]/../ul/li/text()').extract()
#         item['claim'] = response.xpath('//div[text()="工作要求："]/../ul/li/text()').extract()
#         return item
