# enviar_mensagens.py
# Esse código lê um arquivo Excel com contatos e envia mensagens de admissão no WhatsApp.

import time
import webbrowser
import pyautogui as guia
import pandas as pd


def enviar_mensagens(caminho_arquivo):
    # Carrega o arquivo Excel com a lista de contatos
    df = pd.read_excel(caminho_arquivo)

    # Define a mensagem padrão a ser enviada
    mensagem = "Mensagem"

    # Loop para enviar a mensagem a cada contato na coluna 'Telefone Candidato'
    for telefone in df['Telefone Candidato']:

        # Remove caracteres especiais do número de telefone, deixando apenas os dígitos
        numero = ''.join(filter(str.isdigit, str(telefone)))

        # Constrói a URL do WhatsApp com o número e a mensagem
        url = f"https://web.whatsapp.com/send?phone=55{numero}&text={mensagem}"

        # Abre o navegador com a URL gerada para enviar a mensagem
        webbrowser.open(url)

        # Aguarda o tempo necessário para carregar a página do WhatsApp
        time.sleep(20)

        # Pressiona Enter para enviar a mensagem
        guia.press('enter')

        # Aguarda 5 segundos após o envio da mensagem para garantir o envio
        time.sleep(5)

        # Fecha a aba do WhatsApp para preparar o envio para o próximo contato
        guia.hotkey('ctrl', 'w')

        # Aguarda 5 segundos antes de reiniciar o loop para o próximo contato
        time.sleep(5)
