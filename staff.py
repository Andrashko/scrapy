import scrapy


class StaffSpider(scrapy.Spider):
    name = 'staff'
    start_urls = ['http://www.irbis-nbuv.gov.ua//cgi-bin/irbis_nbuv/cgiirbis_64.exe?C21COM=F&I21DBN=UJRN&P21DBN=UJRN&S21CNR=20&Z21ID=']

    def parse(self, response):
        print(len(response.css("li.product-item").extract()))