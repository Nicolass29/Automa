# main.py
# Executa o fluxo completo de login, exportação, processamento de planilha e envio de mensagens.

from login import realizar_login
from exportar_planilha import exportar_admissao
from processar_planilha import processar_planilha
from enviar_mensagens import enviar_mensagens
from config import iniciar_navegador
import keyboard


def main():
    # Inicializa o navegador para automação
    navegador = iniciar_navegador()

    # Realiza o login na plataforma com o CPF e senha fornecidos
    realizar_login(navegador, "cpf", "senha")

    # Exporta a planilha de admissão da plataforma
    exportar_admissao(navegador)

    # Processa a planilha baixada e retorna o caminho do arquivo
    caminho_arquivo = processar_planilha()

    # Verifica se o caminho do arquivo é válido e, se for, inicia o envio de mensagens
    if caminho_arquivo:
        enviar_mensagens(caminho_arquivo)

    # Aguarda o usuário pressionar 'end' para finalizar o programa e fechar o navegador
    keyboard.wait('end')
    navegador.quit()


# Executa a função principal se o script for chamado diretamente
if __name__ == "__main__":
    main()
