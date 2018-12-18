# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Spideredu.Pitutspider.Pitutspider.items import PitutspiderItem
from scrapy.cmdline import execute

class TyutSpider(CrawlSpider):
    name = 'tyut'

    start_urls = ['http://www.xdkj.tyut.edu.cn/2016/n_news.asp?id=49&page=1']

    pageLink = LinkExtractor(allow=r'page=\d+')

    rules = (
        Rule(pageLink, callback='parse_item', follow=True),
    )

    def parse(self, response):
        for content in response.xpath("//ul[@class='listul']/li"):  #获取标题
            data_item = PitutspiderItem()
            data_item["title"] = content.xpath("./a/text()").extract()[0].strip()
            data_item["time"] = content.xpath("./span/text()").extract()[0].strip()
            data_item["author"] = content.xpath("./a/@href").extract()[0].strip()





execute(['scrapy','crawl','tyut'])f