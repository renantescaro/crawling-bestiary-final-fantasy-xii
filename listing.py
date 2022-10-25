import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'listing'
    url = 'https://finalfantasy.fandom.com'
    start_urls = [f'{url}/wiki/Bestiary_(Final_Fantasy_XII)']

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'

    def parse(self, response):
        for quote in response.css('ol li'):
            if quote.css('a::text').get() != '\u2191':
                if quote.css('sup'):
                    if quote.css('a::text').get() not in ['a', 'b', 'c', 'd', 'e', 'f']:
                        fields = {
                            'name': quote.css('a::text').get(),
                            'link': f"{self.url}{quote.css('a::attr(href)').get()}",
                        }
                    else:
                        fields = {
                            'name': quote.css('li::text').get(),
                        }
                    sups = quote.css('sup a::attr(href)').getall()
                    if len(sups) > 0:
                        fields['sups'] = []
                        for index, sup in enumerate(sups):
                            fields['sups'].append({
                                f"link_{index}" : f"{self.url}{sup}"
                            })

                    yield fields
                else:
                    yield {
                        'name': quote.css('a::text').get(),
                        'link': f"{self.url}{quote.css('a::attr(href)').get()}",
                    }
