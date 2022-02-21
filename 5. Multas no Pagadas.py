from bs4 import BeautifulSoup
import requests, time
from selenium import webdriver
wea='http://consultamultas.srcei.cl/ConsultaMultas/consultaMultasExterna.do'
API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
page_url ='http://consultamultas.srcei.cl/ConsultaMultas/buscarConsultaMultasExterna.do'
PROXY='20.47.108.204:8888'
def Solver(url):
    sitekey = '6Ld_vfsSAAAAAGbw9u9u1V2x8pqV_3Y5AS4h9mW1'
    u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={url}&json=1"
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
    print("captcha solved")

#key=str(Solver(page_url))

driver=webdriver.Chrome()
driver.get(wea)
time.sleep(1)
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/form/table/tbody/tr[7]/td[2]/span/input').send_keys('BJRS94')
Solver(page_url)
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