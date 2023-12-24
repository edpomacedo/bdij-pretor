# operations/uploader.py
import os
from requests_oauthlib import OAuth1
from api_handler import obter_token_edicao, realizar_edicao
from config import OAUTH_CONFIG
import time

def obter_entrada_usuario(mensagem):
    return input(mensagem)

def processar_arquivos():
    # Obtém o caminho para a pasta "documents" do projeto
    diretorio_base = os.path.join(os.getcwd(), 'documents')

    # Solicitar ao usuário o nome do subdiretório onde os arquivos .txt estão localizados
    subdiretorio = obter_entrada_usuario('Informe o subdiretório onde os arquivos .txt estão localizados: ')

    # Monta o caminho completo para o diretório
    diretorio = os.path.join(diretorio_base, subdiretorio)

    # Utilizando as credenciais do arquivo de configuração
    consumer_key = OAUTH_CONFIG['consumer_key']
    consumer_secret = OAUTH_CONFIG['consumer_secret']
    access_token = OAUTH_CONFIG['access_token']
    access_token_secret = OAUTH_CONFIG['access_token_secret']

    # Configuração do cliente OAuth1
    oauth = OAuth1(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret
    )

    # Obter o token de edição
    token = obter_token_edicao(oauth)

    # Iterar sobre os arquivos no diretório
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".txt"):
            caminho_arquivo = os.path.join(diretorio, arquivo)

            # Ler o conteúdo do arquivo
            with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                linhas = file.readlines()

            # Usar a primeira linha como título e o restante como corpo da postagem
            page_title = linhas[0].strip()
            post_content = ''.join(linhas[1:])

            # Realizar a verificação e edição na página, passando o nome do arquivo
            realizar_edicao(page_title, post_content, token, oauth, arquivo)

            # Aguardar 2 segundos antes da próxima postagem
            time.sleep(2)

if __name__ == "__main__":
    processar_arquivos()
