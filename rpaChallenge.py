from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as teclado

navegador = opcoesSelenium.Firefox()

navegador.get("https://rpachallenge.com")

#Variaveis
numeroTelefoene = "11938373893"
nomeEmpresa = "Jzn Store"
endereco = "Rua das flores"
cargoNaEmpresa = "Dono"
email = "jznstore@jznstore.xyz"
nome = "Joao"
sobrenome = "Silva"

teclado.sleep(1)

#//*[] - localizar o campo com o ngreflect name

#Preenche o endereço
navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelAddress"]').send_keys(endereco)

navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelCompanyName"]').send_keys(nomeEmpresa)

navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelEmail"]').send_keys(email)

navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelRole"]').send_keys(cargoNaEmpresa)

navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelFirstName"]').send_keys(nome)

navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelPhone"]').send_keys(numeroTelefoene)

navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelLastName"]').send_keys(sobrenome)

navegador.find_element(By.XPATH,'/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()