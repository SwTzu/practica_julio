from selenium import webdriver
from twocaptcha import TwoCaptcha
from bs4 import BeautifulSoup
import urllib,os

API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
page_url ='https://www.autoviasantiagolampa.cl/oficina-virtual/consultar-transito-sin-tag'

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(page_url)
    idf=driver.find_element_by_xpath('//*[@id="imagen_captcha"]')
    img= idf.get_attribute('src')
    
    urllib.request.urlretrieve(img, 'captcha12.png')

    api_key = os.getenv('1abc234de56fab7c89012d34e56fa7b8', '2a2b5480b431e8976a70ebbf3d38f550')
    solver = TwoCaptcha(api_key)
    result=solver.normal('./captcha12.png')

    driver.find_element_by_xpath('//*[@id="solicitar_contrasena_plate"]').send_keys('GSSV42')
    driver.find_element_by_xpath('//*[@id="solicitar_contrasena_plate_dv"]').send_keys('6')
    driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(result.get('code'))
    driver.find_element_by_xpath('//*[@id="transitos_sin_sesion_form"]/div[3]/div/button').click()
    table=driver.find_element_by_xpath('/html/body/div/div[3]').text
    data=[]
    if 'usted no posee' not in table:
        soup=BeautifulSoup(driver.page_source,'html.parser')
        rows=((soup.find('table',class_='table table-bordered dataTable no-footer',role='grid')).find('tbody')).find_all('tr')
        for row in rows:
            cols=row.find_all('th')
            cols=[ele.text for ele in cols]
            data.append([ele for ele in cols if ele])
        print(data)