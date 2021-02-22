import scrapy


class LaptopSpider(scrapy.Spider):
    name = 'laptop'
    start_urls = ['https://hotline.ua/computer/noutbuki-netbuki/']
    out_file = open("laptops.txt", "w")

    def parse(self, response):
        for product in response.css("li.product-item"):
            model = product.css("p.h4 a::text").extract_first()
            price = product.css("div.price-md span.value::text").extract_first()
            img = product.css("img.img-product::attr(src)").extract_first()
            if img != None:
                img_url = "https://hotline.ua/"+img 

            if model != None and price != None:
                laptop = {
                    "model":model.strip(),
                    "price":price.replace("\xa0",""),
                    "img_url":img_url
                }              
                self.out_file.write(str(laptop)+"\n")
           
        
        next = response.css("a.next::attr(href)").extract_first()
        if next != None:
            next_url = "https://hotline.ua/computer/noutbuki-netbuki/"+next
            yield scrapy.Request(url=next_url, callback=self.parse)

    def closed (self, reason):
        self.out_file.close()