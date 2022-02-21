from selenium import webdriver
import os
def get_driver(name_path: str = 'chromedriver.exe', options: None = None, verbose: int = 0, debug: bool = False):
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
options = webdriver.ChromeOptions()

# options.add_argument('--proxy-server=%s' % PROXY[0])
options.add_argument('--ignore-certificate-errors')
options.add_argument("--lang=es")
driver = get_driver(name_path='chromedriver.exe',
                    options=options, verbose=1, debug=True)

link1 = 'https://www.registrocivil.cl/OficinaInternet/web/carro.srcei'
driver.get(link1)