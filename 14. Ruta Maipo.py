from selenium import webdriver
import time, os,requests
from bs4 import BeautifulSoup

def getProxies():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        if row.find_all('td')[4].text =='elite proxy':
            proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
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
            driver = webdriver.Chrome(executable_path=chrome_path,options=options)
    except:
        chrome_path = os.path.abspath('./f{name_path}')
        if verbose == 0:
            driver = webdriver.Chrome(executable_path=chrome_path)
        elif verbose == 1:
            driver = webdriver.Chrome(executable_path=chrome_path,options=options)
    return driver

chrome_path = os.path.abspath('./chromedriver.exe')
options=webdriver.ChromeOptions() 
options.add_argument('--ignore-certificate-errors')
options.add_argument("--lang=es")
driver = get_driver(name_path='chromedriver.exe', options=options, verbose=1, debug=True)

link='https://www.rutamaipo.cl/taginterurbano/pasaste-sin-tag'
driver.get(link)
imput=driver.find_element_by_xpath('//*[@id="patente"]')
imput.send_keys('WT8329')
driver.find_element_by_xpath('//*[@id="consultar_sintag"]').click()
time.sleep(2)
try:
    driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div/div/button').click()
except:
    pass 
table1=driver.find_element_by_xpath('/html/body/div/main/div[1]/section/div[2]/div/form').text
table2=driver.find_element_by_xpath('/html/body/div/main/div[1]/section/div[2]/div/div[2]').text
print(table1)
print(table2)