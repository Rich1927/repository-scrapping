import scrapy
from scrapy.crawler import CrawlerProcess

class DivanLightsSpider(scrapy.Spider):
    name = "divanlights"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        products = response.css('div._Ud0k')  # карточка товара

        for product in products:
            yield {
                'name': product.css('div.lsooF span::text').get(),
                'price': product.css('div.pY3d2 span::text').get(),
                'url': response.urljoin(product.css('a').attrib.get('href'))
            }

        # Переход на следующую страницу
        next_page = response.css('a[data-testid="pagination-forward"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

# Запуск паука и сохранение в JSON и CSV
process = CrawlerProcess(settings={
    'FEEDS': {
        'lights.json': {'format': 'json', 'encoding': 'utf8'},
        'lights.csv': {'format': 'csv', 'encoding': 'utf8'},
    }
})

process.crawl(DivanLightsSpider)
process.start()
# открыть папку с файлом D:\DocumentsGitHub\GitHub\repository-scrapping\divanpars\divanpars\spiders
# запуск python divanlightscsv.py