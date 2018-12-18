# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from it_spiders.items import ItSpidersItem
from scrapy.cmdline import execute

class DemoSpider(CrawlSpider):
    name = 'tyut'

    start_urls = ['http://www.xdkj.tyut.edu.cn/2016/n_news.asp?id=49&page=1']

    pageLink = LinkExtractor(allow=r'page=\d+')

    rules = (
        Rule(pageLink, callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        for content in response.xpath("//ul[@class='listul']/li"):  #获取标题
            data_item = ItSpidersItem()
            data_item["news_title"] = content.xpath("./a/text()").extract()[0].strip()
            data_item["news_data"] = content.xpath("./span/text()").extract()[0].strip()
            data_item["news_URL"] = content.xpath("./a/@href").extract()[0].strip()
            with open("C:\idd.txt", "a+", encoding="utf-8") as f:
                f.write(str(data_item["news_title"] + data_item["news_data"] + data_item["news_URL"] + '\n'))


execute(['scrapy','crawl','tyut'])
