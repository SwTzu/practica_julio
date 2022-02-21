from selenium import webdriver
import time
import os
import requests
from bs4 import BeautifulSoup


def getProxies():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        if row.find_all('td')[4].text == 'elite proxy':
            proxy = ':'.join([row.find_all('td')[0].text,
                             row.find_all('td')[1].text])
            proxies.append(proxy)
        else:
            pass
    return proxies


def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def get_driver(name_path: str = 'chromedriver.exe', options: None = None, verbose: int = 0, debug: bool = False):
    try:
        chrome_path = os.path.dirname(__file__) + f'./{name_path}'
        if verbose == 0:
            driver = webdriver.Chrome(executable_path=chrome_path)
        elif verbose == 1:
            driver = webdriver.Chrome(
                executable_path=chrome_path, options=options)
    except:
        chrome_path = os.path.abspath('./f{name_path}')
        if verbose == 0:
            driver = webdriver.Chrome(executable_path=chrome_path)
        elif verbose == 1:
            driver = webdriver.Chrome(
                executable_path=chrome_path, options=options)
    return driver


chrome_path = os.path.abspath('./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--lang=es")
driver = get_driver(name_path='chromedriver.exe',
                    options=options, verbose=1, debug=True)
# cabezera=open("headers.json")

# cabezera=dict(json.load(cabezera))
primary_link = 'http://www.rutasdelpacifico.cl/pago/valida'
link1 = 'https://boton.unired.cl/BotonPago/IniciaFlujoOnline?u='
Dato1 = {
    'patente': 'CKFL14'
}
response = requests.post(primary_link, data=Dato1)
print(response.text, file=open("costanera_norte copy.txt", "w"))
soup = BeautifulSoup(response.text, 'html.parser')
id = soup.find_all("input", value=True)

for i in id:
    link2 = (i['value'])
# print(link2)

c_link = link1+str(link2)
# print(c_link)
driver.get(c_link)
time.sleep(5)
cajaDeuda = driver.find_elements_by_xpath(
    '/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[2]/div')
for i in cajaDeuda:
    print(i.text)
