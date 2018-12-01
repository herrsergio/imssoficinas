# -*- coding: utf-8 -*-
import scrapy

counter=0
class DirectorioSpider(scrapy.Spider):
    name = 'directorio'
    allowed_domains = ['www.imss.gob.mx']
    start_urls = ['http://www.imss.gob.mx/directorio/']

    def parse(self, response):
        global counter
        print('I just visited: ' + response.url)

        results = response.xpath('//*[@class="table table-responsive"]//tbody/tr')

        for result in results:
            item = {
                'a' : result.xpath('td[1]/p[1]/text()').extract_first(),
                'aa' : result.xpath('td[1]/p[2]/text()').extract_first(),
                'b' : result.xpath('td[2]/p[1]/text()').extract_first(),
                'c' : result.xpath('td[3]/p[1]/text()').extract_first(),
                'cc' : result.xpath('td[3]/p[2]/a/@href').extract()[0],
                'd' : result.xpath('td[4]//text()').extract_first(),
                'e' : result.xpath('td[5]//text()').extract_first(),
                'f' : result.xpath('td[6]//text()').extract_first(),
            }
            print(item)
            yield item

        counter += 1
        next_page_url = "/directorio/?page=%s"%str(counter)
        if counter < 770:
        #if counter < 2:
            if next_page_url:
                next_page_url = response.urljoin(next_page_url)
                yield scrapy.Request(url=next_page_url, callback=self.parse)


