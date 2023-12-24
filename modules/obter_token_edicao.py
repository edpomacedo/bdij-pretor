# Pretor/1.1 - @edpomacedo - modules/obter_token_edicao.py
import requests
from config import MEDIAWIKI_CONFIG

def obter_token_edicao(oauth):
    # URL para obter o token de edição
    api_token_url = MEDIAWIKI_CONFIG['api_url'] + '?action=query&meta=tokens&type=csrf&format=json'
    response_token = requests.get(url=api_token_url, auth=oauth)

    if response_token.status_code == 200:
        return response_token.json()['query']['tokens']['csrftoken']
    else:
        raise Exception(f'Erro ao obter o token de edição. Status: {response_token.status_code}, Resposta: {response_token.text}')