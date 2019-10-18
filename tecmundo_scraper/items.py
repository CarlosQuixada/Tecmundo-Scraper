# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TecmundoScraperItem(scrapy.Item):
    title = scrapy.Field()
    date_news = scrapy.Field()
    text = scrapy.Field()
    categories = scrapy.Field()
    link = scrapy.Field()
