# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Movie(scrapy.Item):
    subject_id = scrapy.Field()  # 影片id
    poster = scrapy.Field()  # 海报
    name = scrapy.Field()  # 影片名
    year = scrapy.Field()  # 年份
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


class Celebrity(scrapy.Item):
    celebrity_id = scrapy.Field()  # 演员id
    celebrity_name = scrapy.Field()  # 演员姓名


class Category(scrapy.Item):
    category_id = scrapy.Field()  # 类型id
    category_name = scrapy.Field()  # 类型名


class Tag(scrapy.Item):
    tag_id = scrapy.Field()  # 标签id
    tag_name = scrapy.Field()  # 标签名
