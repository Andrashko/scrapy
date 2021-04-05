import scrapy


class FacultyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    processed = scrapy.Field()
    number = scrapy.Field()

class DepartmetItem(scrapy.Item):
    name = scrapy.Field()
    faculty = scrapy.Field()
    url = scrapy.Field()
