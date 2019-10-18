# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class TecmundoScraperPipeline(object):
    def open_spider(self, spider):
        self.title = []
        self.date_news = []
        self.text = []
        self.categories = []
        self.link = []

    def close_spider(self, spider):
        data = pd.DataFrame({
            'title': self.title,
            'date_news': self.date_news,
            'text': self.text,
            'categories': self.categories,
            'link': self.link
        })

        data.to_csv("tecmundo.csv", index=False)

    def __process_categories(self, list_categories):
        categories = [categorie.strip() for categorie in list_categories]

        categories = "/".join(categories)
        return categories

    def process_item(self, item, spider):
        self.title.append(item['title'])
        self.date_news.append(item['date_news'])
        self.text.append(item['text'])
        self.link.append(item['link'])
        categories = self.__process_categories(item['categories'])
        self.categories.append(categories)

        return item
