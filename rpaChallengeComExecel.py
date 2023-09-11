from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as teclado
from openpyxl import load_workbook
import os

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

nomeArquivo = "C:\\Users\\Jzn\\Documents\\Automação\\02 - Selenium panta e openpyxl\\venv\\desafio.xlsx"
planilha =load_workbook(nomeArquivo)

#Seleciona a sheet com as informações da planilha
sheet_selecionada = planilha["Sheet1"]

teclado.sleep(1)

#navegador.find_element(By.XPATH,'/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()
#teclado.sleep(1)

for linha in range(2, len(sheet_selecionada['A']) + 1):
    #teclado.sleep(1)
    #O Ele pega o valor da linha tal e a transforma em string



    firstname = sheet_selecionada['A%s' % linha].value
    # //*[] - localizar o campo com o ngreflect name
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(firstname)
    #teclado.sleep(1)

    lastName = sheet_selecionada['B%s' % linha].value
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(lastName)
    #teclado.sleep(1)

    andress = sheet_selecionada['E%s' % linha].value
    navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelAddress"]').send_keys(andress)
    #teclado.sleep(1)

    companyName = sheet_selecionada['C%s' % linha].value
    navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelCompanyName"]').send_keys(companyName)
    #teclado.sleep(1)

    email2 = sheet_selecionada['F%s' % linha].value
    navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelEmail"]').send_keys(email2)
    #teclado.sleep(1)

    labelRole = sheet_selecionada['D%s' % linha].value
    navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelRole"]').send_keys(labelRole)
    #teclado.sleep(1)

    phone = sheet_selecionada['B%s' % linha].value
    navegador.find_element(By.XPATH,'//*[@ng-reflect-name="labelPhone"]').send_keys(phone)
    #teclado.sleep(1)

    navegador.find_element(By.XPATH,'/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()

print("Dados enviados com sucesso")