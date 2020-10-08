import scrapy


class TataSpider(scrapy.Spider):
    name = 'tata'
    allowed_domains = ['https://www.carone.com.br/iogurte-tata-flocos-1000g']
    start_urls = ['https://www.carone.com.br/iogurte-tata-flocos-1000g']

    def parse(self, response):
        price = response.css('span.price::text').get()
        yield {
            'price': price
        }

