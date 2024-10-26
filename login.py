# login.py
# Esse código realiza o login em uma plataforma usando CPF, senha e resolução de captcha.

import time
from config import iniciar_navegador
from selenium.webdriver.common.by import By


def realizar_login(navegador, cpf, senha):
    # Abre a página de login
    navegador.get("link")
    time.sleep(1)

    # Localiza o campo CPF, limpa-o para evitar problemas e insere o CPF fornecido
    campo_email = navegador.find_element(By.XPATH, '//*[@id="Cpf"]')
    campo_email.clear()
    time.sleep(0.5)
    campo_email.send_keys(cpf)
    time.sleep(1)

    # Localiza o campo de senha e insere a senha fornecida
    campo_senha = navegador.find_element(By.XPATH, '//*[@id="Senha"]')
    campo_senha.send_keys(senha)
    time.sleep(1)

    # Localiza o iframe do captcha e muda o contexto de navegação para dentro dele
    iframe = navegador.find_element(
        By.XPATH, '//*[@id="frmLogin"]/div/div/div/div[2]/div[4]/div/div/iframe')
    navegador.switch_to.frame(iframe)

    # Localiza e clica na caixa de verificação do reCAPTCHA, aguardando para resolver manualmente se necessário
    recaptcha_box = navegador.find_element(
        By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
    recaptcha_box.click()
    # Retorna ao contexto principal após o captcha
    navegador.switch_to.default_content()
    time.sleep(15)  # Tempo para resolver o captcha manualmente, se necessário

    # Localiza e clica no botão "Entrar" para concluir o login
    botao_entrar = navegador.find_element(By.XPATH, '//*[@id="btnEntrar"]')
    botao_entrar.click()
    time.sleep(5)  # Aguarda o carregamento da página após o login
