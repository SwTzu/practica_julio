from selenium import webdriver
driver=webdriver.Chrome()
page='https://www.aach.cl/conremate/'
driver.get(page)
letras='KYDX'
numeros='57'
driver.find_element_by_xpath('//*[@id="masterContenido_txtLetras"]').send_keys(letras)
driver.find_element_by_xpath('//*[@id="masterContenido_txtNumeros"]').send_keys(numeros)
driver.find_element_by_xpath('//*[@id="masterContenido_chkCondiciones"]').click()
driver.find_element_by_xpath('//*[@id="masterContenido_btnLnkConsultar"]').click()
