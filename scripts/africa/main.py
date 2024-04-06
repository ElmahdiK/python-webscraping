import requests
from bs4 import BeautifulSoup
import json

links = []

url = 'https://fr.wikipedia.org/wiki/Liste_des_pays_africains_par_population'
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    # content = soup.find('title')
    section = soup.find('div', id='mw-content-text')
    lis = section.find_next('ul').find_all('li')

    # len(lis)
    # [print(str(li) + '\n\n') for li in lis]
    for li in lis:
        a = li.find('a')
        link = a['href']
        links.append('https://fr.wikipedia.org'+link)

    links_to_json = json.dumps(links)
    # print(links_to_json)
    jsonFile = open('africa.json', 'w')
    jsonFile.write(links_to_json)
    jsonFile.close()
