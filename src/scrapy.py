# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup


URL = 'https://www.amazon.com.br/s?k=iphone'
header = {
    'user-agente': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

response = requests.get(URL, header)

while response.status_code != 200:
    response = requests.get(URL, header)

soup = BeautifulSoup(response.content, 'html.parser')
iphones = soup.find_all("div", attrs={"class": "s-card-border"})

for iphone in iphones:
    name = iphone.select("h2 > a > span")[0].string
    price = iphone.select("span > .a-offscreen")
    if price:
        print(name, price[0].string)
    else:
        print(name)


with open(
    'amazon-iphone-list.csv', 'w', newline='', encoding='utf-8-sig',
) as file:
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
