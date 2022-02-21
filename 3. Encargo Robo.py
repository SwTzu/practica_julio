from selenium import webdriver
from bs4 import BeautifulSoup
import requests, time


API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
page_url ='https://www.autoseguro.gob.cl'

def Solver(driver,url):
    soup = BeautifulSoup(driver.page_source, 'html.parser') 
    sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
    #sitekey = '6LctMP8SAAAAANBvpGMjkMm5bBJ7TY-7X9UuGAaq'
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


    #time.sleep(10)
'''

'''
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(page_url)
    driver.find_element_by_xpath('//*[@id="txt_placa_patente"]').send_keys('LBBB52')
    Solver(driver,page_url)
    btt=driver.find_element_by_xpath('//*[@id="btn_consultar"]')
    btt.click()
    time.sleep(5)
    print(driver.page_source, file=open("robo.html", "w"))
    '''
    with open("robo.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    '''
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #print(soup)
    content=soup.find_all('div', class_='modal-content')

    for i in content:
        for z in i.find_all('label', id='lbl_Vehiculo'):
            mensaje=z.text
            print(z.text)
        for z in i.find_all('th'):
            print(z.text)
        for z in i.find_all('td', align='left'):
            print(z.text)
    #driver.close()