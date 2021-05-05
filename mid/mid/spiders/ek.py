import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class EkSpider(scrapy.Spider):
    name = 'ek'
    start_urls = ['https://ek.ua/ua/list/163/']

    def start_requests(self):
        yield SeleniumRequest(
            url = self.start_urls[0],
            callback = self.parse,
            wait_time=10,
            screenshot=True
        )

    def parse(self, response):
        td = response.css("td.model-hot-prices-td").get()
        print (td)
        with open('image.png', 'wb') as image_file:
            image_file.write(response.meta['screenshot'])
