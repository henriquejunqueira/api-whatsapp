from sys import executable

from selenium import webdriver
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

# Configurações do Chrome
dir_path = os.getcwd()
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={dir_path}/profile/zap")

# Inicializa o WebDriver
service = Service(executable_path='./chromedriver.exe') # Substitua pelo caminho para o seu chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://web.whatsapp.com/')

'''#######API DO EDITACODIGO##########################################'''
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

api = requests.get("https://editacodigo.com.br/index/api-whatsapp/x4klmOS8Xln6AAWlNU9ttz2LQLl4n7TM", headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()

'''#################################################'''

time.sleep(10)

def bot():
    try:
        bolinha = driver.find_element(By.CLASS_NAME, bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME, bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha, 0, -20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
    except:
        print('Buscando novas notificações...')

    while True:
        bot()