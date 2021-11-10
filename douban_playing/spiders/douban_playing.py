#!/user/bin/env python
# coding=utf-8
"""
@project : douban_playing
@author  : huyi
@file   : douban_playing.py
@ide    : PyCharm
@time   : 2021-11-10 16:31:23
"""

import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from douban_playing.items import DoubanPlayingItem


class DoubanPlayingSpider(scrapy.Spider):
    name = 'dbp'
    # allowed_domains = ['blog.csdn.net']
    start_urls = ['https://movie.douban.com/cinema/nowplaying/nanjing/']
    nowplaying = "//*[@id='nowplaying']/div[@class='mod-bd']//*[@class='list-item']/@{}"
    properties = ['data-title', 'data-score', 'data-release', 'data-duration', 'data-region', 'data-director',
                  'data-actors']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=chrome_options,
                                        executable_path="E:\\chromedriver_win32\\chromedriver.exe")
        self.browser.set_page_load_timeout(30)

    def parse(self, response, **kwargs):
        titles = response.xpath(self.nowplaying.format(self.properties[0])).extract()
        scores = response.xpath(self.nowplaying.format(self.properties[1])).extract()
        releases = response.xpath(self.nowplaying.format(self.properties[2])).extract()
        durations = response.xpath(self.nowplaying.format(self.properties[3])).extract()
        regions = response.xpath(self.nowplaying.format(self.properties[4])).extract()
        directors = response.xpath(self.nowplaying.format(self.properties[5])).extract()
        actors = response.xpath(self.nowplaying.format(self.properties[6])).extract()
        for x in range(len(titles)):
            item = DoubanPlayingItem()
            item['title'] = titles[x]
            item['score'] = scores[x]
            item['release'] = releases[x]
            item['duration'] = durations[x]
            item['region'] = regions[x]
            item['director'] = directors[x]
            item['actors'] = actors[x]
            yield item
