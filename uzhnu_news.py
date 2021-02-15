import scrapy


class UzhnuNewsSpider(scrapy.Spider):
    name = 'uzhnu_news'
    allowed_domains = ['www.uzhnu.edu.ua']
    start_urls = ['https://www.uzhnu.edu.ua/']

    def parse(self, response):
        #articles = response.css("article>h1>a>span:nth-last-child(1)::text").extract()
        #urls = response.css("article a::attr(href)").extract()
        for a in response.css("article"):
            article = {
                "title": a.css("h1>a>span:nth-last-child(1)::text").extract_first(),
                "url": "https://www.uzhnu.edu.ua"+a.css("a::attr(href)").extract_first()
            }
            print (article)
            yield scrapy.Request(url=article["url"], callback=self.parse_news)
    
    def parse_news(self, response):
        news_date = response.css("div.news_date::text").extract_first()
        print(news_date)
        