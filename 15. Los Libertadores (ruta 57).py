import json, time, os, urllib
from pip._vendor import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from twocaptcha import TwoCaptcha

class LosLibertadores:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        driver = webdriver.Chrome()
        primary_link='https://www.autopistaloslibertadores.cl/pago/valida'
        link1='https://boton.unired.cl/BotonPago/IniciaFlujoOnline?u='
        datos={'patente':self.__patenteVehiculo}
        response=requests.post(primary_link,data=datos)
        soup=BeautifulSoup(response.text,'html.parser')
        for i in soup.find_all('input',value=True):
            link2=i['value']
        c_link=link1+str(link2)
        driver.get(c_link)
        while True:
            try:
                driver.find_element_by_xpath('/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[1]/div[2]/label/span').click()
                break
            except:
                time.sleep(1)
        driver.find_element_by_xpath('/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[1]/div[2]/label/span').click()
        cajaDeuda = driver.find_elements_by_xpath(
            '/html/body/app-root/app-inicia-flujo-on-line/div[1]/div[4]/div[2]/div')
        info=''
        for i in cajaDeuda:
            info = info+i.text

        driver.close()

        if('No existen' in info):
            return []

        else:

            string1_new = info.split('\n')
            array = []
            aux_array = []
            for i in string1_new:
                if('Transito sin Tag' in i):
                    array.append(aux_array)
                    aux_array = []
                    aux_array.append(i)
                else:
                    aux_array.append(i)

            array.append(aux_array)
            array.remove(array[0])
            
            indice = 0
            array_datos = []
            aux_array_datos = []
            array_detalles = []
            aux_array_detalles = []
            aux_array_detalles_2 = []

            for i in array:
                while(indice<5):
                    aux_array_datos.append(i[indice])
                    indice+=1

                array_datos.append(aux_array_datos)
                aux_array_datos = []

                while(True):
                    try:
                        aux_array_detalles.append(i[indice])
                        indice+=1
                    except:
                        indice=0
                        array_detalles.append(aux_array_detalles)
                        aux_array_detalles = []
                        break

            for i in array_datos:
                len_array_datos = len(array_datos)

                for j in range(0, len_array_datos):
                    if('Transito' in i[j]):
                        i[j] = (i[j].split('Ruta')[1]).strip()

                    if('Vence' in i[j]):
                        i.pop(j)
                        len_array_datos-=1

            for i in array_detalles:
                len_array_i = len(i)

                for j in range(0, len_array_i):
                    try:
                        k = i[j].split(':', 1)[1]
                    except:
                        k = i[j]

                    if(':' in k):
                        k = k.split(' ')

                    if(len(k)==2 and not('-' in k)):
                        aux_array_detalles.append(k[1])
                        aux_array_detalles.append(k[0])
                    else:
                        aux_array_detalles.append(k)

                aux_array_detalles_2.append(aux_array_detalles)
                aux_array_detalles = []

            array_detalles_final = []

            for i in aux_array_detalles_2:
                array_i = []
                aux_array_i = []

                for j in i:
                    if(j==self.__patenteVehiculo):
                        array_i.append(aux_array_i)
                        aux_array_i = []
                        aux_array_i.append(j) 
                    
                    else:
                        aux_array_i.append(j)

                array_i.append(aux_array_i)
                array_i.remove(array_i[0])
                array_detalles_final.append(array_i)

            print(array_datos)
            print(array_detalles_final)

            return [array_datos, array_detalles_final]

if __name__ == '__main__':
    registro_los_libertadores = LosLibertadores('CKFL14')
    print(registro_los_libertadores.getInfracciones())