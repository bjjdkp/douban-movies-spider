# -*- coding: utf-8 -*-

import re
import scrapy
from douban.items import Movies
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MoviesSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['douban.com']
    start_urls = [
        'https://movie.douban.com/subject/1292849/',
    ]
    rules = (
        # subject
        Rule(LinkExtractor(allow=r'movie.douban.com/subject/\d+/(\?from=subject-page)?$'), callback='parse_movie', follow=True),

        # doulist
        Rule(LinkExtractor(allow=r'movie.douban.com/subject/\d+/doulists'), follow=True),
        Rule(LinkExtractor(allow=r'douban.com/doulist/\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'douban.com/people/\w+/doulists/(all|collect)'), follow=True),

        # celebrity
        Rule(LinkExtractor(allow=r'movie.douban.com/celebrity/\d+/$'), callback='parse_celebrity', follow=True),
        Rule(LinkExtractor(allow=r'movie.douban.com/celebrity/\d+/movies'), follow=True),
        Rule(LinkExtractor(allow=r'movie.douban.com/celebrity/\d+/partners'), follow=True),
        Rule(LinkExtractor(allow=r'movie.douban.com/subject/\d+/celebrities'), follow=True),

    )

    # def start_requests(self):
    #
    #     tag_list = [
    #         "热门", "豆瓣猜", "最新", "经典", "可播放", "豆瓣高分", "冷门佳片", "华语", "欧美",
    #         "韩国", "日本", "动作", "喜剧", "爱情", "科幻", "悬疑", "恐怖", "文艺",
    #     ]
    #
    #     for tag in tag_list:
    #         url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%s&page_limit=1000/" % tag
    #         yield scrapy.Request(
    #             url
    #         )


    def is_data_exist(self, data):
        """
        判断数据是否存在
        """
        if isinstance(data, list):
            if len(data):
                return data[0]
            else:
                return "null"
        else:
            if data:
                return data
            else:
                return "null"

    def parse_movie(self, response):
        print("parse_item~~~~~~~~~")
        detail_info = Movies()

        detail_info["subject_id"] = re.search(r"subject/(\d+)", response.url).group()
        detail_info["poster"] = response.xpath('/html[1]/body[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]').extract()


        # # 职位名称
        # detail_info["job_name"] = self.is_data_exist(response.xpath('//title/text()').extract()).split("_")[0][1:]
        # # 职位月薪(元/月)
        # detail_info["salary"] = self.is_data_exist(response.xpath('//div[@class="terminalpage-left"]/ul/li[1]/strong/text()').extract()).strip()[:-3]
        # # 工作地点
        # detail_info["job_site"] = self.is_data_exist(response.xpath('//div[@class="terminalpage-left"]/ul/li[2]/strong/a/text()').extract())
        # # 发布日期
        # detail_info["launch_time"] = self.is_data_exist(response.xpath('//div[@class="terminalpage-left"]/ul/li[3]/strong/span/text()').extract())
        # # 工作性质
        # detail_info["job_nature"] = self.is_data_exist(response.xpath('//div[@class="terminalpage-left"]/ul/li[4]/strong/text()').extract())
        # # 工作经验
        # detail_info["experience"] = self.is_data_exist(response.xpath('//div[@class="terminalpage-left"]/ul/li[5]/strong/text()').extract())
        # # 最低学历
        # detail_info["education"] = self.is_data_exist(response.xpath('//div[@class="terminalpage-left"]/ul/li[6]/strong/text()').extract())
        # # 招聘人数
        # detail_info["requirements"] = self.is_data_exist(response.xpath('//div[@class="terminalpage-left"]/ul/li[7]/strong/text()').extract()).strip()[:-1]
        # # 职位类别
        # detail_info["job_type"] = self.is_data_exist(response.xpath('//div[@class="terminalpage-left"]/ul/li[8]/strong/a/text()').extract())
        # # 职位描述
        # job_desc_all = "".join(response.xpath('//div[@class="terminalpage-main clearfix"]/div/div[1]//text()').extract())
        # job_desc = re.sub(r"\r|\n| ", "", job_desc_all)
        # detail_info["job_desc"] = job_desc
        # # 公司介绍
        # # detail_info["company_info"] = response.xpath('//div[@class="terminalpage-main clearfix"]/div/div[2]/p/text()').extract()
        # # 公司名称
        # detail_info["company_name"] = self.is_data_exist(response.xpath('//div[@class="company-box"]/p/a/text()').extract())

        # node_list = response.xpath('//div[@class="company-box"]/ul/li')
        # if len(node_list) == 4:
        #     for node in node_list:
        #         # 公司规模
        #         detail_info["company_size"] = self.is_data_exist(node.xpath('//div[@class="company-box"]/ul/li[1]/strong/text()').extract())
        #         # 公司性质
        #         detail_info["company_nature"] = self.is_data_exist(node.xpath('//div[@class="company-box"]/ul/li[2]/strong/text()').extract())
        #         # 公司行业
        #         detail_info["company_trade"] = self.is_data_exist(node.xpath('//div[@class="company-box"]/ul/li[3]/strong/a/text()').extract())
        #         # 公司地址
        #         detail_info["company_address"] = self.is_data_exist(node.xpath('//div[@class="company-box"]/ul/li[4]/strong/text()').extract()).strip()
        # elif len(node_list) == 5:
        #     for node in node_list:
        #         # 公司规模
        #         detail_info["company_size"] = self.is_data_exist(node.xpath('//div[@class="company-box"]/ul/li[1]/strong/text()').extract())
        #         # 公司性质
        #         detail_info["company_nature"] = self.is_data_exist(node.xpath('//div[@class="company-box"]/ul/li[2]/strong/text()').extract())
        #         # 公司行业
        #         detail_info["company_trade"] = self.is_data_exist(node.xpath('//div[@class="company-box"]/ul/li[3]/strong/a/text()').extract())
        #         # 公司地址
        #         detail_info["company_address"] = self.is_data_exist(node.xpath('//div[@class="company-box"]/ul/li[5]/strong/text()').extract()).strip()

        # 页面url
        detail_info["data_url"] = response.url
        # 页面源码
        # detail_info["data_html"] = response.body

        return detail_info


    def parse_celebrity(self, response):
        pass
