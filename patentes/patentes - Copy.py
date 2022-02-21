
from selenium import webdriver
from bs4 import BeautifulSoup
import requests, time


API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
page_url ='https://www.google.com/recaptcha/api2/demo'

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
    driver.execute_script(f'verifyDemoRecaptcha("{form_tokon}")')

    time.sleep(10)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://2captcha.com/demo/recaptcha-v2-callback')
    #imput=driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_patenteInput"]')
    #imput.send_keys('CKFL14')
    Solver(driver,page_url)

    #driver.close()