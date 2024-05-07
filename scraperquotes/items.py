# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperquotesItem(scrapy.Item):
    # define the fields for your item here like:
    citation = str
    author = str
    # quote = scrapy.Field()

