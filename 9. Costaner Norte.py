#hay que pegarle una ordenada de datosyera
from bs4 import BeautifulSoup
from selenium import webdriver
import requests, time


API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
page_url ='https://web.costaneranorte.cl/circulaste-sin-tag/consultar-transitos-sin-tag/'

def Solver(url):
    #soup = BeautifulSoup(driver.page_source, 'html.parser') 
    #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
    sitekey = '6Lfchk8UAAAAAMPIv-l8SB4CfG385t6a5UfR08vt'
    u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={url}&json=1"
    r1 = requests.get(u1)
    print(r1.json())
    rid = r1.json().get("request")
    u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
    time.sleep(5)
    while True:
        r2 = requests.get(u2)
        print(r2.json())
        if r2.json().get("status") == 1:
            form_tokon = r2.json().get("request")
            break
        time.sleep(5)
    wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
    driver.execute_script(wirte_tokon_js)
    time.sleep(3)
    print("captcha solved")


link='https://www.costaneranorte.cl/infraccion/VerificaInfraccion.aspx'
#patente
driver=webdriver.Chrome()
driver.get(link)
driver.find_element_by_xpath('//*[@id="txtpatente"]').send_keys('CKFL14')
Solver(link)
driver.find_element_by_xpath('//*[@id="Button1"]').click()
soup = BeautifulSoup(driver.page_source, 'html.parser')
fecha,categoria,estado=[],[],[]
a = soup.find_all('table')
for i in a:
    for z in i.find_all('td')[0::3]:
        fecha.append(z.text)
        print(z.text)
    print('------------------')
    for z in i.find_all('td')[1::3]:
        categoria.append(z.text)
        print(z.text)
    print('------------------')
    for z in i.find_all('td')[2::3]:
        estado.append(z.text)
        print(z.text)
    print('------------------')