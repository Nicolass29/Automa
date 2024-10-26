# exportar_planilha.py
# Esse código realiza o download de um arquivo de admissão em uma plataforma web.

import time
from selenium.webdriver.common.by import By


def exportar_admissao(navegador):
    # Localiza o botão de exportação e clica nele
    campo_exportar = navegador.find_element(
        By.XPATH, '//*[@id="content"]/div/div[10]/div/div/div/div[1]/div[1]/a[2]')
    campo_exportar.click()
    time.sleep(1)

    # Localiza o campo de opções de filtro e clica nele para exibir as opções disponíveis
    botao_opcoes = navegador.find_element(
        By.XPATH, '//*[@id="select2-IdFiltroRelatorio-container"]')
    botao_opcoes.click()
    time.sleep(1)

    # Seleciona a opção no menu de opções
    botao_admissao = navegador.find_element(
        By.XPATH, '/html/body/span/span/span[2]/ul/li[3]')
    botao_admissao.click()
    time.sleep(1)

    # Clica no botão de download para baixar o arquivo com os dados
    botao_baixar = navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]')
    botao_baixar.click()

    # Aguarda o tempo necessário para concluir o download
    time.sleep(5)
