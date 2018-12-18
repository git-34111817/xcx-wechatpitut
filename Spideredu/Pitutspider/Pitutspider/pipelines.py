# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PitutspiderPipeline(object):
    def process_item(self, data_item, spider):

        title = data_item["news_title"]
        data = data_item["news_data"]
        URL= data_item["news_URL"]

        print(title + data + URL + "\n" )

        return data_item