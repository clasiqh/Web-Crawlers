import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd


table = {
    'Title': [],
    'URL': [],
    'Budget': []
}


class MoviesSpider(scrapy.Spider):
    name = 'spiderman'
    start_urls = [
        'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture']

    def parse(self, response):
        url_path = '//tr[@style="background:#FAEB86"]/td[1]//a/@href'
        title_path = '//tr[@style="background:#FAEB86"]/td[1]//a/@title'

        movies = response.xpath(url_path).getall()
        titles = response.xpath(title_path).getall()

        for movie in movies:
            table.get('URL').append("https://en.wikipedia.org/"+movie)
        for title in titles:
            table.get('Title').append(title)

        for link in table.get('URL'):
            yield scrapy.Request(url=link, callback=self.parse2)

    def parse2(self, response):
        budget_path = '//th[contains(text(), "Budget")]/following-sibling::td/text()'
        budget = response.xpath(budget_path).get()
        table['Budget'].append(budget)


process = CrawlerProcess()
process.crawl(MoviesSpider)
process.start()

df = pd.DataFrame(table)
print(df)

k = input("press any key to exit")
