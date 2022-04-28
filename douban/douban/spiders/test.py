import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/p/b29375404479']

    def start_requests(self):
        url = "https://www.jianshu.com/p/b29375404479"
        yield scrapy.Request(
            url=url,
            callback=self.parse_item,
            dont_filter=True,
        )


    def parse(self, response):
        print("func parse")

    def parse_item(self, response):
        print("function parse item")
        print(response.body)
        print(123)

