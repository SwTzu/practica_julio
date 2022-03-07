from selenium import webdriver
from bs4 import BeautifulSoup
import requests, time

class EncargoRobo:
    def __init__(self, patenteVehiculo, API_KEY, page_url):
        self.__patenteVehiculo = patenteVehiculo
        self.__API_KEY = API_KEY
        self.__page_url = page_url

    def __Solver(self, driver, API_KEY, page_url):
        print('ENTRE EN SOLVEEEEER')
        soup = BeautifulSoup(driver.page_source, 'html.parser') 
        sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
        #sitekey = '6LctMP8SAAAAANBvpGMjkMm5bBJ7TY-7X9UuGAaq'
        u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={page_url}&json=1"
        r1 = requests.get(u1)
        rid = r1.json().get("request")
        u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
        time.sleep(5)
        while True:
            r2 = requests.get(u2)
            if r2.json().get("status") == 1:
                form_tokon = r2.json().get("request")
                break
            time.sleep(5)
        wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
        driver.execute_script(wirte_tokon_js)
        time.sleep(3)

    def resultado(self):

        driver = webdriver.Chrome()
        driver.get(self.__page_url)
        driver.find_element_by_xpath('//*[@id="txt_placa_patente"]').send_keys(self.__patenteVehiculo)
        self.__Solver(driver, self.__API_KEY, self.__page_url)
        btt=driver.find_element_by_xpath('//*[@id="btn_consultar"]')
        btt.click()
        time.sleep(5)
        print(driver.page_source, file=open("robo.html", "w"))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #print(soup)
        content=soup.find_all('div', class_='modal-content')
        informacion = [] 
        estado = [] 
        for i in content:
            for z in i.find_all('label', id='lbl_Vehiculo'):
                mensaje=z.text
                informacion.append(z.text)

            for z in i.find_all('td', align='left'):
                estado.append(z.text)

        #driver.close()
        return [informacion, estado]

if __name__ == '__main__':
    registro_encargo_robo = EncargoRobo('HKCB50',"2a2b5480b431e8976a70ebbf3d38f550", 'https://www.autoseguro.gob.cl' )
    print(registro_encargo_robo.resultado())