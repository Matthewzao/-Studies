from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedrive = ("C:\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\ESTUDOS GIT\\Matthew\\chromedriver.exe")

driver = webdriver.Chrome(chromedrive)
driver.get("https://www.atheleco.com.br/")
# clicar = driver.find_element_by_xpath('//*[@id="container"]/section[1]/div/button')
# clicar.click()
# clicar2 = driver.find_element_by_xpath ('//*[@id="topo"]/div[3]/div/nav/ul/li[2]/a/span')
# clicar2.click()
# clicar_aba = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/section/div[1]/ul/li[3]/label')
# clicar_aba.click()
# categoria = driver.find_element_by_xpath('//*[@id="conteudo"]/div/h1/span')  
