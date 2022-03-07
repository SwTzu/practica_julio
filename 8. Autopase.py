from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

class Autopase:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo
        self.__API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
        self.__page_url = 'https://www.autopase.cl/circulaste_sin_tag/consulta_infracciones'

    def __Solver(self, driver, url):
            #soup = BeautifulSoup(driver.page_source, 'html.parser')
            #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
            sitekey = '6LdkAAgTAAAAAGaG1OjDMAn4q-zvgrArJDrIuPif'
            u1 = f"https://2captcha.com/in.php?key={self.__API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={url}&json=1"
            r1 = requests.get(u1)
            rid = r1.json().get("request")
            u2 = f"https://2captcha.com/res.php?key={self.__API_KEY}&action=get&id={int(rid)}&json=1"
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

    def getInfracciones(self):
        driver = webdriver.Chrome()

        driver.get(self.__page_url)
        driver.find_element_by_xpath('//*[@id="sInputRadio1"]').click()
        driver.find_element_by_xpath('//*[@id="sInput"]').send_keys(self.__patenteVehiculo)
        self.__Solver(driver,self.__page_url)
        driver.find_element_by_xpath('//*[@id="Pagar"]').click()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #tablaVentana = soup.find_all('table', id='tabla_ventana')
        noFac = soup.find_all('table', id='tabla_nofacturados')
        Fac = soup.find_all('table', id='tabla_facturados')
        Det = soup.find_all('div', role='dialog', class_=True,style=True, attrs={'aria-hidden': 'true'})
    
        noFacturados = []
        Facturados = []
        aux_Detalle = []
        Detalle = []

        all_rut_1 = []
        all_patente_1 = []
        all_fecha_1 = []
        all_total_1 = []
        contador_Autopase1 = 0

        all_rut_2 = []
        all_patente_2 = []
        all_numero_boleta_2 = []
        all_cargo_mes_2 = []
        contador_Autopase2=0

        all_patente_3 = []
        all_fecha_3= []
        all_hora_3 = []
        contador_Autopase3=0

        for detalle_1 in noFac:
            for rut_1 in detalle_1.find_all('td')[0::4]:
                all_rut_1.append(rut_1.text)
                contador_Autopase1+=1
            for patente_1 in detalle_1.find_all('td')[1::4]:
                 all_patente_1.append(patente_1.text)
            for fecha_1 in detalle_1.find_all('td')[2::4]:
                all_fecha_1.append(fecha_1.text)
            for total_1 in detalle_1.find_all('td')[3::4]:
                all_total_1.append(total_1.text)

        if(len(all_rut_1)!=len(all_total_1)):
            pass

        else:
            for i_detalle_1 in range(0, contador_Autopase1):
                aux_noFacturado = []
                aux_noFacturado.append(all_rut_1[i_detalle_1])
                aux_noFacturado.append(all_patente_1[i_detalle_1])
                aux_noFacturado.append(all_fecha_1[i_detalle_1])
                aux_noFacturado.append(all_total_1[i_detalle_1])
                noFacturados.append(aux_noFacturado)

        for detalle_2 in Fac:
            
            for rut_2 in detalle_2.find_all('td', rowspan=False, class_=False)[0::6]:
                all_rut_2.append(rut_2.text)
                contador_Autopase2+=1
            for patente_2 in detalle_2.find_all('td', rowspan=False, class_=False)[1::6]:
                all_patente_2.append(patente_2.text)
            for numero_boleta_2 in detalle_2.find_all('td', rowspan=False, class_=False)[3::6]:
                all_numero_boleta_2.append(numero_boleta_2.text)
            for cargo_mes_2 in detalle_2.find_all('td', rowspan=False, class_=False)[4::6]:
                all_cargo_mes_2.append(cargo_mes_2.text)

        if(len(all_rut_2)!=len(all_cargo_mes_2)):
            pass

        else:
            for i_detalle_2 in range(0, contador_Autopase2):
                aux_Facturado = []
                aux_Facturado.append(all_rut_2[i_detalle_2])
                aux_Facturado.append(all_patente_2[i_detalle_2])
                aux_Facturado.append(all_numero_boleta_2[i_detalle_2])
                aux_Facturado.append(all_cargo_mes_2[i_detalle_2])
                Facturados.append(aux_Facturado)

        cont_numb_boleta_2 = 0

        for detalle_3 in Det:
            
            aux_all_patente_3=[]
            aux_all_fecha_3=[]
            aux_all_hora_3=[]
            contador_Autopase3+=1

            for patente_3 in detalle_3.find_all('td')[0::3]:
                if(patente_3.text.replace('Patente','-')=='-'):
                    pass
                else:
                    aux_all_patente_3.append(patente_3.text)
            for fecha_3 in detalle_3.find_all('td')[1::3]:
                if(fecha_3.text.replace('Fecha','-')=='-'):
                    pass
                else:
                    aux_all_fecha_3.append(fecha_3.text)
            for hora_3 in detalle_3.find_all('td')[2::3]:
                if(hora_3.text.replace('Hora','-')=='-'):
                    pass
                else:
                    aux_all_hora_3.append(hora_3.text)

            all_patente_3.append(aux_all_patente_3)
            all_fecha_3.append(aux_all_hora_3)
            all_hora_3.append(aux_all_hora_3)


            aux_Detalle.append([all_numero_boleta_2[cont_numb_boleta_2] ,aux_all_patente_3, aux_all_fecha_3, aux_all_hora_3])
            cont_numb_boleta_2+=1

        if(len(all_patente_3)!=len(all_hora_3)):
            pass

        else:

            for i_detalle_3 in aux_Detalle:
                
                #aux_Detalle_final.append(i_detalle_3[0])
                for detalles in range(0, len(i_detalle_3[1])):
                    aux_Detalle_final = []
                    #aux_Detalle_final.append([i_detalle_3[0], i_detalle_3[1][detalles], i_detalle_3[2][detalles], i_detalle_3[3][detalles]])
                    aux_Detalle_final.append(i_detalle_3[0])
                    aux_Detalle_final.append(i_detalle_3[1][detalles])
                    aux_Detalle_final.append(i_detalle_3[2][detalles])
                    aux_Detalle_final.append(i_detalle_3[3][detalles])

                    Detalle.append(aux_Detalle_final)

        return [noFacturados, Facturados, Detalle]

if __name__ == '__main__':
    registro_autopase = Autopase('CKFL14')
    print(registro_autopase.getInfracciones())