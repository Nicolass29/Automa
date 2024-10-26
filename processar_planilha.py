# processar_planilha.py
# Verifica se a planilha foi baixada, aplica filtros específicos e salva um novo arquivo filtrado.

import os
import pandas as pd
from datetime import datetime
from pathlib import Path


def processar_planilha():
    # Define o caminho para a pasta de Downloads e o nome do arquivo a ser processado
    pasta_downloads = str(Path.home() / 'Downloads')
    arquivo = os.path.join(pasta_downloads, 'arquivo.xlsx')

    # Verifica se o arquivo existe para prosseguir com a filtragem
    if os.path.exists(arquivo):
        # Lê o arquivo Excel em um DataFrame do pandas
        df = pd.read_excel(arquivo)

        # Define uma lista com os valores que serão usados para filtrar a coluna 'Coluna2'
        clientes_filtrados = ["Filtros"]

        # Aplica os filtros nas colunas relevantes do DataFrame
        df_filtrado = df[
            # Filtro para valores específicos em 'Coluna1'
            (df['Coluna1'].isin(['filtro1', 'filtro2'])) &
            # Filtro para valores específicos em 'Coluna2'
            (df['Coluna2'].isin(clientes_filtrados))
        ]

        # Define o nome do novo arquivo, incluindo a data e hora no formato "novo_DD-MM-YYYY_HH.xlsx"
        now = datetime.now().strftime("%d-%m-%Y_%H")
        arquivo_filtrado = fr'caminho\novo_{
            now}.xlsx'

        # Salva o DataFrame filtrado em um novo arquivo Excel
        df_filtrado.to_excel(arquivo_filtrado, index=False)

        # Remove o arquivo original para liberar espaço e manter apenas o arquivo filtrado
        os.remove(arquivo)

        # Retorna o caminho do novo arquivo filtrado para uso posterior
        return arquivo_filtrado
    else:
        # Informa ao usuário que o arquivo original não foi encontrado
        print(f'O arquivo "{arquivo}" não existe.')
        return None
