# Pretor/1.1 - @edpomacedo - modules/verificar_pagina_existe.py
import requests
from config import MEDIAWIKI_CONFIG

def verificar_pagina_existe(page_title, oauth):
    # URL para verificar se a página existe
    api_page_url = MEDIAWIKI_CONFIG['api_url'] + f'?action=query&titles={page_title}&format=json'
    response_page = requests.get(url=api_page_url, auth=oauth)

    if response_page.status_code == 200:
        pages = response_page.json()['query']['pages']
        return list(pages.keys())[0] != "-1"  # Retorna True se a página existe, False caso contrário
    else:
        raise Exception(f'Erro ao verificar se a página existe. Status: {response_page.status_code}, Resposta: {response_page.text}')