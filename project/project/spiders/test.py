import scrapy
from project.items import ProjectItem


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://hotline.ua/computer/noutbuki-netbuki/']

    def parse(self, response):
        for product in response.css("li.product-item"):
            model = product.css("p.h4 a::text").extract_first()
            price = product.css("div.price-md span.value::text").extract_first()
            img = product.css("img.img-product::attr(src)").extract_first()
            if img != None:
                img_url = "https://hotline.ua/"+img 

            if model != None and price != None:
                result = ProjectItem()
                result["model"] = model.strip()
                result["price"] = int (price.replace("\xa0",""))              
                result["img_url"] = img_url
                yield result
