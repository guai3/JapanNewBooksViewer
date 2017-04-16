# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Oreillybook(scrapy.Item):
    """
    オライリーの本を表す項目
    """

    title = scrapy.Field()
    subtitle = scrapy.Field()
    url = scrapy.Field()
    imgurl = scrapy.Field()
