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

sitekey='6Lc03YYUAAAAAL0m-kzq5mX0LuAXU9qIYl5cZITc'
#6LfLcM0ZAAAAAD7Hg4naLOztkivPicp2rESqr47n
API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
APIKEY_2CAPTCHA="1abc234de56fab7c89012d34e56fa7b8"
api_key = os.getenv(APIKEY_2CAPTCHA, API_KEY)
solver= TwoCaptcha(api_key)

options = webdriver.ChromeOptions()

# options.add_argument('--proxy-server=%s' % PROXY[0])
options.add_argument('--ignore-certificate-errors')
options.add_argument("--lang=es")
driver = get_driver(name_path='chromedriver.exe',
                    options=options, verbose=1, debug=True)

page='https://www.aach.cl/conremate/'
driver.get(page)
letras='KYDX'
numeros='57'
driver.find_element_by_xpath('//*[@id="masterContenido_txtLetras"]').send_keys(letras)
driver.find_element_by_xpath('//*[@id="masterContenido_txtNumeros"]').send_keys(numeros)
try:
    result=solver.recaptcha(sitekey=sitekey,
                            url=driver.current_url)
except:
    print('error')
else:
    result=str(result.get('code'))
driver.find_element_by_xpath('//*[@id="masterContenido_chkCondiciones"]').click()
driver.find_element_by_xpath('//*[@id="masterContenido_btnLnkConsultar"]').click()
soup=BeautifulSoup(driver.page_source,'html.parser')
#print(driver.page_source, file=open('4rematados.html','w'))
table=driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/main/section/form/div[3]/div/div/table/tbody/tr/td/div/table[3]/tbody')
for i in table:
    print(i.text)