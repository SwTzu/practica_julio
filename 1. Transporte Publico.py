import requests
from bs4 import BeautifulSoup

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

#patente con info: 'KXPS43'
#patente sin info: 'HKCB50'

if __name__ == '__main__':
    registro_transporte_publico = TransportePublico('KXPS43')
    print(registro_transporte_publico.resultado())