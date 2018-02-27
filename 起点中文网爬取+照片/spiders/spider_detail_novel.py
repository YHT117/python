import scrapy
from scrapy.http import Request
from time import sleep
from qidianNovel.spiders.connectionSQL import getredis,getMongodb
# 把起点首页的所有列表,起点是最后两页没有下一页（此处当做一页）
ii=0
class spider_list_novel(scrapy.Spider):
    name = "spider_list_novel" #要调用的名字
    allowed_domains = ["qidian.com"] #分一个域
    start_urls = []
    dict = {}
    red = getredis()
    mongodb=getMongodb('novel','novels')
    def __init__(self):

        urls = self.red.lrange('all_novel_href', 0,5)
        for url in urls:
            url = str(url, encoding="utf-8")
            url = url.split(',')
            spider_list_novel.start_urls.append(url[1])
            spider_list_novel.dict[url[1]] = url[0]
            # break
    #每爬完一个网页会回调parse方法
    def parse(self, response):
        print(response.url)
        Pid = self.dict[response.url]
        print(Pid)
        links = response.xpath('//div[@class="book-mid-info"]/h4/a')


