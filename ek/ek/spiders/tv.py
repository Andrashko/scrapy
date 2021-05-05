import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TvSpider(scrapy.Spider):
    name = 'tv'
    start_urls = ['https://ek.ua/ua/list/160/']

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url = url, 
                callback = self.parse,
                wait_time = 10,
                wait_until = EC.element_to_be_clickable((By.XPATH, '//a[@class="ib model-all-shops no-mobile"]'))
            )

    def parse(self, response):
        price_tables = response.xpath('//table[@class="model-short-block"]//td[@class="model-hot-prices-td"]')
        for table in price_tables:
            #print (table.get())
            return
