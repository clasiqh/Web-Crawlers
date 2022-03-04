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
        pages = response.xpath('//div[@class="pagination"]/a/@href').getall()
        pages.insert(0, response.url.split(':')[1])
        pages.pop()
        print(pages)
        for page in pages:
            yield scrapy.Request('https:'+page, self.parse2, headers=h)

    def parse2(self, response):
        links = response.xpath('//div[@class="wrapper"]/a/@href').getall()
        for link in links:
            data['Link'].append("https:"+link)
        for link in data['Link']:
            yield scrapy.Request(link, self.parse3, headers=h)

    def parse3(self, response):

        # XPATHS
        xRating = '//span[@class="rating-box__value"]/text()'
        xRef = '//p[@class="reference"]/span/text()'
        xPrice = '//div[@class="default-price"]//strong/text()'
        xMRP = '//del/text()'
        xDescTitle = '//section[@class="feature-values"]//li/strong/text()'
        xDescVal = '//section[@class="feature-values"]//li/text()'
        xImg = '//figure/img[@itemprop="image"]/@src'
        xTitle = '//h1[@data-productname]/text()'

        data['Rating'].append(response.xpath(xRating).get())
        data['Ref'].append(response.xpath(xRef).get())
        data['Price'].append(response.xpath(xPrice).get())
        data['MRP'].append(response.xpath(xMRP).get())
        data['Title'].append(response.xpath(xTitle).get())

        desc = []
        desc_title = response.xpath(xDescTitle).getall()
        desc_val = response.xpath(xDescVal).getall()
        for i in range(len(desc_title)):
            txt = desc_title[i]+" "+desc_val[i]
            desc.append(txt)
        data['Description'].append(desc)

        img = []
        images = response.xpath(xImg).getall()
        for url in images:
            img.append(str.split(url, '?')[0])
        data['Images'].append(img)


process = CrawlerProcess()
process.crawl(NetShoes)
process.start()

df = pd.DataFrame(data)
print(df)
