# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanPlayingPipeline:
    def __init__(self):
        self.file = open('result.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(
            "电影:{}\t分数:{}\t发行年份:{}\t电影时长:{}\t地区:{}\t电影导演:{}\t电影主演:{}\n".format(
                item['title'],
                item['score'],
                item['release'],
                item['duration'],
                item['region'],
                item['director'],
                item['actors']))
        return item

    def close_spider(self, spider):
        self.file.close()
