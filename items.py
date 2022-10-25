import scrapy
from bs4 import BeautifulSoup


class QuotesSpider(scrapy.Spider):
    name = 'items'
    url = 'https://finalfantasy.fandom.com'
    start_urls = [f'{url}/wiki/Bestiary_(Final_Fantasy_XII)']

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'

    def parse(self, response):
        for quote in response.css('ol li'):
            if quote.css('a::text').get() != '\u2191':
                if quote.css('sup'):
                    if quote.css('a::text').get() not in ['a', 'b', 'c', 'd', 'e', 'f']:
                        link =  f"{self.url}{quote.css('a::attr(href)').get()}"
                        yield response.follow(link, self.parse_item)

                    sups = quote.css('sup a::attr(href)').getall()
                    for sup in sups:
                        link = f"{self.url}{sup}"
                        yield response.follow(link, self.parse_item)
                else:
                    link = f"{self.url}{quote.css('a::attr(href)').get()}"
                    yield response.follow(link, self.parse_item)

    def parse_item(self, response):
        section = response.css('aside section')[0]
        div_location = section.css('div.pi-item')[0].css('div.pi-data-value').extract()[0]
        div_type = section.css('div.pi-item')[1].css('div.pi-data-value').extract()[0]
        div_data = section.css('div.pi-item')[2].css('div.pi-data-value').extract()[0]

        yield {
            'name': self.clean_text(response.css('h1::text').get()),
            'image': response.css('aside figure a::attr(href)').get(),
            'url': response.url,
            'location': self.get_div_text(div_location),
            'type': self.get_div_text(div_type),
            'data': self.get_div_text(div_data)
        }

    def get_div_text(self, div:str) -> str:
        try:
            soup = BeautifulSoup(div, 'html.parser')
            return soup.get_text()
        except Exception:
            return ''

    def clean_text(self, text:str):
        chars_remove = ['(', ')', '\t', '\n']
        for char in chars_remove:
            text = text.replace(char, '')
        return text
