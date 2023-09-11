from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as teclado

navegador = opcoesSelenium.Firefox()

#Abrindo o site
navegador.get("https://lista.mercadolivre.com.br/informatica/componentes-pc/placas/placas-mae/kit-upgrade-ryzen-5-5600g_Desde_145_NoIndex_True")

teclado.sleep(2)
#ui-search-results ui-search-results--without-disclaimer shops__search-results
listaProdutos = navegador.find_elements(By.CLASS_NAME,"ui-search-layout__item")

for item in listaProdutos:
    nomeProduto = ""
    precoProduto = ''
    urlProduto = ''

    if nomeProduto == "":
        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "ui-search-item__title.shops__item-title").text

        except Exception:
            pass
    elif nomeProduto == "":
        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "ui-search-item__title").text
            print("Consegui com a class 2 ")
        except Exception:
            pass

    elif nomeProduto == "":
        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "shops__item-title").text
            print("Consegui com a Class 3 ")
        except Exception:
            pass

    elif nomeProduto == "":
        try:
            nomeProduto = item.find_element(By.XPATH, '//*[@id="react-aria-:Raklp:"]/div[2]/div[1]/a/h2').text
            print("Consegui com o XPATH")
        except Exception:
            pass

    #-------------------------------------

    if precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text

        except Exception:
            pass
    elif precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "ui-search-price__second-line").text
            print("Consegui com a class 2 ")
        except Exception:
            pass
    elif precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "shops__price-second-line").text
            print("Consegui com a class 2 ")
        except Exception:
            pass

    #---------------------------------------------------


    if urlProduto == "":
        try: urlProduto = item.find_element(By.TAG_NAME,"a").get_attribute("href")

        except Exception:
            pass

    else:
        urlProduto = "-"

    print(nomeProduto + ";" + precoProduto + ";" + urlProduto)