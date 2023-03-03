import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen, Request
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

#pegando a lista de fii's:
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
url_lista = 'https://fiis.com.br/lista-de-fundos-imobiliarios/'

lista_fii = []

navegador.get(url_lista)
qtd = 100

l_abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for abc in range(1,len(l_abc)):

    for l_fii in range(1,qtd):

        try:
            cod_acao = navegador.find_element(By.XPATH, '//*[@id="letter-id-'+l_abc[abc]+'"]/div[1]/div['+str(l_fii)+']/a/div').text
            lista_fii.append(cod_acao)

        except Exception as e:
            print(e)

navegador.quit()

##pegando os daddos:
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

lista_indicadores_fii = []

for fii in lista_fii:

    #  Criando URL
    url = f'https://statusinvest.com.br/fundos-imobiliarios/{fii}'
    
    try:
        navegador.get(url)
    
        #Coletando infos
        valor_atual = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[2]/div[1]/div[1]/div/div[1]/strong').text
        dy = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[2]/div[1]/div[4]/div/div[1]/strong').text
        pvp = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[2]/div[5]/div/div[2]/div/div[1]/strong').text
        segmento = navegador.find_element(By.XPATH, '//*[@id="fund-section"]/div/div/div[4]/div/div[1]/div/div/div/a/strong').text
        segmento_ambima = navegador.find_element(By.XPATH, '//*[@id="fund-section"]/div/div/div[2]/div/div[6]/div/div/strong').text
    
        dicionario = {
                    'codigo': fii, 
                    'segmento': segmento, 
                    'valor_atual': valor_atual, 
                    'segmento ambima': segmento_ambima,
                    'dividend_yield': dy, 
                    'pvp': pvp
                    }

        lista_indicadores_fii.append(dicionario)
    except Exception as e:
        print(e)

navegador.quit()

df = pd.DataFrame.from_dict(lista_indicadores_fii)
print(df)