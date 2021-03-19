import scrapy
from rozetka.items import RozetkaItem


class LaptopSpider(scrapy.Spider):
    name = 'laptop'
    start_urls = ['https://rozetka.com.ua/ua/notebooks/c80004/']

    def parse(self, response):
        grid = response.xpath('//ul[@class="catalog-grid"]')
        for img in grid.xpath('.//a[@class="goods-tile__picture"]'):
            url = img.xpath('./img/@src').getall()[1]
            res = RozetkaItem()
            res["image_urls"] = [url]
            res["file_urls"] = [url]
            yield res
            
