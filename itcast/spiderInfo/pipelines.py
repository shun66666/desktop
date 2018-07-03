# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 可以在这里面定义类对数据进行处理， 但需要在setting中设置权重值


class SpiderinfoPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item
