import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"
    
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"): #response.css('div.quote'):
            yield {
                'text': quote.xpath(".//span[@class='text']/text()").get(), 
                        #quote.css('span.text::text').get(),
                'author': quote.xpath(".//small[@class='author']/text()").get(),
                        #quote.css('small.author::text').get(),
                'tags': quote.xpath(".//div[@class='tags']/a[@class='tag']/text()").getall(), 
                        #quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
                    #response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)