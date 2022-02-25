import requests
from bs4 import BeautifulSoup
import requests
import time
from re import A
from selenium import webdriver
from importlib.resources import path
from twocaptcha import TwoCaptcha
import os

class Vehiculos_Rematados:

    def __init__(self, sitekey, API_KEY, APIKEY_2CAPTCHA, letras, numeros, page):
        self.sitekey = sitekey
        self.API_KEY = API_KEY
        self.APIKEY_2CAPTCHA = APIKEY_2CAPTCHA
        self.letras = letras
        self.numeros = numeros
        self.page = page

    def get_driver(self, name_path: str = 'chromedriver.exe', options: None = None, verbose: int = 0, debug: bool = False):
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
    
    def resultado(self,sitekey, API_KEY, APIKEY_2CAPTCHA, letras, numeros, page):
        #6LfLcM0ZAAAAAD7Hg4naLOztkivPicp2rESqr47n
        api_key = os.getenv(APIKEY_2CAPTCHA, API_KEY)
        solver = TwoCaptcha(api_key)
        options = webdriver.ChromeOptions()
        # options.add_argument('--proxy-server=%s' % PROXY[0])
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--lang=es")
        driver = self.get_driver(name_path='chromedriver.exe', options=options, verbose=1, debug=True)
        driver.get(page)
        driver.find_element_by_xpath('//*[@id="masterContenido_txtLetras"]').send_keys(letras)
        driver.find_element_by_xpath('//*[@id="masterContenido_txtNumeros"]').send_keys(numeros)
        try:
            result = solver.recaptcha(sitekey=sitekey,url=driver.current_url)
        except:
            print('error')
        else:
            result=str(result.get('code'))
        driver.find_element_by_xpath('//*[@id="masterContenido_chkCondiciones"]').click()
        driver.find_element_by_xpath('//*[@id="masterContenido_btnLnkConsultar"]').click()
        soup=BeautifulSoup(driver.page_source,'html.parser')
        #print(driver.page_source, file=open('4rematados.html','w'))
        table = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/main/section/form/div[3]/div/div/table/tbody/tr/td/div/table[3]/tbody')
        a = []
        for i in table:
            a.append(i.text)

        return a

class Multas_No_Pagadas:
    def __init__(self, patente, API_KEY, page_url, x):
        self.patente = patente
        self.API_KEY = API_KEY
        self.page_url = page_url
        self.x = x

    def Solver(self, driver, API_KEY, page_url):
        sitekey = '6Ld_vfsSAAAAAGbw9u9u1V2x8pqV_3Y5AS4h9mW1'
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

    def resultado(self, patente, API_KEY, page_url, x):

        driver=webdriver.Chrome()
        driver.get(x)
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[7]/td[2]/span/input').send_keys(patente)
        self.Solver(driver, API_KEY, page_url)
        driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[8]/td/table/tbody/tr[2]/td/a').click()
        datosTable1,datosTable2=[],[]
        cont=0
        try:
            soup=BeautifulSoup(driver.page_source,'html.parser')
            for i in soup.find_all("table",class_="grilla"):
                for j in i.find_all("td"):
                    if cont==0:
                        datosTable1.append(j.text)
                        #print(j.text)
                    if cont==1:
                        datosTable2.append(j.text)
                        #print(j.text)
                cont+=1

                
        except:
            pass
        for i in datosTable1:
            print(i)
        print ('------------------')
        for i in datosTable2:
            print(i)
        
        return datosTable1, datosTable2

patente = 'PHSS63'

#Vehiculos rematados
#Vehiculos_Rematados1 = Vehiculos_Rematados('6Lc03YYUAAAAAL0m-kzq5mX0LuAXU9qIYl5cZITc', "2a2b5480b431e8976a70ebbf3d38f550", "1abc234de56fab7c89012d34e56fa7b8", 'KYDX','57', 'https://www.aach.cl/conremate/')
#print(Vehiculos_Rematados1.resultado('6Lc03YYUAAAAAL0m-kzq5mX0LuAXU9qIYl5cZITc', "2a2b5480b431e8976a70ebbf3d38f550", "1abc234de56fab7c89012d34e56fa7b8", 'KYDX','57', 'https://www.aach.cl/conremate/'))

#Multas no pagadas
Multas_No_Pagadas1 = Multas_No_Pagadas(patente, "2a2b5480b431e8976a70ebbf3d38f550",'http://consultamultas.srcei.cl/ConsultaMultas/buscarConsultaMultasExterna.do', 'http://consultamultas.srcei.cl/ConsultaMultas/consultaMultasExterna.do')
print(Multas_No_Pagadas1.resultado(patente, "2a2b5480b431e8976a70ebbf3d38f550",'http://consultamultas.srcei.cl/ConsultaMultas/buscarConsultaMultasExterna.do', 'http://consultamultas.srcei.cl/ConsultaMultas/consultaMultasExterna.do'))


