import time
import os


while True:
    os.system("scrapy crawl neihan")
    os.system("scrapy crawl jiefu")
    os.system("scrapy crawl gaoxiaogif")
    os.system("scrapy crawl chaojigaoxiao")
    time.sleep(86400)  #每隔一天运行一次 24*60*60=86400s
