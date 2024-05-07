import scrapy
# from ..items import ScraperquotesItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        # itemes =ScraperquotesItem() 


        quotes = response.xpath('//*[@class="quote"]')
        for quote_ in quotes :
        # all_div_quotes = response.css('dive.quote')
        # for quotes in all_div_quotes:
        #     title = quotes.css('span.text: : text').extract()
        #     author = quotes.css('.author: ; text').extract()
        #     yield {
        #         'title' : title,
        #         'author': author,
        #     }
            quote = {
                "quote" : quote_.xpath('.//*[@class="text"]/text()').extract_first(),
                "author" : quote_.xpath('.//*[@class="author"]/text()').extract_first(),
            }
            # itemes.quote['quote'] = quote['quote']
            # itemes.quote['author'] = quote['author']
           
            yield quote
            
            # follow next page

        url = response.xpath('//*[@class="next"]//a/@href').extract_first()
        if url:
            yield response.follow(url, callback=self.parse)
     
