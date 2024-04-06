import requests
from bs4 import BeautifulSoup
import json
import os

links = []


links = []

url = 'https://www.poesie-francaise.fr/poemes-auteurs/'
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    # content = soup.find('title')
    lis = soup.find('ul', id='poemes_a').find_all('li')

    # len(lis)
    # [print(str(li) + '\n\n') for li in lis]
    for li in lis:
        a = li.find('a')
        link = a['href']
        links.append(link)

    # print(links)
    links_to_json = json.dumps(links)
    # print(links_to_json)
    jsonFile = open('poemia.json', 'w')
    jsonFile.write(links_to_json)
    jsonFile.close()