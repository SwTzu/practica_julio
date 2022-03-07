import requests,json

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

if __name__ == '__main__':
    registro_vespucio_norte = VespucioNorte('PHSS63')
    print(registro_vespucio_norte.getInfracciones())