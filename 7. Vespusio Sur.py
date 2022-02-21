#hay que pegarle una ordenada de datosyera
from bs4 import BeautifulSoup
import requests, time


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
  'txtpatente': 'XF7651',
  'g-recaptcha-response': f'{str(Solver(page_url))}',
  'Button1': 'Consultar'
}

response = requests.post('https://oficina.vespuciosur.cl/tags/VerificaInfraccion.aspx', headers=headers, data=data)
print(response.text, file=open("costaneraSur.html", "w"))
soup = BeautifulSoup(response.text, 'html.parser')
fecha,categoria,estado=[],[],[]
a = soup.find_all('table')
for i in a:
    for z in i.find_all('td')[0::3]:
        fecha.append(z.text)
        print(z.text)
    print('------------------')
    for z in i.find_all('td')[1::3]:
        categoria.append(z.text)
        print(z.text)
    print('------------------')
    for z in i.find_all('td')[2::3]:
        estado.append(z.text)
        print(z.text)
    print('------------------')