# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    big_category = scrapy.Field()
    big_category_id = scrapy.Field()
    small_category = scrapy.Field()
    small_category_id = scrapy.Field()


    book_name = scrapy.Field()
    author = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
