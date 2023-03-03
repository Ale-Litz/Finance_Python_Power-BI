import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen, Request
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager


#pegando a lista de acoes:
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
url_lista = 'https://www.fundamentus.com.br/resultado.php'
headers ={'User-Agent': 'Chrome/94.0.4606.61'}
dados = urlopen(Request(url_lista,headers=headers))
html = BeautifulSoup(dados.read())
lista = html.find('table')
qtd = html.findAll('span',class_='tips') 

lista_acao = []

navegador.get(url_lista)

for l_acao in range(1,int(len(qtd)-1)):

    try:
        cod_acao = navegador.find_element(By.XPATH, '//*[@id="resultado"]/tbody/tr['+str(l_acao)+']/td[1]/span/a').text
        lista_acao.append(cod_acao)

    except Exception as e:
        print(e)

navegador.quit()

##pegando os daddos:
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

lista_indicadores_acao = []

for acao in lista_acao:

    #Criando url
    url_indicador = f'https://statusinvest.com.br/acoes/{acao}'
    
    try:
        navegador.get(url_indicador)

        # Indicadores de Valuation
        dy = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[1]/div/div/strong').text
        preco = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[2]/div/div[1]/div/div[1]/div/div[1]/strong').text
        p_l = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong').text
        peg_ratio = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[3]/div/div/strong').text
        p_vp = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[4]/div/div/strong').text
        ev_ebitda = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[5]/div/div/strong').text
        ev_ebit = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[6]/div/div/strong').text
        p_ebitda = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[7]/div/div/strong').text
        p_ebit = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[8]/div/div/strong').text
        vpa = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[9]/div/div/strong').text
        p_ativo = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[10]/div/div/strong').text
        lpa = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[11]/div/div/strong').text
        p_sr = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[12]/div/div/strong').text
        p_cap_giro = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[13]/div/div/strong').text
        p_ativo_circ_liq = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[14]/div/div/strong').text

        # Indicadores de Endividamento
        div_liquida_pl = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[1]/div/div/strong').text
        div_liquida_ebitda = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[2]/div/div/strong').text
        div_liquida_ebit = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[3]/div/div/strong').text
        pl_ativos = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[4]/div/div/strong').text
        passivos_ativos = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[5]/div/div/strong').text
        liq_corrente = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[6]/div/div/strong').text

        # Indicadores de Eficiencia
        m_bruta = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[1]/div/div/strong').text
        m_ebitda = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[2]/div/div/strong').text
        m_ebit = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[3]/div/div/strong').text
        m_liquida = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[4]/div/div/strong').text

        # Indicadores de Rentabilida
        roe = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[1]/div/div/strong').text
        roa = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[2]/div/div/strong').text
        roic = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[3]/div/div/strong').text
        gira_ativos = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[4]/div/div/strong').text

        # Indicadores de Crescimento
        cagr_receita_5_anos = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[5]/div/div[1]/div/div/strong').text
        cagr_lucro_5_anos = navegador.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[5]/div/div[2]/div/div/strong').text
    
        dicionario = {
                    'codigo':acao,
                    'preco':preco,
                    'D.Y': dy,
                    'P/L': p_l,
                    'PEG RATIO': peg_ratio,
                    'P/VP': p_vp,
                    'EV/EBITDA': ev_ebitda,
                    'EV/EBIT': ev_ebit,
                    'P/EBITDA': p_ebitda,
                    'P/EBIT': p_ebit,
                    'VPA': vpa,
                    'P/ATIVO': p_ativo,
                    'LPA': lpa,
                    'P/SR': p_sr,
                    'P/CAP.GIRO': p_cap_giro,
                    'P/ATIVO CIRC. LIQ.': p_ativo_circ_liq,
                    'DIV. LIQUIDA/PL': div_liquida_pl,
                    'DIV. LIQUIDA/EBITDA': div_liquida_ebitda,
                    'DIV. LIQUIDA/EBIT': div_liquida_ebit,
                    'PL/ATIVOS': pl_ativos,
                    'PASSIVOS/ATIVOS': passivos_ativos,
                    'LIQ. CORRENTE': liq_corrente,
                    'M. BRUTA': m_bruta,
                    'M EBITDA': m_ebitda,
                    'M. EBIT': m_ebit,
                    'M. LIQUIDA': m_liquida,
                    'ROE': roe,
                    'ROA': roa,
                    'ROIC': roic,
                    'GIRO ATIVOS': gira_ativos,
                    'CAGR RECEITAS 5 ANOS': cagr_receita_5_anos,
                    'CAGR LUCROS 5 ANOS': cagr_lucro_5_anos,
                    }

        lista_indicadores_acao.append(dicionario)
    
    except Exception as e:
        print(e)

navegador.quit()

df = pd.DataFrame.from_dict(lista_indicadores_acao)
print(df)