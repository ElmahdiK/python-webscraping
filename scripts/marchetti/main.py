import requests
from bs4 import BeautifulSoup
import json
import os

links = []

urlName = 'http://marchetti.chez.com/'
url = urlName+'peintres.htm'
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    # content = soup.find('title')
    lis = soup.find('table').find_all('tr')

    # len(lis)
    # [print(str(li) + '\n\n') for li in lis]
    for li in lis:
        a = li.find('a')
        i = li.find('img')
        cat = li.find('ul')
        if cat != None:
            specialites = []
            for spe in cat.find_all('li'):
                specialites.append(spe.text)
        if a != None:
            filename, file_extension = os.path.splitext(urlName+a['href'])
            peintre_name=(a['href'].split('/')[0])
            imgs = []
            if filename[-1].isnumeric():
                remove_last = filename[:-1]
                for n in range(1, 10):
                    responsePage = requests.get(remove_last+str(n)+file_extension)
                    if responsePage.ok:
                        soupImg = BeautifulSoup(responsePage.text, 'html.parser')
                        for img in soupImg.find('table').find_all('img'):
                            imgs.append(urlName+peintre_name+'/'+img['src'])
                    else:
                        break

            else:
                soupImg = BeautifulSoup(requests.get(urlName+a['href']).text, 'html.parser')
                for img in soupImg.find('table').find_all('img'):
                    imgs.append(urlName+peintre_name+'/'+img['src'])

            links.append({'name': a.text, 'href': urlName+a['href'], 'country': urlName+i['src'], 'img': imgs, 'specialites': specialites})

    links_to_json = json.dumps(links)
    # print(links_to_json)
    jsonFile = open('marchetti.json', 'w')
    jsonFile.write(links_to_json)
    jsonFile.close()
