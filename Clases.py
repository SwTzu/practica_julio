import json, time, os, urllib
from pip._vendor import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from twocaptcha import TwoCaptcha

#lista_patentes=['PHSS63', 'CKFL14', 'XF7651', 'JLWF50', 'CZCX24', 'TC2442', 'CPLH89', 'LTZ011', 'HWLF62', 'CBKV63', 'LYCH67', 'HKTW30', 'DFBG70', 'BI0875', 'LDY042', 'FTD049', 'WF5936', 'CFSC19', 'HPKP41', 'VE7020', 'BWDR40', 'BFDL17', 'PS7532', 'BXDY16', 'BBRL36', 'BPRV37', 'ZW9270', 'YH8274', 'DSBX73', 'SD4437', 'VD5486', 'TJ2248', 'ZD4101', 'GPR092', 'LFB012', 'YW4448', 'FP7732', 'DJLR32', 'SV7591', 'LG7679', 'KSWB78', 'HHYW27', 'WL0100', 'GYD099', 'KK8693', 'JPYK29', 'KXPP51', 'GLKD79', 'UY6416', 'ED6761', 'JFKK59', 'WG2532', 'KW7915', 'BGD021', 'FKRR71', 'JCBV97', 'JXD084', 'GY8298', 'KRLC41', 'YR0403', 'BWSR23', 'YG2586', 'XC4499', 'DYJP22', 'GTRR68', 'CGFY25', 'ZB7546', 'FXKK99', 'LRCW17', 'KJWK97', 'JPKS44', 'DHSL81', 'BHZK99', 'UE0649', 'FSHR31', 'LHGH69', 'LSXB75', 'HYJ025', 'GGCF74', 'PG5945', 'KGZB62', 'HRTB99', 'DHV013', 'GPF070', 'GCZK17', 'SU9716', 'CBYB72', 'CWWR43', 'LKDZ91', 'CKVS68', 'LV2755', 'GGGB47', 'EE8342', 'DZDZ48', 'HKP045', 'LR2813', 'JRRJ13', 'WB3923', 'DLX035', 'KFPR52', 'BD6139', 'LXPX30', 'DPF068', 'GGFZ69', 'CRLT12', 'CFVB55', 'JXBW26', 'HDJY17', 'JDYG86', 'FHRF34', 'BZKK47', 'KTCH36', 'KXJD90', 'KGT040', 'DJGH61', 'WK0220', 'LPJH14', 'CPTH49', 'WK0637', 'CCJC40', 'WK7854', 'FLSS16', 'WB3994', 'WW4000', 'SD2996', 'LLSX48', 'FDK014', 'HPDW71', 'KVLY79', 'HJHT22', 'FYJJ29', 'LCCY83', 'ZX1227', 'WL4499', 'DBVH42', 'JWVT67', 'WB7258', 'DYCF71', 'NR0364', 'FBGG46', 'CVPP53', 'GXYT43', 'BVKH13', 'CYXZ34', 'KK8337', 'GDJK17', 'VR9229', 'NF2417', 'DX7389', 'FPLX76', 'RT2943', 'ZY4092', 'HKCB50', 'CGXZ27', 'VV9606', 'YT5012', 'XG5973', 'KGHX97', 'YV7398', 'FKGJ96', 'KKZJ39', 'DBTZ25', 'HKTV27', 'CCGH83', 'GYS092', 'UT8872', 'DDBD17', 'DSZG88', 'DBDK99', 'KTHV37', 'CPRK17', 'HTVT12', 'KS0852', 'CKGK80', 'QL0885', 'LS2484', 'KWSP28', 'JFKW46', 'WK9995', 'LLPX65', 'UN0384', 'DPJG58', 'LHDB85', 'LTPF27', 'KGH047', 'FDRG49', 'RW5289', 'BCR031', 'LSWW93', 'GSZB46', 'LTVJ41', 'BXJB48', 'HHSL37', 'JD0509', 'HYBP90', 'UG6239', 'BXSP64', 'PC6312', 'KT1046', 'BSTL76', 'KTPF65', 'CLZK25', 'KCPW61', 'RP8576', 'VZ6997', 'KLBJ58', 'WY4231', 'KH4878', 'DVGY65', 'LXBL35', 'BGS065', 'JXFL75', 'BYYL42', 'JCLL52', 'KZTS68', 'DZZX64', 'XF4131', 'FSKZ53', 'NE9952', 'JWTZ94', 'JYXJ49', 'YT2598', 'KRTG35', 'JKHV11', 'WZ5936', 'DXZZ71', 'FBTD79', 'ZY4313', 'JWGD90', 'JHTP61', 'XD1946', 'UH7384', 'LSTS13', 'CTWX77', 'FLBS46', 'LLZD13', 'JZTZ44', 'HJFT18', 'GBY078', 'TG5204', 'KTRY76', 'GCFH23', 'NC5093', 'WU9402', 'CTVF29', 'RR1601', 'GRZ045', 'KTDP50', 'DN5078', 'LFZ060', 'GWHP33', 'BCJP46', 'CJZZ41', 'SX5531', 'ZL3706', 'WE9030', 'CSJC87', 'HJZ073', 'OW0214', 'HWFL68', 'HFBF78', 'LHKW76', 'GXDX66', 'DJZJ56', 'TJ2673', 'WE9401', 'GN8893', 'VH8584', 'FVTT87', 'BFLH77', 'GZ7035', 'FLC060', 'LFRF19', 'DS9370', 'DD5495', 'JWSS57', 'XP0825', 'DPC062', 'JRW071', 'LS8370', 'LBGB61', 'NV3646', 'LVYZ15', 'FLGH58', 'HSW078', 'DYTF21', 'JHDW92', 'KKVG27', 'CSXS77', 'CLCP61', 'XF7794', 'BDF019', 'FXPX64', 'BSZW75', 'LB8361', 'KXGP72', 'PJ1416', 'KZJC56', 'AA3565', 'HRVP22', 'RR4674', 'DHLV93', 'MY6693', 'GFRD40', 'BSB024', 'FZTJ81', 'SP2634', 'LS4566', 'KJZR11', 'QR0929', 'CBKZ44', 'TD1370', 'VF4896', 'YA9953', 'IK0753', 'QP0935', 'BBZG92', 'XA7060', 'KJ4524', 'UF9103', 'FTLL26', 'FP8987', 'DX3050', 'KR0684', 'XJ1326', 'HCZX54', 'FJPV89', 'EC7118', 'KWVZ74', 'IB0282', 'HFVW64', 'NU3439', 'EP9151', 'JXGW98', 'BBLK74', 'LBPW42', 'DBLZ57', 'LN4084', 'JXYK14', 'LWBP37', 'OP0628', 'EL9722', 'LFHP14', 'KDW077', 'HLDS80', 'WH4542', 'JC0535', 'JKHW96', 'JLFK64', 'RE7838', 'PBDT23', 'UW3781', 'JXXT73', 'BXZP30', 'DPPJ10', 'JZRD97', 'BFGG68', 'YW1975', 'LPFW92', 'WZ4398', 'GHSW85', 'YP3098', 'KPJP44', 'QZ0357', 'WV7713', 'CCDV39', 'GWC067', 'VZ9141', 'VL0805', 'CSJR94', 'XL0398', 'CVSV95', 'NB4250', 'DGJX11', 'WN0756', 'VB8209', 'KTGR27', 'DTBP86', 'DHXB95', 'RB3899', 'DS3203', 'CLCJ66', 'DBTX65', 'XT0586', 'DXKR65', 'BHDK99', 'DS5662', 'FRLF55', 'SZ4763', 'BZSB71', 'FDPX24', 'GXDW96', 'FJVY60', 'HTRY57', 'RA9997', 'BGRY62', 'CTSX30', 'LRXY83', 'VJ5558', 'UE2005', 'HYYC59', 'BZZR24', 'ZL3357', 'KFKY18', 'FVBR57', 'UE7845', 'CBWL83', 'CHBJ12', 'BHBC32', 'BFWK67', 'LN8359', 'WR6936', 'CFBG91', 'LTTT95', 'LDVZ20', 'JCHB87', 'TN6728', 'VZ5287', 'KLYV97', 'DZ7000', 'OL0621', 'RY7521', 'BVVH25', 'FVGT37', 'NZ8785', 'HHBH58', 'JRLT56', 'BCDL51', 'YC9293', 'LWSR61', 'HGV013', 'KXYB57', 'CKHB27', 'LP5630', 'KSKV71', 'UE6124', 'ZV1824', 'RX8578', 'KFFW76', 'KWYX70', 'XB0551', 'BHVF75', 'PL9456', 'KHZ033', 'RD8080', 'YR6392', 'KRYZ47', 'DHJB96', 'UE6142', 'OZ0565', 'ZX2244', 'YK4774', 'LSBC98', 'LYRK53', 'KJSD73', 'JFDV41', 'GXSB39', 'SJ7800', 'WX1399', 'BM0775', 'GRZR56', 'GJHH78', 'FZCS14', 'HTVB43', 'KYTF30', 'NN6666', 'UN9815', 'FZCV44', 'KR4288', 'RN7396', 'KTJB19', 'XB4500', 'YJ4950', 'OA0176', 'FYSG49', 'ZJ7904', 'DXLY69', 'FSW075', 'DSLV58', 'BYJS56', 'KRLZ71', 'BDCW12', 'YG4109', 'DWRD44', 'JFHB24', 'FGXT80', 'DVVT95', 'GWD085', 'HKZJ63', 'BDGH13', 'FBJJ18', 'DYTL17', 'DCJB81', 'WE5891', 'BWXH65', 'DR2031', 'KV1759', 'BJB066', 'YA4780', 'BJK033', 'DDRD35', 'BXXV72', 'CFRW98', 'HYCS13', 'VR6058', 'FHPJ20', 'BYKB85', 'GTBD52', 'FPDV84', 'LFGP43', 'HPPT36', 'BRKW37', 'QJ0489', 'YR6149', 'ON0383', 'NW3360', 'TP8146', 'FGTK52', 'AA4647', 'ML0930', 'LDYF27', 'GRKX56', 'CPDB38', 'GWKD92', 'VP9596', 'XZ8634', 'GDC053', 'CLBH87', 'BLJB62', 'HXZL78', 'YX0424', 'DT9796', 'KWZ077', 'ZK9520', 'JGPZ32', 'HJFP92', 'XF3677', 'JDT053', 'DYCP92', 'YX1980', 'WL4063', 'RY3475', 'VX3632', 'KB1729', 'GLTD30', 'KF7964', 'HZFY24', 'DYXF86', 'XH6463', 'KGZH15', 'KC9784', 'BJZB79', 'KN8117', 'LVLB84', 'JPLZ84', 'FPRX43', 'HPR093', 'GHVF48', 'JDSC31', 'VV4408', 'FZR039', 'LDHC61', 'LTBP58', 'YC9378', 'VV9929', 'JJRK66', 'FSGC26', 'CJTD86', 'ID0474', 'KW2877', 'LTGC17', 'PCSY12', 'KTST75', 'SC8081', 'DFDR93', 'DVWR56', 'JRXB32', 'DR2286', 'KGHB37', 'ZU1801', 'FHPS67', 'LSGT12', 'VF2339', 'KDLB19', 'BBRC52', 'DSCG32', 'LBB040', 'KGHV88', 'YN4779', 'HCGR27', 'FKZL28', 'QS0114', 'BR5709', 'XS8512', 'GPZH23', 'BKGL33', 'GDV053', 'JSWG76', 'GXGW96', 'BDCX70', 'XX7043', 'YC1023', 'KSXH28', 'KHHR23', 'NP7231', 'KHBT75', 'WE8528', 'LXBY69', 'NS0501', 'FJWY92', 'LRWD25', 'FDDT51', 'GSSV42', 'JPDB82', 'HKSD23', 'HHHH64', 'SN8762', 'RL0316', 'WD2584', 'EU6960', 'CKKW95', 'GHF080', 'JCLJ79', 'DV8862', 'HDZK26', 'LLXR82', 'JYXP21', 'FBJY24', 'JSDF86', 'TK3201', 'LZDV47', 'BVFG17', 'PCDX60', 'CSYK20', 'HVXD27', 'WD4418', 'ZE3757', 'DWLB53', 'FCPX10', 'KZ2331', 'ZS0673', 'BDSV35', 'KSHW34', 'PW5248', 'LRBH58', 'HRFV90', 'MN0965', 'CZJR43', 'WL0943', 'CJXB92', 'JU0893', 'BZ5920', 'CSTW59', 'JLTW73', 'WF1749', 'MK0928', 'LFZT82', 'DU6266', 'FYCS46', 'FKSK45', 'HTJZ64', 'FSX091', 'LGWB40', 'DBC085', 'JDS050', 'IZ0334', 'TW6504', 'XU7011', 'JDKX64', 'KSDL27', 'DT1283', 'GPVK42', 'KHYY66', 'GJRZ47', 'LFFR76', 'YD6860', 'BSBZ43', 'JWYH45', 'ZF8502', 'CA4909', 'GXVV43']

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
        self.__registro_revision_tecnica = []
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

    def getRegistroRevisionTecnica(self):

        print('\nREGISTRO DE REVISION TECNICA\n')

        registrosDeRevision = self.__registro_revision_tecnica

        titulos = ['Patente: ', 'Tipo: ', 'Marca: ', 'Modelo: ', 'Año Fabricacion: ', 'Numero Motor: ', 'Numero Chasis: ', 'Numero Vin: ']
        indice_titulos = 0

        print('\nInformacion del Vehiculo: \n')

        if(registrosDeRevision[0]!=[]):
            for dato in registrosDeRevision[0]:
                print(titulos[indice_titulos] + dato)
                indice_titulos+=1
        else:
            print('El vehiculo de patente ', self.__patente, 'no posee información registrada.')

        print('\nInformacion de Revision Tecnica: \n')

        if(registrosDeRevision[1]!=[]):
            for indice_revision in range(0, len(registrosDeRevision[1])):
                print('Fecha: ', registrosDeRevision[1][indice_revision])
                print('Cod. Planta: ', registrosDeRevision[2][indice_revision])
                print('Planta: ', registrosDeRevision[3][indice_revision])
                print('Nro. Certificado: ', registrosDeRevision[4][indice_revision])
                print('Fecha Vec: ', registrosDeRevision[5][indice_revision])
                print('Estado: ', registrosDeRevision[6][indice_revision],'\n')
        else:
            print('El vehiculo de patente ', self.__patente, 'no posee información de revision tecnica registrada.')

        return self.__registro_revision_tecnica

    def setRegistroRevisionTecnica(self, registroRevisionTecnica):
        self.__registro_revision_tecnica = registroRevisionTecnica
    
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
        self.__API_KEY = API_KEY
        self.__page_url = page_url

    def resultado(self):
        #soup = BeautifulSoup(driver.page_source, 'html.parser')
        #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
        sitekey = '6LctMP8SAAAAANBvpGMjkMm5bBJ7TY-7X9UuGAaq'
        u1 = f"https://2captcha.com/in.php?key={self.__API_KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl={self.__page_url}&json=1"
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
        datoVehiculos = []
        infoRevision_Fecha, infoRevision_CodPlanta,infoRevision_Planta,infoRevision_NroCertificado,infoRevision_FechaVec, infoRevision_Estado= [],[],[],[],[],[]
        infoVehiculo = soup.find_all('span', id='ContentPlaceHolder1_lblDatosVehiculo')
        infoRevision = soup.find_all('span', id='ContentPlaceHolder1_lblHistorico')

        for i in infoVehiculo:
            for z in i.find_all('span'):

                if('Nota :' not in z.text):
                    datoVehiculos.append(z.text)

        for i in infoRevision:
            for z in i.find_all('td')[0::6]:
                infoRevision_Fecha.append(z.text)

            for z in i.find_all('td')[1::6]:
                infoRevision_CodPlanta.append(z.text)

            for z in i.find_all('td')[2::6]:
                infoRevision_Planta.append(z.text)

            for z in i.find_all('td')[3::6]:
                infoRevision_NroCertificado.append(z.text.split('(g)')[0])

            for z in i.find_all('td')[4::6]:
                infoRevision_FechaVec.append(z.text)

            for z in i.find_all('td')[5::6]:
                infoRevision_Estado.append(z.text)

        return [datoVehiculos, infoRevision_Fecha, infoRevision_CodPlanta,infoRevision_Planta,infoRevision_NroCertificado,infoRevision_FechaVec, infoRevision_Estado]

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

# Para obtener Registro de Transporte Publico
# auto.setRegistroTransportePublico(TransportePublico(auto.getPatente()).resultado())
# auto.getRegistroTransportePublico()

# Para obtener Revision Tecnica
auto.setRegistroRevisionTecnica(RevisionTecnica(auto.getPatente(),"2a2b5480b431e8976a70ebbf3d38f550",'http://www.prt.cl/Paginas/RevisionTecnica.aspx').resultado())
auto.getRegistroRevisionTecnica()

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






# Encargo_Robo1 = EncargoRobo(auto.getPatente(), "2a2b5480b431e8976a70ebbf3d38f550",'https://www.autoseguro.gob.cl')
# a,b,c = Encargo_Robo1.resultado("2a2b5480b431e8976a70ebbf3d38f550",'https://www.autoseguro.gob.cl')
# print(a,b,c)

