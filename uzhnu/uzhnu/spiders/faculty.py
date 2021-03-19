import scrapy
from uzhnu.items import FacultyItem


class FacultySpider(scrapy.Spider):
    name = 'faculty'
    start_urls = ['https://www.uzhnu.edu.ua/uk/cat/faculty']

    def parse(self, response):
        for f in response.xpath('//ul[@class="departments_unfolded"]/li'):
            fac = FacultyItem()
            fac["name"] = f.xpath(".//a/text()").extract_first()
            fac["url"] = "https://www.uzhnu.edu.ua"+f.xpath(".//a/@href").extract_first()
            fac["processed"] = False
            #yield fac
            yield scrapy.Request(url=fac["url"], callback=self.parse_faculty, meta = {}, cb_kwargs={"faculty": fac})

    def parse_faculty(self, response, faculty):
        print(faculty)
