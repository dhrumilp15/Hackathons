
# coding: utf-8

# In[ ]:

import scrapy

class TweetSpider(scrapy.Spider):
    name = "tweets"
    start_urls = ['https://twitter.com/BMO',]
    
    def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        for quote in response.css('div.js-tweet-text-container'):
            yield {
                'tweet-text':quote.css('p.tweet-text::text').extract_first(),
            }
        
        #next_page = response.css('li.next a::attr(href)').extract_first()
        #counter = 0
        #if next_page is not None and counter < 6:
        #    yield response.follow(next_page, callback=self.parse)
        #    counter += 1