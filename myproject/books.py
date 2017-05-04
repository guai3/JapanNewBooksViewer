# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class OreillyBook(scrapy.Item):
    """
    オライリーの本を表す項目
    """

    publisher =scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    url = scrapy.Field()
    imgurl = scrapy.Field()
