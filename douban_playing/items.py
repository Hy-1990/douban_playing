# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanPlayingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名
    title = scrapy.Field()
    # 电影分数
    score = scrapy.Field()
    # 电影发行年份
    release = scrapy.Field()
    # 电影时长
    duration = scrapy.Field()
    # 地区
    region = scrapy.Field()
    # 电影导演
    director = scrapy.Field()
    # 电影主演
    actors = scrapy.Field()
