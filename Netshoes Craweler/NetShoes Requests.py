import requests_html
import requests
import pandas as pd

table = {
    'Title': [],
    'Rating': [],
    'URL': [],
    'Ref' : []
}


h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
}


session = requests_html.HTMLSession()
response = session.get(
    'https://www.netshoes.com.br/lst/top-marcas/adidas', headers=h)

pages = ['//www.netshoes.com.br/lst/top-marcas/adidas']
aLinks = response.html.find('div.pagination a')

for element in aLinks:
    pages.append(element.attrs['href'])
pages.pop()

for page in pages:  # pagination
    response = session.get('https:'+page, headers=h)
    prodList = response.html.find('div.wrapper a[parent-sku]')
    for element in prodList:  # append all product URLs in each page
        table['URL'].append('https:'+element.attrs['href'])

for product in table['URL']:  # get data for each product
    response = session.get(product, headers=h)
    title = response.html.find('h1[data-productname]', first=True).text
    rating = response.html.find('span.rating-box__value', first=True)
    ref = response.html.find('span[data-product-sku]', first=True).text
    table['Title'].append(title)
    table['Rating'].append(rating)
    table['Ref'].append(ref)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
df = pd.DataFrame(table)
print(df)
