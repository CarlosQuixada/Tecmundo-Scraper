# -*- coding: utf-8 -*-
import scrapy
from tecmundo_scraper.items import TecmundoScraperItem


class TecmundoSpider(scrapy.Spider):
    name = 'Tecmundo'
    allowed_domains = ['tecmundo.com.br']
    start_urls = ['http://tecmundo.com.br/novidades/']

    def parse(self, response):
        for article in response.css("article"):
            link = article.css("div.tec--card__info h3.tec--card__title a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        link = response.url
        title = response.css("h1.tec--article__header__title ::text").extract_first()
        date_news = response.css("div.tec--timestamp__item time::attr(datetime)").extract_first()
        text = "".join(response.css("div.tec--article__body ::text").extract())
        categories = response.css("div.z--px-16 div#js-categories a ::text").extract()

        tecmundo = TecmundoScraperItem(title=title, date_news=date_news, text=text, categories=categories, link=link)

        yield tecmundo
