# Pretor/1.0 - @edpomacedo - tests/authentication.py

import sys
import os
import requests
from requests_oauthlib import OAuth1

# Adiciona o diretório pai (raiz do projeto) ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import OAUTH_CONFIG, MEDIAWIKI_CONFIG

def test_authentication():
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

    # URL para a API de consulta de usuário do MediaWiki
    api_user_info_url = MEDIAWIKI_CONFIG['api_url'] + '?action=query&meta=userinfo&format=json'

    # Requisição para obter informações do usuário
    response = requests.get(url=api_user_info_url, auth=oauth)

    # Verificar o status da resposta
    if response.status_code == 200:
        print('Conexão bem-sucedida. Informações do usuário:')
        print(response.json())
    else:
        print(f'Erro na autenticação: {response.text}')

if __name__ == "__main__":
    test_authentication()
