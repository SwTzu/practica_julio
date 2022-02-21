from selenium import webdriver
from twocaptcha import TwoCaptcha
import os
from bs4 import BeautifulSoup
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

API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
APIKEY_2CAPTCHA="1abc234de56fab7c89012d34e56fa7b8"
api_key = os.getenv(APIKEY_2CAPTCHA, API_KEY)
solver= TwoCaptcha(api_key)
sitekey='6LeGGUsUAAAAAGA45yjoGkJ__EKeRqa-KipeYSW-'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--lang=es")
driver = get_driver(name_path='chromedriver.exe',
                        options=options, verbose=1, debug=True)
driver.get('https://www.costaneranorte.cl/LoginNoFrecuente.html')
driver.find_element_by_xpath('//*[@id="PATENTE"]').send_keys('PHSS63')
driver.find_element_by_xpath('/html/body/div/section/div/div[2]/form/a').click()
driver.find_element_by_xpath('/html/body/div/section/div/div[2]/form/p[2]/a').click()
#print(str(driver.current_url))
try:
    result=solver.recaptcha(sitekey=sitekey,
                            url=driver.current_url)
except:
    print('error')
else:
    result=str(result.get('code'))
driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{result}";')
driver.find_element_by_xpath('/html/body/div[1]/section/div/form/div[2]/a').click()
soup=BeautifulSoup(driver.page_source,'html.parser')
table=soup.find_all('table', id='TablaConvenioDeuda')
for i in table:
    for z in i.find_all('td'):
        print(z.text)
