# -*- coding: utf-8 -*-
import csv
from bs4 import BeautifulSoup

from scrapy import ScrapyData


URL = 'https://www.amazon.com.br/s?k=iphone'
scrapy = ScrapyData()
response = scrapy.get_data(URL)

soup = BeautifulSoup(response, 'html.parser')
iphones = soup.find_all("div", attrs={"class": "s-card-border"})

with open(
    'amazon-iphone-list.csv', 'w', newline='', encoding='utf-8-sig',
) as file:
    print('Iniciando coleta de dados!')
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['cod', 'description', 'price'])

    for i, iphone in enumerate(iphones):
        name = iphone.select("h2 > a > span")[0].string
        price = iphone.select("span > .a-offscreen")
        if price:
            writer.writerow([i, name, price[0].string])
        else:
            writer.writerow([i, name, 'Sem Estoque'])

file.close()
print('Coleta de dados finalizada.')
