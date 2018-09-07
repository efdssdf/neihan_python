# coding=utf-8

import scrapy
import datetime
import time
from neihan.items import NeihanItem
import random
page=0

class QuotesSpider(scrapy.Spider):
    name = "jiefu"

    def start_requests(self):
        global page

        yield scrapy.FormRequest(
            url = "http://api.jiefu.tv/app2/api/article/list.html",
            headers = {"Content-Type": "application/x-www-form-urlencoded"},
            formdata = {"sourceType":"1","versionNo":"230","pageSize":"20","typeId":"3","deviceCode":"866378032733894","pageNum":str(page)},
            callback = self.parse
        )

    def parse(self, response):
        global page
        page+=1
        d = eval(response.body.decode('utf-8').replace('true','"true"').replace('\\n',''))
        for i in d['data']:
            mktime = time.mktime(datetime.datetime.now().timetuple())
            item = NeihanItem()
            item['title'] = i['itemView']['content']
            item['thumbnail'] = i['itemView']['gifPath']
            item['createAt'] = mktime
            item['source'] = 'jiefu'
            item['count'] = random.randint(200,1000)
            yield item
        else:
            if len(d['data'])>0:
                yield scrapy.FormRequest(
                    url = "http://api.jiefu.tv/app2/api/article/list.html",
                    headers = {"Content-Type": "application/x-www-form-urlencoded"},
                    formdata = {"sourceType":"1","versionNo":"230","pageSize":"20","typeId":"3","deviceCode":"866378032733894","pageNum":str(page)},
                    callback = self.parse
                )
            else:
                print('end')
