from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Função que instala o drive do selenium


def iniciar_navegador():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    return navegador
