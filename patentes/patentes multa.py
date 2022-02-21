#hay que pegarle una ordenada de datosyera
from bs4 import BeautifulSoup
import requests, time


API_KEY = "2a2b5480b431e8976a70ebbf3d38f550"
page_url ='http://consultamultas.srcei.cl/ConsultaMultas/buscarConsultaMultasExterna.do'

def Solver(url):
    #soup = BeautifulSoup(driver.page_source, 'html.parser') 
    #sitekey = str(soup.find('div', class_='g-recaptcha').get('data-sitekey'))
    sitekey = '6Ld_vfsSAAAAAGbw9u9u1V2x8pqV_3Y5AS4h9mW1'
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
    return form_tokon

#key=str(Solver(page_url))
cookies = {
    'JSESSIONID': 's3~366E6E4653824944297EB57DC8651019',
    '___utmvm': '###########',
    'TBMCookie_17651042677121688418': '380628001638412076Z+Cw8dSOuRQSnUHCVm8lihX3EUM=',
}
headers = {
    'Proxy-Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Proxy-Authorization': 'Basic M0RFQkM5MDg2RDFCQUNCMEYyQkFFRjQ5NTg1ODQ5MkU4MjJFMTc3QzpleUpoYkdjaU9pSkZRMFJJTFVWVEswRXlOVFpMVnlJc0ltTjBlU0k2SWtwWFZDSXNJbVZ1WXlJNklrRXlOVFpIUTAwaUxDSmxjR3NpT25zaWEzUjVJam9pUlVNaUxDSmpjbllpT2lKUUxUSTFOaUlzSW5naU9pSjRTa2hQU2padFJHOWlXREEyUmtSSmIzRnpSelZHTW5GRE1tbFBORnBrUkZSSVYxTXlORWhPWnpoVklpd2llU0k2SW05clJHMWxiMFZKU3pob1RGOVlSWFJrZVUxdFZVMU9NelF0U0hJMllrcERZV0o2VEhaNmFVdEpUa2tpZlgwLjdNdVkyOXdkSGlQbTN3OHZnSzZVR3g1MlNQelhyVWJJYTFoeTJ1ZVZWSkFaR3RIcFNjamh5US44TnZpWTkzenZ1R05Md1liLlJBdWdkQUJ0bEpXdHZxQmtLTUNvUFg1dlU2dzRxOXc5cXhiNXM0SUJzQjdCVzd0a3V1NkZtQkJiMWFLLXVNckVMcWtjZHFpdXVZNWtLRE5yTlFQZklIci1reFlHaGFXcE5xOUh2ZW9CVEdqTGFCNnZxSzZYbEhuT0V6eGZoWTFKWVlnWDJPUi1wb2pqWDRISEgwalhfclNzTnp1NXRacWVZWWlnVUQxTW84TGU2X2NaMTJSQnV6M3ZkWkt2ekxuekxWRlQ2eUVfWnBmb0FaWGVMRTZfQ0tpVThNU0doR0JqODJELXkzZ2p3NHdiTEd2TlF4ZG1XcVB0S29mNGVYRmhObWVsZnBPQW9TYkl5ZTQ5eXpOTzR0UGtZWEJTR3luTVAwT25tRjVQVWxncXIxSjVYeUFpTld6Z2FlRXpkWjhuYU1BMm82R1lUdkdYekR4RHhIdUlmMGNZR19UbUNsY2VYamQtckJDbXB5OTVpSmZWWldYQUZIV3JJbklETnFFcTNPVHhVOVBaMkRoUVdxWkZUc21HRk16R25jajJoWUdTeGIzcUhvMG9QajRYTXlrYjFPMC1pVGtuOXUwYmU0N0oudGF0U2NocUF3VFVxX1pDTnN5REpMZw==',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://consultamultas.srcei.cl',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://consultamultas.srcei.cl/ConsultaMultas/consultaMultasExterna.do',
    'Accept-Language': 'en-US,en;q=0.9',
}

'''data = {
  'org.apache.struts.taglib.html.TOKEN': 'a944953c01dcd6db77d6ab96efc85b8e',
  'reponseReCAPTCHA2': f'{key}',
  'ppu': 'CKFL14',
  'g-recaptcha-response': f'{key}'
}'''
with requests.Session() as s:
    r = s.get('http://consultamultas.srcei.cl/ConsultaMultas/buscarConsultaMultasExterna.do')
    print(r.headers)
    print(r.cookies)
    #r = s.post('http://consultamultas.srcei.cl/ConsultaMultas/buscarConsultaMultasExterna.do', headers=headers, data=data,cookies=cookies, verify=False)
    #print(r.__attrs__)
    #print(r.text)