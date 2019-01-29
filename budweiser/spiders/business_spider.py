import scrapy


class BusinessSpider(scrapy.Spider):
    name = "business"

    def start_requests(self):
        urls = [
            'https://www.vtsosonline.com/online/BusinessInquire/BusinessInformation?businessID=300113',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for business in response.css('td'):
            yield {
                'text': business.css('td.text::text').extract_first(),

            }
