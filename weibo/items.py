# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    uid = scrapy.Field()
    name = scrapy.Field()
    gender = scrapy.Field()
    location = scrapy.Field()
    intro = scrapy.Field()
    signin = scrapy.Field()
    school = scrapy.Field()
    company = scrapy.Field()
