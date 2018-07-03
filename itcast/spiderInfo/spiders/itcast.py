# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']  # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 开始爬取的网址

    def parse(self, response):
        # 返回一个特殊的列表，元素是Selector对象
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()")
        # 这个列表被scrapy赋予了extract方法 获取元素对象的data数据
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)

        # 分组  获得的是Selector对象的列表
        li_list = response.xpath("//div[@class='tea_con']//li")
        # print(li_list)
        for li in li_list:
            item = dict()
            # extract_first 没有值时返回None
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # print(item)
            yield item