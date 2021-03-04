import scrapy
from uzhnu.items import FacultyItem


class FacultySpider(scrapy.Spider):
    name = 'faculty'
    start_urls = ['https://www.uzhnu.edu.ua/uk/cat/faculty']

    def parse(self, response):
        for f in response.css("ul.departments_unfolded li"):
            fac = FacultyItem()
            fac["name"] = f.css("a::text").extract_first()
            fac["url"] = "https://www.uzhnu.edu.ua"+f.css("a::attr(href)").extract_first()
            fac["processed"] = False
            yield fac
