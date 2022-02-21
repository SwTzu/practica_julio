# hay que pegarle una ordenada de datosyera
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

driver = webdriver.Chrome()

API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
page_url = 'https://www.autopase.cl/circulaste_sin_tag/consulta_infracciones'


def Solver(driver, url):
    #soup = BeautifulSoup(driver.page_source, 'html.parser')
    #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
    sitekey = '6LdkAAgTAAAAAGaG1OjDMAn4q-zvgrArJDrIuPif'
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
    print("captcha solved")
    wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
    driver.execute_script(wirte_tokon_js)

driver.get(page_url)
driver.find_element_by_xpath('//*[@id="sInputRadio1"]').click()
driver.find_element_by_xpath('//*[@id="sInput"]').send_keys('PHSS63')
Solver(driver,page_url)
driver.find_element_by_xpath('//*[@id="Pagar"]').click()
soup = BeautifulSoup(driver.page_source, 'html.parser')
tablaVentana = soup.find_all('table', id='tabla_ventana')
noFacturados = soup.find_all('table', id='tabla_nofacturados')
Facturados = soup.find_all('table', id='tabla_facturados')
detalle = soup.find_all('div', role='dialog', class_=True,style=True, attrs={'aria-hidden': 'true'})
tablaVentana_rut, tablaVentana_placaPatente, tablaVentana_fecha, tablaVentana_total = [], [], [], []
noFacturados_rut, noFacturados_placaPatente, noFacturados_fecha, noFacturados_total = [], [], [], []
facturados_rut, facturados_placaPatente, facturados_BE, facturados_cargoMes = [], [], [], []
detalle_patente,detalle_fecha,detalle_hora=[],[],[]

for i in tablaVentana:
    for z in i.find_all('td')[0::4]:
        tablaVentana_rut.append(z.text)
        print(z.text)
    for z in i.find_all('td')[1::4]:
        tablaVentana_placaPatente.append(z.text)
        print(z.text)
    for z in i.find_all('td')[2::4]:
        tablaVentana_fecha.append(z.text)
        print(z.text)
    for z in i.find_all('td')[3::4]:
        tablaVentana_total.append(z.text)
        print(z.text)

for i in noFacturados:
    for z in i.find_all('td')[0::4]:
        noFacturados_rut.append(z.text)
        print(z.text)
    for z in i.find_all('td')[1::4]:
        noFacturados_placaPatente.append(z.text)
        print(z.text)
    for z in i.find_all('td')[2::4]:
        noFacturados_fecha.append(z.text)
        print(z.text)
    for z in i.find_all('td')[3::4]:
        noFacturados_total.append(z.text)
        print(z.text)

for i in Facturados:
    for z in i.find_all('td', rowspan=False, class_=False)[0::6]:
        facturados_rut.append(z.text)
        print(z.text)
    for z in i.find_all('td', rowspan=False, class_=False)[1::6]:
        facturados_placaPatente.append(z.text)
        print(z.text)
    for z in i.find_all('td', rowspan=False, class_=False)[3::6]:
        facturados_BE.append(z.text)
        print(z.text)
    for z in i.find_all('td', rowspan=False, class_=False)[4::6]:
        facturados_cargoMes.append(z.text)
        print(z.text)

for i in detalle:
    for z in i.find_all('td')[0::3]:
        detalle_patente.append(z.text.replace('Patente','-'))
        print(z.text.replace('Patente','-'))
    for z in i.find_all('td')[1::3]:
        detalle_fecha.append(z.text.replace('Fecha','-'))
        print(z.text.replace('Fecha','-'))
    for z in i.find_all('td')[2::3]:
        detalle_hora.append(z.text.replace('Hora','-'))
        print(z.text.replace('Hora','-'))



#driver.quit()
'''
df = pd.DataFrame(data=Tudick, columns=columns)
json_response = df.to_json(orient='records')
'''
