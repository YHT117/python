import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.runoob.com/python/python-tutorial.html",
        "http://python.jobbole.com/"
    ]
    #每爬完一个网页会回调parse方法
    def parse(self, response):
        filename = response.url.split("/")[-2]
        print('-------------------------------')
        print(filename)
        with open(filename, 'wb') as f:
            f.write(response.body)