
import requests
from bs4 import BeautifulSoup
headers = {
    'authority': 'www.volanteomaleta.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Opera GX";v="83", "Chromium";v="97", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'origin': 'https://www.volanteomaleta.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.volanteomaleta.com/',
    'accept-language': 'en-US,en;q=0.9,es-CL;q=0.8,es;q=0.7',
    'cookie': '_ga=GA1.2.125922202.1646149308; _gid=GA1.2.656936339.1646149308; _gat_gtag_UA_158657120_1=1',
}
with open("gen-ruts-1646148869994.txt",'r') as f:
    ruts = f.readlines()
    for i in ruts:
        i=(i.strip('\n').replace(',','.'))
        data = {
        'term': i
        }

        response = requests.post('https://www.volanteomaleta.com/rut', headers=headers, data=data)
        soup=BeautifulSoup(response.text, 'html.parser')
        for x in soup.find('table',class_='table table-hover').find('tbody').find_all('tr'):
            print(x.find_all('td')[0].text,file=open('patentes.txt','a'))
