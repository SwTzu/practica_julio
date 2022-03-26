from selenium import webdriver
import time
import os
import random
import requests
import urllib
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha
# config = {"USER": "foo", "EMAIL": "foo@example.org"}
#config = dotenv_values(".env")
# print(config)
#BASEDIR = os.path.abspath(os.path.dirname(__file__))
'''
CLAVE-BANCO="magister42662456"
RUT="20483685k"
MAIL="jeclatino@gmail.com"
MAIL1="ni.brevis"
MAIL2="gmail.com"
'''
psw_paypal = "magister42662456"
rut = "20483685k"
mail_paypal = "jeclatino@gmail.com"
mail_usuario='ni.brevis@gmail.com'

API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"


def Solver(url):
    #soup = BeautifulSoup(driver.page_source, 'html.parser') 
    #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
    
    sitekey = '6Ld_vfsSAAAAAGbw9u9u1V2x8pqV_3Y5AS4h9mW1'
    u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={url}&json=1&enterprise=1"
    r1 = requests.get(u1)
    #print(r1.json())
    rid = r1.json().get("request")
    u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
    time.sleep(5+random.randint(1,3))
    while True:
        r2 = requests.get(u2)
        #print(r2.json())
        if r2.json().get("status") == 1:
            form_tokon = r2.json().get("request")
            break
        time.sleep(5+random.randint(1,3))
    #print("Captcha Solved")
    return form_tokon


def certificado():
    options = webdriver.ChromeOptions()

    # options.add_argument('--proxy-server=%s' % PROXY[0])
    #options.add_argument('--ignore-certificate-errors')
    #options.add_argument('--headless')
    driver = webdriver.Chrome("./chromedriver.exe", options=options)

    link1 = 'https://www.registrocivil.cl/OficinaInternet/web/carro.srcei'
    driver.get(link1)

    time.sleep(2+random.randint(1,3))
    driver.find_element_by_xpath('//*[@id="title_0"]').click()
    driver.find_element_by_xpath('//*[@id="title_5"]').click()
    time.sleep(2+random.randint(1,3))
    driver.find_element_by_xpath(
        '/html/body/div/div[7]/div[1]/div[7]/div[2]/table/tbody/tr[1]/td[1]/div/ins').click()
    driver.find_element_by_xpath('//*[@id="idInputPPU_4_4_1"]').send_keys('GRYD37')
    driver.find_element_by_xpath('//*[@id="btn_agregarCarro_1#4_4_1#1"]').click()

    driver.switch_to.frame(driver.find_element_by_id('cu_idIframe4'))
    img=driver.find_element_by_xpath('html/body/img[1]').get_attribute('src')


    urllib.request.urlretrieve(img, 'captchacav.png')

    api_key = os.getenv('1abc234de56fab7c89012d34e56fa7b8', '2a2b5480b431e8976a70ebbf3d38f550')
    solver = TwoCaptcha(api_key)
    result=solver.normal('./captchacav.png')
    #/html/body/img[1]
    driver.find_element_by_xpath('/html/body/input').send_keys(result.get('code'))
    driver.find_element_by_xpath('/html/body/button').click()
    driver.switch_to.default_content()
    time.sleep(2+random.randint(1,3))
    driver.find_element_by_xpath(
        '//*[@id="carro_solicitanteInputEmail"]').send_keys(mail_usuario)
    driver.find_element_by_xpath(
        '//*[@id="carro_solicitanteInputEmailConfirm"]').send_keys(mail_usuario)
    driver.find_element_by_xpath('//*[@id="carro_btnContinuar"]').click()
    time.sleep(1+random.randint(1,3))
    driver.find_element_by_xpath(
        '/html/body/div/div[1]/div[1]/form/div/div[1]/input').click()
    driver.find_element_by_xpath('//*[@id="continuar_btn_button"]').click()
    driver.maximize_window()
    time.sleep(5+random.randint(1,3))
    driver.find_element_by_xpath('//*[@id="todos15"]').click()
    driver.find_element_by_xpath('//*[@id="id-button-button-icon"]').click()
    time.sleep(5+random.randint(1,3))
    driver.find_element_by_xpath(
        '/html/body/app-root/app-order/div/div/div/div/section/app-order-pay/div/div/div/div[3]/app-button-paypal/div/div/div').click()
    time.sleep(4+random.randint(1,3))
    main_page = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != main_page:
            pay_page = handle
    driver.switch_to.window(pay_page)
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1+random.randint(1,3))
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/main/p/a').click()
    time.sleep(2+random.randint(1,3))
    driver.find_element_by_xpath(
        '/html/body/div[1]/section[2]/div/div/form/div[3]/div[1]/div[2]/div[1]/input').send_keys(mail_paypal)
    time.sleep(1+random.randint(1,3))
    driver.find_element_by_xpath(
        '/html/body/div[1]/section[2]/div/div/form/div[3]/div[2]/button').click()
    time.sleep(1+random.randint(1,3))


    time.sleep(2+random.randint(1,3))
    driver.find_element_by_xpath(
        '/html/body/div[1]/section[2]/div/div/form/div[4]/div[1]/div/div/div[1]/input').send_keys(psw_paypal)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section[2]/div/div/form/div[4]/div[4]/button').click()
    time.sleep(10+random.randint(1,3))
    driver.quit()
    # DESDE AQUI COMIENZA LA CONFIRMACION DEL PAGO


while True:
    try:
        print('Iniciando')
        certificado()
        #break
    except:
        time.sleep(60+random.randint(1,3))
        pass
