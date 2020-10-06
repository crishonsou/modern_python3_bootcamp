# https://scrapy.org

# pithon -m pip install scrapy

import scrapy

class Bookspider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css('.price_color::text').extract_first(),
                'title': article.css('h3 > a::attr(title)').extract_first()
            }
            next = response.css('.next > a::attr(href)').extract.first()
            if next:
                yield response.follow(next, self.parse)
        


# Para executar:

# Ir no diretorio onde está o executável .py criado para o crawler e rodar
# scrapy runspider -o <file_name.csv> or <file_name.json> <file_name.py>
