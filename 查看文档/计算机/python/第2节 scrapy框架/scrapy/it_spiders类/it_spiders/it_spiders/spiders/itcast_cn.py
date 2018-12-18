# -*- coding: utf-8 -*-
import scrapy
from scrapy.cmdline import execute
from it_spiders.items import ItSpidersItem

class ItcastCnSpider(scrapy.Spider):
    name = 'itcast_cn'
    allowed_domains = ['www.xdkj.tyut.edu.cn']
    page = 1
    url = 'http://www.xdkj.tyut.edu.cn/2016/n_news.asp?id=49&page='
    start_urls = [url + str(page)]

    def parse(self, response):
        # print(response.text)



        for content in response.xpath("//ul[@class='listul']/li"):  #获取标题
            data_item = ItSpidersItem()

            data_item["news_title"] = content.xpath("./a/text()").extract()[0].strip()
            data_item["news_data"] = content.xpath("./span/text()").extract()[0].strip()
            data_item["news_URL"] = content.xpath("./a/@href").extract()[0].strip()

            yield data_item
        #转换执行下一步
        self.page += 1
        yield scrapy.Request(self.url + str(self.page) , callback=self.parse)


execute(['scrapy','crawl','itcast_cn'])
