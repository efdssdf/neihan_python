# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeihanItem(scrapy.Item):
    title = scrapy.Field() #标题
    thumbnail = scrapy.Field() #动态图
    createAt = scrapy.Field() #创建时间
    source =  scrapy.Field() #来源
    count = scrapy.Field() #数量
