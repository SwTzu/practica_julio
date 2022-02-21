import requests
from bs4 import BeautifulSoup
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
  'ctl00$MainContent$ppu': 'KXPS43',
  'ctl00$MainContent$btn_buscar': 'Buscar'
}

response = requests.post('http://apps.mtt.cl/consultaweb/', headers=headers, cookies=cookies, data=data, verify=False)

soup = BeautifulSoup(response.text, 'html.parser')
table=soup.find_all("table", id='MainContent_tablaDatos')
for i in table:
    print(i.text.replace('\n', ' '))
#print(table).text