from selenium import webdriver
import urllib,os,time
from twocaptcha import TwoCaptcha
from bs4 import BeautifulSoup
API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
page_url ='https://www.autoviasantiagolampa.cl/oficina-virtual/consultar-transito-sin-tag'

driver = webdriver.Chrome()
if __name__ == '__main__':
    with open('patentes_dv.txt','r') as f:
        for i in f.readlines():
            i=i.strip('\n')
            driver.get(page_url)
            idf=driver.find_element_by_xpath('//*[@id="imagen_captcha"]')
            img= idf.get_attribute('src')
            
            urllib.request.urlretrieve(img, 'captcha12.png')
            api_key = os.getenv('1abc234de56fab7c89012d34e56fa7b8', '2a2b5480b431e8976a70ebbf3d38f550')
            solver = TwoCaptcha(api_key)
            result=solver.normal('./captcha12.png')
            driver.find_element_by_xpath('//*[@id="solicitar_contrasena_plate"]').send_keys(i.split('-')[0])
            driver.find_element_by_xpath('//*[@id="solicitar_contrasena_plate_dv"]').send_keys(i.split('-')[1])
            driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(result.get('code'))
            driver.find_element_by_xpath('//*[@id="transitos_sin_sesion_form"]/div[3]/div/button').click()
            table=driver.find_element_by_xpath('/html/body/div/div[3]').text
            if 'usted no posee' not in table:
                soup=BeautifulSoup(driver.page_source,'html.parser')
                for t in soup.find('table',id='transitos_sin_tag_no_auth_tbl'):
                    print(t.text)
                print(i)
        time.sleep(3)
driver.close()
driver.quit()