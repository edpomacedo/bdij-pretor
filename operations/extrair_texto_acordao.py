# Pretor/1.4 - @edpomacedo - operations/extrair_texto_acordao.py
import os
import hashlib
from pdfminer.high_level import extract_text
from utils.logger import logger
from modules.obter_token_edicao import obter_token_edicao
from modules.validar_credenciais import validar_credenciais
from modules.realizar_edicao import realizar_edicao

# Define a função principal para extrair texto de acórdãos
def extrair_texto_acordao():
    # Define os diretórios de entrada e saída, e o arquivo de controle
    pasta_entrada = 'documents/acordaos'
    pasta_saida = 'documents/wikitext'
    arquivo_controle = 'logs/arquivos_processados.txt'

    # Lista todos os arquivos na pasta de entrada com extensão .pdf
    arquivos_pdf = [arquivo for arquivo in os.listdir(pasta_entrada) if arquivo.endswith('.pdf')]

    # Inicializa um conjunto para armazenar arquivos já processados
    arquivos_processados = set()

    # Carrega a lista de arquivos processados do arquivo de controle, se existir
    if os.path.exists(arquivo_controle):
        with open(arquivo_controle, 'r') as controle:
            arquivos_processados = set(controle.read().splitlines())

    # Prefixo a ser adicionado ao título da página
    prefixo_pagina = "File:"

    # Obtém o token de edição e valida as credenciais
    oauth = validar_credenciais()
    token_edicao = obter_token_edicao(oauth)

    # Loop através de cada arquivo PDF na pasta de entrada
    for arquivo_pdf in arquivos_pdf:
        caminho_do_pdf_entrada = os.path.join(pasta_entrada, arquivo_pdf)

        # Calcula o hash do nome do arquivo como identificador único
        hash_nome_arquivo = hashlib.md5(arquivo_pdf.encode('utf-8')).hexdigest()
        nome_arquivo_saida = f"{hash_nome_arquivo}.txt"
        caminho_do_txt_saida = os.path.join(pasta_saida, nome_arquivo_saida)

        # Verifica se o arquivo já foi processado
        if nome_arquivo_saida in arquivos_processados:
            print(f'O arquivo {arquivo_pdf} já foi processado. Pulando para o próximo.')
            continue

        # Tenta extrair o texto do PDF
        try:
            texto_extraido = extract_text(caminho_do_pdf_entrada)
        except Exception as e:
            print(f"Erro ao extrair texto do arquivo {arquivo_pdf}: {e}")
            continue

        # Salva o texto extraído em um arquivo de texto na pasta de saída
        with open(caminho_do_txt_saida, 'w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(texto_extraido)

        # Imprime mensagens indicando o sucesso da extração
        print(f'Texto extraído de {arquivo_pdf} e salvo em {nome_arquivo_saida}.')
        logger.info(f'Texto extraído de {arquivo_pdf} e salvo em {nome_arquivo_saida}.')

        # Adiciona o arquivo à lista de arquivos processados no arquivo de controle
        arquivos_processados.add(nome_arquivo_saida)
        with open(arquivo_controle, 'a') as controle:
            controle.write(f"{nome_arquivo_saida}\n")

        # Realiza a edição na página da BDIJ
        realizar_edicao(f"{prefixo_pagina}{arquivo_pdf}", texto_extraido, token_edicao, oauth, nome_arquivo_saida)

# Exporta a função para ser chamada em outros módulos quando o script for executado diretamente
if __name__ == "__main__":
    extrair_texto_acordao()
