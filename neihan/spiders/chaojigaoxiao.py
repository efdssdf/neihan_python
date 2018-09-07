# coding=utf-8

import scrapy
import datetime
import time
from neihan.items import NeihanItem
import random
n=0

class QuotesSpider(scrapy.Spider):
    name = "chaojigaoxiao"

    def start_requests(self):
        url = "https://video.beanmedia.cn/api/gifs?format=json"
        yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        global n
        n+=1
        d = eval(response.body.decode('utf-8'))
        for i in d['data']:
            mktime = time.mktime(datetime.datetime.now().timetuple())
            item = NeihanItem()
            item['title'] = ''
            item['thumbnail'] = i['img']
            item['createAt'] = mktime
            item['source'] = 'chaojigaoxiao'
            item['count'] = random.randint(200,1000)
            yield item
        else:
            if len(d['data'])>0 and n<100:
                url = "https://video.beanmedia.cn/api/gifs?format=json"
                yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)
            else:
                print('end')
