import scrapy
from db.items import FacultyItem, DepartmetItem

class UzhnuSpider(scrapy.Spider):
    name = 'uzhnu'
    start_urls = ['https://www.uzhnu.edu.ua/uk/cat/faculty']

    def parse(self, response):
        for f in response.xpath('//ul[@class="departments_unfolded"]/li'):
            fac = FacultyItem()
            fac["name"] = f.xpath(".//a/text()").extract_first()
            fac["url"] = "https://www.uzhnu.edu.ua"+f.xpath(".//a/@href").extract_first()
            yield fac
            yield scrapy.Request(url=fac["url"],
                callback=self.parse_faculty, 
                meta = {}, 
                cb_kwargs={
                    "faculty": fac
                    }
            )

    def parse_faculty(self, response, faculty):
        for dep in response.xpath('//ul[@class="departments"]//a'):
            department = DepartmetItem()
            department["name"] = dep.xpath("./text()").get()#.extract_first()
            department["faculty"] = faculty
            department["url"] = dep.xpath('./@href').getall()[0] #.extract()
            yield department

