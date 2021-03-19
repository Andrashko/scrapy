import scrapy


class UzhnuSpiderSpider(scrapy.Spider):
    name = 'uzhnu_spider'
    allowed_domains = ['uzhnu.edu.ua']
    start_urls = ['https://www.uzhnu.edu.ua/uk/cat/faculty/']

    def parse(self, response):
        for faculty in response.css("ul.departments_unfolded li a"):
            faculty_name = faculty.css("::text").extract()[1]
            faculty_ref ="https://www.uzhnu.edu.ua"+faculty.css("::attr(href)").extract_first()
            print(faculty_name, faculty_ref)
            yield scrapy.Request(url=faculty_ref, callback=self.parse_faculty)
    
    def parse_faculty(self, response):
        print(response.css("h1.supercat::text").extract_first())