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
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        data = response.body
        links = Selector(text=data).xpath('//body/div[@class="site-w index clearfix"]/div[@class="col1"]/div/ul/li')
        next_page = Selector(text=data).xpath('//body/div[@class="site-w index clearfix"]/div[@class="col1"]/div/div[@class="pager"]/a[@class="next"]/@href').extract()
        for link in links:
            b = link.xpath('p/span[@class="showtxt"]').extract()
            if len(b) >0:
                mktime = time.mktime(datetime.datetime.now().timetuple())
                item = NeihanItem()
                item['title'] = b[0][b[0].find('>')+1:b[0].find('</')].replace('\r\n','')
                item['thumbnail'] = link.xpath('p[@class="img"]/a/img/@data-original').extract()[0].replace('\r\n','')
                item['createAt'] = mktime
                item['source'] = 'gaoxiaogif'
                item['count'] = random.randint(200,1000)
                yield item
        else:
            if len(next_page)>0:
                url = "http://www.gaoxiaogif.cn"+next_page[0]
                yield scrapy.Request(url=url,callback=self.parse)
            else:
                print('end')
