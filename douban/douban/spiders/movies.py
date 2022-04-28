# -*- coding: utf-8 -*-

import re
import scrapy
from douban.items import Movie, Celebrity
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
        movie_info = Movie()
        celebrity_info = Celebrity()

        movie_info["subject_id"] = re.search(r"subject/(\d+)", response.url).group()
        movie_info["poster"] = response.xpath('//a[@class="nbgnbg"]/img/@src').extract()
        movie_info["name"] = response.xpath('//h1/span[1]/text()').extract()
        movie_info["year"] = response.xpath('//h1/span[2]/text()').extract().strip("()")
        movie_info["director"] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()
        movie_info[""] = response.xpath('').extract()



        director = scrapy.Field()  # 导演
        writer = scrapy.Field()  # 编剧
        cast = scrapy.Field()  # 主演
        category = scrapy.Field()  # 类型
        region = scrapy.Field()  # 制片国家/地区
        language = scrapy.Field()  # 语言
        release_date = scrapy.Field()  # 上映日期
        duration = scrapy.Field()  # 片长
        other_name = scrapy.Field()  # 又名
        rating = scrapy.Field()  # 评分
        rating_number = scrapy.Field()  # 评分人数
        rating_5 = scrapy.Field()  # 5星比例
        rating_4 = scrapy.Field()  # 4星比例
        rating_3 = scrapy.Field()  # 3星比例
        rating_2 = scrapy.Field()  # 2星比例
        rating_1 = scrapy.Field()  # 1星比例
        synopsis = scrapy.Field()  # 剧情简介
        seeing = scrapy.Field()  # 在看人数
        seen = scrapy.Field()  # 看过人数
        wanna_see = scrapy.Field()  # 想看人数
        tag = scrapy.Field()  # 标签
        brief_review = scrapy.Field()  # 短评数
        topic = scrapy.Field()  # 话题数
        review = scrapy.Field()  # 影评数
        discuss = scrapy.Field()  # 小组讨论数
        question = scrapy.Field()  # 问题数
        create_time = scrapy.Field()  # 数据添加时间
        update_time = scrapy.Field()  # 数据更新时间
        subject_url = scrapy.Field()  # 数据url

        celebrity_id = scrapy.Field()  # 演员id
        celebrity_name = scrapy.Field()  # 演员姓名



        # 页面url
        movie_info["data_url"] = response.url
        # 页面源码
        # movie_info["data_html"] = response.body

        return movie_info


    def parse_celebrity(self, response):
        pass
