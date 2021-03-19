import scrapy
from laptops.items import LaptopItem


class LaptopSpider(scrapy.Spider):
    name = 'laptop'
    start_urls = ['https://hotline.ua/computer/noutbuki-netbuki/']

    def parse(self, response):
        for product in response.css("li.product-item"):
            model = product.css("p.h4 a::text").extract_first()
            price = product.css("div.price-md span.value::text").extract_first()
            img = product.css("img.img-product::attr(src)").extract_first()
            if img != None:
                img_url = "https://hotline.ua/"+img 

            if model != None and price != None:
                laptop = LaptopItem()
                laptop["model"] = model.strip()
                laptop["price"] = float(price.replace("\xa0",""))
                laptop["img_url"] = img_url
                yield laptop
           
        
        next = response.css("a.next::attr(href)").extract_first()
        if next != None:
            next_url = "https://hotline.ua/computer/noutbuki-netbuki/"+next
            yield scrapy.Request(url=next_url, callback=self.parse)