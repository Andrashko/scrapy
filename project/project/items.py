# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    model = scrapy.Field()
    price = scrapy.Field()
    img_url = scrapy.Field()
    
