import json, time, os, urllib
from pip._vendor import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from twocaptcha import TwoCaptcha

lista_patentes=['KXPS43']
class Functions():
    def Solver(self,img,text):
        urllib.request.urlretrieve(img, f'captcha{text}.png')
        api_key = os.getenv('1abc234de56fab7c89012d34e56fa7b8', '2a2b5480b431e8976a70ebbf3d38f550')
        solver = TwoCaptcha(api_key)
        result=solver.normal(f'./captcha{text}.png')
        return result.get('code')

def getDriverNororiente(name_path: str = 'chromedriver.exe', options: None = None, verbose: int = 0, debug: bool = False):
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

class Vehiculo:
    def __init__ (self, patente):
        self.__patente = patente
        self.__registro_transporte_publico = []
        self.__infracciones_vespucio_norte = []
        self.__infracciones_vespucio_sur = []
        self.__infracciones_autopase = []
        self.__infracciones_costanera_norte = []
        self.__infracciones_nororiente = []
        self.__infracciones_vias_exclusivas = []
        self.__infracciones_lampa_santiago = []
        self.__infracciones_del_sol = []
        self.__infracciones_ruta_maipo = []
        self.__infracciones_los_libertadores = []
        self.__infracciones_el_pacifico = []

    def getPatente(self):
        return self.__patente

    def getRegistroTransportePublico(self):

        print('\nREGISTRO NACIONAL DE TRANSPORTE PÚBLICO Y ESCOLAR\n')

        registro = self.__registro_transporte_publico

        if(self.__registro_transporte_publico==[]):
            print('El vehículo de patente ', self.__patente, ' no pertenece al Registro Nacional de Servicios de Transporte Público de Pasajeros ni al Registro Nacional de Servicios de Transporte Remunerado de Escolares\n')
        else:
            print('Placa Patente:', registro[0])
            print('Fecha de Entrada RNT:',registro[1])
            print('Tipo de Servicio:',registro[2])
            print('Capacidad:',registro[3])
            print('Estado de Vehiculo:' ,registro[4])
            print('Region:',registro[5])
            print('Año de fabricacion: ',registro[6])
            print('Cinturon de seguridad obligatorio: ',registro[7])
            print('Antigüedad del Vehiculo: ',registro[8])
            print('Marca:',registro[9])
            print('Modelo:',registro[10])
            print('Folio Servicio:',registro[11])
            print('Flota Asociada al Servicio:',registro[12])
            print('Nombre del Responsable del Servicio:',registro[13])
            print('Estado del Servicio:',registro[14])

        return self.__registro_transporte_publico

    def setRegistroTransportePublico(self, registroTransportePublico):
        self.__registro_transporte_publico = registroTransportePublico

    def getInfraccionesVespucioNorte(self):

        if(self.__infracciones_vespucio_norte==[]):
            print('El vehiculo de patente ', self.__patente, 'no tiene infracciones en Vespucio Norte.')

        else:
            for detalle in self.__infracciones_vespucio_norte:
                print('\n')
                print('Numero boleta: ', detalle[0])
                print('Pago total: $', detalle[1])

                fecha_hora = detalle[2].split(' ')
                print('Fecha: ', fecha_hora[0])
                print('Hora: ', fecha_hora[1])

        return self.__infracciones_vespucio_norte

    def setInfraccionesVespucioNorte(self, infraccionesVespucioNorte):

        self.__infracciones_vespucio_norte = infraccionesVespucioNorte

    def getInfraccionesVespucioSur(self):

        if(self.__infracciones_vespucio_sur==[]):
            print('El vehiculo de patente', self.__patente, 'no tiene infracciones en Vespucio Sur.')
        else:

            print('Infracciones Vespucio Sur: \n')

            for detalle in self.__infracciones_vespucio_sur:

                print('Fecha de infraccion: ',detalle[0])
                print('Categoria de infraccion: ', detalle[1])
                print('Estado de infraccion: ', detalle[2])

        return self.__infracciones_vespucio_sur

    def setInfraccionesVespucioSur(self, infraccionesVespucioSur):

        self.__infracciones_vespucio_sur = infraccionesVespucioSur

    def getInfraccionesAutopase(self):

        print('\nAutopase\n')

        if(self.__infracciones_autopase[0]==[]):
            print('El vehiculo de patente', self.__patente, 'no tiene infracciones no facturadas en Autopase\n')

        else:
            print('Infracciones no facturadas: \n')
            for infraccion_no_facturada in self.__infracciones_autopase[0]:
                print('Rut: ', infraccion_no_facturada[0])
                print('Patente: ', infraccion_no_facturada[1])
                print('Fecha: ', infraccion_no_facturada[2])
                print('Total: ', infraccion_no_facturada[3], '\n')

        if(self.__infracciones_autopase[1]==[]):
            print('El vehiculo de patente', self.__patente, 'no tiene infracciones facturadas en Autopase\n')

        else:
            print('Infracciones facturadas: \n')
            for infraccion_facturada in self.__infracciones_autopase[1]:
                print('Rut: ', infraccion_facturada[0])
                print('Patente: ', infraccion_facturada[1])
                print('Numero de boleta: ', infraccion_facturada[2])
                print('Cargo del mes: ', infraccion_facturada[3], '\n')

        if(self.__infracciones_autopase[2]==[]):
            print('El vehiculo de patente', self.__patente, 'no tiene detalles de infracciones en Autopase\n')

        else:
            print('Detalles de boleta: \n')

            numero_boleta = ''
            condicion_boleta = True

            for detalle_infraccion in self.__infracciones_autopase[2]:

                if(condicion_boleta==True):
                    numero_boleta = detalle_infraccion[0]
                    condicion_boleta=False
                    pass

                else:
                    numero_boleta_aux = detalle_infraccion[0]
                    if(numero_boleta == numero_boleta_aux):
                        pass
                    else:
                        print('Siguiente boleta...\n')
                        condicion_boleta=True

                print('Numero de boleta: ', detalle_infraccion[0])
                print('Patente: ', detalle_infraccion[1])
                print('Fecha: ', detalle_infraccion[2])
                print('Hora: ', detalle_infraccion[3], '\n')

        return self.__infracciones_autopase

    def setInfraccionesAutopase(self, infraccionesAutopase):
        self.__infracciones_autopase = infraccionesAutopase

    def getInfraccionesCostaneraNorte(self):

        infracciones_Costanera_Norte = self.__infracciones_costanera_norte

        if(infracciones_Costanera_Norte==[[],[],[]]):
           print('El vehiculo de patente', self.__patente, 'no presenta infracciones en Costanera Norte')

        else:
            print('Infracciones en Costanera Norte \n')
            for detalles_cn in range(0, len(infracciones_Costanera_Norte[0])):
                print('Fecha: ', infracciones_Costanera_Norte[0][detalles_cn])
                print('Categoria: ', infracciones_Costanera_Norte[1][detalles_cn])
                print('Estado: ', infracciones_Costanera_Norte[2][detalles_cn], '\n')

        return self.__infracciones_costanera_norte

    def setInfraccionesCostaneraNorte(self, infraccionesCostaneraNorte):
        self.__infracciones_costanera_norte = infraccionesCostaneraNorte

    def getInfraccionesNororiente(self):

        infracciones_Nororiente = self.__infracciones_nororiente

        if(infracciones_Nororiente==[[],[],[],[],[],[]]):
            print('El vehiculo de patente ', self.__patente, 'no tiene infracciones en Nororiente')

        else:
            print('\nInfracciones Nororiente: \n')
            for i in range(0, len(infracciones_Nororiente[0])):
                print('Convenio: ', infracciones_Nororiente[0][i])
                print('Documento: ', infracciones_Nororiente[1][i])
                print('Deuda vencida: ', infracciones_Nororiente[2][i])
                print('Deuda por vencer: ', infracciones_Nororiente[3][i])
                print('Total Deuda: ', infracciones_Nororiente[4][i], '\n')

            print('Total a pagar: ', infracciones_Nororiente[5][0])

        return self.__infracciones_nororiente

    def setInfraccionesNororiente(self, infraccionesNororiente):
        self.__infracciones_nororiente = infraccionesNororiente

    def getInfraccionesViasExclusivas(self):

        if(self.__infracciones_vias_exclusivas==[]):
            print('El vehiculo de patente ', self.__patente, 'no registra infracciones en Vias Exclusivas')
        else:
            pass
            #falta un for en caso de que recorra una lista con datos
        return self.__infracciones_vias_exclusivas

    def setInfraccionesViasExclusivas(self, infraccionesViasExclusivas):

        if((isinstance(infraccionesViasExclusivas, list))==True):
            self.__infracciones_vias_exclusivas = infraccionesViasExclusivas
        
        else:
            self.__infracciones_vias_exclusivas = []
    
    def getInfraccionesLampaSantiago(self):

        if(self.__infracciones_lampa_santiago==[]):
            print('El vehiculo de patente ', self.__patente, 'no registra infracciones en Lampa-Santiago')


        return self.__infracciones_lampa_santiago

    def setInfraccionesLampaSantiago(self, infraccionesLampaSantiago):
        self.__infracciones_lampa_santiago = infraccionesLampaSantiago

    def getInfraccionesDelSol(self):
        return self.__infracciones_del_sol

    def setInfraccionesDelSol(self, infraccionesDelSol):
        self.__infracciones_del_sol = infraccionesDelSol

    def getInfraccionesRutaMaipo(self):

        if(self.__infracciones_ruta_maipo[0]==[]):
            print('El vehiculo de patente ', self.__patente, 'no tiene registros de tránsitos de más de 30 días no facturados')
        else:
            print('Tiene tránsitos de más de 30 días no facturados')

        if(self.__infracciones_ruta_maipo[1]==[]):
            print('El vehiculo de patente, ', self.__patente, 'no tiene registros de tránsitos de más de 30 días facturados')

        else:
            print('Tien trásnsitos de más de 30 días facturados.')

        return self.__infracciones_ruta_maipo

    def setInfraccionesRutaMaipo(self, infraccionesRutaMaipo):
        self.__infracciones_ruta_maipo = infraccionesRutaMaipo

    def getInfraccionesLosLibertadores(self):
        return self.__infracciones_los_libertadores

    def setInfraccionesLosLibertadores(self, infraccionesLosLibertadores):
        self.__infracciones_los_libertadores = infraccionesLosLibertadores

    def getInfraccionesElPacifico(self):
        print(self.__infracciones_el_pacifico)
        return self.__infracciones_el_pacifico

    def setInfraccionesElPacifico(self, infraccionesElPacifico):
        self.__infracciones_el_pacifico = infraccionesElPacifico

#separar los datos
class TransportePublico:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def resultado(self):
        cookies = {
            'ASP.NET_SessionId': '0sla4exrmtiuesonv2pvmhqf',
            '_ga': 'GA1.2.1806332623.1637258376',
            '_gid': 'GA1.2.1544212551.1637804958',    
        }

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'Origin': 'http://apps.mtt.cl',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://apps.mtt.cl/consultaweb/',
            'Accept-Language': 'es-ES,es;q=0.9',
            }


        data = {
        '__VIEWSTATE': '/wEPDwUKMTc0MTY3NTE3MQ9kFgJmD2QWAgIDD2QWAgIBD2QWAgIBD2QWAgIBD2QWAgIFDw8WBB4EVGV4dAWFAjxpbWcgc3JjPSdodHRwOi8vYXBwcy5tdHQuY2wvd3d3L2ltZ3MvcGxhY2FfbHVwYS5wbmcnIC8+PGJyIC8+PHN0cm9uZz5FbCB2ZWjDrWN1bG8gZW4gY29uc3VsdGEgbm8gcGVydGVuZWNlIGFsIFJlZ2lzdHJvIE5hY2lvbmFsIGRlIFNlcnZpY2lvcyBkZSBUcmFuc3BvcnRlIFDDumJsaWNvIGRlIFBhc2FqZXJvcyBuaSBhbCBSZWdpc3RybyBOYWNpb25hbCBkZSBTZXJ2aWNpb3MgZGUgVHJhbnNwb3J0ZSBSZW11bmVyYWRvIGRlIEVzY29sYXJlczwvc3Ryb25nPh4HVmlzaWJsZWdkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUgY3RsMDAkTWFpbkNvbnRlbnQkaW1nQnRuQ29uc3VsdGHi2oH8N/l6WPK18/lBTVqKUyDl6cjAz/FPHWG90t6r+g==',
        '__VIEWSTATEGENERATOR': '522DF3F1',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__EVENTVALIDATION': '/wEdAASTj8RE1t+b0rmqH5lXzbQHIKnzPnVFgXAZ20CcrnWXzeHx18AZ0epHV1po9+JEZeBnTMb45aJIIeXNdhdxmB5y16hbBVTD9sA1Df7Tv3JDHwkxYnhJbQWRrG6M43r0Y20=',
        'ctl00$MainContent$ppu': self.__patenteVehiculo,
        'ctl00$MainContent$btn_buscar': 'Buscar'
        }

        try:
            response = requests.post('http://apps.mtt.cl/consultaweb/', headers=headers, cookies=cookies, data=data, verify=False)

            soup = BeautifulSoup(response.text, 'html.parser')
            table=soup.find_all("table", id='MainContent_tablaDatos')
            registro_aux = ''
            for palabra in table:

                try:
                    registro_aux = registro_aux+palabra.text.replace('\n', ' ')
                except:
                    registro_aux = registro_aux+palabra.text

            registro_array = registro_aux.split('   ')

            for i in registro_array:
                if((i.isupper()==True) or (i=='') or (i=='  ')):
                    registro_array.remove(i)

            registro_array.remove(registro_array[len(registro_array)-1])
            registro_array.remove(registro_array[len(registro_array)-1])

            registro_array_final = []

            registro_array_final.append(registro_array[0].split(' ')[2])
            registro_array_final.append(registro_array[1].split(' ')[4])

            registro_indice_2 = registro_array[2].split(' ')
            cont_bucle = 0
            while(cont_bucle<3):
                registro_indice_2.remove(registro_indice_2[0])
                cont_bucle+=1

            tipo_transporte = ''
            for i in registro_indice_2:
                tipo_transporte = tipo_transporte+' '+i
            registro_array_final.append(tipo_transporte.strip())

            registro_array_final.append(registro_array[3].split(' ')[1])
            registro_array_final.append(registro_array[4].split(' ')[3])
            registro_array_final.append(registro_array[5].split(' ')[1])
            registro_array_final.append(registro_array[6].split(' ')[3])
            registro_array_final.append(registro_array[7].split(' ')[4])
            registro_array_final.append(registro_array[8].split(' ')[3])

            registro_indice_9 = registro_array[9].split(' ')
            registro_indice_9.remove(registro_indice_9[0])

            marca_transporte = ''
            for i in registro_indice_9:
                marca_transporte = marca_transporte+' '+i
            registro_array_final.append(marca_transporte.strip())

            registro_indice_10 = registro_array[10].split(' ')
            registro_indice_10.remove(registro_indice_10[0])

            modelo_transporte = ''
            for i in registro_indice_10:
                modelo_transporte=modelo_transporte+' '+i
            registro_array_final.append(modelo_transporte.strip())

            registro_array_final.append(registro_array[11].split(' ')[2])
            registro_array_final.append(registro_array[12].split(' ')[4])

            registro_indice_13 = registro_array[13].split(' ')
            cont_bucle = 0
            while(cont_bucle<5):
                registro_indice_13.remove(registro_indice_13[0])
                cont_bucle+=1

            nombre_responsable = ''
            for i in registro_indice_13:
                nombre_responsable=nombre_responsable+' '+i
            registro_array_final.append(nombre_responsable.strip())

            registro_array_final.append(registro_array[14].split(' ')[3])

            return registro_array_final
        except:
            return []


#ordenar los datos
class RevisionTecnica:
    def __init__(self, patenteVehiculo, API_KEY, page_url):
        self.__patenteVehiculo = patenteVehiculo
        self.API_KEY = API_KEY
        self.page_url = page_url

    def resultado(self, API_KEY, page_url):
        #soup = BeautifulSoup(driver.page_source, 'html.parser')
        #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
        sitekey = '6LctMP8SAAAAANBvpGMjkMm5bBJ7TY-7X9UuGAaq'
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

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://www.prt.cl',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://www.prt.cl/Paginas/RevisionTecnica.aspx',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': 'Iq601Ta4fJGLhgkDHTJBOkqcUPBHIqu88qsauJlotK5C8nJnoJv+6DsYXNn9YYkpNoLKf8k7tul7AD420ptaKveliplDcWaOESiUKOT64GthfNBU+GlFjX5GhXW4W0aUKbC2DVO3MnB0lPXjG+WdlUuWtK6NqAJr5+CRbsVaihh3L6OueqVEZkrcFr0ytvgtBi6gATZgmLcNAMVDnFX8epyXQKQtfcxP8jOr6j/4rnUju2iHsuVUAmWBO+QwZpo2sFZkL/cFg/vbjdR6Wr04fQ3hbAaAKNrpgPdY/9T2uB8DD4scFHhRH2IwgMYFgsy9tUANEMLG4sKLcQuX3+3NdBc4YHYFIf7aTur0eQT68C9Z9xocQj2frfsIWXAxXo9g6PTIawOYdkezOf7+rq4yIHIsRQActtxvLax2u/QtYTYIlQ5o26YnaVW7bZjUsoJ/iXIdmENbTkm/94eN8w/kB+JdDrGZRS8mi6gmgfx3RAzOhnFC6gUQu6+z0brWvIXnf03Mcg==',
            '__VIEWSTATEGENERATOR': '4F717C3B',
            '__EVENTVALIDATION': 'qxLAMNT9rltV6gVzxoPJtyrO5UOBnCx/6RiNSQl2d9NSqeox2pP+gXMGDu4Vs0V3mKmV+MhiWu7mZ3rLYHwpxyaWEXdTs6GwVbqEeSlIeJ2jmyX2j7IFVeZz+p5VK8mrGnU05qAOlnGuMibqG2Mj71Jw2w7tKb3NkWBu5U9J/O5AMJudnwQ35rmWpc+wp7VPiy0T9bdAFa5zvH4n9HyJNRBtMpLOzt3uUTb/NHNL9QP4DtzTIL/GhOFlavFP4ZFOYZjQ1g==',
            'ctl00$ContentPlaceHolder1$hddPPU': '',
            'ctl00$ContentPlaceHolder1$hddPRT': '',
            'ctl00$ContentPlaceHolder1$hddDIRPRT': '',
            'ctl00$ContentPlaceHolder1$patenteInput': self.__patenteVehiculo,
            'ctl00$ContentPlaceHolder1$buscar.x': '36',
            'ctl00$ContentPlaceHolder1$buscar.y': '23',
            'g-recaptcha-response': form_tokon,
            'ctl00$ContentPlaceHolder1$MyAccordion_AccordionExtender_ClientState': '0'
        }

        response = requests.post('http://www.prt.cl/Paginas/RevisionTecnica.aspx', headers=headers, data=data, verify=False)

        soup = BeautifulSoup(response.text, 'html.parser')
        datoVeiculos = []
        infoRevision_Fecha, infoRevision_CodPlanta,infoRevision_Planta,infoRevision_NroCertificado,infoRevision_FechaVec, infoRevision_Estado= [],[],[],[],[],[]
        infoVeiculo = soup.find_all('span', id='ContentPlaceHolder1_lblDatosVehiculo')
        infoRevision = soup.find_all('span', id='ContentPlaceHolder1_lblHistorico')
        for i in infoVeiculo:
            for z in i.find_all('span'):
                datoVeiculos.append(z.text)

        for i in infoRevision:
            for z in i.find_all('td')[0::6]:
                infoRevision_Fecha.append(z.text)

            for z in i.find_all('td')[1::6]:
                infoRevision_CodPlanta.append(z.text)

            for z in i.find_all('td')[2::6]:
                infoRevision_Planta.append(z.text)

            for z in i.find_all('td')[3::6]:
                infoRevision_NroCertificado.append(z.text)

            for z in i.find_all('td')[4::6]:
                infoRevision_FechaVec.append(z.text)

            for z in i.find_all('td')[5::6]:
                infoRevision_Estado.append(z.text)

        return datoVeiculos, infoRevision_Fecha, infoRevision_CodPlanta,infoRevision_Planta,infoRevision_NroCertificado,infoRevision_FechaVec, infoRevision_Estado

#no se entiende lo que retorna
class EncargoRobo:
    def __init__(self, patenteVehiculo, API_KEY, page_url):
        self.__patenteVehiculo = patenteVehiculo
        self.API_KEY = API_KEY
        self.page_url = page_url

    def Solver(self, driver, API_KEY, page_url):
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

    def resultado(self, API_KEY, page_url):

        if __name__ == '__main__':
            driver = webdriver.Chrome()
            driver.get(page_url)
            driver.find_element_by_xpath('//*[@id="txt_placa_patente"]').send_keys(self.__patenteVehiculo)
            self.Solver(driver, API_KEY, page_url)
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
            a = [] 
            b = [] 
            c = [] 
            for i in content:
                for z in i.find_all('label', id='lbl_Vehiculo'):
                    mensaje=z.text
                    a.append(z.text)
                for z in i.find_all('th'):
                    b.append(z.text)
                for z in i.find_all('td', align='left'):
                    c.append(z.text)
            #driver.close()
        return a,b,c

class VespucioNorte:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):

        infraccionesVespucioNorte = []

        cookies = {
            '_ga': 'GA1.2.1222882760.1637102421',
            '_gid': 'GA1.2.75323150.1638659755',
            'ASP.NET_SessionId': '1md502mphs2isqh4mvztxoks',
            '__RequestVerificationToken': 'FEleRsgHGbuM1DCVKdY59FpL9OOnRnk2j_nsfRNjMw2rZJc68ASJWziBeDr6U5L46fHaqVq3XTz-tVIU6xx60FrCCrsSlb-QpObZQps1Jdg1',
            '_gat': '1',
        }

        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://www.vespucionorte.cl',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.vespucionorte.cl/Home/CirculasteSinTag',
            'Accept-Language': 'es-ES,es;q=0.9',
        }

        data = {
            'patente': self.__patenteVehiculo
        }

        try:
            lista=[]
            lista2=[]

            dict={}
            response = requests.post('https://www.vespucionorte.cl/Ajax/GetInfractores', headers=headers, cookies=cookies, data=data)

            response=json.loads(response.text)
            for i in response['tablaTransitosFact']:
                lista.append(str(i['numeroBoleta']).strip('00000000'))
                lista2.append(i['totalBoleta'])
            for i in lista:
                dict[i]=[]
                dict[i].append(str(lista2[lista.index(i)]).strip('0000000000000'))
            for i in response['tablaDetalleTransito']:
                dict[str(i['numeroBoleta']).strip('00000000')].append(i['fechaTransito']+' '+i['horaTransito'])

            for key in dict:
                numb_boleta = key
                total_boleta = dict[key][0]
                fecha_hora = dict[key][1]
                infraccionesVespucioNorte.append([numb_boleta, total_boleta, fecha_hora])

            return infraccionesVespucioNorte

        except:
            return []

class VespucioSur:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
        page_url ='https://web.costaneranorte.cl/circulaste-sin-tag/consultar-transitos-sin-tag/'

        def Solver(url):
            #soup = BeautifulSoup(driver.page_source, 'html.parser') 
            #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
            sitekey = '6Lfchk8UAAAAAMPIv-l8SB4CfG385t6a5UfR08vt'
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
            return form_tokon

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '"Opera GX";v="81", " Not;A Brand";v="99", "Chromium";v="95"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'https://oficina.vespuciosur.cl',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'object',
            'Referer': 'https://oficina.vespuciosur.cl/tags/VerificaInfraccion.aspx',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {
            '__VIEWSTATE': '/wEPDwUJODk5Njg1MjM4D2QWAgIBD2QWAgIDDzwrAA0AZBgBBQlHcmlkVmlldzEPZ2QDiTKwJd6tbi3bDalwny11bDci1w==',
            '__VIEWSTATEGENERATOR': '99B6AABA',
            '__EVENTVALIDATION': '/wEWAwKpo6u1BQKeluy/BgKM54rGBrNpLVRtfVH7j2QrJsFQY7Ss+rwV',
            'txtpatente': self.__patenteVehiculo,
            'g-recaptcha-response': f'{str(Solver(page_url))}',
            'Button1': 'Consultar'
        }

        response = requests.post('https://oficina.vespuciosur.cl/tags/VerificaInfraccion.aspx', headers=headers, data=data)
        print(response.text, file=open("costaneraSur.html", "w"))
        soup = BeautifulSoup(response.text, 'html.parser')
        tabla = soup.find_all('table')

        fechas_infracciones = []
        categoria_infracciones = []
        estado_infracciones = []
        contador_VespucioSur = 0

        infraccionesVespucioSur = []

        for detalle in tabla:
            for fecha in detalle.find_all('td')[0::3]:
                fechas_infracciones.append(fecha.text)
                contador_VespucioSur+=1

            for categoria in detalle.find_all('td')[1::3]:
                categoria_infracciones.append(categoria.text)

            for estado in detalle.find_all('td')[2::3]:
                estado_infracciones.append(estado.text)

        for i in range(0, contador_VespucioSur):
            infraccion = []
            infraccion.append(fechas_infracciones[i])
            infraccion.append(categoria_infracciones[i])
            infraccion.append(estado_infracciones[i])
            infraccionesVespucioSur.append(infraccion)

        return infraccionesVespucioSur

class Autopase:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
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
        driver.find_element_by_xpath('//*[@id="sInput"]').send_keys(self.__patenteVehiculo)
        Solver(driver,page_url)
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

class CostaneraNorte:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
        page_url ='https://web.costaneranorte.cl/circulaste-sin-tag/consultar-transitos-sin-tag/'

        def Solver(url):
            #soup = BeautifulSoup(driver.page_source, 'html.parser') 
            #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
            sitekey = '6Lfchk8UAAAAAMPIv-l8SB4CfG385t6a5UfR08vt'
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
            print("captcha solved")


        link='https://www.costaneranorte.cl/infraccion/VerificaInfraccion.aspx'
        #patente
        driver=webdriver.Chrome()
        driver.get(link)
        driver.find_element_by_xpath('//*[@id="txtpatente"]').send_keys(self.__patenteVehiculo)
        Solver(link)
        driver.find_element_by_xpath('//*[@id="Button1"]').click()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        fechas,categorias,estados=[],[],[]
        tabla_CostaneraNorte = soup.find_all('table')

        for detalles_CostaneraNorte in tabla_CostaneraNorte:
            for fecha_actual in detalles_CostaneraNorte.find_all('td')[0::3]:
                fechas.append(fecha_actual.text)
            for categoria_actual in detalles_CostaneraNorte.find_all('td')[1::3]:
                categorias.append(categoria_actual.text)
            for estado_actual in detalles_CostaneraNorte.find_all('td')[2::3]:
                estados.append(estado_actual.text)

        return [fechas, categorias, estados]

class Nororiente:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):

        API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
        APIKEY_2CAPTCHA="1abc234de56fab7c89012d34e56fa7b8"
        api_key = os.getenv(APIKEY_2CAPTCHA, API_KEY)
        solver= TwoCaptcha(api_key)
        sitekey='6LeGGUsUAAAAAGA45yjoGkJ__EKeRqa-KipeYSW-'
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--lang=es")
        driver = getDriverNororiente(name_path='chromedriver.exe', options=options, verbose=1, debug=True)
        driver.get('https://www.costaneranorte.cl/LoginNoFrecuente.html')
        driver.find_element_by_xpath('//*[@id="PATENTE"]').send_keys(self.__patenteVehiculo)
        driver.find_element_by_xpath('/html/body/div/section/div/div[2]/form/a').click()
        driver.find_element_by_xpath('/html/body/div/section/div/div[2]/form/p[2]/a').click()
        #print(str(driver.current_url))
        try:
            result=solver.recaptcha(sitekey=sitekey,
                                    url=driver.current_url)
        except:
            print('error')
        else:
            result=str(result.get('code'))
        driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{result}";')
        driver.find_element_by_xpath('/html/body/div[1]/section/div/form/div[2]/a').click()
        soup=BeautifulSoup(driver.page_source,'html.parser')
        table=soup.find_all('table', id='TablaConvenioDeuda')
        convenios, documentos, deudas_vencidas, deudas_por_vencer, total_deudas, importes_a_pagar = [],[],[],[],[],[]
        for i in table:
            for convenio in i.find_all('td')[0::6]:
                if(convenio.text=='\xa0'):
                    pass
                else:
                    convenios.append(convenio.text)
            for documento in i.find_all('td')[1::6]:
                if(documento.text=='\xa0'):
                    pass
                else:
                    documentos.append(documento.text)
            for deuda_vencida in i.find_all('td')[2::6]:
                if(deuda_vencida.text=='\xa0'):
                    pass
                else:
                    deudas_vencidas.append(deuda_vencida.text)
            for deuda_por_vencer in i.find_all('td')[3::6]:
                if(deuda_por_vencer.text=='\xa0' or not(any(char.isdigit() for char in deuda_por_vencer.text))):
                    pass
                else:
                    deudas_por_vencer.append(deuda_por_vencer.text)
            for total_deuda in i.find_all('td')[4::6]:
                if(total_deuda.text=='\xa0'):
                    pass
                else:
                    total_deudas.append(total_deuda.text)
            for importe_a_pagar in i.find_all('td')[5::6]:
                if(importe_a_pagar.text=='\n\n'):
                    pass
                else:
                    importes_a_pagar.append(importe_a_pagar.text)

        return [convenios, documentos, deudas_vencidas, deudas_por_vencer, total_deudas, importes_a_pagar]            

#no hay un "caso" donde exista una patente con registros
class ViasExclusivas:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        driver = webdriver.Chrome()
        driver.get('http://rrvv.fiscalizacion.cl')
        driver.find_element_by_xpath('//*[@id="patente"]').send_keys(self.__patenteVehiculo)
        idf=driver.find_element_by_xpath('//*[@id="captcha_widget"]/div[3]/img')
        img= idf.get_attribute('src')
        code = Functions().Solver(img,'Vias_exclusivas')
        driver.find_element_by_xpath('//*[@id="captcha_response"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="bBuscarPatente"]').click()
        time.sleep(5)

        #pendiente, porque no retorna una tabla al parecer

        try:
            return driver.find_element_by_xpath('/html/body/div[1]/div/font/div[3]/div[2]/div[2]/form/div[1]').text
        except:
            return []

#no lleva a una parte para poner patente
class LampaSantiago:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        driver = webdriver.Chrome()
        #patente,dv=patente.split('-')[0],patente.split('-')[1]
        driver.get('https://www.autoviasantiagolampa.cl/oficina-virtual/consultar-transito-sin-tag')
        idf=driver.find_element_by_xpath('//*[@id="imagen_captcha"]')
        img= idf.get_attribute('src')
        result=Functions().Solver(img,'lampa_santiago')
        driver.find_element_by_xpath('//*[@id="solicitar_contrasena_plate"]').send_keys(self.__patenteVehiculo)
        driver.find_element_by_xpath('//*[@id="solicitar_contrasena_plate_dv"]').send_keys(dv)
        driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(result)
        driver.find_element_by_xpath('//*[@id="transitos_sin_sesion_form"]/div[3]/div/button').click()
        table=driver.find_element_by_xpath('/html/body/div/div[3]').text
        data=[]
        if ('usted no posee' not in table):
            soup=BeautifulSoup(driver.page_source,'html.parser')
            rows=((soup.find('table',class_='table table-bordered dataTable no-footer',role='grid')).find('tbody')).find_all('tr')
            for row in rows:
                cols=row.find_all('th')
                cols=[ele.text for ele in cols]
                data.append([ele for ele in cols if ele])

            print(data)
        return data

#separar datos
class DelSol:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        driver = webdriver.Chrome()
        primary_link = 'http://www.autopistadelsol.cl/pago/valida'
        link1 = 'https://boton.unired.cl/BotonPago/IniciaFlujoOnline?u='
        Dato1={'patente':self.__patenteVehiculo}
        response=requests.post(primary_link,data=Dato1)
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
        lista=[]
        for i in cajaDeuda:
            lista.append(i.text)
        print(lista)
        return lista

#separar datos
class RutaMaipo:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        try:
            driver = webdriver.Chrome()
            driver.get('https://www.rutamaipo.cl/taginterurbano/pasaste-sin-tag')
            driver.find_element_by_xpath('//*[@id="patente"]').send_keys(self.__patenteVehiculo)
            driver.find_element_by_xpath('//*[@id="consultar_sintag"]').click()
            time.sleep(2)
            try:
                driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div/div/button').click()
            except:
                pass 
            table1=driver.find_element_by_xpath('/html/body/div/main/div[1]/section/div[2]/div/form').text
            table2=driver.find_element_by_xpath('/html/body/div/main/div[1]/section/div[2]/div/div[2]').text

            return [[table1],[table2]]

        except:
            return [[],[]]
        

#separar datos
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
        lista=[]
        for i in cajaDeuda:
            lista.append(i.text)
        return lista

#separar datos
class ElPacifico:
    def __init__(self, patenteVehiculo):
        self.__patenteVehiculo = patenteVehiculo

    def getInfracciones(self):
        driver = webdriver.Chrome()
        primary_link = 'http://www.rutasdelpacifico.cl/pago/valida'
        link1 = 'https://boton.unired.cl/BotonPago/IniciaFlujoOnline?u='
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
        lista=[]
        for i in cajaDeuda:
            lista.append(i.text)
        return lista

auto = Vehiculo('PHSS63')

auto.setRegistroTransportePublico(TransportePublico(auto.getPatente()).resultado())
auto.getRegistroTransportePublico()

#auto.setInfraccionesViasExclusivas(ViasExclusivas(auto.getPatente()).getInfracciones())
#auto.getInfraccionesViasExclusivas()

#auto.setInfraccionesLampaSantiago(LampaSantiago(auto.getPatente()).getInfracciones())
#auto.getInfraccionesLampaSantiago()

#auto.setInfraccionesDelSol(DelSol(auto.getPatente()).getInfracciones())
#auto.getInfraccionesDelSol()

#auto.setInfraccionesElPacifico(ElPacifico(auto.getPatente()).getInfracciones())
#auto.getInfraccionesElPacifico()

#auto.setInfraccionesRutaMaipo(RutaMaipo(auto.getPatente()).getInfracciones())
#print(auto.getInfraccionesRutaMaipo())



# Revision_tecnica1 = RevisionTecnica(auto.getPatente(), "2a2b5480b431e8976a70ebbf3d38f550",'http://www.prt.cl/Paginas/RevisionTecnica.aspx')
# datoVeiculos, infoRevision_Fecha, infoRevision_CodPlanta,infoRevision_Planta,infoRevision_NroCertificado,infoRevision_FechaVec, infoRevision_Estado = Revision_tecnica1.resultado("2a2b5480b431e8976a70ebbf3d38f550",'http://www.prt.cl/Paginas/RevisionTecnica.aspx')
# print(datoVeiculos, infoRevision_Fecha, infoRevision_CodPlanta,infoRevision_Planta,infoRevision_NroCertificado,infoRevision_FechaVec, infoRevision_Estado)


# Encargo_Robo1 = EncargoRobo(auto.getPatente(), "2a2b5480b431e8976a70ebbf3d38f550",'https://www.autoseguro.gob.cl')
# a,b,c = Encargo_Robo1.resultado("2a2b5480b431e8976a70ebbf3d38f550",'https://www.autoseguro.gob.cl')
# print(a,b,c)

