import json, time
from pip._vendor import requests
from bs4 import BeautifulSoup

lista_patentes=['XF7651', 'JLWF50', 'CZCX24', 'TC2442', 'CPLH89', 'LTZ011', 'HWLF62', 'CBKV63', 'LYCH67', 'HKTW30', 'DFBG70', 'BI0875', 'LDY042', 'FTD049', 'WF5936', 'CFSC19', 'HPKP41', 'VE7020', 'BWDR40', 'BFDL17', 'PS7532', 'BXDY16', 'BBRL36', 'BPRV37', 'ZW9270', 'YH8274', 'DSBX73', 'SD4437', 'VD5486', 'TJ2248', 'ZD4101', 'GPR092', 'LFB012', 'YW4448', 'FP7732', 'DJLR32', 'SV7591', 'LG7679', 'KSWB78', 'HHYW27', 'WL0100', 'GYD099', 'KK8693', 'JPYK29', 'KXPP51', 'GLKD79', 'UY6416', 'ED6761', 'JFKK59', 'WG2532', 'KW7915', 'BGD021', 'FKRR71', 'JCBV97', 'JXD084', 'GY8298', 'KRLC41', 'YR0403', 'BWSR23', 'YG2586', 'XC4499', 'DYJP22', 'GTRR68', 'CGFY25', 'ZB7546', 'FXKK99', 'LRCW17', 'KJWK97', 'JPKS44', 'DHSL81', 'BHZK99', 'UE0649', 'FSHR31', 'LHGH69', 'LSXB75', 'HYJ025', 'GGCF74', 'PG5945', 'KGZB62', 'HRTB99', 'DHV013', 'GPF070', 'GCZK17', 'SU9716', 'CBYB72', 'CWWR43', 'LKDZ91', 'CKVS68', 'LV2755', 'GGGB47', 'EE8342', 'DZDZ48', 'HKP045', 'LR2813', 'JRRJ13', 'WB3923', 'DLX035', 'KFPR52', 'BD6139', 'LXPX30', 'DPF068', 'GGFZ69', 'CRLT12', 'CFVB55', 'JXBW26', 'HDJY17', 'JDYG86', 'FHRF34', 'BZKK47', 'KTCH36', 'KXJD90', 'KGT040', 'DJGH61', 'WK0220', 'LPJH14', 'CPTH49', 'WK0637', 'CCJC40', 'WK7854', 'FLSS16', 'WB3994', 'WW4000', 'SD2996', 'LLSX48', 'FDK014', 'HPDW71', 'KVLY79', 'HJHT22', 'FYJJ29', 'LCCY83', 'ZX1227', 'WL4499', 'DBVH42', 'JWVT67', 'WB7258', 'DYCF71', 'NR0364', 'FBGG46', 'CVPP53', 'GXYT43', 'BVKH13', 'CYXZ34', 'KK8337', 'GDJK17', 'VR9229', 'NF2417', 'DX7389', 'FPLX76', 'RT2943', 'ZY4092', 'HKCB50', 'CGXZ27', 'VV9606', 'YT5012', 'XG5973', 'KGHX97', 'YV7398', 'FKGJ96', 'KKZJ39', 'DBTZ25', 'HKTV27', 'CCGH83', 'GYS092', 'UT8872', 'DDBD17', 'DSZG88', 'DBDK99', 'KTHV37', 'CPRK17', 'HTVT12', 'KS0852', 'CKGK80', 'QL0885', 'LS2484', 'KWSP28', 'JFKW46', 'WK9995', 'LLPX65', 'UN0384', 'DPJG58', 'LHDB85', 'LTPF27', 'KGH047', 'FDRG49', 'RW5289', 'BCR031', 'LSWW93', 'GSZB46', 'LTVJ41', 'BXJB48', 'HHSL37', 'JD0509', 'HYBP90', 'UG6239', 'BXSP64', 'PC6312', 'KT1046', 'BSTL76', 'KTPF65', 'CLZK25', 'KCPW61', 'RP8576', 'VZ6997', 'KLBJ58', 'WY4231', 'KH4878', 'DVGY65', 'LXBL35', 'BGS065', 'JXFL75', 'BYYL42', 'JCLL52', 'KZTS68', 'DZZX64', 'XF4131', 'FSKZ53', 'NE9952', 'JWTZ94', 'JYXJ49', 'YT2598', 'KRTG35', 'JKHV11', 'WZ5936', 'DXZZ71', 'FBTD79', 'ZY4313', 'JWGD90', 'JHTP61', 'XD1946', 'UH7384', 'LSTS13', 'CTWX77', 'FLBS46', 'LLZD13', 'JZTZ44', 'HJFT18', 'GBY078', 'TG5204', 'KTRY76', 'GCFH23', 'NC5093', 'WU9402', 'CTVF29', 'RR1601', 'GRZ045', 'KTDP50', 'DN5078', 'LFZ060', 'GWHP33', 'BCJP46', 'CJZZ41', 'SX5531', 'ZL3706', 'WE9030', 'CSJC87', 'HJZ073', 'OW0214', 'HWFL68', 'HFBF78', 'LHKW76', 'GXDX66', 'DJZJ56', 'TJ2673', 'WE9401', 'GN8893', 'VH8584', 'FVTT87', 'BFLH77', 'GZ7035', 'FLC060', 'LFRF19', 'DS9370', 'DD5495', 'JWSS57', 'XP0825', 'DPC062', 'JRW071', 'LS8370', 'LBGB61', 'NV3646', 'LVYZ15', 'FLGH58', 'HSW078', 'DYTF21', 'JHDW92', 'KKVG27', 'CSXS77', 'CLCP61', 'XF7794', 'BDF019', 'FXPX64', 'BSZW75', 'LB8361', 'KXGP72', 'PJ1416', 'KZJC56', 'AA3565', 'HRVP22', 'RR4674', 'DHLV93', 'MY6693', 'GFRD40', 'BSB024', 'FZTJ81', 'SP2634', 'LS4566', 'KJZR11', 'QR0929', 'CBKZ44', 'TD1370', 'VF4896', 'YA9953', 'IK0753', 'QP0935', 'BBZG92', 'XA7060', 'KJ4524', 'UF9103', 'FTLL26', 'FP8987', 'DX3050', 'KR0684', 'XJ1326', 'HCZX54', 'FJPV89', 'EC7118', 'KWVZ74', 'IB0282', 'HFVW64', 'NU3439', 'EP9151', 'JXGW98', 'BBLK74', 'LBPW42', 'DBLZ57', 'LN4084', 'JXYK14', 'LWBP37', 'OP0628', 'EL9722', 'LFHP14', 'KDW077', 'HLDS80', 'WH4542', 'JC0535', 'JKHW96', 'JLFK64', 'RE7838', 'PBDT23', 'UW3781', 'JXXT73', 'BXZP30', 'DPPJ10', 'JZRD97', 'BFGG68', 'YW1975', 'LPFW92', 'WZ4398', 'GHSW85', 'YP3098', 'KPJP44', 'QZ0357', 'WV7713', 'CCDV39', 'GWC067', 'VZ9141', 'VL0805', 'CSJR94', 'XL0398', 'CVSV95', 'NB4250', 'DGJX11', 'WN0756', 'VB8209', 'KTGR27', 'DTBP86', 'DHXB95', 'RB3899', 'DS3203', 'CLCJ66', 'DBTX65', 'XT0586', 'DXKR65', 'BHDK99', 'DS5662', 'FRLF55', 'SZ4763', 'BZSB71', 'FDPX24', 'GXDW96', 'FJVY60', 'HTRY57', 'RA9997', 'BGRY62', 'CTSX30', 'LRXY83', 'VJ5558', 'UE2005', 'HYYC59', 'BZZR24', 'ZL3357', 'KFKY18', 'FVBR57', 'UE7845', 'CBWL83', 'CHBJ12', 'BHBC32', 'BFWK67', 'LN8359', 'WR6936', 'CFBG91', 'LTTT95', 'LDVZ20', 'JCHB87', 'TN6728', 'VZ5287', 'KLYV97', 'DZ7000', 'OL0621', 'RY7521', 'BVVH25', 'FVGT37', 'NZ8785', 'HHBH58', 'JRLT56', 'BCDL51', 'YC9293', 'LWSR61', 'HGV013', 'KXYB57', 'CKHB27', 'LP5630', 'KSKV71', 'UE6124', 'ZV1824', 'RX8578', 'KFFW76', 'KWYX70', 'XB0551', 'BHVF75', 'PL9456', 'KHZ033', 'RD8080', 'YR6392', 'KRYZ47', 'DHJB96', 'UE6142', 'OZ0565', 'ZX2244', 'YK4774', 'LSBC98', 'LYRK53', 'KJSD73', 'JFDV41', 'GXSB39', 'SJ7800', 'WX1399', 'BM0775', 'GRZR56', 'GJHH78', 'FZCS14', 'HTVB43', 'KYTF30', 'NN6666', 'UN9815', 'FZCV44', 'KR4288', 'RN7396', 'KTJB19', 'XB4500', 'YJ4950', 'OA0176', 'FYSG49', 'ZJ7904', 'DXLY69', 'FSW075', 'DSLV58', 'BYJS56', 'KRLZ71', 'BDCW12', 'YG4109', 'DWRD44', 'JFHB24', 'FGXT80', 'DVVT95', 'GWD085', 'HKZJ63', 'BDGH13', 'FBJJ18', 'DYTL17', 'DCJB81', 'WE5891', 'BWXH65', 'DR2031', 'KV1759', 'BJB066', 'YA4780', 'BJK033', 'DDRD35', 'BXXV72', 'CFRW98', 'HYCS13', 'VR6058', 'FHPJ20', 'BYKB85', 'GTBD52', 'FPDV84', 'LFGP43', 'HPPT36', 'BRKW37', 'QJ0489', 'YR6149', 'ON0383', 'NW3360', 'TP8146', 'FGTK52', 'AA4647', 'ML0930', 'LDYF27', 'GRKX56', 'CPDB38', 'GWKD92', 'VP9596', 'XZ8634', 'GDC053', 'CLBH87', 'BLJB62', 'HXZL78', 'YX0424', 'DT9796', 'KWZ077', 'ZK9520', 'JGPZ32', 'HJFP92', 'XF3677', 'JDT053', 'DYCP92', 'YX1980', 'WL4063', 'RY3475', 'VX3632', 'KB1729', 'GLTD30', 'KF7964', 'HZFY24', 'DYXF86', 'XH6463', 'KGZH15', 'KC9784', 'BJZB79', 'KN8117', 'LVLB84', 'JPLZ84', 'FPRX43', 'HPR093', 'GHVF48', 'JDSC31', 'VV4408', 'FZR039', 'LDHC61', 'LTBP58', 'YC9378', 'VV9929', 'JJRK66', 'FSGC26', 'CJTD86', 'ID0474', 'KW2877', 'LTGC17', 'PCSY12', 'KTST75', 'SC8081', 'DFDR93', 'DVWR56', 'JRXB32', 'DR2286', 'KGHB37', 'ZU1801', 'FHPS67', 'LSGT12', 'VF2339', 'KDLB19', 'BBRC52', 'DSCG32', 'LBB040', 'KGHV88', 'YN4779', 'HCGR27', 'FKZL28', 'QS0114', 'BR5709', 'XS8512', 'GPZH23', 'BKGL33', 'GDV053', 'JSWG76', 'GXGW96', 'BDCX70', 'XX7043', 'YC1023', 'KSXH28', 'KHHR23', 'NP7231', 'KHBT75', 'WE8528', 'LXBY69', 'NS0501', 'FJWY92', 'LRWD25', 'FDDT51', 'GSSV42', 'JPDB82', 'HKSD23', 'HHHH64', 'SN8762', 'RL0316', 'WD2584', 'EU6960', 'CKKW95', 'GHF080', 'JCLJ79', 'DV8862', 'HDZK26', 'LLXR82', 'JYXP21', 'FBJY24', 'JSDF86', 'TK3201', 'LZDV47', 'BVFG17', 'PCDX60', 'CSYK20', 'HVXD27', 'WD4418', 'ZE3757', 'DWLB53', 'FCPX10', 'KZ2331', 'ZS0673', 'BDSV35', 'KSHW34', 'PW5248', 'LRBH58', 'HRFV90', 'MN0965', 'CZJR43', 'WL0943', 'CJXB92', 'JU0893', 'BZ5920', 'CSTW59', 'JLTW73', 'WF1749', 'MK0928', 'LFZT82', 'DU6266', 'FYCS46', 'FKSK45', 'HTJZ64', 'FSX091', 'LGWB40', 'DBC085', 'JDS050', 'IZ0334', 'TW6504', 'XU7011', 'JDKX64', 'KSDL27', 'DT1283', 'GPVK42', 'KHYY66', 'GJRZ47', 'LFFR76', 'YD6860', 'BSBZ43', 'JWYH45', 'ZF8502', 'CA4909', 'GXVV43']
class Cookies_Headers:

    def __init__(self, patenteActual):
        self.__patenteActual = patenteActual

    def getBoletasVespucioNorte(self):

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
            'patente': self.__patenteActual
        }

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

        boletas = []

        for key in dict:

            numb_boleta = key
            total_boleta = dict[key][0]
            fecha_hora = dict[key][1]
            boletas.append([numb_boleta, total_boleta, fecha_hora])

        return boletas

    def getInfraccionesVespucioSur(self):

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
            'txtpatente': self.__patenteActual,
            'g-recaptcha-response': f'{str(Solver(page_url))}',
            'Button1': 'Consultar'
        }

        response = requests.post('https://oficina.vespuciosur.cl/tags/VerificaInfraccion.aspx', headers=headers, data=data)
        print(response.text, file=open("costaneraSur.html", "w"))
        soup = BeautifulSoup(response.text, 'html.parser')
        a = soup.find_all('table')

        return a

class Vehiculo:
    def __init__ (self, patente):
        self.__patente = patente
        self.__boletas_vespucio_norte = []
        self.__infracciones_vespucio_sur = []

    def get_Patente(self):
        return self.__patente

    def getBoletasVespucioNorte(self):

        for detalle in self.__boletas_vespucio_norte:
            print('\n')
            print('Numero boleta: ', detalle[0])
            print('Pago total: $', detalle[1])

            fecha_hora = detalle[2].split(' ')
            print('Fecha: ', fecha_hora[0])
            print('Hora: ', fecha_hora[1])

        return self.__boletas_vespucio_norte
            
    def setBoletasVespucioNorte(self, boletas):

        self.__boletas_vespucio_norte = boletas

    def getInfraccionesVespucioSur(self):

        if(self.__infracciones_vespucio_sur==[]):
            print('El vehiculo de patente', self.__patente, 'no tiene infracciones en Vespucio Sur.')
        else:

            for detalle in self.__infracciones_vespucio_sur:

                print('Fecha de infraccion: ',detalle[0])
                print('Categoria de infraccion: ', detalle[1])
                print('Estado de infraccion: ', detalle[2])

                return self.__infracciones_vespucio_sur

    def setInfraccionesVespucioSur(self, infracciones):

        fechas_infracciones = []
        categoria_infracciones = []
        estado_infracciones = []
        contador = 0

        infracciones_final = []

        for detalle in infracciones:
            for fecha in detalle.find_all('td')[0::3]:
                fechas_infracciones.append(fecha.text)
                contador+=1

            for categoria in detalle.find_all('td')[1::3]:
                categoria_infracciones.append(categoria.text)

            for estado in detalle.find_all('td')[2::3]:
                estado_infracciones.append(estado.text)

        for i in range(0, contador):
            infraccion = []
            infraccion.append(fechas_infracciones[i])
            infraccion.append(categoria_infracciones[i])
            infraccion.append(estado_infracciones[i])
            infracciones_final.append(infraccion)

        self.__infracciones_vespucio_sur = infracciones_final

class Vespucio_Norte:

    def __init__(self):

        for i in lista_patentes:

            #patente = input('\nIngrese la patente del vehículo: ')
            patente = i
            if(patente=='0'):
                break

            else:
                vehiculo = Vehiculo(patente)

            try:
                vehiculo.setBoletasVespucioNorte(Cookies_Headers(vehiculo.get_Patente()).getBoletasVespucioNorte())
                vehiculo.getBoletasVespucioNorte()
                print('\n')

            except:
                print('El vehiculo de patente', patente, 'no tiene boletas en Vespucio Norte.')

class Vespucio_Sur:

    def __init__(self):

        for i in lista_patentes:

            #patente = input('\nIngrese la patente del vehículo: ')
            patente = i
            if(patente=='0'):
                break

            else:
                vehiculo = Vehiculo(patente)

            vehiculo.setInfraccionesVespucioSur(Cookies_Headers(vehiculo.get_Patente()).getInfraccionesVespucioSur())
            vehiculo.getInfraccionesVespucioSur()
                

# Vespucio_Norte()
# Vespucio_Sur()



'''Pendientes
8 Autopase
9 Costanera Norte
10 Nororiente
'''