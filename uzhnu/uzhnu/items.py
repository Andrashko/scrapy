import scrapy


class FacultyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    processed = scrapy.Field()
    number = scrapy.Field()
