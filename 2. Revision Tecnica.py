from bs4 import BeautifulSoup
import requests
import time

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

        try:
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
        except:
            return [[],[],[],[],[],[],[]]

if __name__ == '__main__':
    registro_revision_tecnica = RevisionTecnica('KXPS43', "2a2b5480b431e8976a70ebbf3d38f550",'http://www.prt.cl/Paginas/RevisionTecnica.aspx' )
    print(registro_revision_tecnica.resultado())