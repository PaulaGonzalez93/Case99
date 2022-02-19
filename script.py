from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# Download dos arquivos .csv
url = "https://covid.saude.gov.br/ "
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
b = soup.find("ion-button",attrs={"class": "btn-white"})
# b['onclick']  esta chamada deveria clicar o botão e fazer o download
# Aqui os arquivos deveriam ser baixados e salvos na pasta atual

# Aqui importo os arquivos para trabalhar sobre eles
parte1 = pd.read_csv("HIST_PAINEL_COVIDBR_2020_Parte1_18fev2022.csv", sep=';')
parte2 = pd.read_csv("HIST_PAINEL_COVIDBR_2020_Parte2_18fev2022.csv", sep=';')
# Aqui estou usando apenas as primeiras linhas de cada arquivo para agilizar a prova de conceito
head1 = (parte1.head())
head2 = (parte2.head())
# Aqui concateno os dois arquivos para ter todos os dados numa planilha só
juncao = pd.concat([head1,head2])

# Aqui trataria os dados conforme necessidade (excluindo informações desnecessárias)

# Aqui exporto o arquivo tratado 
juncao.to_excel("resultado.xlsx",index=False)