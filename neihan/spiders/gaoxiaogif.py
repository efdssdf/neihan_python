# coding=utf-8

import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import datetime
import time
from neihan.items import NeihanItem
import random

class QuotesSpider(scrapy.Spider):
    name = "gaoxiaogif"

    def start_requests(self):
        url = "http://www.gaoxiaogif.cn/"
        yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        d = response.body.decode('utf-8')
        a = Selector(text=d).xpath('//body/div[@class="site-w index clearfix"]/div[@class="col1"]/div/ul/li').re()
        print(a,'--------------------------')
        # for i in d['data']:
        #     mktime = time.mktime(datetime.datetime.now().timetuple())
        #     item = NeihanItem()
        #     item['title'] = ''
        #     item['thumbnail'] = i['img']
        #     item['createAt'] = mktime
        #     item['source'] = 'gaoxiaogif'
        #     item['count'] = random.randint(200,1000)
        #     yield item
        # else:
        #     if len(d['data'])>0:
        #         url = "https://video.beanmedia.cn/api/gifs?format=json"
        #         yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)
        #     else:
        #         print('end')
