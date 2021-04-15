import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PublicationsSpider(scrapy.Spider):
    name = 'publications'
    start_urls = ['https://www.scopus.com/authid/detail.uri?authorId=6508250738']
    default_headers = {
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language":"uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
    }

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url = url, 
                callback = self.parse,
                wait_time = 100,
                wait_until = EC.element_to_be_clickable((By.XPATH, '//li[@data-component="results-list-item"]')),
                headers = self.default_headers
            )

    def parse(self, response):
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(response.css("body").get())
