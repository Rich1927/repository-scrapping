import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/divany-i-kresla"]
# start_urls - это та ссылка, от которой начинается парсинг
    def parse(self, response):
        pass
