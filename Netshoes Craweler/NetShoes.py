import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess

data = {
    'Title': [],
    'Link': [],
    'Rating': [],
    'Ref': [],
    'Price': [],
    'MRP': [],
    'Images': [],
    'Description': []

}

h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
}


class NetShoes(scrapy.Spider):
    name = "netShoes"

    def start_requests(self):
        req = scrapy.Request(
            'https://www.netshoes.com.br/lst/top-marcas/adidas', headers=h)
        yield req

    def parse(self, response):
        data['Title'] = response.xpath(
            '//div[@class="wrapper"]/a/@title').getall()

        links = response.xpath('//div[@class="wrapper"]/a/@href').getall()
        for link in links:
            data['Link'].append("https:"+link)

        for link in data['Link']:
            yield scrapy.Request(url=link, headers=h, callback=self.parse2)

    def parse2(self, response):

        data['Rating'].append(response.xpath(
            '//span[@class="rating-box__value"]/text()').get())

        data['Ref'].append(response.xpath(
            '//p[@class="reference"]/span/text()').get())

        data['Price'].append(response.xpath(
            '//div[@class="default-price"]//strong/text()').get())

        data['MRP'].append(response.xpath('//del/text()').get())

        desc = []
        desc_title = response.xpath(
            '//section[@class="feature-values"]//li/strong/text()').getall()
        desc_val = response.xpath(
            '//section[@class="feature-values"]//li/text()').getall()

        for i in range(len(desc_title)):
            txt = desc_title[i]+" "+desc_val[i]
            desc.append(txt)

        data['Description'].append(desc)

        images = response.xpath(
            '//figure/img[@itemprop="image"]/@src').getall()
        img = []
        for url in images:
            img.append(str.split(url, '?')[0])

        data['Images'].append(img)


process = CrawlerProcess()
process.crawl(NetShoes)
process.start()

df = pd.DataFrame(data)
print(df)
